> [Wiki](Home) > [The Backend System](The-Backend-System) > Useful tools

* [CA snooper](CA-snooper)

* [ISIS modules for file handling](ISIS-modules-for-file-handling)

* [Check DB file script](Check-db-file)

* [Add sim records script](Add-sim-records-script)

* [DB changes script](https://github.com/ISISComputingGroup/DbChanges)

## Caget, caput, zhex and uzhex

To get the value of a compressed, hexed PV (such as those on the blockserver) type into an EPICS terminal:
`caget -S -t PV | uzhex` where PV is the PV you are looking for

To send compressed, hexed values to a PV (such as those on the blockserver) type into an EPICS terminal:
`for /f "tokens=*" %x in ('zhex VAL') do caput -S PV %x` where PV is as above and VAL is the data you wish to send

## Console

The console can be used to inspect output from an IOC. To use it, launch the IBEX server and then, from an EPICS terminal, run

```
console -M localhost [IOCNAME]
```

The IOCs available can be listed using
```
console -M localhost -x
```

To look at an IOC remotely

```
console -M [MACHINE_NAME] -l [USERNAME] [IOCNAME]
```

where username is the local user on the instrument PC (e.g. `spudulike`).

To stop/restart an IOC, press `CTRL+X` and to exit the console press `CTRL+E`, then `C`, then `.`.

## Modbus

[QModMaster](https://sourceforge.net/projects/qmodmaster/) is a useful piece of software to probe Modbus devices much like Putty is used with serial/Ethernet connected devices.