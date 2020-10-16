> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Other](Other) > CAEN v895

This is a VME card used on muons to set discriminator levels. Unfortunately the card has no readbacks, so you can only set it.

The underlying code is an asyn driver communicating via a vendor DLL to set register values. This code is in the EPICS-CAENVME support module. The driver overrides the `drvUserCreate` method so that it can parse an asyn parameter passed from the DB file like `VMEWRITE_0x4` and then split this into a call to a "VMEWRITE" method with an additional value of "0x4" within the asynUser structure. 

The ioc is configured using
```
CAENVMEConfigure("CRATE0", 0, 0, 0, 0x10000, $(CAENVMESIM=0)) 
```
0x10000 is a VME base address. Records loaded for a Crate number (CRATE) and card number on crate (C) e.g.
```
dbLoadRecords("$(CAENVME)/db/v895Crate.db","P=$(MYPVPREFIX),Q=$(IOCNAME):,CRATE=0,PORT=CRATE0")
dbLoadRecords("$(CAENVME)/db/v895Card.db","P=$(MYPVPREFIX),Q=$(IOCNAME):,CRATE=0,PORT=CRATE0,C=0")
```
The managing of sets of parameters is done using the epics autosave option called `configMenu` - see notes for recent release of
http://htmlpreview.github.io/?https://github.com/epics-modules/autosave/blob/master/documentation/autosave.html

A configuration called `vmeconfig` is created and enabled
```
dbLoadRecords("$(AUTOSAVE)/db/configMenu.db","P=$(MYPVPREFIX)AS:$(IOCNAME):,CONFIG=vmeconfig")
makeAutosaveFileFromDbInfo("vmeconfig_settings.req", "vmeconfig")
create_manual_set("vmeconfigMenu.req","P=$(MYPVPREFIX)AS:$(IOCNAME):,CONFIG=vmeconfig,CONFIGMENU=1")
```
Then the `defaults` config is applied
```
dbpf("$(MYPVPREFIX)AS:$(IOCNAME):vmeconfigMenu:name", "defaults")
```
As noted above a simulation mode can be enabled by setting the `CAENVMESIM` macro to 1

configMenu lets you dynamically load and save autosaved values by writing to PVs. If you look in the DB files for cards you will see
```
info(vmeconfig, "VAL")
```
This means the VAL field of that record is part of the `vmeconfig` config menu set. Calling `makeAutosaveFileFromDbInfo` will create `vmeconfig_settings.req` at ioc start and then `create_manual_set` create the autosave set to manage the pvs (vmeconfigMenu.req references `vmeconfig_settings.req`). The OPI for the v895 loads the `configMenu.opi` supplied with autosave which allows different sets of PVS to be loaded and saved, however in practice they just load the first one called `defaults` as done by `dbpf` in the `st.cmd`

configMenu docs: https://epics.anl.gov/bcda/synApps/autosave/autoSaveRestore_R5-6-1.html#configMenu

## Sending settings

It should be noted that a channel does not have to be disabled for the setting to be sent and applied, e.g. a threshold.
