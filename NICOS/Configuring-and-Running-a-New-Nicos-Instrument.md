# Configuring and Running a New Nicos Instrument

Nicos instruments configurations are stored under ```nicos-core/custom/```. These configurations are designed to be very modular.

## Configuring an Instrument

The name of an instrument's directory must be typed in the instrument's own ```nicos.conf``` file, particularly in the ```setup_subdirs``` section (and, if the gui is in use, also the ```guiconfig``` files).

An instrument can be configured as to which Nicos commands it should run. These are set in the file ```setups/system.py```, in the ```modules``` section, which lists the file names that should be included. Command files are located in:
* ```nicos-core/nicos/commands``` in the case of generic Nicos commands
* the instrument's own ```lib/``` directory in the case of instrument-specific commands

It might be possible for an instrument to include files from another instrument too, as long as it is listed in the ```setup_subdirs``` section of the ```nicos.conf``` file (e.g. see ```antares/```, which includes ```frm2/```). NOTE: this hasn't been tested, but if it's the case it would allow us to have a basic Ibex instrument containing core commands and settings common to all Ibex instruments, without committing new files to the core ```nicos/commands``` directory.

## Running an Instrument

If no instrument is specified, Nicos will run ```demo``` by default.

There are two ways of specifying which instrument to run:
* have an environmnent variable called ```INSTRUMENT``` containing the instrument's name: Nicos will then look for an instrument with that name under ```custom/```
* have a ```nicos.conf``` file in the root ```nicos-core/``` directory, pointing at the instrument we wish to run. For example, to run the instrument ```IbexTestInstrument```, the file would contain:
```
[nicos]
instrument = IbexTestInstrument
```

Now, as we need the correct EPICS and CA environmnent variables to be set for running genie_python commands (and ultimately Nicos to run with all the other Ibex instrument processes), we need to launch Nicos processes through an EPICS terminal. This terminal already sets an ```INSTRUMENT``` environmnent variable, which gives us the option to simply have an instrument directory called ```custom/NDXXXX```, e.g. for ```NDXDEMO``` we would have ```custom/NDXDEMO```.

For testing purposes though it's more convenient to have a ```nicos.conf``` file specifying the instrument to launch, even when running from an EPICS terminal.



