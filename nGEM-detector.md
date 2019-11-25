The nGEM detector is a portable detector that connects via a private ethernet connection to vendor software running on a laptop. It is often used on INES. Detector group will normally set up the laptop with the vendor software, on ines this is installed to c:\users\ines_mgr\documents\ngem and a program ngemapp.exe is left running.

Ibex support is via the NGEM IOC, which is installed on the laptop. It could in principle run on the NDX computer and talk to the ngemapp.exe program over the network, but the IOC needs to move files off the laptop after collection ends so it is more convenient to run on the laptop. The IOC connects to localhost port 61000 by default, this would only need to be changed (via a macro) if the IOC was not running on the laptop.  

For a clean setup on laptop (skip relevant steps if previously configured)
* Install EPICS
* Edit config_env_base.bat to set correct instrument name (e.g. INSTRUMENT=INES, ISIS_INSTRUMENT=1). This will make the NGEM prefix be IN:INES:
* Edit globals.txt to define ACF_IH1 so the NX computer can start/stop nGEM via PVs e.g. ACF_IH1=NDXINES
* Create shortcuts on desktop pointing at gateway/start_gateways and runIOC.bat for iocs/NGEM
* edit copycmd.bat in support/ngem-bbtx/master/utils to set ARCHIVE location for files to be copied to
* put notes on running both shortcuts on reboot and location of copycmd.bat into a README/NOTES file on desktop





     