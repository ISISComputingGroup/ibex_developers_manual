# CAEN Hexagon (MUX Data Acquisition Electronics)

The CAEN hexagon is the data acquisition used on MUX. It is currently controlled by the CAENMCA IOC (`CAENMCA_01`). There are two hexagon hardware boxes, but these are controlled from a single IOC so both hardware stops and starts at the same time. They will be running their ISISICP DAE in simulation mode which is purely to log sample environment data, recently from a McLennan rotation stage. To avoid confusing users simulation mode is not printed in the dashboard. The CAEN IOC syncs run number with the simulated DAE and also writes its own data files. So you will have the usual log and nxs file as per an instrument plus some extra bin and nxs files from the hexagon. The hexagon raw `.bin` files currently have a rather strange file timestamp due to a clock issue in the hexagon hardware.

Data is published to the usual instrument network archive on `d:`, but to the `autoreduced` subfolder at the moment

The hexagon runs in event mode (which it calls list mode). It is running embedded linux and generates a file locally, this local disk is served via samba and looks like a windows network share. At the end of acquisition the CAEN IOC copies files from the hexagon onto the local computer, runs a script to convert these `.bin` to `.nxs`, then archives both sets of files. The ISISICP also saves a nexus file, but this has suffix `.nxs_se`. The `.nxs` file that is generated contains a link to open the sample environment from `.nxs_se` so both files are needed for analysis.

Scripting uses usual `begin` and `end` commands, however these have local modifications to start the hexagon which in turn starts the simulated ISISDAE/isisicp. Run numbers are synced between hexagon and simulated DAE, the custom dashboard db has been changed to read values from the hexagon not the ISISDAE ioc.

Files on the hexagon digitiser have names like `HEX0_00000213_ch0.bin` - there are 2 hexagons with 2 channels, so 4 files in all like this. The end of a run goes like:
- CAENMCA_01 IOC stops hexagon from acquiring and stops ISISDAE too
- CAENMCA_01 creates an initial `.nxs` file - this contains all information except hexagon events from the *.bin files
- The `copydata.bat` script is spawned which then
- - reopens the `.nxs` and then reads all the `*.bin` to insert events into the file
- - moves the `*.bin` and `*.nxs*` files to the archive
 
## Troubleshooting

Sometimes the hexagon loses connection with the IOC, this can be due to a hexagon spontaneous reboot or it may have hung. If you see errors like `exception in pollerTask: CAENMCA::GetData(): Generic error` then
- try an IOC restart
- try a hexagon power cycle then an IOC restart

After a hexagon power cycle, a timing register needs to be set on the hexagon using the CAEN MCA2 vendor software to make the event/list mode work properly. The scientists know about this and will do this. 
