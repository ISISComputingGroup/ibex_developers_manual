> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC) > [Reflectometry Configuration](Reflectometry-Configuration) > Reflectometry Config Training

# Reflectometry Config Training: Overview & Setup

### Jump To Section:
> 0. [Overview & Setup](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Overview-&-Setup)
> 1. [The Basics](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-1)
>1. [Building Up The Beamline Model](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-2)
>1. [Modes](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-3) 
>1. [Theta](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-4)
>1. [Parking Components](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-5)
>1. [Beamline Parameter Misc](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-6)
>1. [Engineering Corrections](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-7)
>1. [The Bench](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-8)

This training unit presents a series of exercises which take you through the creation of a reflectometry config. The aim of this is to become more confident in working with the python configuration itself as well as to hopefully learn something about how the reflectometry IOC works internally. 

**NB:** While I have taken care that the examples in the exercises produce a beamline model that resembles those of real instruments, it will be simplified in many ways for the sake of clarity.

#### Useful Resources:

- [Reflectometry View User Manual](https://github.com/ISISComputingGroup/ibex_user_manual/wiki/Reflectometry-View)
- [Reflectometry Config Documentation & Reference Manual](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Configuration)
- [Reflectometry Glossary](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Glossary)

## Setup Instrument Configuration & Dev Environment:

1. Make sure your IBEX Server is not running
1. In `/Instrument/settings/config/<ND...>/`, pull branch `REFL_TRAINING`. This contains a blank reflectometry config `config.py` for the exercises, as well as example solutions. **Please do not commit anything to this branch directly** as it is intended as a blank starting point for anyone wanting to do this course. If you want to keep your local changes under version control, please create your own branch based off `REFL_TRAINING`.
1. (Optional) in `/Instrument/settings/config/<ND...>/Python/` rename `init_inst.py` to `init_<your machine name>.py`. This will load relevant reflectometry routines into genie_python sessions. Scripting is outside of the scope of this course so you should be able to complete everything without having done this, so this is just in case you want to play around.
1. (Optional but recommended) in `/Instrument/Apps/EPICS/ioc/master/Galil/iocBoot/iocGALIL-IOC-01/st-common.cmd`, find a line that says "Save motor settings every 30 seconds" and delete the relevant `$(IFNOTRECSIM)` conditional. This will make it so that simulated Galil axes retain their settings (limits, naming etc.) on IOC restart which can otherwise be a bit tedious to reapply every time.
1. Start IBEX Server
1. From an EPICS terminal, run `/Instrument/settings/config/<ND...>/configurations/refl/motor_setup.bat`. This will set up your motor axes to look like the SURF beamline through a series of caputs. SURF was chosen as a base as it is one of the more simple reflectometers.
1. In the IBEX Menu Bar, navigate to `Preferences > Select Visible Perspectives` and tick yes for "Reflectometry"
1. Restart the `REFL_01` IOC. The front panel on the Reflectometry Perspective should display a server status of "OKAY". If you see a lot of purple disconnected boxes, don't worry, this is expected. All other tabs should be blank at this point, i.e. no items listed.
1. You will be editing the python reflectometry configuration at `/Instrument/settings/config/<ND...>/configurations/refl/config.py` Next to it, there should be a list of example solutions to all exercises. I highly recommend opening this in an IDE of your choice that lets you add `/Instrument/Apps/EPICS/support/refl/` as a project dependency, as having access to class/function definitions and autocomplete will be extremely useful.

You should now be all set up! If you want to load one of the example solutions as the config for the reflectometry server, you can do this by setting a macro on the reflectometry IOC:
1. Navigate to `Menu > Configurations > Components > Edit > Reflectometry`
1. Edit the `REFL_01` IOC
1. Set the `CONFIG_FILE` macro to e.g. `ex1_solution.py`

### [Next: The Basics >](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-1)
