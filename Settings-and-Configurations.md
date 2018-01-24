> [Wiki](Home) > [The Backend System](The-Backend-System) > [Settings and Configurations](Settings-and-Configurations)

How is an instrument configured and what is stored in the settings directory.

The settings directory should be in `c:\Instrument\Settings`, it contains (each level is a directory):

- gwblock.pvlist: TODO
- config
    - common: [Calibration files specific to equipment but potentially shared](Calibration-Files)
    - <Instrument name>
        - Python: Instrument specific python modules (TODO create a page)
        - configurations directory

# Configurations directory

The configurations directory has the settings for the instrument in. 

## Files
It contains some files:
- config_version.txt: configuration version
- globals.txt: overriding definition of macros for IOCs
- last_config.txt: last loaded config in IBEX
- rc_setting.cmd: commands to load in runcontrol

## User configuration

The user configuration is items we expect an instrument scientist to change using the GUI. These include the
 - [configurations: contains configurations](Configuration-Rules)
 - [components: contains the components which can be included in a configuration](Configuration-Rules#components)
 - synoptics: graphical representation of the instrument
 - device: device screens

### DAE Configuration

Configuration files for the DAE.

- tables: wiring, spectra and detector tables
- tcb: tcb parameter files

### Configuration of devices and extensions

These are directories which configure devices which would be too complicated for macro configuration. For example the Galil configuration with the need to setup the controller, homeing routines etc. Historically this was named after a category of device, e.g. galil. This allow configuration of devices as a whole. They can also be named after an IOC which allow configuration of a single IOC, e.g SM300_01. 

The extensions are items which extend an IOC for example a motion setpoints which allow a motor to stop at labelled positions. These are configured from the IOC configuration directory and may need optional extra configuration directories.

The pattern for both device configuration and extensions configuration is that the IOC loads a command file sitting in a directory if it is present.

Directories:

- galil: configures the galil [Galil](Galil) and extenstions
- mclen: configures McLennan motors [McLennan](McLennan) and extenstions
- sm300_01: configures the [SM300_01](SM300) motor extensions 
- motionSetPoints: setpoint look up files

Common extensions:
 - [motion setpoints](Motor-SetPoints) (works for galil, McLennan and sm300)
 - [axes](Motor-Axes) (works for galil, McLennan and sm300)
 - [sample changer](Sample-Changers) (works for galil, McLennan and sm300)
 - [Barn doors and Momentum slits](Barndoors-and-Momentum-Slits-on-MUON-Front-End)
 - [larmor Beamstop](Larmor-Beamstop) (galil)
