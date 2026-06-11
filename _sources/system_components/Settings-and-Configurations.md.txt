# Settings & Configurations

```{toctree}
:glob:
:titlesonly:
:maxdepth: 1
:hidden:

configurations/*
```

How is an instrument configured and what is stored in the settings directory.

The settings directory should be in `c:\Instrument\Settings`, it contains (each level is a directory):

- `gwblock.pvlist`: created by the blockserver on each config change and used to configure the block gateway, which provides aliases for PVs to blocks. See [here](#gateway_pvlist_files) for format.
- config
    - common: [Calibration files specific to equipment but potentially shared](configurations/Calibration-Files)
    - <Instrument name>
        - Python: Instrument specific python modules (TODO create a page)
        - configurations directory

## Configurations directory

The configurations directory has the settings for the instrument in. 

### Files
It contains some files:
- config_version.txt: configuration version
- globals.txt: overriding definition of macros for IOCs
- last_config.txt: last loaded config in IBEX
- rc_setting.cmd: commands to load in runcontrol
- banner.xml: customised displays and buttons for the GUI banner
- custom_records.db: records specific to the instrument which are loaded by INSTETC
   - Pass macros through from globals.txt with `CUSTOM_RECORD_MACROS="DSC_EUROTHRM=03,DSC_LKSH336=02"`

### User configuration

The user configuration is items we expect an instrument scientist to change using the GUI. These include the
 - [configurations: contains configurations](configurations/Configuration-Rules)
 - [components: contains the components which can be included in a configuration](configurations/Configuration-Rules)
 - synoptics: graphical representation of the instrument
 - device: device screens

### DAE Configuration

Configuration files for the DAE.

- tables: wiring, spectra and detector tables
- tcb: tcb parameter files

### Configuration of devices and extensions

```{note}
Motion-related configuration has now been moved to [motorExtensions](https://github.com/ISISComputingGroup/EPICS-motorExtensions/tree/master/settings) as per [this ticket](https://github.com/ISISComputingGroup/IBEX/issues/8427)
```

These are directories which configure devices which would be too complicated for macro configuration. For example the Galil configuration with the need to setup the controller, homing routines etc. Historically this was named after a category of device, e.g. galil. This allow configuration of devices as a whole. They can also be named after an IOC which allow configuration of a single IOC, e.g TC_01. 

The extensions are items which extend an IOC for example a motion setpoints which allow a motor to stop at labelled positions. These are configured from the IOC configuration directory and may need optional extra configuration directories.

The pattern for both device configuration and extensions configuration is that the IOC loads a command file sitting in a directory if it is present.

Directories:

- `galil`: configures the galil [Galil](/specific_iocs/motors/Galil) and extensions
- `mclen`: configures McLennan motors [McLennan](/specific_iocs/motors/McLennan-motors) and extensions
- `motionSetPoints`: setpoint look up files
- `refl` (for reflectometers only): contains a file `config.py`, which tells instruments using the [Reflectometry IOC](/specific_iocs/Reflectometry-IOC) what their beamline looks like (follow the link for details)

Common extensions:
 - [Motion Set points](/specific_iocs/motor_extensions/Motion-Set-points) (works for galil, McLennan and TC)
 - [axes](/specific_iocs/motor_extensions/Axis) (works for galil, McLennan and TC)
 - [sample changer](/specific_iocs/motor_extensions/Sample-Changer-Support-Module) (works for galil McLennan and TC)
 - [Barn doors and Momentum slits](/specific_iocs/motor_extensions/jaws/Barndoors-and-Momentum-Slits-on-MUON-Front-End)

### Version Control

The configuration directory is backed up into git. This is done by the [Blockserver](/system_components/BlockServer).

Each instrument stores the configurations in their own branch in this repository, these branches are named the same as the instrument machine.

The repository is stored in a [local repository](/processes/git_and_github/New-Local-Git-Repository).

## Special cases

`Detmon` has a special case for their configuration because they want to create configurations with the same info for multiple CAEN crates. The way this is created is [described on the ibex instrument page](/processes/instrument_details/DETMON-Instrument-Details).
