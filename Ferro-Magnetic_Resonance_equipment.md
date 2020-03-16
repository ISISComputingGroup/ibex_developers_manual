## Ferro-Magnetic Resonance equipment (FMR)

This is a small collection of devices which internal users of ISIS are testing offline, but have used on the POLREF beamline.  They have written a control program in LabVIEW which communicates with these devices and handles the setpoints, scan/sweep procedure and data file generation.

The individual pieces of equipment are:

- Rhode & Schwartz (ZNB20?) Vector Network Analyser
- Hirst (GM08?) portable Hall probe
- Danfysik 858 PSU (when used on POLREF, Danfysik 8000(?) when offline)

The current solution for using the FMR setup on the beamline, is that the control VI is "wrapped" by an LVDCOM IOC to isolate the users' code and provide remote access from the POLREF control machine.  Therefore the equipment PC runs a "Mini-Inst" to enable this LVDCOM IOC to function.

A CALAB VI runs on the POLREF control machine to enable communication with the FMR equipment IOC and provide logging and scripting capabilities in the SECI system.

### Future Development

Currently, the users' FMR VI does not conform to ISIS standards and would need a reasonable amount of work to bring it up to them (in addition to the changes that have already been made).  As POLREF will be migrated to IBEX sometime in the (near?) future, it may be decided to rewrite the FMR as a native IOC, or collection of IOCs (c.f. zerofield) and possibly run a "remote IOC" (c.f. Triton) installation.  This will depend on the results of the online tests, how much effort is/will be available from the team and how much the equipment will be subsequently used.
