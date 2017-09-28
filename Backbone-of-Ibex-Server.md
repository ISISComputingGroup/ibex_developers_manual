This is a table of the programs forming the backbone of IBEX server. Useful for reference:

Name | Console Name | Type | What it does
---  | ------------ | ----- | ------------
Block server | BLOCKSRV | Python | Manages configurations and blocks associated with them
Block Archive | ARBLOCK | Java | Archives (in mysql db) blocks set in a configuration (restarted when blocks change)
Instrument Archive | ARINST | Java | Archives (in mysql db) pvs with archive property
Database server | DBSVR | Python | PVs for items stored in the data base, e.g. ioc pv info, experiment details
Proc Serve Control | PSCTRL | Epics IOC | Control proc serves  (start, stop and status)
