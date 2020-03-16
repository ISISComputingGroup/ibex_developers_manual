## Ferro-Magnetic Resonance equipment (FMR)

This is a small collection of devices which internal users of ISIS are testing offline, but have used on the POLREF beamline.  They have written a control program in LabVIEW which runs on a separate machine and communicates with these devices and handles the setpoints, scan/sweep procedure and data file generation.

The individual pieces of equipment are:

- Rohde & Schwartz (ZNB20?) Vector Network Analyser
- Hirst (GM08?) portable Hall probe
- Danfysik 858 PSU (when used on POLREF, Danfysik 8000(?) when offline) connected to...
- GMW conventional electromagnet (not cryogenic, no direct control required)

The current solution for using the FMR setup on the beamline, is that the control VI is "wrapped" by an LVDCOM IOC to isolate the users' code and provide remote access from the POLREF control machine.  Modifications had to be made to this VI to enable it to be run continuously and make the front panel item names compatible with LVDCOM (remove trailing spaces and scientific notation values e.g. `Start Frequency (300.0e3) `).  The equipment PC runs a "Mini-Inst" to enable this LVDCOM IOC to function.

A bespoke CALAB VI was written and runs on the POLREF control machine.  This enables communication with the FMR equipment IOC and provides scripting and logging capabilities in the SECI system.

### Future Development

Currently, the users' FMR VI does not conform to ISIS standards and would need a reasonable amount of work to bring it up to them.  Rather than concentrate efforts on this VI, and as POLREF will be migrated to IBEX sometime in the (near?) future, it may be decided to rewrite the FMR control program as a native IOC, or collection of IOCs (c.f. [zerofield](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Zero-field-controller)) and possibly run a "[remote IOC](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Remote-IOCs)" (c.f. Triton) installation.  This will depend on the results of the online tests, how much effort is/will be available from the team and how much the equipment will subsequently be used.
