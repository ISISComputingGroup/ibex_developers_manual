> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Sample Changers](Sample-Changers)

# Generic Sample Changers Support Module

See [Sample Changers Support Module](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Sample-Changer-Support-Module)

# Rotating Sample Changer

There a couple of specific ISIS built rotating sample changers that are mostly used on GEM, POLARIS and HRPD. The version on HRPD has slightly different firmware but basically the same hardware. The hardware consists of a carousel that can hold 20 samples. When a new sample if requested the carousel rotates to the specified position and a sample arm will push the sample down into the beam.

## Dropped samples

Occasionally a sample can fall down below the beam, called a 'dropped' sample. If the device drops a sample it will tell you that it has done so as it moves on to the next sample. There is a retrieve command to collect the sample again, IBEX will attempt to retrieve the sample (as well as perform some other error checking) using the following state machine:

![state machine](https://raw.githubusercontent.com/ISISComputingGroup/ibex_developers_manual/master/images/Rotating_sample_changer.png)