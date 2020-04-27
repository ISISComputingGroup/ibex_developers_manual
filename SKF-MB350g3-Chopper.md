> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Choppers](Choppers) > [SKF MB350g3 Chopper](SKF-MB350g3-Chopper)

The SKF MB350g3 chopper is a fermi chopper located on the EMMA beamline and was previously used on the LET beamline.  The chopper is mounted on a lifting mechanism detailed [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Fermi-Chopper-Lifter).

It's possible that the controller may need to be reset (press `RESET` button on front panel) after power-on or other condition.  The display will show `INHIBIT` in this case and `READY` after resetting.  The indicator marked `READY` on the OPI will be initially unlit and then lit afterwards.

# Physical setup

Original configuration:
NDXLET <---Ethernet---> AnyWhereUSB <---USB/RS232---> SeaLevel RS232-RS485 converter <---RS485---> MB350PC


New configuration:
NDXLET <---Ethernet---> MOXA NPort <---RS232---> Patton RS232-RS485 converter <---RS485---> MB350PC


Notes:
Originally, the passive RS232-RS485 converter could not be made to work correctly despite much effort, so an alternative, more convoluted solution was adopted in the hope that the original design could be reinstated at a later date.  This alternative solution involved a "SeaLevel SeaLink USB serial adapter" (RS232-RS485 converter) connected to a "Digi USBAnywhere" (remote USB hub over Ethernet).

This worked well for many cycles, however, the USBAnywhere box suddenly developed a regular problem in that it appeared to lose connection to the chopper controllers every couple of days.  Suspected causes are a network scan (either for security or inventory) or a driver issue for the USBAnywhere or SeaCOM converter.  The remedy was to reboot the USBAnywhere box either using the utility on NDXLET or by power-cycling the unit.

New solution follows the original design to use a passive converter (Patton 2085) in circuit with the serial line between the MOXA and chopper controller.  This removes the dependency on additional Windows drivers for extra hardware (AnyWhere USB & SeaLink) and simplifies the cabling as a MOXA is already present.


Switch settings for Patton 2085 Converter:

DCE / DTE switch:  DCE selected

DIP switches:  (All off originally, but this configuration seems to work also)
1: Off
2: Off
3: On
4: Off
5: On
6: Off
7: Off
8: Off


DB9M Pin to 2085 terminal connections:
1 -> RCV-
2 -> RCV+
3 -> XMT+
4 -> XMT-
5 -> G


# Software setup

From a software setup point of view this can be treated as a standard serial device. It needs a COM port and all the usual COM settings to talk to (Baud, parity etc.). From testing on EMMA, the defaults in st.cmd are ok.


# Software

The driver for this chopper has a couple of peculiarities:

## Serial breaks 

The device requires the changes in https://github.com/ISISComputingGroup/EPICS-asyn/pull/6 and the following lines in its st.cmd:

```
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("L0", -1, "break_duration", "20")
$(IFNOTDEVSIM) $(IFNOTRECSIM) asynSetOption("L0", -1, "break_delay", "20")
```

These lines tell it to sleep for 20ms and then send a serial break for 20ms after every message. If these items are not done then the chopper will not respond to messages.

## Custom checksum

The device implements a custom checksum algorithm which has been implemented in https://github.com/ISISComputingGroup/EPICS-StreamDevice/pull/3 and also in the lewis emulator


## Packet format

The device sends and receives a modbus-like (but not actually modbus) packet. This is a packet of binary data which contains various data from the chopper


## Addressing

The chopper can be set up on a multi-drop setup. The first byte of every packet to/from the chopper contains the address of the chopper which is an integer between 0 and 15.
