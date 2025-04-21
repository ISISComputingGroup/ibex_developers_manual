# Galil

## Introduction

This page contains information and references regarding the operation and maintenance of the Galil IOC

## Useful references

Useful information about the Galil can be found on the following pages:

- [Motors Trouble Shooting](/iocs/troubleshooting/Motors-Trouble-Shooting)
- [IOC And Device Trouble Shooting](/iocs/troubleshooting/IOC-And-Device-Trouble-Shooting)
- [Differences between real Galil and simulated motor](galil/Differences-between-real-Galil-and-simulated-motor)
- [Galil Instrument Configuration](galil/Galil-Instrument-Configuration)
    - [Axis (Alias)](../motor_extensions/Axis)
    - [Barndoors and Momentum Slits on MUON Front End](../motor_extensions/jaws/Barndoors-and-Momentum-Slits-on-MUON-Front-End)
    - [Bump Strip](../motor_extensions/Bump-Strip)
    - [Jaws](../motor_extensions/Jaws)
    - [Motion Set Points](../motor_extensions/Motion-Set-points) 
    - [Sample Changer](../motor_extensions/Sample-Changer-Support-Module)
- [Creating soft motors to control real motors](../motor_extensions/Creating-soft-motors-to-control-real-motors)
- [Galil default parameters](galil/Galil-default-parameters)
- [Galil homing routines](galil/Galil-homing-routines)
- [Galil userdef records](galil/Galil-Userdef-Records)

## Technical information

### Manuals

There are many manuals in the usual place:

- `manc2xxx.pdf`: contains basic commands for the Galil
- `dmc2280\man2100.pdf`: contains some extended commands

{#galil_startup}
### Startup

For each Galil crate in use on the IOC, you should have a corresponding `Galilnn.cmd` file in `C:\Instrument\Settings\config\*machine_name*\configurations\galil`. For example, if I am using galil crate 1 on LARMOR, I have a file called `Galil01.cmd` in `C:\Instrument\Settings\config\NDXLARMOR\configurations\galil`

The file should contain 3 sets of commands:

### configure galil crate 1

```
GalilCreateController("Galil", "$(GALILADDR)", 20)
```

This initiates the Galil controller program. It takes the following arguments:

- Port name
- Address: This is typically the macro to the address of the crate and will correspond to the macro name used in the IOC setup for this Galil. This can be:
    1. An IP address of the form `XXX.XXX.XXX.XXX`, e.g. `192.168.0.1`
    1. An serial port of the form `<com port> <speed>`, e.g. `COM23 38400`
- Update period: The number of ms between polls of the Galil. If this number is set to be negative then the Galil will use synchronous rather than asynchronous polling by default
- Quiet start: If set to 1, the Galil program will check on startup whether any new code is waiting to be uploaded to the Galil. If not, it will leave any existing control programs running. If set to 0 (or defaulted as in this case) then all threads will be restarted along with the IOC. This is especially relevant for the LET oscillating collimator
 
```
GalilCreateAxis("Galil","A",0,"",1)
GalilCreateAxis("Galil","B",0,"",1)
```

These lines create the axis controllers. It takes the following arguments:
- Port name: Same as above
- Axis name: The name of the axis in the controller (the galil labels axes A-H)
- Limit as home: Set to zero if the axis has a home switch that it homes to, one if it homes in any other way.
- Enables string: A comma separated list of digital ports to use for enabling/disabling motors. (Not currently used at ISIS)
- Switch type: Whether the ports specified on the enables string enable or disable the motor. (Not currently used at ISIS)

```
GalilStartController("Galil","$(GALIL)/gmc/galil_Default_Header.gmc;$(GALIL)/gmc/galil_Home_Dummy_Do_Nothing.gmc!$(GALIL)/gmc/galil_Home_Dummy_Do_Nothing.gmc!$(GALIL)/gmc/galil_Home_Dummy_Do_Nothing.gmc!$(GALIL)/gmc/galil_Home_Dummy_Do_Nothing.gmc!$(GALIL)/gmc/galil_Home_Dummy_Do_Nothing.gmc!$(GALIL)/gmc/galil_Home_Dummy_Do_Nothing.gmc!$(GALIL)/gmc/galil_Home_Dummy_Do_Nothing.gmc!$(GALIL)/gmc/galil_Home_Dummy_Do_Nothing.gmc;$(GALIL)/gmc/galil_Default_Footer.gmc!$(GALIL)/gmc/galil_Oscillating_Collimator_Merlin.gmc",0,0,3)
```

This starts the Galil controller. It takes the following arguments:

- Port name: As before
- Code file: The code to be uploaded to the Galil
- Burn program: Whether to burn the program to EEPROM
- Display code: Whether to display the code being uploaded (1 displays code currently on controller, 2 displays code put on the controller, 3 both)
- Thread mask: Which threads we expect to be running after code has been delivered (e.g. `7`, `1+2+4` for threads 0, 1, and 2)

The largest and most frequently changed of these arguments is the code file. It uses semi colons and exclamation marks to demarcate different sections of the Galil code. It is arranged as:

```
[Header];[Body];[Footer]
```

- Header: Sets initial conditions on the Galil and initiates the homing programs on thread 1
- Body: This should be an 8 element list of exclamation mark separated values. Each element is a path to the homing routine used for each axis in sequence A-H. The galil homing [routines are described in this wiki(Galil-homing-routines) and each is found at [Galil homing routines](https://github.com/ISISComputingGroup/EPICS-galil/tree/master/GalilSup/Db)
- Footer: Additional code executed after homing programs have started

As you can see above, we have two programs in the footer, separated by exclamation marks.

### Threading

Threads 0 and 1 are reserved for homing operations. As described above, thread 0 is where the uploaded code is executed. It delegates the homing programs to thread 1. 

Threads 2-8 are available for other operations but beware of conflicts. For example, the LET oscillating collimator is currently set to run on thread 2 by default.

By default, the Galil IOC will stop all running threads when it restarts. If you wish for active threads to keep running, then the upload program cannot have changed since the previous launch and the quiet_start parameter must be set in `GalilController` as described above.

### Things that we know run on separate Galil threads:

- Oscillating collimator. LET, MERLIN.  Thread number defaults to 2, but can be set via PV
- Fermi chopper lift. EMMA. Thread number fixed to 5

### Assigning IP addresses

The IP address of a Galil can only be established using a serial connection. This must be set up.
  
For a Galil DMC 2280, there are no problems
1) Enter the command IA n1,n2,n3,n4 e.g. IA 192,168,1,201
2) Enter the command BN to burn permanently into Galil
  
For a Galil DMC 4280, the firmware will not retain the IP address. As a result a trick must be used :
1) The IP address can not be burnt into the Galil. As a result, a program must be saved into the Galil that assigns the IP address when the Galil is powered up. It must also turn off the DHCP setting as we use a private network for the Galils.
2) Send the following program to the Galil (For the IA command, use the appropriate IP address desired.):
```
#AUTO
DH0
IA 192,168,1,201
EN
```
3) Once entered, the program must be saved into the Galil permanently.
4) Issue command BP (for burn program)
5) Power cycle and the Galil should be available on the network.
6) Please note : do not overwrite the permanent program resident in the Galil. It can be overwritten as long as it is not made permanent. Other programs, such as homing routines can be downloaded into the device but should not be burnt in.

## Syncing encoder and motor steps

It can be useful to sync the motor steps to the encoder steps before each move. This is especially true with an absolute encoder where a power cycle of a Galil controller can change the motor steps to 0 but not the encoder steps because this makes the soft limits stop the motion at strange places. To do this the PV `<MOT:MTR0X0X>_MOT_ENC_SYNC_TOL_SP` should be set to a non zero value, when the difference differs by more than this tolerance the motor steps will be resynced. If the encoder is not absolute you should be cautious when doing this, the encoder and motor steps should not get out of sync so don't do it without recording the reason somewhere.

## Trouble Shooting

See [Motors Trouble Shooting](/iocs/troubleshooting/Motors-Trouble-Shooting)

## Further Information

```{toctree}
:glob:
:titlesonly:
:maxdepth: 1

galil/*
```
