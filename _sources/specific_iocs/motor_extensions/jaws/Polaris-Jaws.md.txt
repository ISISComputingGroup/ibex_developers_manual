# POLARIS Jaws

Polaris jaws are a set of 5 jaws which work in concert to limit the beam of neutrons reaching the sample (see [Jaws Manager](Jaws-Managers)). Jaws 1-4 are instrument user controlled and work together in a pyramid shape to reduce the beam size in stages. The gap in each jaw set is set based on its distance from the sample. There are documents stored in [sharepoint](http://stfc365.sharepoint.com/sites/ISISExperimentControls/ICP%20Discussions/POLARIS/polarisCalculations.zip). The 5 jaws are ordered 1 nearest the beam and 5 nearest the sample. 
Jaw set 5 is under on instrument scientist control. To change these settings the user must put the GUI into management mode. 

The parameters are (with reference to the diagram in [Jaws Manager](Jaws-Managers)):

Letter | Parameter | Value | Notes
--- | --------- | ----- | -----
c | Collimator position | 1610 mm |  Distance from moderator
j1 | Jaw 1 position | 6502 mm | Distance from moderator
j2 | Jaw 2 position | 9440 mm |  Distance from moderator
j3 | Jaw 3 position | 11085 mm |  Distance from moderator
j4 | Jaw 4 position | 11735 mm |  Distance from moderator
j5 | Jaw 5 position | 13175 mm |  Distance from moderator
s | Sample position | 14000 mm | Distance from moderator
w | Width of Collimator | 82.2 | 
h | Height of Collimator | 79.4 | 
x | Width at sample | user set |
y | Height at sample | user set |

## Setup

The control files for the Polaris jaws are part of the galil motor set up and are per instrument. There is an example in `...\EPICS\support\motorExtensions\master\settings\polaris_jaws\*.cmd` which would need to be copied to `C:\Instrument\Settings\config\<instrument host name>\configurations\galil`
