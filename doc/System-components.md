> [Wiki](Home) > [The Backend System](The-Backend-System) > [System Components](System-components)

This is a table of the major components of IBEX server.

Name | Console Name | Type | What it does
---  | ------------ | ----- | ------------
[Active MQ](ActiveMQ) | `JMS` | Java | ActiveMQ used to transmit log and alarm data
[Alarm server](Alarms) | `ALARM` | Java | Serves alarms which appear in the alarms perspective. It checks to PVs to see if they are in alarm mode and relays that information to the client. Actual range checking is done a EPICS server.
[Archive Access](Logging-from-the-archive) | `ARACCESS` | python | Creates log files based on the MySQL database for some devices with special needs.
Archive Engine | `ARBLOCK` | Java | Archives (in mysql db) blocks set in a configuration (restarted when blocks change) see [CSS-Archive-Engine](CSS-Archive-Engine)
Block Gateway | `GWBLOCK` | EPICS Gateway | Aliases the dynamically created block PVs e.g. CS:SB:FURNACE_TEMP to the underlying PV e.g. EUROTHRM_01:A01:TEMP see [Block server](BlockServer#what-it-does)
[Block server](BlockServer) | `BLOCKSRV` | Python | Manages configurations and blocks associated with them see [Settings-and-Configurations](Settings-and-Configurations). It configures the Archive Engine and starts the IOCs read from the configuration files.
CA Repeater | `CAREP` | Executable | A epics CA repeater that is started before all other processes. This repeats UDP broadcasts to CA clients on the same machine
[Database server](The-DatabaseServer) | `DBSVR` | Python | Intermediary between MySQL and the GUI, only used for PVs that hold instrument information, such as experiment data, which IOCs are used and information about PVs of an instrument. Legacy software, not that necessary now.
[Experiment DB](Experimental-Database) | N/A - runs centrally | Python | Similar to DB server but for PVs for the experimental database which contains users and run numbers.
[External/Access Gateway](Access-Gateway) | `GWEXT` | EPICS Gateway | Gateway to allow access to PVs from outside localhost
[icpconfig](icpconfig) | N/A | Library of functions | functions called on IOC start up to load macros into the IOC.
[Inst etc](Inst-etc-IOC) | `INSTETC_01` |  Epics IOC | PVs which are for instrument level, e.g. motors moving and security pvs
Instrument Archive | `ARINST` | Java | Archives (in mysql db) pvs with archive property see [CSS-Archive-Engine](CSS-Archive-Engine). It is a separate archive engine from Archive engine. PVs with archive property are PVs set by developers to be logged always, regardless of what scientists do, so that we can use them for diagnostics.
[IOC Message Logger](IOC-message-logging) | `IOCLOG` | Java | Instrument level software that collects messages sent by any IOC, logs it in the database and put it on the JMS message queue. 
[ISIS DAE](DAE-and-the-ICP) | `ISISDAE_01` | Epics IOC | Controls the ISIS ICP program which collects data. It is an IOC-like needed because ICP can not talk over Channel Access.
[MySQL](The-MySQL-Database) | runs as a service | Service | My SqlDatabase is used for persisting data
[Nicos](Nicos) | `NICOSDAEMON` | Python | Process which runs and queues users' python scripts on an instrument
Proc Serve Control | `PSCTRL` | Epics IOC | Control proc serves  (start, stop and status). A wrapper that makes starting and stopping IOCs much easier.
[Reflectometry Server](Reflectometers) | `REFL` | pcaspy | Complex reflectometry motion
[Run Control](Run-control) | `RUNCTRL_01` | Epics IOC | Add run control to blocks. Run Control is a feature of IBEX that allows users to configure the instrument so when a PV is out of a certain range, neutron data is not being gathered. Needed because neutron data has an extremely large volume and sometimes that data would not be needed so it is better to not pollute the Nexus files with it.
[Script server (Interface to Nicos)](Nicos) | `SCRIPTSERVER` | Python | Script server is a proxy in front of nicos to allow communication with it.
[The Journal Viewer](The-Journal-Viewer) | N/A | Database, webserver and part of the client | Provides information about what experiments have been done on the instrument in the past

All components are started via [Startup and Shutdown](Startup-and-Shutdown)
