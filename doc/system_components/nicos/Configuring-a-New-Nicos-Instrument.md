# Configuring a new Nicos instrument

Nicos instruments configurations are stored under ```nicos-facility/inst-name/```. These configurations are designed to be very modular.

## Configuring an Instrument

An instrument requiring the Nicos daemon must have, as a minimum, a ```setups/``` directory containing two setup files:
* ```daemon.py```, which contains configuration parameters to run the daemon. This file is usually located in a ```special/``` subdirectory, which would normally contain all the setup files for the Nicos services to run (e.g. ```cache.py``` when the Nicos cache is needed). Some documentation about the daemon setup file is available [here] (http://cdn.frm2.tum.de/fileadmin/stuff/services/ITServices/nicos-master/dirhtml/services/daemon/).
* ```startup.py```, which doesn't have to contain much at all, but Nicos won't run without it. The startup files of various FRM II instruments contain the following comment:
```
# The startup setup is loaded first thing on NICOS session startup.  It should
# usually stay empty.  In particular, it should not include any other setups
# without good reason, so that on startup the previous master setups are loaded
# automatically.
```

A Nicos instrument can then have any number of additional setup files in the ```setups``` directory, each specifying a set of devices and commands that the daemon is configured to recognise (see for example Nicos ```demo```). A setup file called ```system.py``` if present, is always loaded. Here we can define a ```modules``` section, listing the file names of the modules that should be included. Command files can be located in:
* ```nicos-core/nicos/commands``` in the case of generic Nicos commands
* the instrument's own directory in the case of instrument-specific commands

More documentation on the setup files is available [here] (http://cdn.frm2.tum.de/fileadmin/stuff/services/ITServices/nicos-master/dirhtml/setups/#setups).


It looks like it's possible for an instrument to include setup files from another instrument too, as long as it is listed in the ```setup_subdirs``` section of a file called ```nicos.conf``` in the root instrument directory (e.g. see ```antares/```, which includes ```frm2/```). NOTE: this hasn't been tested, but if it's the case it would allow us to have a basic Ibex instrument containing core commands and settings common to all Ibex instruments, without committing new files to the core ```nicos/commands``` directory.

To run the Nicos GUI, the instrument must have a ```guiconfig.py``` file in the root instrument directory (if copying from another Nicos instrument, make sure any hard-coded path containing the instrument name is adjusted correctly).

## Running an Instrument

If no instrument is specified, Nicos will run ```demo``` by default.

There are at least two ways of specifying which instrument to run:
* have an environment variable called ```INSTRUMENT``` containing the instrument's facility and name in the format ```_facility_._name_```: Nicos will then look for an instrument with that name under ```facility/```
* have a ```nicos.conf``` file in the root ```nicos-core/``` directory, pointing at the instrument and facility we wish to run. For example, to run the instrument ```ibex``` in ```nicos_isis```, the file would contain:
```
[nicos]
instrument = ibex
setup_package = nicos_isis
```

Now, as we need the correct EPICS and CA environment variables to be set for running genie_python commands (and ultimately Nicos to run with all the other Ibex instrument processes), we need to launch Nicos processes through an EPICS terminal. This terminal already sets an ```INSTRUMENT``` environment variable, and so the ```start_script_server.bat``` will override this to be the ISIS default.

For testing purposes though, it's more convenient to have a ```nicos.conf``` file specifying the instrument to launch, even when running from an EPICS terminal.

Instructions on how to run Nicos can be found [here](Running-Nicos-(Script-Server)).
