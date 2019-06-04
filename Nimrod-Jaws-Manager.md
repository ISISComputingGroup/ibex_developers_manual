> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Jaws and Slits](Jaws-and-slits) > [Nimrod Jaws](Nimrod-Jaws-Manager)

Nimrod jaws are a set of 6 jaws which work in concert to limit the beam of neutrons reaching the sample (see [Jaws Manager](Jaws-Managers)). The 6 jaws are ordered 1 nearest the beam and 6 nearest the sample. 

The parameters are (with reference to the diagram in [Jaws Manager](Jaws-Managers)):

Letter | Parameter | Value | Notes
--- | --------- | ----- | -----
c | Collimator position | 0 mm |  No collimator so beam tapered from moderator
j1 | Jaw 1 position | 6458 mm | Distance from moderator
j2 | Jaw 2 position | 8072 mm |  Distance from moderator
j3 | Jaw 3 position | 12072 mm |  Distance from moderator
j4 | Jaw 4 position | 15450 mm |  Distance from moderator
j5 | Jaw 5 position | 17235 mm |  Distance from moderator
j5 | Jaw 5 position | 19691 mm |  Distance from moderator
s | Sample position | 19691 mm | Distance from moderator
w | Width of moderator | user set | 
h | Height of moderator | user set | 
x | Width at sample | user set |
y | Height at sample | user set |

## Setup

The control files for the nimrod jaws are part of the gallil motor set up and are per instrument. There is an example in `...\EPICS\support\motorExtensions\master\settings\nimrod_jaws\*.cmd` which would need to be copied to `C:\Instrument\Settings\config\<instrument host name>\configurations\galil`. IOC System tests also exist for the logic.
