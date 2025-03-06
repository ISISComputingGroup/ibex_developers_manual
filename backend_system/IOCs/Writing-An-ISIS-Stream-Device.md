


Writing an ISIS StreamDevice
============================

Note: The support module is put in the EPICS\\support directory, but the actual IOC(s) are put in the EPICS\\ioc directory

Using the Hameg 8123 as an example.

Make the main directory::
```
    cd C:\EPICS\support
    mkdir Hameg_8123
    cd Hameg_8123
 ```
Create a version directory::
```
    mkdir 1-0
```
Create a stream support module::
```
    cd 1-0
    makeSupport.pl -t streamSCPI Hameg_8123
```

Edit the protocol file in Hameg_8123Sup, so it reads like::
```
    Terminator = '\r\n';
    ReplyTimeout = 2000;

    getIDN {
        out "*IDN?";
        #Read no more that 39 chars (EPICS limit)
        in "%/(.{0,39})/";
        ExtraInput = Ignore;
    }

    getTriggerLevel {
        out "LV\$1?";
        in "%s";
        ExtraInput = Ignore;
    }

    setTriggerLevel {
        out "LV\$1%s?";
    }
    
    resetCounts {
        out "RES";
    }
```
Note: I have only included a very small section of the command set for this device for brevity.

Delete the db file in Hameg_8123Sup and modify the Makefile so it not longer refers to it.

The next step is to create the IOC, the instructions are [here](Creating-an-ISIS-StreamDevice-IOC)



