# Adding an instrument to the instrument list

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

## Restricting the GUI to switching to a reduced set of instruments
On the IDaaS machines we need to be able to limit the instruments that a user can switch to in the GUI, to protect the data of other users. This is performed by adding a whitelist to the instrument preferences supplier. This needs to be applied for each VM group that needs to be restricted.

This shouldn't get overwritten during the RPM deploy as the preferences folder is created by the GUI when it first starts, and isn't in the build.

1. Locate the preferences supplier in the VM group (`Client_E4\plugins\uk.ac.stfc.isis.ibex.instrument_1.0.0.SNAPSHOT\resources\allowed_groups.conf`).
1. Add the following line to the preferences file, replacing the instrument names for those which the users of this group are allowed to access:
`MUONS,SANS`
   - This would allow the GUI to only switch to MUON or SANS instruments from the switch instrument dialogue
   - The definitive list of group names is in the instrument list, set by `inst_servers\scripts\set_instrument_list.py`