The nGEM detector is a portable detector that connects via a private ethernet connection to vendor software running on a laptop. It is often used on INES. Detector group will normally set up the laptop with the vendor software, on ines this is installed to `c:\users\ines_mgr\documents\ngem` or `c:\nGEM-software` and a program `ngemapp.exe` is left running.

Ibex support is via the NGEM IOC, which is installed and run on the laptop. It could in principle run on the NDX computer and talk to the `ngemapp.exe` program over the network, but the IOC needs to move files off the laptop to a locally attached USB hard drive after collection ends so it is more convenient to run on the laptop rather than the NDX. The IOC connects to localhost port 61000 by default, this would only need to be changed (via a macro) if the IOC was not running on the laptop. This port number is the same as passed to the `ngemapp.exe` program running in a separate window, it is the "UI Port" of the ngem software. The nGEM detector itself is network based and will be in a local 192.168 local address attached to the laptop, ibex does not need to be aware of this as it talks to the nGEM server program and does not need to directly communicate with the detector hardware.   

For a clean setup on laptop (skip relevant steps if previously configured)
* Install EPICS (you can just run `install_to_inst.bat` in the epics release on `kits$` rather than a full installer run)
* run `config_env.bat` in `c:\instrument\apps\epics` to create the `c:\instrument\settings` tree
* now close this cmd window and create a file `c:\instrument\settings\config\NDLTxxx\configurations\mypvprefixnc.txt` that contains the correct PV prefix but without a trailing : e.g. `IN:INES` (the `nc` suffix in `mypvprefixnc.txt` means "no colon") 
* now re-run `config_env.bat` from a cmd window and check `%MYPVPREFIX%` etc is as expected
* Create `c:\instrument\settings\config\NDLTxxx\configurations\globals.txt` to define `ACF_IH1` so the NX computer can start/stop nGEM via PVs e.g. `ACF_IH1=NDXINES`
* Create shortcuts on desktop pointing at `c:\instrument\apps\epics\gateway\start_gateways.bat` and the `runIOC.bat` for the NGEM ioc directory
* put notes on running both shortcuts on reboot into a README/NOTES file on desktop
* start gateways and ngemIOC via shortcuts
* agree to popups to allow firewall access to domain network for carepeater, gateway, ngemioc

The is an `nGEM.opi` on the NDX, this has just need to be installed as a device screen.

The ioc will move data files to the directory specified in the opi settings area

The ngem IOC picks up the run number from the instrument of the same prefix to add to data files  

INES has some simple python commands to set the START/STOP pvs for the detector. 

If the detector is moved to another instrument with the same laptop then:

* edit `mypvprefixnc.txt` and `globals.txt` as appropriate
* specify a new copy to location of data files in the opi
* create share/map drive on destination computer if it is not a simple attached USB drive
* start the IOC on the laptop and then view from the GUI OPI device screen on the NDX instrument (**do not** start NGEM from start/stop IOC in IBEX GUI)

## problems/debugging 

* If the NGEM vendor software is restarted, the IOC on the laptop will need to be restarted. Kill the running ioc cmd window and then run runIOC.bat shortcut on desktop
* Make sure the NGEM IOC isn't running in two places with the same PV prefix, currently this means the IOC should be **running only on the laptop and not on the associated NDX computer** (NGEM is listed in the start/stop IOCs menu so can get started accidentally). If there are two IOCs running, you will have issues starting/stopping collection and probably see "multiple PV warning" if you use a command line tool
* the program will rename the datafile to include the run number currently used on the instrument. If this is not happening, it could be an issue with the epics external gateway on the NDX computer (`GWEXT`) - check if e.g. for INES `caget IN:INES:DAE:RUNNUMBER` works when run from a computer separate to the NDX, if it doesn't then try locating and terminating the `gateway.exe` for the external gateway (procServ will automatically restart it). If that doesn't work, you may need to restart ibex server on the NDX             