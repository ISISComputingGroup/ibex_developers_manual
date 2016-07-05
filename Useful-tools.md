* [CA snooper](CA-snooper)

* [ISIS modules for file handling](ISIS-modules-for-file-handling)

* [Check DB file script](Check-db-file)

* [Add sim records script](Add-sim-records-script)

## Caget, caput, zhex and uzhex

To get the value of a compressed, hexed PV (such as those on the blockserver) type into an EPICS terminal:
`caget -S -t PV | uzhex` where PV is the PV you are looking for

To send compressed, hexed values to a PV (such as those on the blockserver) type into an EPICS terminal:
`for /f "tokens=*" %x in (`zhex VAL`) do caput -S PV %x` where PV is as above and VAL is the data you wish to send