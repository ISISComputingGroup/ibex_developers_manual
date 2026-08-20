# IOC Generator

Generates the boilerplate structure required for developing an IBEX [IOC](../../IOCs).

## How you use it

Use these [instructions](https://github.com/ISISComputingGroup/IBEX-device-generator).

## How to edit it/how it works/file locations

Clone the [repository](https://github.com/ISISComputingGroup/IBEX-device-generator) into C:\Instrument\Dev.

This program makes git branches and pushes to the remote repo, you can stop this by adding a return statement at the start of each method in git_utils (including the RepoWrapper constructor).

The program starts in IBEX_device_generator.py, so we'll start there.
generate_device calls create_component for each component you might want, passing in an instance method.
These instance methods are grouped into classes:
 - support_utils (generic IOC config)
 - ioc_utils (ISIS specific IOC config)
 - ioc_test_framework_utils (testing)
 - emulator_utils (emulation)
 - gui_utils (opi template creation)

### support_utils

Makes files in C:\Instrument\Apps\EPICS\support

Templates for support module: C:\Instrument\Apps\EPICS\support\asyn\master\templates\streamSCPI
These templates are **generated from** templates in: C:\Instrument\Apps\EPICS\support\asyn\master\makeSupport\streamSCPI


### create_submodule

Creates the top level directory in C:\Instrument\Apps\EPICS\support\, adds a makefile and tries to create a new git repo.

### apply_support_dir_template

Requires the directories made by create_submodule.
This will call a Perl script which generates the .db and .proto files for the support module.
The Perl script is C:\Instrument\Apps\EPICS\support\asyn\master\bin\windows-x64\makeSupport.pl.
The Perl script uses the templates in C:\Instrument\Apps\EPICS\support\asyn\master\templates\streamSCPI\_NAME_Sup.
These templates are **generated from** templates in: C:\Instrument\Apps\EPICS\support\asyn\master\makeSupport\streamSCPI\_NAME_Sup


## ioc_utils

Makes files in C:\Instrument\Apps\EPICS\ioc\master

Templates for ioc configuration: C:\Instrument\Apps\EPICS\base\master\templates\makeBaseApp\top
These templates are **generated from** templates in: C:\Instrument\Apps\EPICS\base\master\src\template\base\top
Run make in C:\Instrument\Apps\EPICS\base\master\src to regenerate the templates.

## ioc_test_framework_utils


## emulator_utils



## gui_utils

Generates an opi template for the IOC.