> [Wiki](Home) > [The Backend System](The-Backend-System) > [System components](System-components) > BlockServer

The BlockServer is **responsible** for:

* Creating blocks
* Creating groups
* Loading and saving configurations

It can also be used to:

* Start and stop IOCs via ProcServ

See [BlockServer Structure](BlockServer-Structure) for further information.

------------
What it does
------------
The BlockServer is a Channel Access Server (CAS) written in Python using the [PCASpy](https://code.google.com/archive/p/pcaspy/) module.
It provides a number of PVs that allow the blocks to be configured (see below) and configurations to be created and loaded.
The blocks are PV aliases created using the blocks gateway - a standard [channel access gateway](Access-Gateway) running on localhost. When a configuration is loaded or the blocks changed then the BlockServer regenerates the PV file for the gateway. 

The PV file is typically stored in `C:\Instrument\Settings\gwblock.pvlist` and looks something like this:

    INST:CS:SB:MyBlock\([.:].*\)    ALIAS    INST:EUROTHRM_01:TEMP\1
    INST:CS:SB:MYBLOCK\([.:].*\)    ALIAS    INST:EUROTHRM_01:TEMP\1
    INST:CS:SB:MyBlock\(:RC.*\)     ALIAS    INST:CS:MYBLOCK\1
    INST:CS:SB:MYBLOCK\(:RC.*\)     ALIAS    INST:CS:MYBLOCK\1

Pattern matching is used so that patterns like BLOCKNAME:SP and BLOCKNAME:SP:RBV can be used, aliases are created for both the case specified by the user and full uppercase so that clients can be case insensitive. Once this file is written the BlockServer will restart the gateway, running as `GWBLOCK`. The `RC` lines are used for [Run Control](Run-control), which the BlockServer is also responsible for configuring. Run control PVs live in a separate IOC (which also adds case insensitive aliases) with the `CS` namespace and the gateway moves them into the `CS:SB` namespace. In this way all client interactions with specific blocks are going through `GWBLOCK`.

It is possible to override the blockserver generation of a `gwblock.pvlist` and block_config.xml for a configuration by setting the `configuresBlockGWAndArchiver` tag to true in the meta.xml file and providing the files in the same directory as the `meta.xml` file. This is used on DETMON to manage a large set of blocks. If the configuration directory does not contain the `gwblock.pvlist` or `block_config.xml` files then the blockserver will instead generate the relevant files even if the `configuresBlockGWAndArchiver` tag is true. If the tag is true and the configuration directory only contains one of the files, the blockserver will use the file the configuration contains and generate the other.

The BlockServer is also responsible for configuring the blocks archiver to log the current blocks.

Configurations are saved in a directory with the configuration's name. The directory contains separate XML files for the blocks, groups, components, IOCs and meta-data that make up the configuration.

The BlockServer also provides a mechanism for starting and stopping IOCs and retrieving the interesting PVs for the currently running IOCs. The BlockServer can start and stop IOCs that are running inside [ProcServ](http://sourceforge.net/projects/procserv/) as ProcServ provides PVs to enable this. The PVs for the currently running IOCs are read directly from a database.

NOTE: As the BlockServer often needs to send a lot of data via channel access (as a CHAR waveform), it it necessary in some cases to compress the data before sending using zlib. The compressed data is then converted to hex to avoid any null characters been sent across channel access.

-----------------------
Channel Access Commands
-----------------------

-------------
Read Commands
-------------

**BLOCKSERVER:BLOCKNAMES**
Note: this used by genie_python for checking block names used in CSETs etc. are valid

    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:BLOCKNAMES
    Returns the block names as compressed and hexed JSON list (CHAR waveform)

**BLOCKSERVER:BLOCK_DETAILS**

    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:BLOCK_DETAILS
    TODO: add description

**BLOCKSERVER:BLOCK_RULES**
```
    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:BLOCK_RULES
    Returns the rules for naming blocks. Specifically, a regex that new blocks must match and specific blocknames which are disallowed are returned.
    Example JSON: {"regex": "^[a-zA-Z]\\w*$", "regexMessage": "Block name must start with a letter and only contain letters, numbers and underscores", "disallowed": ["lowlimit", "highlimit", "runcontrol", "wait"]}
```
**BLOCKSERVER:GROUPS**
Note: This PV is currently used by the web dashboard

    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:GROUPS
    Returns the groups and their blocks as a compressed then hexed JSON list of dictionaries (CHAR waveform).
    Example JSON (dehexed and decompressed):
        '[{"blocks": ["testblock1", "testblock2"], "name": "Example group", "component": null},
          {"blocks": ["testblock3", "testblock4"], "name": "Different group", "component": null},
          {"blocks": [], "name": "NONE", "component": null}
         ]'

**BLOCKSERVER:GROUP_RULES**

    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:GROUP_RULES
    TODO: add description

**BLOCKSERVER:CONFIGS**

    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:CONFIGS
    Returns a list of the available configurations, including descriptions and the pv associated with the configuration, as compressed then hexed JSON (CHAR waveform)
	Example JSON (dehexed and decompressed):
		'[{"name": "Test Config", "description": "A test configuration", "pv": "TEST_CONFIG"}
		  {"name": "Another Config", "description": "To test again", "pv": "ANOTHER_CONFIG"}
		  {"name": "TeSt CoNfIg", "description": "This config has the same name", "pv": "TEST_CONFIG1"}]'
	
**BLOCKSERVER:COMPS**

    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:COMPS
    Returns a list of the components available, including descriptions and the pv associated with the configuration, as compressed then hexed JSON (CHAR waveform)
		'[{"name": "Test component", "description": "A test component", "pv": "TEST_COMP"}
		  {"name": "Another component", "description": "To test again", "pv": "ANOTHER_COMP"}
		  {"name": "TeSt ComPonent", "description": "This component has the same name", "pv": "TEST_COMP1"}]'

**BLOCKSERVER:ALL_COMPONENT_DETAILS**

    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:ALL_COMPONENT_DETAILS
    Returns a list of the available components with all their details, as if reading e.g. the current configuration. Read as compressed then hexed JSON (CHAR waveform)
        [{
            "blocks": [{"log_rate": 30, "log_deadband": 0.0, "component": null, "runcontrol": false, "visible": true, "pv": "TE:NDLT882:DAE:BEAMCURRENT", "name": "BEAMCURR", "highlimit": 0.0, "log_periodic": true, "lowlimit": 0.0, "local": true}], 
            "groups": [{"component": null, "blocks": ["BEAMCURR"], "name": "NONE"}], 
            "iocs": [{"macros": [], "pvs": [{"name": "NEW_PV", "value": "NEW_VALUE"}], "name": "GALIL_01", "autostart": false, "pvsets": [], "component": null, "restart": false, "simlevel": "recsim"}], 
            "description": "pong", 
            "component_iocs": [{"macros": [], "pvs": [{"name": "NEW_PV", "value": "NEW_VALUE"}], "name": "GALIL_01", "autostart": false, "pvsets": [], "component": null, "restart": false, "simlevel": "recsim"}],
            "components": [],
            "history": ["2017-02-08 16:34:15"],
            "synoptic": "", 
            "name": "TEST_COMP2" 
        },
        {
            "blocks": [],
            "groups": [],
            "iocs": [{"macros": [], "pvs": [], "name": "CRYVALVE_01", "autostart": false, "pvsets": [], "component": null, "restart": true, "simlevel": "none"}],
            "description": "ping",
            "component_iocs": [{"macros": [], "pvs": [], "name": "CRYVALVE_01", "autostart": false, "pvsets": [], "component": null, "restart": true, "simlevel": "none"}],
            "components": [], "history": ["2017-02-08 16:30:40"], 
            "synoptic": "", 
            "name": "TEST_COMP1"
        }
        , ...]

**BLOCKSERVER:GET_RC_OUT**

    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:GET_RC_OUT
    Returns a list of the PVs that are outside of their run-control limits as compressed then hexed JSON (CHAR waveform)

**BLOCKSERVER:GET_RC_PARS**

    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:GET_RC_PARS
    Returns a dictionary of the run-control settings for the blocks as compressed then hexed JSON (CHAR waveform)

**BLOCKSERVER:GET_CURR_CONFIG_DETAILS**

    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:GET_CURR_CONFIG_DETAILS
    Returns a compressed and hexed JSON dictionary describing the current configuration or component.
    Example JSON (dehexed and decompressed):
        '{"iocs":
                 [{"simlevel": "None", "autostart": true, "restart": false, "pvsets": [{"name": "SET", "enabled": "true"}], "pvs": [], "macros": [], "name": "SIMPLE1", "component": null},
                  {"simlevel": "devsim", "autostart": true, "restart": false, "pvsets": [{"name": "SET", "enabled": "true"}], "pvs": [], "macros": [], "name": "SIMPLE2", "component": null}
                 ],
          "blocks":
                   [{"name": "testblock1", "local": true, "pv": "NDWXXX:xxxx:SIMPLE:VALUE1", "component": null, "visible": true, "log_periodic": true, "log_rate": 10, "log_deadband": 0},
                    {"name": "testblock2", "local": true, "pv": "NDWXXX:xxxx:SIMPLE:VALUE1", "component": null, "visible": true, "log_periodic": true, "log_rate": 5, "log_deadband": 0},
                    {"name": "testblock3", "local": true, "pv": "NDWXXX:xxxx:EUROTHERM1:RBV", "component": null, "visible": true, "log_periodic": false, "log_rate": 0, "log_deadband": 1.0}
                   ],
          "components":
                       [{"name": "comp1"}],
          "groups":
                   [{"blocks": ["testblock1"], "name": "Group1", "component": null},
                    {"blocks": ["testblock2"], "name": "Group2", "component": null},
                    {"blocks": ["testblock3"], "name": "NONE", "component": null}],
          "name": "TESTCONFIG1",
		  "description": "A test configuration",
		  "history": ["2015-02-16"]
         }'

**BLOCKSERVER:*config_pv*:GET_CONFIG_DETAILS**

	Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:*config_pv*:GET_CONFIG_DETAILS
	Returns a compressed and hexed JSON dictionary describing the configuration with the pv *config_pv*. (To find config pvs use the CONFIGS command)
	Example JSON (dehexed and decompressed):
        '{"iocs":
                 [{"simlevel": "None", "autostart": true, "restart": false, "pvsets": [{"name": "SET", "enabled": "true"}], "pvs": [], "macros": [], "name": "SIMPLE1", "component": null},
                  {"simlevel": "devsim", "autostart": true, "restart": false, "pvsets": [{"name": "SET", "enabled": "true"}], "pvs": [], "macros": [], "name": "SIMPLE2", "component": null}
                 ],
          "blocks":
                   [{"name": "testblock1", "local": true, "pv": "NDWXXX:xxxx:SIMPLE:VALUE1", "component": null, "visible": true, "log_periodic": true, "log_rate": 10, "log_deadband": 0},
                    {"name": "testblock2", "local": true, "pv": "NDWXXX:xxxx:SIMPLE:VALUE1", "component": null, "visible": true, "log_periodic": true, "log_rate": 5, "log_deadband": 0},
                    {"name": "testblock3", "local": true, "pv": "NDWXXX:xxxx:EUROTHERM1:RBV", "component": null, "visible": true, "log_periodic": false, "log_rate": 0, "log_deadband": 1.0}
                   ],
          "components":
                       [{"name": "comp1"}],
          "groups":
                   [{"blocks": ["testblock1"], "name": "Group1", "component": null},
                    {"blocks": ["testblock2"], "name": "Group2", "component": null},
                    {"blocks": ["testblock3"], "name": "NONE", "component": null}],
          "name": "TESTCONFIG1",
		  "description": "A test configuration",
		  "history": ["2015-02-16"]
         }'	
		 
**BLOCKSERVER:*component_pv*:GET_COMPONENT_DETAILS**

	Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:*component_pv*:GET_COMPONENT_DETAILS
	Returns a compressed and hexed JSON dictionary describing the component with the pv *component_pv*. (To find component pvs use the COMPS command)
 	Example JSON (dehexed and decompressed):
        '{"iocs":
                 [{"simlevel": "None", "autostart": true, "restart": false, "pvsets": [{"name": "SET", "enabled": "true"}], "pvs": [], "macros": [], "name": "SIMPLE1", "component": null},
                  {"simlevel": "devsim", "autostart": true, "restart": false, "pvsets": [{"name": "SET", "enabled": "true"}], "pvs": [], "macros": [], "name": "SIMPLE2", "component": null}
                 ],
          "blocks":
                   [{"name": "testblock1", "local": true, "pv": "NDWXXX:xxxx:SIMPLE:VALUE1", "component": null, "visible": true, "log_periodic": true, "log_rate": 10, "log_deadband": 0},
                    {"name": "testblock2", "local": true, "pv": "NDWXXX:xxxx:SIMPLE:VALUE1", "component": null, "visible": true, "log_periodic": true, "log_rate": 5, "log_deadband": 0},
                    {"name": "testblock3", "local": true, "pv": "NDWXXX:xxxx:EUROTHERM1:RBV", "component": null, "visible": true, "log_periodic": false, "log_rate": 0, "log_deadband": 1.0}
                   ],
          "components": [],
          "groups":
                   [{"blocks": ["testblock1"], "name": "Group1", "component": null},
                    {"blocks": ["testblock2"], "name": "Group2", "component": null},
                    {"blocks": ["testblock3"], "name": "NONE", "component": null}],
          "name": "TESTCOMP1",
		  "description": "A test component",
		  "history": ["2015-02-16"]
         }'	
		 
**BLOCKSERVER:BLANK_CONFIG**

	Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:BLANK_CONFIG
	Returns a compressed and hexed JSON dictionary describing a blank configuration.
        '{"iocs": [],
          "blocks": [],
          "components": [],
          "groups": [],
          "name": "",
		  "description": ""
         }'	

**BLOCKSERVER:CONF_DESC_RULES**

    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:CONF_DESC_RULES
    TODO: add description	

**BLOCKSERVER:*component_pv*:DEPENDENCIES**

    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:*component_pv*:DEPENDENCIES
    Returns a list of the configurations that contain the component specified in *component_pv*, formatted as compressed then hexed JSON (CHAR waveform)


**BLOCKSERVER:SERVER_STATUS**

    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:SERVER_STATUS
    TODO: add description

**BLOCKSERVER:BUMPSTRIP_AVAILABLE**

    Command: caget %MYPVPREFIX%CS:BLOCKSERVER:BUMPSTRIP_AVAILABLE
    TODO: add description

**BLOCKSERVER:GET_SCREENS**

    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:GET_SCREENS
    Returns a compressed and hexed string containing the XML for the list of the available device screens descriptions (CHAR waveform)

**BLOCKSERVER:SCREENS_SCHEMA**

    Command: caget -S %MYPVPREFIX%CS:BLOCKSERVER:SCREENS_SCHEMA
    Returns a compressed and hexed string containing the devices screens XML schema (CHAR waveform)

**BLOCKSERVER:CURR_CONFIG_NAME**

    Command: caget %MYPVPREFIX%CS:BLOCKSERVER:CURR_CONFIG_NAME
    Returns a string containing the name of the current configuration (CHAR waveform)

**SYNOPTICS:NAMES**

    Command: caget -S %MYPVPREFIX%CS:SYNOPTICS:NAMES
    Returns a list of the available synoptics formatted as compressed then hexed JSON (CHAR waveform)

**SYNOPTICS:*synoptic_name*:GET**

    Command: caget -S %MYPVPREFIX%CS:SYNOPTICS:*synoptic_name*:GET
    Returns a compressed and hexed string containing the XML for the specified synoptic (CHAR waveform)

**SYNOPTICS:GET_DEFAULT**

    Command: caget -S %MYPVPREFIX%CS:SYNOPTICS:GET_DEFAULT
    Returns a compressed and hexed string containing the XML for the current synoptic (CHAR waveform)

**SYNOPTICS:\__BLANK\__:GET**

    Command: caget -S %MYPVPREFIX%CS:SYNOPTICS:__BLANK__:GET
    TODO: add description

**SYNOPTICS:SCHEMA**

    Command: caget -S %MYPVPREFIX%CS:SYNOPTICS:SCHEMA
    Returns a compressed and hexed string containing the synoptics XML schema (CHAR waveform)

		 
--------------
Write Commands
--------------
| NOTE: Unless specified otherwise all of these command return OK if they succeed, otherwise they return an error message.
| NOTE: Some of these commands take a few seconds to process, so if done using caput it might be necessary to increase the timeout.
|

**BLOCKSERVER:LOAD_CONFIG**

    Command: caput -S %MYPVPREFIX%CS:BLOCKSERVER:LOAD_CONFIG config1234567890
    Loads the specified configuration. Requires a compressed and hexed JSON string. This automatically restarts the blocks gateway and updates the archiver

    Returns "OK" or an error message (compressed and hexed JSON).
    
**BLOCKSERVER:CLEAR_CONFIG**

    Command: caput -S %MYPVPREFIX%CS:BLOCKSERVER:CLEAR_CONFIG clear
    Send any non-null value to clear the current configuration, i.e. remove blocks, groups and IOCs.
    Note: it does not restart the gateway.

    Returns "OK" or an error message (compressed and hexed JSON).

**BLOCKSERVER:START_IOCS**

    Command: caput -S %MYPVPREFIX%CS:BLOCKSERVER:START_IOCS config1234567890
    Starts the specified IOC or IOCs. Requires compressed and hexed JSON list of IOCS.

    Returns "OK" or an error message (compressed and hexed JSON).

**BLOCKSERVER:STOP_IOCS**

    Command: caput -S %MYPVPREFIX%CS:BLOCKSERVER:STOP_IOCS config1234567890
    Stops the specified IOC or IOCS. Requires compressed and hexed JSON list of IOCS.

    Returns "OK" or an error message (compressed and hexed JSON).

**BLOCKSERVER:RESTART_IOCS**


    Command: caput -S %MYPVPREFIX%CS:BLOCKSERVER:RESTART_IOCS config1234567890
    Restarts the specified IOC or IOCs. Requires compressed and hexed JSON list of IOCS.

    Returns "OK" or an error message (compressed and hexed JSON).

**BLOCKSERVER:SET_RC_PARS**

    Command: caput -S %MYPVPREFIX%CS:BLOCKSERVER:SET_RC_PARS config1234567890
    Edits the run-control settings on a block or blocks. Requires compressed and hexed JSON dictionary of dictionaries with the following parameters:
        name - the name of the block
        LOW - the lowlimit
        HIGH - the highlimit
        ENABLE - whether run-control is enable for the block
    Example JSON (dehexed and decompressed):
        '{"testblock": {"HIGH": 5, "ENABLE": true, "LOW": -5}}'

    Returns "OK" or an error message (compressed and hexed JSON).


**BLOCKSERVER:SET_CURR_CONFIG_DETAILS**

    Command: caput -S %MYPVPREFIX%CS:BLOCKSERVER:SET_CURR_CONFIG_DETAILS config1234567890
    Sets the current configuration to the setting specified. Requires compressed and hexed JSON dictionary.
    Example JSON (dehexed and decompressed):
        '{"iocs":
                 [{"simlevel": "None", "autostart": true, "restart": false, "pvsets": [{"name": "SET", "enabled": "true"}], "pvs": [], "macros": [], "name": "SIMPLE1", "component": null},
                  {"simlevel": "recsim", "autostart": true, "restart": false, "pvsets": [{"name": "SET", "enabled": "true"}], "pvs": [], "macros": [], "name": "SIMPLE2", "component": null}
                 ],
          "blocks":
                   [{"name": "testblock1", "local": true, "pv": "NDWXXX:xxxx:SIMPLE:VALUE1", "component": null, "visible": true, "log_periodic": true, "log_rate": 10, "log_deadband": 0},
                    {"name": "testblock2", "local": true, "pv": "NDWXXX:xxxx:SIMPLE:VALUE1", "component": null, "visible": true, "log_periodic": true, "log_rate": 5, "log_deadband": 0},
                    {"name": "testblock3", "local": true, "pv": "NDWXXX:xxxx:EUROTHERM1:RBV", "component": null, "visible": true, "log_periodic": false, "log_rate": 0, "log_deadband": 1.0}
                   ],
          "components":
                       [{"name": "comp1"}],
          "groups":
                   [{"blocks": ["testblock1"], "name": "Group1", "component": null},
                    {"blocks": ["testblock2"], "name": "Group2", "component": null},
                    {"blocks": ["testblock3"], "name": "NONE", "component": null}],
          "name": "TESTCONFIG1",
		  "description": "A test configuration",
		  "history": ["2015-02-16"]
         }'

**BLOCKSERVER:SAVE_NEW_CONFIG**

	Command: caput -S %MYPVPREFIX%CS:BLOCKSERVER:SAVE_NEW_CONFIG config1234567890
	Saves a configuration to XML without affecting the current active configuration.
	This will give an error if trying to overwrite the current active configuration but will allow overwriting of other saved configurations.
	Requires compressed and hexed JSON dictionary.
	
	Example JSON (dehexed and decompressed):
		'{"iocs":
				 [{"simlevel": "None", "autostart": true, "restart": false, "pvsets": [{"name": "SET", "enabled": "true"}], "pvs": [], "macros": [], "name": "SIMPLE1", "component": null},
				  {"simlevel": "recsim", "autostart": true, "restart": false, "pvsets": [{"name": "SET", "enabled": "true"}], "pvs": [], "macros": [], "name": "SIMPLE2", "component": null}
				 ],
		  "blocks":
                   [{"name": "testblock1", "local": true, "pv": "NDWXXX:xxxx:SIMPLE:VALUE1", "component": null, "visible": true, "log_periodic": true, "log_rate": 10, "log_deadband": 0},
                    {"name": "testblock2", "local": true, "pv": "NDWXXX:xxxx:SIMPLE:VALUE1", "component": null, "visible": true, "log_periodic": true, "log_rate": 5, "log_deadband": 0},
                    {"name": "testblock3", "local": true, "pv": "NDWXXX:xxxx:EUROTHERM1:RBV", "component": null, "visible": true, "log_periodic": false, "log_rate": 0, "log_deadband": 1.0}
				   ],
		  "components":
					   [{"name": "comp1"}],
		  "groups":
				   [{"blocks": ["testblock1"], "name": "Group1", "component": null},
					{"blocks": ["testblock2"], "name": "Group2", "component": null},
					{"blocks": ["testblock3"], "name": "NONE", "component": null}],
		  "name": "TESTCONFIG1",
		  "description": "A test configuration",
		  "history": ["2015-02-16"]
		 }'

**BLOCKSERVER:SAVE_NEW_COMPONENT**

	Command: caput -S %MYPVPREFIX%CS:BLOCKSERVER:SAVE_NEW_COMPONENT config1234567890
	Saves a component to XML without affecting the current configuration.
	This will give an error if trying to overwrite components of the current active configuration.
	Requires compressed and hexed JSON dictionary.
	
	Example JSON (dehexed and decompressed):
		'{"iocs":
				 [{"simlevel": "None", "autostart": true, "restart": false, "pvsets": [{"name": "SET", "enabled": "true"}], "pvs": [], "macros": [], "name": "SIMPLE1", "component": null},
				  {"simlevel": "recsim", "autostart": true, "restart": false, "pvsets": [{"name": "SET", "enabled": "true"}], "pvs": [], "macros": [], "name": "SIMPLE2", "component": null}
				 ],
		  "blocks":
                   [{"name": "testblock1", "local": true, "pv": "NDWXXX:xxxx:SIMPLE:VALUE1", "component": null, "visible": true, "log_periodic": true, "log_rate": 10, "log_deadband": 0},
                    {"name": "testblock2", "local": true, "pv": "NDWXXX:xxxx:SIMPLE:VALUE1", "component": null, "visible": true, "log_periodic": true, "log_rate": 5, "log_deadband": 0},
                    {"name": "testblock3", "local": true, "pv": "NDWXXX:xxxx:EUROTHERM1:RBV", "component": null, "visible": true, "log_periodic": false, "log_rate": 0, "log_deadband": 1.0}
				   ],
		  "groups":
				   [{"blocks": ["testblock1"], "name": "Group1", "component": null},
					{"blocks": ["testblock2"], "name": "Group2", "component": null},
					{"blocks": ["testblock3"], "name": "NONE", "component": null}],
          "components": [],
		  "name": "TESTCOMP1",
		  "description": "A test component",
		  "history": ["2015-02-16"]
		 }'		 
		 
**BLOCKSERVER:DELETE_CONFIGS**

    Command: caput -S %MYPVPREFIX%CS:BLOCKSERVER:DELETE_CONFIGS config1234567890
    Removes a configuration or configurations from the BlockServer and filesystem. Requires a compressed and hexed JSON list of configuration names to remove.
    If this is done in error the configuration can be recovered from version control. For removing one configuration only, create a list of one item.

    Returns "OK" or an error message (compressed and hexed JSON).
	
**BLOCKSERVER:DELETE_COMPONENTS**

    Command: caput -S %MYPVPREFIX%CS:BLOCKSERVER:DELETE_COMPONENTS config1234567890
    Removes a component or components from the BlockServer and filesystem. Requires a compressed and hexed JSON list of component names to remove.
    If this is done in error the component can be recovered from version control. For removing one component only, create a list of one item.

    Returns "OK" or an error message (compressed and hexed JSON).
	
**BLOCKSERVER:BUMPSTRIP_AVAILABLE:SP**

    Command: caput %MYPVPREFIX%CS:BLOCKSERVER:BUMPSTRIP_AVAILABLE:SP
    TODO: add description

**BLOCKSERVER:SET_SCREENS**

    Command: caput -S %MYPVPREFIX%CS:BLOCKSERVER:SET_SCREENS
    Sets a compressed and hexed XML list of available device screens descriptions.

    Returns "OK" or an error message (compressed and hexed JSON).

**SYNOPTICS:SET_DETAILS**

    Command: caput -S %MYPVPREFIX%CS:SYNOPTICS:SET_DETAILS config1234567890
    Saves the synoptic with supplied compressed and hexed XML data, saving under the name specified in the XML.
	
    Returns "OK" or an error message (compressed and hexed JSON).
	
**SYNOPTICS:DELETE**

    Command: caput -S %MYPVPREFIX%CS:SYNOPTICS:DELETE config1234567890
	Removes a synoptic from the BlockServer and filesystem. Requires a compressed and hexed JSON list of synoptics names to remove.
    If this is done in error the synoptic can be recovered from version control. For removing one synoptic only, create a list of one item.
	
    Returns "OK" or an error message (compressed and hexed JSON).

**SYNOPTICS:*synoptic_name*:SET**

    Command: caput -S %MYPVPREFIX%CS:SYNOPTICS:*synoptic_name*:SET
    TODO: add descriptions
	
-----------------
Archiver Settings
-----------------

Blocks can either be set to log periodically or log on change using the JSON "log_periodic" value.

When log_periodic is true the block will be scanned at the rate given in "log_rate", if the value has changed it will be logged. The "log_deadband" is ignored.

When log_periodic is false the block value will be archived whenever the block changes by the deadband given in "log_deadband". The "log_rate" is ignored.
	
-----------------
The File Watcher / Config version control
-----------------

The file watcher has been removed in https://github.com/ISISComputingGroup/EPICS-inst_servers/pull/139

Instead, we now have a much simpler system. A background python thread running as part of the blockserver checks if there are any uncommitted changes at a set interval. If it sees any changes, it does the equivalent of a `git add -A`, `git commit`, `git push`. This means that we get a backup at 5 minute intervals of the configuration area