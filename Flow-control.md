# Flow control 

Flow control is used in serial devices to allow them to better communicate when they are ready to send/receive data. For most devices it should be switched off, unless we know for sure that the device needs to use it. We have seen a number of cases in the past where having it on when not necessary has caused issues.

Flow control comes in two varieties, [hardware](https://en.wikipedia.org/wiki/Flow_control_(data)#Hardware_flow_control) and [software](https://en.wikipedia.org/wiki/Software_flow_control).

## Hardware flow control 

Set using

```
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("$(ASERIAL)",0,"crtscts","Y")
```

in the device's `st.cmd`. To turn this off set it to `N` or remove the line completely. Under windows there is a further option to set it to `D` which ensures the hardware lines are floating (this is usually unnecessary).

## Software flow control 

Set using

```
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("$(ASERIAL)",0,"ixon","Y") 
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("$(ASERIAL)",0,"ixoff","Y") 
```

in the device's `st.cmd`. To turn this off set it to `N` or remove the line completely.