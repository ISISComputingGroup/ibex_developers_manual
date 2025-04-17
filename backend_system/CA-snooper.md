> [Wiki](Home) > [The Backend System](The-Backend-System) > [Useful tools](Useful-tools) > CA snooper

caSnooper is a tool to analyse EPICS name broadcasts, it is good for spotting misnamed PVs as
you will see continued broadcasts for the name with no reply. It is built as part of our EPICS
build so one you type config_env you will have access. A valid existing PV will connect immediately and 
not show up high in the list, incorrectly named PVs or ones without the IOC running will show up higher. 

The following typed at a command line will run caSnooper for 30 seconds and print a report
containing the top 10 names being looked for

    caSnooper -t30 -p10

It prints the lookup frequency in Hz. Initially names are looked for rapidly, but this
backs off over time and 0.7 is a typical long term frequency. You can also type e.g.

    caSnooper -t10 -l1

which will print all lookups occurring more frequently than 1Hz

Another useful option is  -c  which is like -p above, but will also check for existence of the
PV. In the resulting listing a   NC   means "not connected" i.e. PV does not exist. You can use -c0 or
-p0 to mean check/print all PVs found.

CA snooper is run periodically on `control-svcs`. A link to this is at http://control-svcs.isis.cclrc.ac.uk/pv_snoop/pvs.html. 

## Checking IOCs

* start caSnooper in one command window as e.g.      _caSnooper -t30 -c0 > snoop.log_
* restart the IOC under test (or the whole of ibex, but you may need more than 30 seconds)
* look at the generated report
* if you type `set EPICS_CAS_INTF_ADDR_LIST=127.0.0.1` in the command window before running caSnooper it will restrict its check to the loopback interface, which is where local IOCS will normally broadcast
* `NC` next to a PV name means "not connected", however `caSnooper` runs this check at the end so if the ioc terminates before caSnooper then you will see a lot of `NC`. This is only likely to happen if you were running `caSnooper` in parallel with IOC unit tests.
 