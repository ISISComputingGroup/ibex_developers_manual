# Muon TPAR files

There is a soft IOC ( [`MUONTPAR`](https://github.com/ISISComputingGroup/EPICS-ioc/tree/master/MUONTPAR) ) which is used to load and edit the muon `.tpar` files, which are used by their scripts for temperature curve adjustments. 
This works by reading in "master" copies, set up by the scientists, and loading the contents of these into the `current.tpar`/`current_booster.tpar` files. These can then be edited by users, but their contents will never persist beyond the next configuration change (or IOC restart). This has an associated device screen to serve its contents over EPICS and allow editing through our GUI, but editing the file directly in another text editor is also an option.

The IOC works by using the [`FileContentsServer`](https://github.com/ISISComputingGroup/EPICS-FileServer/tree/master/FileContentsServerApp) module, which takes an input and an output file.

The master copies and the `current` tpar files (`current.tpar` and `current_booster.tpar`) reside in `\Instrument\Settings\` on muon instruments. 

They are a custom format that are essentially space-separated files with a header for column names and then rows for values (much like a `csv`)

PVs are loaded in the IOC for the TPAR file names, but these are largely for script backwards compatibility - they previously read in the "master" file.

