> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Imaging Cameras](Imaging-Cameras)

## Imaging Cameras

These are often controlled via their own PCs running bespoke software.  Running an IOC on the camera's control PC allows the instrument control machine to communicate with it.

In general the IMAT instrument scripts create folders on the relevant remote PC for the data to be stored in (using the mapped drives) and then communicates with the IOCs on the remote PC to take data. The remote PCs are mapped to the following drives on the NDX: 

* M: `IMAT-MESSINA-DETECT`
* E: `IMAT-UCB`

### Pixelman

This has been run on the `IMAT-UCB` machine.

[Pixelman](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Pixelman)

### Andor

The Andor camera is run on the `IMAT-MESSINA-DETECT` machine. It uses an areaDetector IOC to communicate.

# Trouble Shooting

If the script is run and it report `Folder does not exist` then this could be because the mapping to the drives (see above) is incorrect.

On the Andor camera computer, there are two scripts on the desktop, start_epics and start_css which should be run in sequence (note the first will not finish but should sit waiting after a few seconds).  If the start_epics fails with an "ERROR: VxD not loaded" it may be a problem with camera power or USB connection.  Note the Andor camera PSU has two lights, both of which should be on.