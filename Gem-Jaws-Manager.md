> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Jaws and Slits](Jaws-and-slits) > [Gem Jaws](Gem-Jaws-Manager)

Gem jaws are a set of 5 jaws which work in concert to limit the beam of neutrons reaching the sample (see the [Jaws Manager](Jaws-Managers) page). The 5 jaws are ordered 1 nearest the beam and 5 nearest the sample. 

The parameters are (use [Jaws Manager](Jaws-Managers) for reference):

Letter | Parameter | Value | Notes
--- | --------- | ----- | -----
c | Collimator position | 0 mm |  No collimator so beam tapered from moderator
j1 | Jaw 1 position | 6322 mm | Distance from moderator
j2 | Jaw 2 position | 8128 mm |  Distance from moderator
j3 | Jaw 3 position | 10329 mm |  Distance from moderator
j4 | Jaw 4 position | 12643 mm |  Distance from moderator
j5 | Jaw 5 position | 15389 mm |  Distance from moderator
s | Sample position | 17000 mm | Distance from moderator
w | Width of moderator | user set | 
h | Height of moderator | user set | 
x | Width at sample | user set |
y | Height at sample | user set |

## Setup

The control files for the nimrod jaws are part of the galil motor set up and are per instrument. There is an example in `...\EPICS\support\motorExtensions\master\settings\gem_jaws\*.cmd` which would need to be copied to `C:\Instrument\Settings\config\<instrument host name>\configurations\galil`. IOC System tests also exist for the logic.
