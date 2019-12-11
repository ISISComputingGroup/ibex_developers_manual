> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Imaging Cameras](Imaging-Cameras)

## Imaging Cameras

These are often controlled via their own PCs running bespoke software.  Running an IOC on the camera's control PC allows the instrument control machine to communicate with it.

In general the IMAT instrument scripts create folders on the relevant remote PC for the data to be stored in (using the mapped drives) and then communicates with the IOCs on the remote PC to take data. The remote PCs are mapped to the following drives on the NDX: 

* M: `IMAT-MESSINA-DETECT`
* E: `IMAT-UCB-DETECT`

### Pixelman

This has been run on the `IMAT-UCB-DETECT` machine.

[Pixelman](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Pixelman)

### Andor

The Andor camera is run on the `IMAT-MESSINA-DETECT` machine. It uses an areaDetector IOC to communicate.