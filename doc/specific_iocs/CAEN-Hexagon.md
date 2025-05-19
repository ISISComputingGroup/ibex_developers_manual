# CAEN Hexagon (MUX Data Acquisition Electronics)

The CAEN hexagon is the data acquisition used on MUX. It is currently controlled by the CAENMCA IOC, of which they run two instances for the two hexagons. They also run their DAE in simulation mode to log sample environment data, then the CAEN syncs run number with the DAE and writes its own data files. So you will have the ususal log and nxs file as per an instrument plus some extra bin and nxs files from the hexagon. The hexagon raw files currently have a rather strange timestamp.  

Data is publicised to the ususal archive, but to the "autoreduced" subfolder

scripting currently has some extra `begin_hexagons` and `end_hexagons` commands defined in the local python to start/stop acquision - this also begibns a ususal run, so do not use normal begin command

