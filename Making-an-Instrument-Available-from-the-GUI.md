> [Wiki](Home) > [Deployment](Deployment) > [Making an Instrument Available from the GUI](Making-an-Instrument-Available-from-the-GUI)

The new instrument must be added to the list of available instruments so that users can control it from the Ibex GUI. The list of available instruments is stored in a PV called `CS:INSTLIST`, which runs on the beam status IOC, and is therefore independent of any specific instrument.

The content of the PV is a string in json format, compressed and hexed, for example:

```
[
        {"name": "LARMOR", "hostName": "NDXLARMOR", "pvPrefix": "IN:LARMOR:", "isScheduled": true},
        {"name": "ALF", "hostName": "NDXALF", "pvPrefix": "IN:ALF:", "isScheduled": true},
        {"name": "DEMO", "hostName": "NDXDEMO", "pvPrefix": "IN:DEMO:", "isScheduled": false},
        {"name": "IMAT", "hostName": "NDXIMAT", "pvPrefix": "IN:IMAT:", "isScheduled": true},
        {"name": "MUONFE", "hostName": "NDEMUONFE", "pvPrefix": "IN:MUONFE:", "isScheduled": false},
        {"name": "ZOOM", "hostName": "NDXZOOM", "pvPrefix": "IN:ZOOM:", "isScheduled": true},
        {"name": "IRIS", "hostName": "NDXIRIS", "pvPrefix": "IN:IRIS:", "isScheduled": true},
]
```

To add a new instrument to this list proceed as follows:

1. Create a new git issue for adding the instrument to the list (for traceability)
1. Check the current PV value from an EPICS terminal: `caget -t -S CS:INSTLIST|uzhex`
1. Edit the instrument list update script to include the new instrument `...EPICS\ISIS\inst_servers\master\scripts\set_instrument_list.py`
1. Create a pull request and get it flash reviewed.
1. Run the script.
1. Verify that all the instruments are picked up by the GUI (e.g. there are no parsing errors): `IBEX -> Switch Instrument` and that they have the correct alarm server and configuration loaded.
1. Verify that the web dashboard for the instruments still works
1. Verify that the [ExperimentDetailsPopulator](Experimental-Database) has updated with the new list
