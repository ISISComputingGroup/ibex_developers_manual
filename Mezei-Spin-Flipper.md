# Hardware

- There is a python script **running on a separate PC** which controls some DAQ units
- This python script reads the timing pulse (this can come from the synchrotron or a chopper) and controls the flipper
- The python script exposes a TCP connection
- The python script is available in `\shares\ISIS_Experimental_Controls\external_code\Mezei Neutron Spin Flipper`
- The current labview and IBEX drivers, running on the NDX instrument control PC, use this TCP connection to talk to the flipper system

See also some of the comments in https://github.com/ISISComputingGroup/IBEX/issues/3738 for further details of the hardware setup.

# Gotchas

The communication protocol has several gotchas:
- There is no outbound terminator
- The inbound terminator is `:`, but this character can also be sent as part of some messages (e.g. `getFilename`)
- The code on the remote PC uses regular expressions to parse messages, sending it a message which it doesn't like will cause it to crash and forcibly disconnect the driver
- Must wait for a reply between each message - Sending messages too fast without waiting for replies will cause crashes on the remote end
- In general any exception in the communication layer on the remote end will cause a disconnect
- Sending the controller a command to turn on the analyser if the analyser is not present will cause the remote software to crash
- The Amplitude should be limited to 3A to avoid burning out the coils
- Sending a positive value for delta-T will cause a remote software crash

# Starting the emulator

The emulator for the spin flipper is not a standard lewis emulator. It is a script provided by the developer which acts as a server. It can be started listening on the emulator port 57677 using this command:

```
python C:\Instrument\Apps\EPICS\support\DeviceEmulator\master\other_emulators\mezei_flipper\flipper_emulator.py --port 57677
```