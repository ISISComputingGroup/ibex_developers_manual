# Add motor to global moving and stop all

There is a global "in motion" PV `$(P)CS:MOT:MOVING` which is maintained by INSTETC from INSTETC.db This is actually a calc record and each motor IOC is responsible for filling in one input of the calc record with its status. As a calc record has finite inputs, additional calcs like `"$(P)CS:MOT:_MOVING1` will get created which will aggregate inputs and feed then into a single input of the overall MOVING PV. The "stop all" PV is also maintained by INSTETC in this file.

To support "stop all" you just need to load `$(MOTOR)/db/motorUtil.db` into the IOC - this sets up a monitor on the INSTETC PV and propagates any stop request to the IOC

To add "in motion" support, the same file must be included, but it will need to be first edited to add support for that IOC to push its status.

Inside `motorUtil.db` add the new IOC (you need one entry per ioc independent of how many things it controls) to the `$(P)_FAN` `dfanout` record. We will take the example of the SMC100 motion IOC.

* Locate an unused calc record input in `$(P)CS:MOT:_MOVING1` - in this case we will use input "A" 
* Add a line like **`$(IFIOC_SMC100_01=#)  field(OUTA, "$(PVPREFIX)CS:MOT:_MOVING1.A CA")`**   to the dfanout record
* Add a line like     **`dbLoadRecords("$(MOTOR)/db/motorUtil.db","P=$(MYPVPREFIX)$(IOCNAME):,$(IFIOC)= ,PVPREFIX=$(MYPVPREFIX)")`**    to your IOC startup
* Make sure you have the line    **`motorUtilInit("$(MYPVPREFIX)$(IOCNAME):")`** somewhere after `iocInit()` in `st.cmd`
* Make sure that the `_MOVING1` field that you are writing to is included in the CALC of the `$(P)CS:MOT:_MOVING1` record (located in `INSTETC.db`)

If your IOC is called SMC100_01 then the ISIS standard startup creates a few useful macros for you: 
* `$(IFIOC_SMC100_01)` will have value `" "`
* `$(IFIOC)` will have value `"IFIOC_SMC100_01"`
So the item   `$(IFIOC)=` , (the space before the comma is important) will expand to   `IFIOC_SMC100_01=` ,  for use within the DB file
 
As motion is across multiple IOCs, splitting each IOC into a different calc record input was the safest approach at the time to avoid possible misses, so each IOC needs to load `motorUtil.db` and map to a different calc record input to avoid clashes of values. The mechanism is independent of what table of motors position the IOC occupies. 
