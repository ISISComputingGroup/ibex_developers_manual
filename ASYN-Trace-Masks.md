# ASYN trace facility 

For asyn based drivers, such as stream device, additional information printing can be enabled on a port via commands from the ioc shell. 

## The ASYN trace mask

This is set to 0x1 (ASYN_TRACE_ERROR) by default, the following additional values
can be ORed together and optionally set:

* 0x1   (ASYN_TRACE_ERROR)    - Print error messages (default)
* 0x2   (ASYN_TRACEIO_DEVICE) - Device support reports I/O activity.
* 0x4   (ASYN_TRACEIO_FILTER) - Any layer between device support and the low level driver
* 0x8   (ASYN_TRACEIO_DRIVER) - Low level driver reports I/O activity
* 0x10  (ASYN_TRACE_FLOW)     - Report logic flow
* 0x20  (ASYN_TRACE_WARNING)  - Report warnings, i.e. conditions between ASYN_TRACE_ERROR and ASYN_TRACE_FLOW

If L0 if your asyn port, then

`asynSetTraceMask("L0",-1,0x9)`

will enable ASYN_TRACE_ERROR and ASYN_TRACEIO_DRIVER for all addresses (-1) on port "L0" which is a good place to start for debugging. You may also want to add ASYN_TRACE_FLOW but this can print a bit too much depending on the driver and you loose the IO device messages amongst them. 

`asynSetTraceMask("L0",0,0x11)`

will enable ASYN_TRACE_ERROR and ASYN_TRACE_FLOW on port "L0" but just for address 0 

## ASYN traceIO mask

If  ASYN_TRACEIO_DRIVER has been enabled, then this mask determines the format of the output produced. The default is ASYN_TRACEIO_NODATA so the count of bytes transferred is reported, but the bytes themselves are not printed.

* 0x0  (ASYN_TRACEIO_NODATA) - print count of bytes transferred, but not bytes themselves
* 0x1  (ASYN_TRACEIO_ASCII)  - Print with a "%s" style format
* 0x2  (ASYN_TRACEIO_ESCAPE) - Calls epicsStrPrintEscaped() to display characters.
* 0x4  (ASYN_TRACEIO_HEX)    - Print hexadecimal values of each byte with " %2.2x".

`asynSetTraceIOMask("L0",-1,0x2)`

would enable ASYN_TRACEIO_ESCAPE printing of bytes read/written

## Additional trace information

This mask determines the information printed at the start of each message

* 0x1  (ASYN_TRACEINFO_TIME)   prints the date and time of the message 
* 0x2  (ASYN_TRACEINFO_PORT)   prints [port,addr,reason], where port is the port name, addr is the asyn address, and reason is pasynUser->reason. These are the 3 pieces of "addressing" information in asyn.
* 0x4  (ASYN_TRACEINFO_SOURCE) prints the file name and line number, i.e. [__FILE__,__LINE__] where the asynPrint or asynPrintIO statement occurs.
* 0x8  (ASYN_TRACEINFO_THREAD)  prints the thread name, thread ID and thread priority, i.e. [epicsThreadGetNameSelf(), epicsThreadGetIdSelf(), epicsThreadGetPrioritySelf()].


