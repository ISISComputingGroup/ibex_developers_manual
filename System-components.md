> [Wiki](Home) > [The Backend System](The-Backend-System) > [System Components](System-components)

This is a table of the major components of IBEX server.

Name | Console Name | Type | What it does
---  | ------------ | ----- | ------------
[Active MQ](ActiveMQ) | JMS | Java | ActiveMQ used to transmit log and alarm data
[Alarm server](Alarms) | ALARM | Java | Serves alarms which appear in the alarms perspective
[Archive access](Logging-from-the-archive) | ARACCESS | python | Creates log files based on the archive
Block Archive | ARBLOCK | Java | Archives (in mysql db) blocks set in a configuration (restarted when blocks change) see [CSS-Archive-Engine](CSS-Archive-Engine)
Block Cache | BLOCKCACHE | Python | Program which caches block values and provides them via a `CS:BLOCKSERVER:BLOCKVALUES`. This is done to avoid genie python etc making too many calls to the various block PVs.
Block Gateway | GWBLOCK | EPICS Gateway | Aliases the dynamically created block PVs e.g. CS:SB:FURNACE_TEMP to the underlying PV e.g. EUROTHRM_01:A01:TEMP see [Block server](BlockServer#what-it-does)
[Block server](BlockServer) | BLOCKSRV | Python | Manages configurations and blocks associated with them see [Settings-and-Configurations](Settings-and-Configurations)
CA Repeater | CAREP | Executable | A epics CA repeater that is started before all other processes. This repeats UDP broadcasts to CA clients on the same machine
[Database server](The-DatabaseServer) | DBSVR | Python | PVs for items stored in the data base, e.g. ioc pv info, experiment details
[Experiment DB](Experimental-Database) | EXPDB | Python | PVs for the experimental database which contains users and run numbers
[External/Access Gateway](Access-Gateway) | GWEXT | EPICS Gateway | Gateway to allow access to PVs from outside localhost
Inst etc | INSTETC_01 |  Epics IOC | PVs which are for instrument level, e.g. motors moving and security pvs
Instrument Archive | ARINST | Java | Archives (in mysql db) pvs with archive property see [CSS-Archive-Engine](CSS-Archive-Engine)
[IOC Message Logger](IOC-message-logging) | IOCLOG | Java | Collects messages sent by any IOC, logs it in the database and put it on the JMS message queue
[ISIS DAE](DAE-and-the-ICP) | ISISDAE_01 | Epics IOC | Controls the ISIS ICP program which collects data
[MySQL](The-MySQL-Database) | runs as a service | Service | My SqlDatabase is used for persisting data
[Nicos](Nicos) | NICOSDAEMON | Python | Process which runs and queues python scripts on an instrument
Proc Serve Control | PSCTRL | Epics IOC | Control proc serves  (start, stop and status)
[Run Control](Run-control) | RUNCTRL_01 | Epics IOC | Add run control to blocks
[Script server (Interface to Nicos)](Nicos) | SCRIPTSERVER | Python | Script server is a proxy in front of nicos to allow communication with it


All components are started via [Startup and Shutdown](Startup-and-Shutdown)
