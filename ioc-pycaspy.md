> [Wiki](Home) > [The Backend System](The-Backend-System) > [Creating and Basics of IOCs](IOCs) > [pycaspy ioc](ioc-pycaspy)

IOCs can be served via python using pycaspy. These let you create IOCs with PVs using channel access. They do not work quite like the normal EPICs so this the start of a guide to help create one.

## Main Loop

To Do

## Allow IBEX to start the IOC

The easiest way to let ibex start the pycaspy server (or in fact any python script) you need:

1. Create dir (use same [naming rules](IOC-Naming) as for other IOCs)
1. Add an empty makefile. Copy the one in LSICORR
1. Create the directory tree: `<ioc name>\iocBoot\ioc<ioc name>-IOC-01`
    1. Add a [standard `config.xml` to the folder](IOC-Finishing-Touches#7-macros-and-details)
    1. Add a `runIoc.bat` file which runs the pycas py server with options.
1. If needed create a similar tree for a second IOC.


## Registering PVs with IBEX
