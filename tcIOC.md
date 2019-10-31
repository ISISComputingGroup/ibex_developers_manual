> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Motor IOCs](Motor-IOCs) > [Beckhoff](Beckhoff) > [tcIOC](tcIOC)

# General information

This IOC was originally written at LIGO and is in a stable state. The original version from tcIOC was targeted at the use of Beckhoffs as generic PLCs and had no specific motion support. It constructs db records by examining the PLC project on the controller and communicates with it using ADS (Beckhoff's own protocol). More detail can be found at https://github.com/ISISComputingGroup/EPICS-tcIoc.

# Motion Support

![Overview](beckhoff/tcIOC_motor_support.png)

We added motor support to tcIOC so that we could use it to control motors in the usual way. As a first prototype implementation the motor support is a Model 3 motor driver that has the structured text variables of interest hardcoded into the driver. tcIOC will convert these to PVs and the driver will talk to them over channel access. This was chosen as the basic implementation that would be quickest to implement and works well, however there are a number of improvements that could be made:

* If tcIOC was converted to an `asyn` driver then the motor could talk to this asyn port rather than communicate across CA
* If the interesting variables in the PLC code change name so must the IOC, we could get around this by tagging in the comments of the PLC code with which variables are the interesting ones
* The number of axes is hardcoded within the IOC this can be solved by tcIOC creating the required number of motor records when it parses the `.tpy` file

# Releasing the IOC

Currently the IOC is not in the normal EPICS release build as it requires VS 2010. To deploy it to an instrument you will need to copy from `build_area_on_share\EPICS\newbuildtest\*\EPICS\support\tcIoc\master` and `build_area_on_share\EPICS\newbuildtest\*\EPICS\ioc\master`. If you're deploying this on CRISP you can test it by running the TWINCAT IOC with appropriate settings (see globals.txt) then confirming that `MOT:MTR0701.RBV` has a realistic value. 

# Troubleshooting

## The IOC reads from the PLC but does not reliably write
Reduce the scan rate of the IOC, the `tcSetScanRate` command in the IOC is responsible for setting this. It appears that if there are many variables to read the driver will spend all it's time reading and will not get round to writing, it does not produce an error when this happens.