# Galil

## Introduction

This page contains information and references regarding the operation and maintenance of the Galil IOC

## Useful references

Useful information about the Galil can be found on the following pages:

- [Motors Trouble Shooting](Motors-Trouble-Shooting)
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

{#galil_mot_enc_sync}
### Syncing encoder and motor steps

The Galil keeps two counters: a motor step counter, and an encoder readback. The motor step counter corresponds to
how far a given axis should have moved, given the number of motor pulses sent to it. The encoder readback is an
independent position readback from the encoder.

These two numbers can get out of sync with each other for various reasons, for example:
- The motor may mechanically stall (motor steps will be sent; some of the sent steps will not cause corresponding motion)
- Motion may be disabled by a safety system (motor steps will be sent; no physical motion will occur)
- The encoder may be broken (motor steps will be sent, motion will occur, but will not be registered by the encoder)

In June 2025, in [ticket 5220](https://github.com/ISISComputingGroup/IBEX/issues/5220), it was decided that the encoder
would be the "source of truth" number used by IBEX (wherever an encoder is present). This means that
IBEX has been set up to resync the motor position and the encoder readback before every move.

This is configured using PVs of the form `MTR0101_MOT_ENC_SYNC_TOL_SP`. If the drift between the motor and encoder 
exceeds the limit defined by this PV, then the motor position will be resynced to the encoder readback just before a
move. The drift is available in PVs of the form `MTR0101_MTRENC_DRIFT`. 
For most axes, a setting equal to `ERES` is appropriate - this re-syncs motor to encoder if they differ by more than one
encoder pulse (which is the smallest increment accurately measurable).

A [config checker test](https://github.com/ISISComputingGroup/InstrumentChecker) checks that the resync tolerance has
been set. If you need to disable the resync mechanism for a particular axis, the resync tolerance should be set to an
explicit large value (e.g. much larger than the total range of travel for the axis).

A side effect of enabling the resync logic on every axis is that if an encoder fails, and is switched to open loop, it
will need to be re-homed or re-scanned to have an accurate position. This is because it will have done a resync to the
broken encoder.
Even without the resync logic, the open-loop axis may have lost its absolute position, for example due to
motor record retries.

### Limits

If the motor is on limits and a move is attempted, you will see a message in the log like:
```
move begin failure axis X after XXX seconds: ... [Decelerating or stopped by FWD limit switch or soft limit FL]"
```

This means that the axis is on a limit, which can be either a hard limit or a soft limit. If it is a hard limit, the
hard limit indicators in IBEX (`.LLS` and `.HLS` PVs will be active) - this means that a mechanical limit switch is
engaged, or that an external system has disabled motion (safety systems commonly cause both limits to show engaged).

If it is a soft limit, these are set in IBEX. For axes where the [motor and encoder resync](#galil_mot_enc_sync),
the internal limits in the galil should match closely with the limits set in IBEX. However, if the motor-encoder resync
tolerance is set very high, it is possible for the internal galil limits to differ from those configured in IBEX.

### Checking historic Galil parameters

It may be useful to check when a Galil parameter was changed. The easiest way to do this is via the `autosave`
directory, which keeps historic files.

For example, if you were interested in the setting `MENCTYPE_CMD` on motor `0403`, the following command
could be used:
```
cd /c/Instrument/var/autosave/GALIL_04
grep -rF "0403_MENCTYPE_CMD"
```

This will list all autosave files that refer to this setting, along with the value it had at that time.

For more fine-grained information, the ICP putlog files (on the archive, or in `c:\data\Export only`) can equally
be searched, using a similar command, to find exactly when a setting was changed.

## Further Information

```{toctree}
:glob:
:titlesonly:
:maxdepth: 1

galil/*
```
