# Beckhoff - Simulate an Instrument

to simulate an instrument's beckhoff and make it virtual rather than driving physical motors etc. you need to: 

1. find the repo for that particular MCU within https://github.com/ISIS-Motion-Control 
1. clone it and checkout master, then `git submodule update --init` in the cloned directory
1. open up the solution in TwinCAT XAR
1. change the `MCU_xxx` in the dropdown next to "solution" to `<local>`

there are a few things we need to disable in XAR in order to get this instance entirely virtual. these are: 

(under the "solution" in the solution explorer)

license: 
1. in SYSTEM -> License remove any dongles (these are normally physical USB sticks)
1. generate a "7 days trial license" from the top-level screen

i/o:

in `I/O -> Devices`, disable all devices that show up by right-clicking and selecting "disable"

safety: 

in `SAFETY`, disable all safety instances

motion:

in `MOTION -> NC - Task 1 SVB` go to Axes and then expand all axes, then go to `Enc` and change the "type" to "Simulation encoder"


after doing all of this you should be able to build the solution from "build" and then hit activate(icon that looks like stairs) and run it locally. 

