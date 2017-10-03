> [Wiki](Home) > [Project overview](Project-overview) > [Major Components of Ibex Server](Major-Components-of-Ibex-Server)

This is a table of the programs forming the backbone of IBEX server. Useful for reference:

Name | Console Name | Type | What it does
---  | ------------ | ----- | ------------
[Block server](BlockServer) | BLOCKSRV | Python | Manages configurations and blocks associated with them
Block Archive | ARBLOCK | Java | Archives (in mysql db) blocks set in a configuration (restarted when blocks change)
Instrument Archive | ARINST | Java | Archives (in mysql db) pvs with archive property
Database server | DBSVR | Python | PVs for items stored in the data base, e.g. ioc pv info, experiment details
Proc Serve Control | PSCTRL | Epics IOC | Control proc serves  (start, stop and status)
[Active MQ](ActiveMQ) | JMS | Java | ActiveMQ used to transmit log line
a | SCRIPTSERVER | | 
a | NICOSDAEMON | |
a | EXPDB | |
a | IOCLOG | |
a | ISISDAE_01 | |
a | RUNCTRL_01 | |
a | BLOCKCACHE | |
a | ALARM | |
a | ARACCESS | | 
a | INSTETC_01 | |
Block Gateway | GWBLOCK | EPICS Gateway | Aliases the dynamically created block PVs e.g. CS:SB:FURNACE_TEMP to the underlying PV e.g. EUROTHRM_01:A01:TEMP
External Gateway | GWEXT | EPICS Gateway | Gateway to allow access to PVs from outside localhost

I am not sure about CAREP