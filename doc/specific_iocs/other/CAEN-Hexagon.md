# CAEN Hexagon (MUX Data Acquisition Electronics)

The CAEN hexagon is the data acquisition used on MUX. It is currently controlled by the CAENMCA IOC (`CAENMCA_01`). There are two hexagon hardware boxes, but these are controlled from a single IOC so both hardware stops and starts at the same time. They will look to be running their ISISICP DAE in simulation mode - this is purely to log sample environment data, recently from a McLennan rotation stage. The CAEN IOC syncs run number with the simulated DAE and also writes its own data files. So you will have the usual log and nxs file as per an instrument plus some extra bin and nxs files from the hexagon. The hexagon raw `.bin` files currently have a rather strange timestamp due to a clock issue in the hardware.

Data is published to the usual instrument network archive, but to the `autoreduced` subfolder

The hexagon runs in event mode (which it calls list mode). It is running embedded linux and generates a file locally, this local disk is served via samba and looks like a windows network share. At the end of acquisition the CAEN IOC copies files from the hexagon onto the local computer, runs a script to convert these `.bin` to `.nxs`, then archives both sets of files.

Scripting currently has some extra `begin_hexagons` and `end_hexagons` commands defined in the local python to start/stop acquisition - this also begins a usual simulated DAE run, so **do not** use normal begin and `end`, use the special hexagon commands instead.

## Troubleshooting

Sometimes the hexagon loses connection with the IOC, this can be due to a hexagon spontaneous reboot or it may have hung. If you see errors like `exception in pollerTask: CAENMCA::GetData(): Generic error` then
- try an IOC restart
- try a hexagon power cycle then an IOC restart

After a hexagon power cycle, a register needs to be set on the hexagon using the CAEN MCA2 software to make the event/list mode work properly. The scientists know about this and will do this. 