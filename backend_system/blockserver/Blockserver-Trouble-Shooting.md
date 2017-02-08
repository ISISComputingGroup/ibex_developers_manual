> [Wiki](Home) > [Trouble-shooting](trouble-shooting-pages) > Blockserver trouble shooting

## Issue with the Config repository

Blockserver log shows the following error:

	MAJOR: Error creating synoptic PV: Lock at 'C:\\Instrument\\Settings\\config\\NDW1298\\.git\\index.lock' could not be obtained
	
and the blockserver fails to do things like load configurations. Re-starting the instrument doesn't make the problem go away. We don't know what causes the blockserver to go in this status, but maybe it happens when an un-handled exception occurs while the blockserver is working on the repository (or maybe in parallel).

In at least one case, this issue seemed to be fixed by simply deleting the `.lock` file indicated in the error message.
If the issue persists, do a `git status` in your local config repository, and if it looks messed up, just delete it and clone it from scratch following the instructions about setting up a configurations directory in the [Getting Started](First-time-installing-and-building-(Windows)) page.

## 'null' configuration

If the instrument appears to start but the GUI shows 'unknown', check what the current configuration is (in the bottom right of the GUI). If it shows `Current configuration: ` rather than `Current configuration: unknown`, you need to go into the configurations menu and choose a configuration (or create one).

This can happen if the configurations are edited on the filesystem - the blockserver then looks for the last configuration, can't find it, so goes into this state.