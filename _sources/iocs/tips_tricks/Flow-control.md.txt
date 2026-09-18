# Flow control 

Flow control is used in serial devices to allow them to better communicate when they are ready to send/receive data. For most devices it should be switched off, unless we know for sure that the device needs to use it. We have seen a number of cases in the past where having it on when not necessary has caused issues.

All IOCs should set this because when connecting to a port if you don't set it the previous value may be used, i.e. if it had the flow control on for the last device the moxa may remember that setting for the next device.

Flow control comes in two varieties, [hardware](https://en.wikipedia.org/wiki/Flow_control_(data)#Hardware_flow_control) and [software](https://en.wikipedia.org/wiki/Software_flow_control).

## Hardware flow control 

Set *off* (probably the most used)
```
    $(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("L0", 0, "clocal", "Y")
    $(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("L0",0,"crtscts","N")
```
Set *on* using
```
    $(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("L0", 0, "clocal", "N")
    $(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("L0",0,"crtscts","Y")
```
in the device's `st.cmd`. To turn this off set it to `N` or remove the line completely. Under windows there is a further option to set it to `D` which ensures the hardware lines are floating (this is usually unnecessary).

## Software flow control 

In the device's `st.cmd`:

Set *off* using
```
    $(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("L0",0,"ixon","N") 
    $(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("L0",0,"ixoff","N") 
```
Set *on* using
```
    $(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("L0",0,"ixon","Y") 
    $(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("L0",0,"ixoff","Y") 
```
