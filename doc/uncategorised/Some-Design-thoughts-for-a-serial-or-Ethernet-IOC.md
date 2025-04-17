## Serial Devices
Applicable - For IOCS (or any code) which ultimately drives something at the end of a real wire or a fibre where the comms. are very much an end-to-end affair.

Not applicable - Some IOCS are to drive things in crates (with hardware slots interrupt lines etc.) this is not about these, also it is not about things that communicate with other bits of manufacturers code (unless this ultimately ends up driving a serial device).

## Different models for device communication
There are generally two sorts of "serial" devices.

Those that "chatter" to the computer regardless of whether you talk to them, for those an IOC should treat this chatter as a heartbeat (i.e. timeout and report a comms. error if it doesn't receive what it should within a time). We’ve generally not preferred these sort of comms. (if we have a choice) because they can be a bit awkward to program and are by definition asynchronous with the code talking to them (unfortunately, hardware people often quite like these).

Alternatively, there are "obedient" devices which only speak when they are spoken to. These must be polled because this is the only way we will know they still are working. In fact, they must really be polled so as to return at least one data value or response packet.  Devices which accept silent commands need to checked for data coming back (one wire may not be connected). The rate of polling for data can then be set lower than this (or on demand) if values are not needed very often. An IOC is simplified if heartbeat and data needs are satisfied at the same rate which is normal.  For "chatterers" it may be possible to alter the rate of chatter with a device command.

As far as I can think, this will apply to any device connected to any simple serial "bus" RS232, Ethernet, MODBUS etc. There is a point to be made that between two bits of code on a local system, polling is generally a poor idea (software should use events/interrupts). When talking to real hardware without its own interrupt lines, it is essential.

The network load of polling is generally very low for real RS232 speeds even at 115Kb (the CPU load of over-polling serial calls might be higher though). On the Ethernet, saturation of an Ethernet link is slightly possible, but as long as the device is fairly dumb and one waits for a reply, the chances of a very tight loop are quite low (I would always put in a delay though).

Just some thoughts as you continue into the design of your IOC.
