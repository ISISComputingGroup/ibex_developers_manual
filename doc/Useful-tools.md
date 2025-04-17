> [Wiki](Home) > [The Backend System](The-Backend-System) > Useful tools

* [CA snooper](CA-snooper)

* [ISIS modules for file handling](ISIS-modules-for-file-handling)

* [Check DB file script](Check-db-file)

* [Add sim records script](Add-sim-records-script)

* [DB changes script](https://github.com/ISISComputingGroup/DbChanges)

* [Powershell Remote](PS-Remote)

* [Moxa Utils](MOXAUTIL-command)

* [Analyse Network Traffic](Network-traffic)

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
and then if you see 
```
[Enter `^Ec?' for help]
[-- MOTD -- IOC console for IOCNAME]
```
then press Ctrl+X to start the IOC.
The IOCs available can be listed using
```
console -M localhost -x
```

To look at an IOC remotely

```
console -M [MACHINE_NAME] -l [USERNAME] [IOCNAME]
```

where username is the local user on the instrument PC (e.g. `spudulike`).

Key combos in the console:

- `<CTRL>+X`: stop/restart an IOC
- `<CTRL>+E` then `C`, then `.`: exit the console press
- `<CTRL>+T`: toggle auto restart process on/off 

If attempting to run your console gives an error about port 782 being in use, the issue may be due to incorrect permissions in your Instrument\Var folder. Try moving/deleting/renaming your current var (you may need to stop the mysql service), then running `config_env.bat` to generate a new one and `upgrade_mysql.bat` in IBEX_Utils to rebuild your database.

## Modbus

[QModMaster](https://sourceforge.net/projects/qmodmaster/) is a useful piece of software to probe Modbus devices much like Putty is used with serial/Ethernet connected devices.