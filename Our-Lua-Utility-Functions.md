## Using our Lua utility functions

Currently we have four functions available as utilities for booting iocs using lua: `getMacroValue`, `setAsynOptions`, `setHardwareFlowControl`, `setSoftwareFlowControl`.

To be able to use these you need to add this to the top of your lua file:

```
package.path = package.path .. ';' .. os.getenv("UTILITIES") .. '/lua/luaUtils.lua;'
ibex_utils = require "luaUtils"
```
### `getMacroValue(options)`

Getting a macro from the environment. If the macro cannot be retrieved from the environment the default options value is returned. If there is no default given and the macro cannot be retrieved an error is raised.

- macro: String, the macro to look up in the 
- default: String, the value to return if the macro if the macro is not set in the environment

Example call: `ibex_utils.getMacroValue{macro="RECSIM", default="0"}`
CMD equivalent: `$(RECSIM=0)`

### `setAsynOptions(device, port, baud, bits, parity, stop)`

Note: This automatically sets asyn address port to -1. If you need to set it differently please use the calls `iocsh.drvAsynSerialPortConfigure` and `iocsh.asynSetOption` in your script.

For a real device configure the asyn serial port and set the baud, bits, parity and stop options for it.

- device: String, the name of the asyn port
- port: String, the name of the physical port the device is connected to
- baud: Integer, The baud rate of the device
- bits: Integer, the number of data bits
- parity: String, the device parity
- stop: Integer, the number of stop bits.

Example call: 
```
if (not isRecsim and not isDevsim) then
    local port = ibex_utils.getMacroValue{macro="PORT", default="NO_PORT_MACRO"}
    local baud = ibex_utils.getMacroValue{macro="BAUD", default="9600"}
    local bits = ibex_utils.getMacroValue{macro="BITS", default="8"}
    local parity = ibex_utils.getMacroValue{macro="PARITY", default="none"}
    local stop = ibex_utils.getMacroValue{macro="STOP", default="1"}
    ibex_utils.setAsynOptions(device, port, baud, bits, parity, stop)
...
```

CMD equivalent: 
```
$(IFNOTDEVSIM) $(IFNOTRECSIM) drvAsynSerialPortConfigure("$(DEVICE)", "$(PORT=NO_PORT_MACRO)", 0, 0, 0, 0)
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("$(DEVICE)", -1, "baud", "$(BAUD=9600)")
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("$(DEVICE)", -1, "bits", "$(BITS=8)")
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("$(DEVICE)", -1, "parity", "$(PARITY=none)")
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("$(DEVICE)", -1, "stop", "$(STOP=1)")
```

### `setHardwareFlowControl(device, flowControlOn)`

Note: This automatically sets asyn address port to -1. If you need to set it differently please use the call iocsh.asynSetOption in your script the way you want.

Set the hardware flow control for when it is off or on. 

- device: String, the name of the asyn port.
- `flowControlOn`: Boolean, true if hardware flow control is on.

### `setSoftwareFlowControl(device, flowControlOn)`

Note: This automatically sets asyn address port to -1. If you need to set it differently please use the call iocsh.asynSetOption in your script the way you want.

Sets the software flow control for when it is off or on.

- device: String, the name of the asyn port
- `flowControlOn`: Boolean, true if software flow control is on.

## Adding to our Lua utility functions

Things to do:
- Add documentation in this page (the plan is to have documentation closer to the code, but that also needs to be worked out first)
- Add it to the imports in "Using our Lua utility functions" section above