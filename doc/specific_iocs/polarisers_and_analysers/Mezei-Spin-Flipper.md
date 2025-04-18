# Mezei spin flipper

## Hardware versions

There are two versions of the Mezei flipper hardware in use, and so the IOC and OPI have two versions to cope with these differences

### V1

This hardware is in use on POLREF. It was originally in use by LET, but was superceded by V2 (which has been set back to V1 because of communication issues as of 16/11/2020) in https://github.com/ISISComputingGroup/IBEX/issues/4871 .

If you need to use V1 hardware, you should set the following macros in `globals.txt` to enable support for the old protocol:

```
MEZFLIPR_01__PROTOCOL_VERSION=1
MEZFLIPR_01__POLARISERPRESENT=yes
MEZFLIPR_01__ANALYSERPRESENT=yes
```

For this hardware, use the `Mezei flipper (v1)` OPI.

### V2

This is newer hardware which is now in use on LET. POLREF plan to eventually also migrate to this hardware, however, this has not been done as of September 2020.

V2 hardware is assumed by default in the ioc; no special configuration is required to use it. It should use the `Mezei flipper` OPI.

The port used by default is 80. As of [#7206](https://github.com/ISISComputingGroup/IBEX/issues/7206) we now enforce that this is added to the `HOST` macro. 

## Hardware

- There is a python script **running on a separate PC** (LET:NDW1889, POLREF:NDW1937) which controls some DAQ units
- This python script reads the timing pulse (this can come from the synchrotron or a chopper) and controls the flipper
- The python script exposes a TCP connection
- The python script is available in `\shares\ISIS_Experiment_Controls\external_code\Mezei Neutron Spin Flipper`
- The current labview and IBEX drivers, running on the NDX instrument control PC, use this TCP connection to talk to the flipper system
- There is also some optimization code. This is an instrument script which runs on the NDX machine and communicates with PVs via genie_python. This is what determines the mode and parameters which the flipper will run with. Therefore these modes and parameters are not expected to be set manually.

See also some of the comments in https://github.com/ISISComputingGroup/IBEX/issues/3738 and https://github.com/ISISComputingGroup/IBEX/issues/4871 for further details of the hardware setup.

The flipper can run in one of four different mode:

| Mode | Explanation |
| --- | --- |
| Constant current | Does what it says on the tin - a simple constant current is supplied to the magnet coils |
| Steps | On LET, they use RRM (repetition-rate multiplication) to select multiple incident energies per neutron pulse (frame). Running the flipper in "steps" mode supplies a different current to the coils for each incident energy. |
| Analytical | This mode varies the current to the coils as a function of time, within each neutron pulse. The equation being modelled is `I = A / (t + t0)` |
| File | This mode uses a file as a lookup table to determine current to the flipper coils as a function of time within each neutron pulse |

Each mode takes a "parameter", which is passed to the flipper as a string. It is passed to the flipper as a string to allow arbitrarily complex data structures to be transmitted to the python code which controls the flipper (for example, a common case is to pass a python list as the parameter). These parameters are only ever written to by an optimization script running on the NDX computer.

The other variables which the flipper can take are:
- **Power**: power to the coils on/off.
- **Compensation**: a fixed current which is always added to whatever value the lookups provide, to compensate for changes caused by the flipper kit itself.