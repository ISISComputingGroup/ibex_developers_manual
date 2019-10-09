> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Fermi chopper lifter](Fermi-Chopper-Lifter)

The fermi chopper lifter is a single-axis Galil-controlled system which lifts the fermi chopper in and out of the beam on the EMMA beamline.  It runs without an encoder and relies solely on limit switches at each end of its travel.  A program running inside the controller moves the lifter between the limits and this is communicated with by a specific OPI.

A bi-directional interlock exists between the chopper controller (an [SKF MB350PC](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/SKF-MB350-Chopper), aka G3) and Galil.  This uses the inhibit input on the axis amplifier card to prevent motion if the chopper is levitated.  Likewise, the chopper is prevented from being levitated if the lifter is in motion.

There is further documentation in the Motion Control Group's SharePoint site: Beamline Motion -> IDD Motion Control -> Technical Files -> EMMA -> EMMA chopper lifter - Handover.docx

[Direct link to document](http://www.facilities.rl.ac.uk/isis/Motion/TestDocuments/EMMA%20chopper%20lifter%20-%20Handover.docx
)
