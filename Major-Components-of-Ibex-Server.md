> [Wiki](Home) > [Project overview](Project-overview) > [Major Components of Ibex Server](Major-Components-of-Ibex-Server)

This is a table of the programs forming the backbone of IBEX server. Useful for reference:

Name | Console Name | Type | What it does
---  | ------------ | ----- | ------------
[Block server](BlockServer) | BLOCKSRV | Python | Manages configurations and blocks associated with them
Block Archive | ARBLOCK | Java | Archives (in mysql db) blocks set in a configuration (restarted when blocks change) see [CSS-Archive-Engine](CSS-Archive-Engine)
Instrument Archive | ARINST | Java | Archives (in mysql db) pvs with archive property see [CSS-Archive-Engine](CSS-Archive-Engine)
Database server | DBSVR | Python | PVs for items stored in the data base, e.g. ioc pv info, experiment details
Proc Serve Control | PSCTRL | Epics IOC | Control proc serves  (start, stop and status)
[Active MQ](ActiveMQ) | JMS | Java | ActiveMQ used to transmit log line
[Script server (Interface to Nicos)](Nicos) | SCRIPTSERVER | Python | Script server is a proxy in front of nicos to allow communication with it.
[Nicos](Nicos) | NICOSDAEMON | Python | Process which runs and queues python scripts on an instrument
[Experiment DB](Experimental-Database) | EXPDB | Python | PVs for the experimental database which contains users and runnumbers
[IOC Message Logger](IOC-message-logging) | IOCLOG | Java | Collects messages sent by any IOC and log it in the database and put it on the JMS message queue
ISIS DAE | ISISDAE_01 | Epics IOC | Controls the ISIS ICP program which collects data.
[Run Control](Run-control) | RUNCTRL_01 | Epics IOC | Add run control to blocks
Block Cache | BLOCKCACHE | | Python | Program which caches block values for
[Alarm server](Alarms) | ALARM | Java | Serves alarms which appear in the alarms perspective
[Archive access](Logging-from-the-archive) | ARACCESS | python | Creates log files based on the archive
Inst etc | INSTETC_01 |  Epics IOC | PVs which are for instrument level, e.g. motors moving and security pvs
Block Gateway | GWBLOCK | EPICS Gateway | Aliases the dynamically created block PVs e.g. CS:SB:FURNACE_TEMP to the underlying PV e.g. EUROTHRM_01:A01:TEMP see [Block server](BlockServer#What it does)
[External/Access Gateway](Access-Gateway) | GWEXT | EPICS Gateway | Gateway to allow access to PVs from outside localhost
CA Repeater | CAREP | Executable | A epics CA repeater that is started before all other processes
