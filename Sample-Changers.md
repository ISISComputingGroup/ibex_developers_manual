> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Sample Changers](Sample-Changers)

# Generic Sample Changers Support Module

The sample changer support module allows a sample changer to be configured on top of [motion set-points](Motion-Set-points). The functionality this adds is to allow a motion set-point list to be created from the definitions of racks and slots.

This takes input files `rackDefinitions.xml` and `samplechanger.xml` and then allows the user to dynamically build the motion setpoints configuration file. As of [October 2020](https://github.com/ISISComputingGroup/IBEX/issues/5720), the user can also select a specific rack, and this will rebuild the list of motion setpoints to only include the positions listed in that rack. If the selected sample changer is the special value `_ALL`, positions from all sample changers will be included in the built motionsetpoints file. This option is automatically added to the list of available sample changers.

An example sampleChanger + motionSetpoints configuration can be found in `support/samplechanger/master/settings`.

# Rotating Sample Changer

There a couple of specific ISIS built rotating sample changers that are mostly used on GEM, POLARIS and HRPD. The version on HRPD has slightly different firmware but basically the same hardware. The hardware consists of a carousel that can hold 20 samples. When a new sample if requested the carousel rotates to the specified position and a sample arm will push the sample down into the beam.

## Dropped samples

Occasionally a sample can fall down below the beam, called a 'dropped' sample. If the device drops a sample it will tell you that it has done so as it moves on to the next sample. There is a retrieve command to collect the sample again, IBEX will attempt to retrieve the sample (as well as perform some other error checking) using the following state machine:

![state machine](https://raw.githubusercontent.com/ISISComputingGroup/ibex_developers_manual/master/images/Rotating_sample_changer.png)