These are used to power the HIFI Cryomag. There are four, one (higher max current) controls the main switched cryomagnet, the other three (lower max current) control the X, Y, and Z 'shim' coil magnets. They are capable of driving the main cryomagnet up to a field of ~4.9 Tesla. 

Magnet cooldowns typically take several days, warm ups take a similar length of time. It usually sits at 3-4K, the temperature is monitored by a [Keithley 2700](Keithley-2700). 

They care connected via USB to serial RS-232 directly to the NDXHIFI_CRYOMAG PC. 

All commands have a longhand and a shorthand version which can be found in the manual on our network share. The emulator has been made such that it can deal with the longhand or the shorthand, since it must be tested against the VI for compatibility, and the VI uses shorthand commands (vs the IOC which, in its current state in July 2019, uses longhand. This is likely to change).

Commands can reply with a myriad of options. Some of these are timestamped, some are not. These are also listed in the manual on the network share. 

### Emulator

An emulator is being developed for this currently (July 2019) which will be one of the most accurate emulators that the IBEX Project will have made. This is becasue the Muon Group need to be sure that the new software will work and _not_ quench a superconducting cryomagnet and cost STFC upwards of £1 million to repair/replace it.  
It is meant to be thoroughly tested against the VI in every capacity that the VI can interact with it (and more), and tested against the IOC to check for equivalent control. This means that it needs to do rmaping, reply with correct status messages, mock a quench, mock a trip, mock fault states, emergency ramp, and much, much more. Fortunately you can run lewis _X_ times faster than realtime, meaning that week-long ramps can be run at 100x speed so that IOC tests don't take weeks to finish. 

### Operation

It initialises and waits in a `Ready` state, depending on things like switch status, temperatures, magnet mode, settle times, etc. `Ready` means that it is ready to drive its field (up or down). It is dangerous to ramp the magnet too fast, so the IOC uses 'ramp tables' which contain field strength-ramp rate pairs. i.e. the magnet can safely ramp up to the field strength at the ramp rate associated with it. Any higher and you risk quenching.

To prevent a quench, the IOC will, upon setting a setpoint, calculate the steps required to safely ramp to the new setpoint. It will then send pairs of values, one ramp rate and one ramp set point, which will start the PSU ramp. The ramp set point is always sent as a new mid setpoint. 