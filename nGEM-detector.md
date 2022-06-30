The nGEM detector is a portable detector that connects via a private ethernet connection to vendor software running on a laptop. It is often used on INES. Detector group will normally set up the laptop with the vendor software, on ines this is installed to `c:\users\ines_mgr\documents\ngem` or `c:\nGEM-software` and a program `ngemapp.exe` is left running.

Ibex support is via the NGEM IOC, which is installed on the laptop. It could in principle run on the NDX computer and talk to the `ngemapp.exe` program over the network, but the IOC needs to move files off the laptop to a locally attached USB hard drive after collection ends so it is more convenient to run on the laptop. The IOC connects to localhost port 61000 by default, this would only need to be changed (via a macro) if the IOC was not running on the laptop.  

For a clean setup on laptop (skip relevant steps if previously configured)
* Install EPICS (you can just run `install_to_inst.bat` in the epics release on `kits$` rather than a full installer run)
* Edit `config_env_base.bat` to set correct instrument name (e.g. INSTRUMENT=INES, ISIS_INSTRUMENT=1). This will make the NGEM prefix be IN:INES:
* Edit `globals.txt` to define `ACF_IH1` so the NX computer can start/stop nGEM via PVs e.g. `ACF_IH1=NDXINES`
* Create shortcuts on desktop pointing at `gateway/start_gateways.bat` and `runIOC.bat` for NGEM ioc
* edit `copycmd.bat` in `support/ngem-bbtx/master/utils` to set ARCHIVE location for files to be copied to (this is the USB attached drive)
* put notes on running both shortcuts on reboot and location of `copycmd.bat` into a README/NOTES file on desktop

The is an `nGEM.opi` on the NDX, this has just need to be installed as a device screen.

INES has some simple python commands to set the START/STOP pvs for the detector. The detector IOC picks up the run number for ines to add to data files as its prefix is also IN:INES  

If the detector is moved to another instrument with the same laptop then:

* edit `config_env_base.bat` as above to set new instrument name
* edit `globals.txt` for access security of the new NDX
* edit `copycmd.bat` to set new location for robocopy of data files
* create share/map drive on destination computer for above `copycmd.bat` if it is not a simple attached USB drive

     