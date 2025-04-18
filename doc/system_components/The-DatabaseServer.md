# Database Server 

The DatabaseServer is a Channel Access Server (CAS) written in Python using the [PCASpy](https://code.google.com/archive/p/pcaspy/) module.

The DatabaseServer serves the following information from the instrument database:

* Details about the IOCs
* Names of all the "interesting" PVs for the currently running IOCs
* Names of the sample and beamline parameter PVs.

It is also updates the database if the run status of an IOC changes.

The names of the beamline and sample parameter PVs are read from a database.

## Channel Access Commands ##

To dehex and decompress see "Reading a Compressed Hex PV": https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Running-IOCs

### Read Commands ###

**BLOCKSERVER:IOCS**

```
    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:IOCS
    Returns a dictionary of IOCs, their statuses and their available macros/pvsets as compressed and hexed JSON (CHAR waveform). 
    The pattern field of a macro gives the regex of allowed values for that macro.
    Example JSON (dehexed and decompressed):
        '{"TPG300_01": 
            {"running": False,
			"macros": [
				{"name": "COMPORT", "description": "Port used to communicate", "pattern": "COM[0-9]+", "hasDefault": "NO"},
				{"name": "TESTMACRO", "description": "A macro I invented for testing", "pattern": ".*", "defaultValue": "someValue", "hasDefault": "YES"}]
			"pvsets": [
				{"name": "Motor Limits", "description": "Motor high and low limits"},
				{"name": "Test Set", "description": "An example pv set"}]
			},
          "SIMPLE": 
            {"running": True,
			"macros": [
				{"name": "TESTMACRO", "description": "A macro I invented for testing", "pattern": ".*", "hasDefault": "UNKNOWN"}]
			"pvsets": [
				{"name": "Test Set", "description": "An example pv set"}]
			},
         }'
```

**BLOCKSERVER:IOCS_NOT_TO_STOP**

```
    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:IOCS_NOT_TO_STOP
    Returns a list of the IOCs that cannot be stopped as compressed then hexed JSON (CHAR waveform)
    Example JSON (dehexed and decompressed):
        '[
            "INSTETC", "PSCTRL", "ISISDAE", "BLOCKSVR", "ARINST", "ARBLOCK", "GWBLOCK", "RUNCTRL"
         ]'
```

**BLOCKSERVER:SAMPLE_PARS**

```
    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:SAMPLE_PARS
    Returns the names of the sample parameters as compressed then hexed JSON (CHAR waveform)
    Example JSON (dehexed and decompressed):
        '[
            "PARS:SAMPLE:AOI", "PARS:SAMPLE:GEOMETRY", "PARS:SAMPLE:HEIGHT", "PARS:SAMPLE:NAME",
            "PARS:SAMPLE:PHI", "PARS:SAMPLE:THICK", "PARS:SAMPLE:WIDTH"
         ]'
```

**BLOCKSERVER:BEAMLINE_PARS**

```
    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:BEAMLINE_PARS
    Returns the names of the beamline parameters as compressed then hexed JSON (CHAR waveform)
    Example JSON (dehexed and decompressed):
        '[
            "PARS:BL:A1", "PARS:BL:A2", "PARS:BL:A3", "PARS:BL:BCX", "PARS:BL:BCY", "PARS:BL:BEAMSTOP:POS",
            "PARS:BL:CHOPEN:ANG", "PARS:BL:FOEMIRROR", "PARS:BL:JOURNAL:BLOCKS", "PARS:BL:L1", "PARS:BL:SDD"
         ]'
```

**BLOCKSERVER:PVS:INTEREST:HIGH**

```
    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:PVS:INTEREST:HIGH
    Gets the details for PVs with an interest level of "HIGH".
    Returns a compressed and hexed JSON list of interesting PVs.
    Example JSON (dehexed and decompressed):
        '[
            ["IN:DEMO:SIMPLE:VALUE1", "ai", "A description", "SIMPLE"],
            ["IN:DEMO:SIMPLE:VALUE2", "ai", "Another description", "SIMPLE"]
         ]'
```

**BLOCKSERVER:PVS:INTEREST:MEDIUM**

```
    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:PVS:INTEREST:MEDIUM
    Gets the details for PVs with an interest level of "MEDIUM".
    Returns a compressed and hexed JSON list of interesting PVs.
    Example JSON (dehexed and decompressed):
        '[
            ["IN:DEMO:SIMPLE:VALUE1", "ai", "A description", "SIMPLE"],
            ["IN:DEMO:SIMPLE:VALUE2", "ai", "Another description", "SIMPLE"]
         ]'
```

**BLOCKSERVER:PVS:ACTIVE**

```
    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:PVS:ACTIVE
    Gets the details for PVs in running IOCs with an interest level of "HIGH".
    Returns a compressed and hexed JSON list of interesting PVs.
    Example JSON (dehexed and decompressed):
        '[
            ["IN:DEMO:SIMPLE:VALUE1", "ai", "A description", "SIMPLE"],
            ["IN:DEMO:SIMPLE:VALUE2", "ai", "Another description", "SIMPLE"]
         ]'
```

**BLOCKSERVER:PVS:ALL**

```
    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:PVS:ALL
    Gets the details for all with an interest level.
    Returns a compressed and hexed JSON list of PVs.
    Example JSON (dehexed and decompressed):
        '[
            ["IN:DEMO:SIMPLE:VALUE1", "ai", "A description", "SIMPLE"],
            ["IN:DEMO:SIMPLE:VALUE2", "ai", "Another description", "SIMPLE"]
         ]'
```

**BLOCKSERVER:INTERESTING_PVS:_ioc_:_level_**

```
    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:INTERESTING_PVS:*ioc*:*level*
    Gets the details for PVs within the ioc *ioc* and with an interest level of *level*.
    Returns a compressed and hexed JSON list of interesting PVs.
    Example JSON (dehexed and decompressed):
        '[
            ["IN:DEMO:SIMPLE:VALUE1", "ai", "A description", "SIMPLE"],
            ["IN:DEMO:SIMPLE:VALUE2", "ai", "Another description", "SIMPLE"]
         ]'
```		 
