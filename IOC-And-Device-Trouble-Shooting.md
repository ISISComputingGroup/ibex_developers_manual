> [Wiki](Home) > [Trouble-shooting](trouble-shooting-pages) > IOC and device trouble shooting

# It doesn't work What Should I Do?

1. Connect over hyperterminal (see *Connect over hyperterminal*)
1. Check command set is correct (look at documentation)
1. Start the IOC and check it is not in SIM mode
1. Set the IOC mask (see *What is Passing between the IOC and the *Stream* Device*)

# Connect over hyperterminal

Start hyper-terminal set up connection to device. Find a command that is returns something or that changes something on the display. Run that command look for the change. Try
1. Reading
1. Writing

If it doesn't work check:

1. Protocol (RS232, RS422, RS482)
1. Baud Rate
1. Com Port
1. Stop Bits
1. Parity
1. Line ending/Termination characters. 
1. Flow control

If this doesn't work check the moxa logging (see data over the moxa connection). If this doesn't work there is a device that can be plugged into a serial port to intercept all traffic.

# What is Passing between the IOC and the *Stream* Device

It is possible to put stream into a debug mode where everything sent and received is written to the console. To do this simply add to you st.cmd file (defined on your aysn port) :

```
asynSetTraceMask("L0",-1,0x9) 
asynSetTraceIOMask("L0",-1,0x2)
```

where <port> is the port name you used in the asyn setup eg `drvAsynSerialPortConfigure(<port>...`

This will include the terminator character, if you don't see it it is not being sent or received.
If no reply is given this will include a message "No reply from device in XXXms"

