> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Other](Other) > CAEN v895

This is a VME card used on muons to set discriminator levels. Unfortunately the card has no readbacks, so you can only set it.

The underlying code is an asyn driver communicating via a vendor DLL to set register values. This code is in the EPICS-CAENVME support module

the ioc is configured using
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
As noted above a simulation mode can be enabled by setting the `CAENVMESIM` macro to `

 

