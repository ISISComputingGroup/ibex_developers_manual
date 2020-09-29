The ISISICP can write an event mode NeXus data file incrementally during the run rather than replaying all events at run end, this means it will take up disk space more gradually rather than grabbing an extra large amount at the end. It will ultimately use the same amount of disk space, but it is easier to judge when to end a run. Also the data file will appear on the archive earlier. The program still needs to save the events to disk as well as write the data file incrementally as an HDF5 file can become corrupt if the program restarts.

To enable incremental mode edit `isisicp.properties` in `C:\labview modules\dae` and add/uncomment lines saying
``` 
isisicp.incrementaleventnexus = true
isisicp.kafkastream = true
``` 
The changes will not take effect until you restart the ISISICP program - make sure you are in SETUP and any runs have finished saving, then kill the `ISISICP` process using task manager (you can restart seci/ibex if you prefer, but that is not necessary)

After this is enabled, you can also run Mantid on any computer and use the kafka live listener to view and process events live during the run.
