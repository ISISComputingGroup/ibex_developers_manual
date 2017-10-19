# Building SECI
SECI only builds on VS2010.
There is a build setup on NDXICAP.
VS2010 must be started in Admin mode.

# Layout
SECI's code is separated out into two parts - `Seci` which contains the backend, and `SeciUserInterface` which as the name suggests contains all the UI code. The different controls have their own sub folders in 

Seci is installed on the instrument at `C:\Program Files (x86)\STFC ISIS Facility\SECI`
The configurations are in the same folder.

# Updating SECI on an instrument
1. Copy 'C:\Program Files (x86)\STFC ISIS Facility\SECI\SeciUserInterface.exe.config` to somewhere safe.
1. Uninstall SECI via control panel
1. Run the latest version of the installer
1. Replace the new 'C:\Program Files (x86)\STFC ISIS Facility\SECI\SeciUserInterface.exe.config` with the one from the first step
1. Start SECI
1. Stop SECI
1. Navigate to `C:\Users\spudulike\AppData\Local\STFC_Rutherford_Appleton_` and enter the most recently modified directory
1. Enter the 2nd most recently directory (something like `1.0.15.23588`) copy the `user.config` file.
1. Go back up one directory and enter the most recently changed folder.
1. Copy `user.config` into there
1. Start SECI

