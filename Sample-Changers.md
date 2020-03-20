> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Sample Changers](Sample-Changers)

# Generic Sample Changers Support Module

The sample changer support module allows a sample changer to be configured on top of [motion set-points](Motion-Set-points). The functionality this adds is to allow a motion set-point list to be created from the definitions of racks and slots.

# Rotating Sample Changer

There a couple of specific ISIS built rotating sample changers that are mostly used on GEM, POLARIS and HRPD. The version on HRPD has slightly different firmware but basically the same hardware. The hardware consists of a carousel that can hold 20 samples. When a new sample if requested the carousel rotates to the specified position and a sample arm will push the sample down into the beam.

## Dropped samples

Occasionally a sample can fall down below the beam, called a 'dropped' sample. If the device drops a sample it will tell you that it has done so as it moves on to the next sample. There is a retrieve command to collect the sample again, IBEX will attempt to retrieve the sample (as well as perform some other error checking) using the following state machine:

![state machine](https://raw.githubusercontent.com/ISISComputingGroup/ibex_developers_manual/master/images/Rotating_sample_changer.png)