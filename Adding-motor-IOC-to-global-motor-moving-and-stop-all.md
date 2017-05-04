There is a global "in motion" PV $(P)CS:MOT:MOVING which is maintained by INSTETC from INSTETC.db This is actually a calc record and each motor IOC is responsible for filling in one input of the calc record with its status. As a calc record has finite inputs, additional calcs like "$(P)CS:MOT:_MOVING1 will get created which will aggregate inputs and feed then into a single input of the overall MOVING PV. The "stop all" PV is also maintained by INSTETC in this file.

To support "stop all" you just need to load $(MOTOR)/db/motorUtil.db into the IOC - this sets up a monitor on the INSTETC PV and propagates any stop request to the IOC

To add "in motion" support, the same file must be included, but it will need to be first edited to add support for that IOC to push its status.

Inside motorUtil.db add the new IOC (you need one entry per ioc independent of how many things it controls) to the $(P)_FAN dfanout record. Ignore how the Galils are done - that way is historic. We will take the example of the SMC100 motion IOC.

* locate an unused calc record input in $(P)CS:MOT:_MOVING1 - in this case we will use input "A" 
* Add a line like $(IFIOC_SMC100_01=#)  field(OUTA, "$(PVPREFIX)CS:MOT:_MOVING1.A CA")   to the dfanout record
* load the motorUtil.db into the IOC

If your IOC is called SMC100_01 then a macro $(IFIOC_SMC100_01) will automatically get created by the ISIS standard init sequence and given a value of " " which can be used in general to conditionally load/include items.
 
* Add a line      
dbLoadRecords("$(MOTOR)/db/motorUtil.db","P=$(MYPVPREFIX)$(IOCNAME):,$(IFIOC)= ,PVPREFIX=$(MYPVPREFIX)")

INSTETC keeps track of the global moving flag, MOVING1 is merged with MOVING so you just need to watch that. As motion is across multiple IOCs splitting each IOC into a different calc record is safest to avoid possible misses, so currently each IOC needs to load motorUtil.db and map to a different calc record input to avoid clashes of values. The mechanism is independent of what table of motors position the ioc occupies, though it might look like that was true from the way the galil is implemented. So it should just require adding IFIOC_MCCLEN_01 to motorUtil.db etc. and loading this into the mclennan ioc
