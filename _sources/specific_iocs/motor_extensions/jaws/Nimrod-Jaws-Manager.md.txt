# NIMROD Jaws

Nimrod jaws are a set of 6 jaws which work in concert to limit the beam of neutrons reaching the sample (see [Jaws Manager](Jaws-Managers) for more). The 6 jaws are ordered 1 nearest the beam and 6 nearest the sample. 

The parameters, with reference to the diagram in [Jaws Manager](Jaws-Managers), are:

Letter | Parameter | Value | Notes
--- | --------- | ----- | -----
c | Collimator position | 0 mm |  No collimator so beam tapered from moderator
j1 | Jaw 1 position | 6458 mm | Distance from moderator
j2 | Jaw 2 position | 8072 mm |  Distance from moderator
j3 | Jaw 3 position | 12072 mm |  Distance from moderator
j4 | Jaw 4 position | 15450 mm |  Distance from moderator
j5 | Jaw 5 position | 17235 mm |  Distance from moderator
j6 | Jaw 6 position | 19691 mm |  Distance from moderator
s | Sample position | 19691 mm | Note that the sample is assumed to be at the final jawset
w | Width of moderator | user set | 
h | Height of moderator | user set | 
x | Width at sample | user set |
y | Height at sample | user set |

## Setup

The control files for the nimrod jaws are part of the galil motor set up and are per instrument. There is an example in `...\EPICS\support\motorExtensions\master\settings\nimrod_jaws\*.cmd` which would need to be copied to `C:\Instrument\Settings\config\<instrument host name>\configurations\galil`. IOC System tests also exist for the logic.

## Jaw centres

The jaws on NIMROD are not centred with respect to the beam, i.e. all jaws being at a centre of (0, 0) will not actually let the beam through. This is due to some of the jaw sets being mounted off-centre during installation.

The expected centres of each jaw set are:

| Jaw set | Horizontal | Vertical |
| -- | -- | -- |
| 1 | -0.135 | -1.5 |
| 2 | -0.126 | -1.457 |
| 3 | -0.205 | -9.634 |
| 4 | 0.159 | -1.460 |
| 5 | -0.303 | -0.801 |
| 6 | -0.378 | -9.507 |

The numbers above correspond to the jaws being centred around the beam in "real" coordinates as opposed to motor coordinates.
