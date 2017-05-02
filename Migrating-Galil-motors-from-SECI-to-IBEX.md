# Physical setup (serial to ethernet conversion)

Under SECI, motors are controlled via a serial connection. The IBEX Galil IOC only works properly with an ethernet connection, so the motors need to be migrated.

- SECI VI needs to be converted from serial to ethernet
- Physical private network, e.g. network switches need to be installed. This is done by another group; make sure they are warned well in advance so that any bits of kit are available when we need them

The motors are assigned IP addresses on the private network in the following way (this is a convention, whoever set up the private network should have set it up like this, if it doesn't look like it's working then check with them):
GALIL_01 -> `192.168.1.201`
GALIL_02 -> `192.168.1.202`
GALIL_03 -> `192.168.1.203`
...

# GALIL macros

For each GALIL IOC that you need to use, you need to set the corresponding GALILADDRx macro.

e.g. if you are setting up `GALIL_02`, the `GALILADDR02` macro should be set to `192.168.1.202` and all other macros should be left blank.

# GALIL configuration file

In the `configurations/galil` directory, you need to create `galilx.cmd` files. These files define the behaviour of a galil controller in terms of the homing modes and other settings.

For example, if you were setting up galil 2 on POLARIS, you would create `\\Ndxpolaris\c$\Instrument\Settings\config\NDXPOLARIS\configurations\galil\galil2.cmd`

The contents of this file looks like the following:

```
## configure galil crate 2 

## passed parameters
##   GCID - galil crate software index. Numbering starts at 0 - will always be 0 if there is one to one galil crate <-> galil IOC mapping  
##   GALILADDR02 - address of this galil

## see README_galil_cmd.txt for usage of commands below

#G21X3Config($(GCID),"$(GALILADDR02)",8,2100,2000) 
GalilCreateController("Galil", "$(GALILADDR02)", 20)

#G21X3NameConfig($(GCID),"A",0,0,0,0,0,1,"",0,0,"",1,0)
#G21X3NameConfig($(GCID),"B",0,0,0,0,0,1,"",0,0,"",1,0)
#G21X3NameConfig($(GCID),"C",0,0,0,0,0,1,"",0,0,"",1,0)
#G21X3NameConfig($(GCID),"D",0,0,0,0,0,1,"",0,0,"",1,0)
#G21X3NameConfig($(GCID),"E",0,0,0,0,0,1,"",0,0,"",1,0)
#G21X3NameConfig($(GCID),"F",0,0,0,0,0,1,"",0,0,"",1,0)
#G21X3NameConfig($(GCID),"G",0,0,0,0,0,1,"",0,0,"",1,0)
#G21X3NameConfig($(GCID),"H",0,0,0,0,0,1,"",0,0,"",1,0)
GalilCreateAxis("Galil","A",1,"",1)
GalilCreateAxis("Galil","B",1,"",1)
GalilCreateAxis("Galil","C",1,"",1)
GalilCreateAxis("Galil","D",1,"",1)
GalilCreateAxis("Galil","E",1,"",1)
GalilCreateAxis("Galil","F",1,"",1)
GalilCreateAxis("Galil","G",1,"",1)
GalilCreateAxis("Galil","H",1,"",1)

#G21X3StartCard($(GCID),"$(GALIL)/db/galil_Default_Header.gmc;$(GALIL)/db/galil_Home_ForwLimit.gmc!$(GALIL)/db/galil_Home_ForwLimit.gmc!$(GALIL)/db/galil_Home_ForwLimit.gmc!$(GALIL)/db/galil_Home_ForwLimit.gmc!$(GALIL)/db/galil_Home_ForwLimit.gmc!$(GALIL)/db/galil_Home_ForwLimit.gmc!$(GALIL)/db/galil_Home_ForwLimit.gmc!$(GALIL)/db/galil_Home_ForwLimit.gmc;$(GALIL)/db/galil_Default_Footer.gmc",0,0)
GalilStartController("Galil","$(GALIL)/gmc/galil_Default_Header.gmc;$(GALIL)/gmc/galil_Home_ForwLimit.gmc!$(GALIL)/gmc/galil_Home_ForwLimit.gmc!$(GALIL)/gmc/galil_Home_ForwLimit.gmc!$(GALIL)/gmc/galil_Home_ForwLimit.gmc!$(GALIL)/gmc/galil_Home_ForwLimit.gmc!$(GALIL)/gmc/galil_Home_ForwLimit.gmc!$(GALIL)/gmc/galil_Home_ForwLimit.gmc!$(GALIL)/gmc/galil_Home_ForwLimit.gmc;$(GALIL)/gmc/galil_Default_Footer.gmc",0,0,3)

# Ensure there is a newline at the end of the file!

```

Typically the only line you will need to pay careful attention to is the last (non-commented) line. This defines the homing modes of the various galils. The structure of this line is that it has a standard header (`$(GALIL)/db/galil_Default_Header.gmc;`), followed by 8 homing modes, followed by a standard footer (`$(GALIL)/gmc/galil_Default_Footer.gmc`).

The homing modes available under IBEX can be seen in `C:\Instrument\Apps\EPICS\support\galil\master\gmc`. You should select the homing mode under IBEX which corresponds to the homing mode under SECI, which can be found using the VI in `\\ndxINSTRUMENT\C$\LABVIEW MODULES\Drivers\Galil DMC2280\Galil - System Functions.llb`. Open up the `Galil - Setup Dialog.vi`. You should now be able to see the "Home method" for all the various Galils/Axes. 

If you're unsure which homing method to use, check with the instrument scientists what the expected behaviour is.

# Copy across the motor setup

There is a LabVIEW VI in `LABVIEW MODULES\Drivers\Galil DMC2280\Galil - EPICS.llb` that will generate a series of `caput` commands to copy the Labview configuration into EPICS.

Open this VI, put the computer name as `IN` and the username as `(INSTNAME):MOT`. This should generate a load of caput commands that look like `caput IN:(INSTNAME):MOT:MTR0101.(FIELD) (value)`

Copy these caput commands into a batch file, open an EPICS terminal and run that batch file. This will apply the settings to the Galil under IBEX. These settings should then be autosaved.

# Set up any axes / jaws / barndoors files.

These files are instrument specific. If you're unsure how to set these files up, ask the developer who originally wrote that part of the system to clarify how they should be setup. Also get them to add this information to the wiki and release notes!

