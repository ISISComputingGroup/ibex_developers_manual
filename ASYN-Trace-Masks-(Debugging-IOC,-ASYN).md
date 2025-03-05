For asyn based drivers, such as stream device, additional information printing can be enabled on a port via commands from the ioc shell. The commands let you see what bytes are being sent and received, and also the flow of control/logic.

## Print commands and responses to screen

The two commands you need are:

```
asynSetTraceIOMask("L0", -1, 0x2)
asynSetTraceMask("L0", -1, 0x9)
```

Note: if the device's messages are longer than 80 characters, you should increase the buffer size by also running:

```
asynSetTraceIOTruncateSize("L0", -1, 1024)
```

Where 1024 is the maximum message length you expect - could be increased if your device requires it.

to turn off use
```
asynSetTraceMask("L0", -1, 0x1)
```

## ASYN trace mask

This determines what you see and is set to 0x1 (ASYN_TRACE_ERROR) by default. The following additional values
can be ORed together and optionally set:

* `0x1`: ASYN_TRACE_ERROR - Print error messages (default)
* `0x2`: ASYN_TRACEIO_DEVICE - Device support reports I/O activity.
* `0x4`: ASYN_TRACEIO_FILTER - Any layer between device support and the low level driver e.g. asyn interpose functions 
* `0x8`: ASYN_TRACEIO_DRIVER - Low level driver reports I/O activity
* `0x10`: ASYN_TRACE_FLOW - Report logic flow
* `0x20`: ASYN_TRACE_WARNING - Report warnings, i.e. conditions between ASYN_TRACE_ERROR and ASYN_TRACE_FLOW

If L0 if your asyn port, then

`asynSetTraceMask("L0",-1,0x9)`

will enable ASYN_TRACE_ERROR and ASYN_TRACEIO_DRIVER for all addresses (-1) on port "L0" which is a good place to start for debugging. You may also want to use ASYN_TRACE_FLOW but this can print a bit too much depending on the driver and you may loose your IO device messages amongst them. If you want to try this separately then e.g. 

`asynSetTraceMask("L0",0,0x11)`

will enable ASYN_TRACE_ERROR and ASYN_TRACE_FLOW on port "L0" but just for address 0.

To see output of interpose functions such as `asynInterposeThrottle` add `0x4`, so `0x9` become `0xD` for example

## ASYN traceIO mask

If  ASYN_TRACEIO_DRIVER  has been enabled, then this mask determines the format of the output produced when reporting I/O. The default is ASYN_TRACEIO_NODATA so the count of bytes transferred is reported, but the bytes themselves are not printed.

* `0x0` (ASYN_TRACEIO_NODATA) - Print count of bytes transferred, but not bytes themselves
* `0x1`  (ASYN_TRACEIO_ASCII)  - Print bytes with a "%s" style format
* `0x2`  (ASYN_TRACEIO_ESCAPE) - Calls epicsStrPrintEscaped() to display bytes
* `0x4`  (ASYN_TRACEIO_HEX)    - Print hexadecimal values of each byte with " %2.2x"

So

`asynSetTraceIOMask("L0",-1,0x2)`

would enable ASYN_TRACEIO_ESCAPE style printing of all bytes read/written by the asyn driver via port "L0", which is a good place to start

## Additional trace information

This mask determines the information printed at the start of each message above. The default is ASYN_TRACEINFO_TIME which just adds a timestamp, normally this is sufficient but it can be changed by calling  asynSetTraceInfoMask  with a combination of flags:

* `0x1`  `(ASYN_TRACEINFO_TIME)`   prints the date and time of the message (default)
* `0x2`  `(ASYN_TRACEINFO_PORT)`   prints `[port,addr,reason]`, where port is the port name, `addr` is the asyn address, and reason is pasynUser->reason. These are the 3 pieces of "addressing" information in asyn.
* `0x4`  `(ASYN_TRACEINFO_SOURCE)` prints the file name and line number, i.e. [__FILE__,__LINE__] where the asynPrint or asynPrintIO statement occurs.
* `0x8`  `(ASYN_TRACEINFO_THREAD)`  prints the thread name, thread ID and thread priority, i.e. [epicsThreadGetNameSelf(), epicsThreadGetIdSelf(), epicsThreadGetPrioritySelf()].

e.g. to print time and port details at start of each message

`asynSetTraceInfoMask("L0",-1,0x3)` 

## Logging to file

By default the trace output is sent to the epics error log (which by default echoes to console too), but it can instead be sent to file e.g.

`asynSetTraceFile("L0",-1,"temp.log")`

# Getting (VERY VERBOSE) output from stream device.

In your `st.cmd`, or at the EPICS prompt from a console session, use:

`var streamDebug 1`

This will turn on debug logging from stream device which is very verbose.

# Seeing all channel access put requests to the IOC

In your `st.cmd`, or at the EPICS prompt from a console session, use:

`var caPutLogToConsole 1`

This will log all details of `caput` etc to the ioc to console using the `caPutLog` mechanism.
 
