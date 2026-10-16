# Hydrogen Lab

The Hydrogen catalysis laboratory in R79 has two IBEX installations. We do not have physical access to the lab; to obtain access, contact the relevant scientists.

These IBEX installations run on a pair of Dell small-form-factor PCs, `NDHHYDROGEN1` and `NDHHYDROGEN2`. These NDH machines host `NDXHYDROGEN1` and `NDXHYDROGEN2` respectively.

Unusually, the `NDH` machines are *also* used as the 'viewing' machine to view the `NDX` machines.

## Hardware

### Nanodac furnace

Eurotherm Nanodac controller, which we talk to via the `NANODAC_01` IOC in IBEX, over Modbus/TCP. This is a ~600C furnace with
the main readback on Channel 1, and two auxiliary heater readbacks on channels 2 & 3.

It uses an "advanced loop" in the Nanodac to do PID control (so Loop1 and Loop2 both do nothing).

The 'engineer' password for the Nanodac is stored in Keeper under `Hydrogen Lab Nanodac 'engineer' password`

### CCD100s

4x Mk2 CCD100 pressure transducers. Connected via Moxa.

### Eurotherms

A collection of 1/2 sensor Eurotherm controllers.

### Mass Spec

There is manufacturer software on the `NDX`, which has been installed by the mass spec manufacturer. Setting up the software requires license keys to be typed in.

Physically, it talks to the rig via a serial connection (via our MOXA). The manufacturer software can also support a TCP connection. The hardware responds to the command `help` with an ASCII response.

IBEX does not control the mass spec in any way.
