> [Wiki](Home) > [Project overview](Project-overview) > [Major Components of Ibex Server](Major-Components-of-Ibex-Server)

This is a table of the programs forming the backbone of IBEX server. Useful for reference:

Name | Console Name | Type | What it does
---  | ------------ | ----- | ------------
Block server | BLOCKSRV | Python | Manages configurations and blocks associated with them
Block Archive | ARBLOCK | Java | Archives (in mysql db) blocks set in a configuration (restarted when blocks change)
Instrument Archive | ARINST | Java | Archives (in mysql db) pvs with archive property
Database server | DBSVR | Python | PVs for items stored in the data base, e.g. ioc pv info, experiment details
Proc Serve Control | PSCTRL | Epics IOC | Control proc serves  (start, stop and status)
Active MQ | JMS | Java | ActiveMQ used to transmit log line
 | SCRIPTSERVER | | 
 | NICOSDAEMON | |
 | EXPDB | |
 | IOCLOG | |
 | ISISDAE_01 | |
 | RUNCTRL_01 | |
 | BLOCKCACHE | |
 | ALARM | |
 |  ARACCESS | | 



I am not sure about CAREP, GWBLOCK, GWEXT