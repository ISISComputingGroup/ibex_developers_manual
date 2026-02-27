# DETMON

```{include} migration_notes_warning.mdinc
```

## Background & Timeline ##
DETMON is a support system for use by the detector teams to monitor and view the status of the HV (High Voltage) crates that are in use across ISIS.
A pilot system should be created before Cycle 2019-01, the final system does not at present have a dead line.

## Equipment ##
The only equipment to consider for this system are CAEN crates (types of HV crate), however, there are about 30+ of them to consider.

## System Requirements ##
### Monitoring ###
The following items need to be monitored for each part of the system:

#### Crates ####

Parameter | Variable | What to record | Type
--- | --- | --- | ---
ON/OFF available in network | `ConnStatus` | Any variation | String
Crate fan status | `HVFanStat` | Any variation | String
Crate fan speed | `HVFanSpeed` | Any variation >+-5% | String
Which slots are used in the crate | | Any variation | 
Model Name | `ModelName` | Any variation | String
Software Release | `SwRelease` | Any variation | String
Power Supply Status | `HvPwSM` | Any Variation | String
IP address | `IPAddr` | Any Variation | String
Boards slots | `Slots` | Any Variation | Integer
CPU Load | `CPULoad` | Any Variation>=+-??? | Integer
Commands in the queue | `CmdQueueStatus` | Any Variation>=+-??? | Integer
Memory Status | `MemoryStatus` | Any Variation >=+-??? | Integer

#### Boards ####

Parameter | Variable | What to record | Type
--- | --- | --- | ---
Model | Model | Any Variation | String
Firmware release | `Fmw Release` | Any Variation | String
Serial Number | `SerNum` | Any Variation | Integer
Number of Channels | `NrOfCh` | Any Variation | Integer
Temperature | `Temp` | Any variation >= +-1 deg C | Float
Max Voltage | `HVMax` | Any Variation | Float
Board Status | `BdStatus` | Any Variation | Integer

#### Channels ####

Parameter | Variable | What to record | Type
--- | --- | --- | ---
Channel Name | Name | Any Variation | String
Voltage Setting | `V0Set` | Any Variation | Float
Current Setting | `I0Set` | Any Variation | Float
Voltage1 Setting | `V1Set` | Any Variation | Float
Current1 Setting | `I1Set` | Any Variation | Float
Rump Up speed | `RUp` | Any Variation | Float
Rump Down speed | `RDWn` | Any Variation | Float
Trip time | Trip | Any Variation | Float
Max Voltage Software limit | `SVMax` | Any Variation | Float
Monitor Voltage | `VMon` | Any Variation >= +-1 V | Float
Monitor Current | `IMon` | Any Variation >= +-2 uA | Float
Status | Status | Any Variation | Integer
Power Down Mode | `PDwn` | Any Variation | Integer

### Notes for the solution ###
* This monitoring would be for every crate in use at ISIS, and for any offline/test crates as well. Note that a crate has many boards, and a board has many channels – in the test system available at time of writing there is 1 crate, 8 cards, and 23 channels per card
* The IOC already deals with the channel requirements, although we may need to verify the trip
* The boards and crates may need some work to add them
* This monitoring also has to be independent of the instrument status or behaviour
* The rate of capture for this information can be relatively slow (1 second per item)
* It is quite possible to link multiple IOCs to the same crate
* Recording data to nexus files is acceptable – as such by creating a large number of blocks we should be able to run a script that is based on time and uses dummy neutron data – the nexus files can be stored, and the data regarding behaviour used to provide long term information. The log plotter will provide short term information for the numeric values. A python script could start a run and end and restart at predetermined times/after certain durations
* Whilst IBEX and NeXus files provide a solution, the data is being logged into a database, and longer term, either logging to a different database or forwarding the data that way may be more suitable – this should be explored mid-long term, but IBEX at least provided short term
* The number of blocks would need to be created by scripting, and the majority should likely be hidden from use on IBEX.
* The sheer number of blocks did raise a concern as to whether or not IBEX could deal with the numbers, as such some testing and proving will be needed
   * to get an idea of the potential numbers of blocks, assume every instrument has one fully populated CAEN crate
   * if every channel is defined as a block (so that it can be recorded in a Nexus file), that's
      * `35 x 8 x 23` = `6440` blocks
   * clearly `6440` blocks is an over-estimate, but it illustrates the scale of the problem
* Currently to tick over log files at midnight a cron job is used to end and begin a run

## Configuration set up

DETMON has a lot of blocks to set up and the CAEN crates create have a dynamic amount of boards and channels set up. This set up is scripted with scripts from the NDADETMON config area (in `Python/inst`). There are two scripts:

1. The script `record_channels.py` searches for the connected boards and channels for the crates (see the script help option for arguments to pass). The output is a JSON file containing information on the crate name, boards and channels. 
1. Using this JSON file you can then create the relevant `blocks.xml`, `groups.xml`, `block_config.xml` and `gwblock.pvlist` files using the `create_config_files_from_recorded_channels.py`. Once produced put them in the config area alongside the meta.xml and other configuration-specific files. In the meta.xml ensure that the `configuresBlockGWAndArchiver` tag is set to true and the blockserver will handle the use of the files you have created. 

This two step process lets you edit the intermediate JSON to include channels and crates which are not currently on the network.

## Notes

- DETMON runs the block gateway and block archiver with customised `gwblock.pvlist` and `block_config.xml` files to tackle handling the high number of blocks that we require on IBEX. See ticket https://github.com/ISISComputingGroup/IBEX/issues/5069.


## Known issues

- The number of blocks is so high that they often timeout when getting them from the blockserver. We do not at the moment care too much as long as they are written correctly to the nexus file and Davide seems quite happy with that.
  - Tackled in https://github.com/ISISComputingGroup/IBEX/issues/5069 by using customised `gwblock.pvlist` and `block_config.xml` files
  - Possible future performance upgrade in https://github.com/ISISComputingGroup/IBEX/issues/5917