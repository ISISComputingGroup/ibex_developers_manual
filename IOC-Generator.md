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

## Support_utils


## ioc_utils


## ioc_test_framework_utils


## emulator_utils



## gui_utils