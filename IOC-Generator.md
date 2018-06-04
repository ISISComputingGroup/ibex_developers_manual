# What is the IOC Generator

Generates the boilerplate structure required for developing an IBEX [IOC](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/IOCs).

# How you use it

Use these [instructions](https://github.com/ISISComputingGroup/IBEX_device_generator).

# How to edit it/how it works/file locations

Clone the [repository](https://github.com/ISISComputingGroup/IBEX_device_generator) into C:\Instrument\Dev.
The program starts in IBEX_device_generator.py, so start there.
generate_device calls create_component for each component you might want, passing in an instance method.
These instance methods are grouped into classes:
 - support_utils (generic IOC config)
 - ioc_utils (ISIS specific IOC config)
 - ioc_test_framework_utils (testing)
 - emulator_utils (emulation)
 - gui_utils (opi template creation)

## support_utils

### create_submodule

Creates the top level directory in C:\Instrument\Apps\EPICS\support\, adds a makefile and tries to create a new git repo.

### apply_support_dir_template

Requires the directories made by create_submodule.
This will call a Perl script which generates the .db and .proto files for the support module.
The Perl script is C:\Instrument\Apps\EPICS\support\asyn\master\bin\windows-x64\makeSupport.pl.
The Perl script uses the templates in C:\Instrument\Apps\EPICS\support\asyn\master\templates\streamSCPI\_NAME_Sup.


## ioc_utils


## ioc_test_framework_utils


## emulator_utils



## gui_utils