Flow control for most devices should be switched off, unless we know for sure that the device needs to use it. To confirm that flow control is switched off, check for 

```
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("$(ASERIAL)",0,"ixon","N") 
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("$(ASERIAL)",0,"ixoff","N") 
```

in the device's `st.cmd`. If it is not present, it defaults to off.