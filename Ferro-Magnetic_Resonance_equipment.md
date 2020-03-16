### Ferro-Magnetic Resonance equipment (FMR)

This is a small collection of devices which internal users of ISIS are testing offline, but have used on the POLREF beamline.  They have written a control program in LabVIEW which communicates with these devices and handles the setpoints, scan/sweep procedure and data file generation.

The individual pieces of equipment are:

- Rhode & Schwartz Vector Network Analyser
- Hirst GM08 portable Hall probe
- Danfysik 858 PSU (when used on POLREF, Danfysik 8000(?) when offline)

The current solution for using the FMR setup on a beamline, is that the control VI is "wrapped" by an LVDCOM IOC to isolate the users' code and provide remote access from the POLREF control machine.  Therefore the equipment PC runs a "Mini-Inst" to enable this LVDCOM IOC to function.
