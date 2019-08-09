> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC) > Alignment


Beamline equipment on a reflectometry instrument needs to be kept aligned, meaning that motor zero positions are redefined to be exactly centered on the straight-through beam (i.e. the beam as it enters the blockhouse, without any modifications to the path from other equipment).

This needs to be done regularly (usually once at the start of each cycle) as positions can become inaccurate over time e.g. due to modifications to the engineering of the beamline, people accidentally leaning on equipment in the blockhouse etc. 

This is done by scanning individual axes around where we roughly expect the neutron beam to be. The `scan` command provided by the [Scans library](https://github.com/ISISNeutronMuon/InstrumentScripts) moves the motor at regular steps within an interval, taking data at each point, which results in an intensity graph. Depending on the type of axis scanned, the scientists then apply fits to the scan results to look for certain features that indicate where the point of interest is. These slides contain some more detail on the various different types of scans.

The IBEX reflectometry server provides parameters which hold positions of individual components relative to the beam, which are a convenient way to scan these axes.

Generally speaking, the process for aligning an axis is as follows:
1. Open slit gaps to sensible parameters
1. Scan beamline parameter in the desired range
1. Find feature in graph indicating zero position
1. (Optionally iterate over this process if you are scanning two dependent axes, e.g. mirror height and mirror angle)
1. Redefine feature as motor zero

Note that as axes need to be scanned in isolation, there is a special case for reflecting angles (such as Phi or the supermirror angle), which need to be scanned in Disabled mode, as the rest of the beamline would otherwise track to match the new angle.