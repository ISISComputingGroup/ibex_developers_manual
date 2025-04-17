## ProcServ Ports

These items have hard-coded ports for ProcServ:

| Name | Port |
|------|------|
| Blockserver | 9006 |
| Database server | 9009 |
| JSON Bourne server | 9012 |

Everything else (IOCs, Block Cache, archivers etc.) are assigned ports as part of the build process starting from 20000.

## Other Ports

| Name | Port |
|------|------|
| Instrument Archiver web port | 4812 |
| Block Archiver web port | 4813 |
| JSON Bourne web port | 60000 |
| Blockserver web port | 8008 |
| Script Server (ActiveMQ STOMP port) | 39991 |
| JMS (ActiveMQ openwire port) | 39990 |



