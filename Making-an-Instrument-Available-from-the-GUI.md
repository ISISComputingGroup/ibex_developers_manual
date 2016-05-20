> [Wiki](Home) > Deployment

# Making an Instrument Available from the GUI

The new instrument must be added to the list of available instruments, so that users can control it from the Ibex GUI. The list of available instruments is stored in a PV called `CS:INSTLIST`, which runs on the beam status IOC, and is therefore independent of any specific instrument.

The content of the PV is a string in json format, compressed and hexed, for example:

    [{"name": "LARMOR"}, {"name": "ALF"}, {"name": "DEMO"}, {"name": "IMAT"}, {"name": "MUONFE"}]
	
To add a new instrument to this list proceed as follows:

1. Create a new git issue for adding the instrument to the list (for traceability)
1. Check the current PV value from an EPICS terminal: `caget -t -S CS:INSTLIST|uzhex`
1. Write a new value to the PV with the new instrument appended. To write a new compressed and hexed value to PV there is a utility Python script `C:\Instrument\Apps\EPICS\ISIS\inst_servers\master\scripts\hex_compress_and_put_pv.py`. This script may not run from its location in the `scripts\` directory, you may have to copy it one level up and run it from there.
1. Verify that all the instruments are picked up by the GUI (e.g. there are no parsing errors): `IBEX -> Switch Instrument`