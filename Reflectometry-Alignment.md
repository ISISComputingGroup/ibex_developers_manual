> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC) > Alignment


Beamline equipment on a reflectometry instrument needs to be kept aligned to preserve flux and data quality, meaning that motor zero positions are redefined to be exactly centred on the straight-through beam (i.e. the beam as it enters the blockhouse, without any modifications to the path from other equipment).

This needs to be done regularly (usually once at the start of each cycle) as positions can become inaccurate over time e.g. due to modifications to the engineering of the beamline, people accidentally leaning on equipment in the blockhouse, natural sagging etc. 

This is done by scanning individual axes around where we roughly expect the neutron beam to be. The `scan` command provided by the [Scans library](https://github.com/ISISNeutronMuon/InstrumentScripts) moves the motor at regular steps within an interval, taking data at each point, which results in an intensity graph. Depending on the type of axis scanned, the scientists then apply fits to the scan results to look for certain features that indicate where the point of interest is. These slides contain some more detail on the various different types of scans.

The IBEX reflectometry server provides [parameters](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Beamline-Parameters) which can hold displacement and angle of individual components relative to the beam, which provide a convenient way to perform these scans.

Generally speaking, the process for aligning an axis is as follows:
1. Open slit gaps to sensible parameters
1. Scan beamline parameter in the desired range
1. Find feature in graph indicating zero position
1. (Optionally iterate over this process if you are scanning two dependent axes, e.g. mirror height and mirror angle)
1. Redefine feature as motor zero

**Note:** With the exception of Theta, axes are scanned in isolation i.e. nothing but the scanned axis should move between data points. This means there is a special case for reflecting angles (such as Phi or the supermirror angle) which need to be scanned in disabled mode, as the rest of the beamline would otherwise track to match the new angle.