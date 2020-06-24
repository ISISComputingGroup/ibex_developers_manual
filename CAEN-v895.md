This is a VME card used on muons to set discriminator levels. Unfortunately the card has no readbacks, so you can only set it.

The underlying code is an asyn driver communicating via a vendor DLL to set register values. This code is in the EPICS-CAENVME support module

the ioc is configured using
```
CAENVMEConfigure("CRATE0", 0, 0, 0, 0x10000, $(CAENVMESIM=0)) 
```
and records loaded e.g.
```
dbLoadRecords("$(CAENVME)/db/v895Crate.db","P=$(MYPVPREFIX),Q=$(IOCNAME):,CRATE=0,PORT=CRATE0")
dbLoadRecords("$(CAENVME)/db/v895Card.db","P=$(MYPVPREFIX),Q=$(IOCNAME):,CRATE=0,PORT=CRATE0,C=0")
```
The managing of sets of parameters is done using the epics autosave option called configMenu - see notes for recent release of
http://htmlpreview.github.io/?https://github.com/epics-modules/autosave/blob/master/documentation/autosave.html

A configuration called "vmeconfig" is enabled
 


