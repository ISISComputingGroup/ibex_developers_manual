# Blockserver troubleshooting

## Running slowly/PVs not getting into the block archiver

As seen on DETMON when you have a lot of blocks the blockserver but more noticeably the block gateway slow down. At about 300 blocks you could no longer caget block pvs e.g. `TE:NDADETF1:CS:SB:BLOCKNAME` but could camonitor them and the block archiver was able to retrieve most values. At about 800 blocks the block gateway and thus the block archiver and nexus files became unusable, many values were not retrieved by the block archiver from the gateway and subsequently not written to the nexus file. The blockserver also takes a lot longer to start and set up everything correctly as well (including the block archiver).

## Issue with the Config repository

Blockserver log shows the following error:

	MAJOR: Error creating synoptic PV: Lock at 'C:\\Instrument\\Settings\\config\\NDW1298\\.git\\index.lock' could not be obtained
	
and the blockserver fails to do things like load configurations. Re-starting the instrument doesn't make the problem go away. We don't know what causes the blockserver to go in this status, but maybe it happens when an unhandled exception occurs while the blockserver is working on the repository (or maybe in parallel).

In at least one case, this issue seemed to be fixed by simply deleting the `.lock` file indicated in the error message.
If the issue persists, do a `git status` in your local config repository, and if it looks messed up, just delete it and clone it from scratch following the instructions about setting up a configurations directory in the [Getting Started](/overview/First-Time-Build) page.

## 'null' configuration

If your instrument appears to start but the GUI shows `NDWxxxx is UNKNOWN`, check what the current configuration is (in the bottom right of the GUI). If it shows `Current configuration: ` rather than `Current configuration: unknown`, you need to go into the configurations menu and choose a configuration (or create one).

This can happen if the configurations are edited on the filesystem - the blockserver then looks for the last configuration, can't find it, so it goes into this state.

## Restarting the blockserver  

Since the blockserver is essentially an IOC, it can be stopped and restarted in the same way. See [this page](/iocs/testing/Running-IOCs) for more details on restarting.  