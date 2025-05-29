# CAEN Hexagon (MUX Data Acquisition Electronics)

The CAEN hexagon is the data acquisition used on MUX. It is currently controlled by the CAENMCA IOC (`CAENMCA_01`). There are two hexagon hardware boxes, but are controlled from a single IOC so they are stopped and started at the same time. They also run their DAE in simulation mode to log sample environment data, then the CAEN syncs run number with the DAE and writes its own data files. So you will have the usual log and nxs file as per an instrument plus some extra bin and nxs files from the hexagon. The hexagon raw `.bin` files currently have a rather strange timestamp due to a clock issue in the hardware.   

Data is published to the usual instrument network archive, but to the `autoreduced` subfolder

scripting currently has some extra `begin_hexagons` and `end_hexagons` commands defined in the local python to start/stop acquisition - this also begins a usual run, so do not use normal begin commands. Do not use `begin` and `end` - this will just start a simulated DAE run, use the special hexagon commands mentioned previously.

## Troubleshooting

Sometimes the hexagon loses connection with the IOC, this can be due to a hexagon spontaneous reboot or it may have hung. If you see errors like `exception in pollerTask: CAENMCA::GetData(): Generic error` then
- try an IOC restart
- try a hexagon power cycle then an IOC restart
