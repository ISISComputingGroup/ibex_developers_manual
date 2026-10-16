# Ocean Optics DH-2000

The only the shutter of the Ocean Optics DH-2000 light source is controlled by IBEX, not the operation of the light source itself. The shutter is controlled by TTL pulses, which are supplied by an Arduino board. The EPICS IOC communicates with this Arduino to open/close the shutter, and to get the status of the interlock.