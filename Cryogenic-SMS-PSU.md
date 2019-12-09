These are used to power the HIFI Cryomag. There are four, one (higher max current) controls the main switched cryomagnet, the other three (lower max current) control the X, Y, and Z 'shim' coil magnets. They are capable of driving the main cryomagnet up to a field of ~4.9 Tesla. 

Magnet cool downs typically take several days, warm ups take a similar length of time. It usually sits at 3-4K, the temperature is monitored by a [Keithley 2700](Keithley-2700). 

They are connected via USB to serial RS-232 directly to the NDXHIFI_CRYOMAG PC. 

All commands have a longhand and a shorthand version which can be found in the manual on our network share. The emulator has been made such that it can deal with the longhand or the shorthand, since it must be tested against the VI for compatibility, and the VI uses shorthand commands (vs the IOC which, in its current state in July 2019, uses longhand. This is likely to change).

Commands can reply with a myriad of options. Some of these are time stamped, some are not. These are also listed in the manual on the network share. 

### Emulator

An emulator is being developed for this currently (July 2019) which will be one of the most accurate emulators that the IBEX Project will have made. This is because the Muon Group need to be sure that the new software will work and _not_ quench a superconducting cryomagnet and cost STFC upwards of £1 million to repair/replace it.  
It is meant to be thoroughly tested against the VI in every capacity that the VI can interact with it (and more), and tested against the IOC to check for equivalent control. This means that it needs to do ramping, reply with correct status messages, mock a quench, mock a trip, mock fault states, emergency ramp, and much, much more. Fortunately you can run lewis _X_ times faster than real time, meaning that week-long ramps can be run at 100x speed so that IOC tests don't take weeks to finish. 

### IOC

An IOC is currently (Dec 2019) being developed for this PSU, named CRYOSMS. In order to prevent users from negligently sending commands to the PSU which could damage the cryomagnet (e.g. manually setting an incorrect ramp rate, sending values in wrong units), this IOC has a very non-standard communication system. Users are able to enter values into a large number of PVs as normal, however no use-facing setpoint PVs send commands to the device. Instead, writes triggered by users are sent to an asyn Port Driver, which handles the complex logic associated with ramping, handling quenches, etc. and feeds back values into a set of PVs with the HIDDEN access security group. Users are completely unable to interact or even view the contents of these PVs, the most they can do is confirm their existence. Finally, these hidden PVs send commands to the PSU through streamDevice, which is necessary due to the difficult syntax of certain responses. For reads from the device, the user-facing PVs interact directly with the PSU through streamDevice.

### Operation

The IOC will handle initialisation in asyn, where it will check various macros do determine whether certain modes should be enabled/disabled:

All writes to the device will be disabled in any of these situations:
* `T_TO_A` not supplied
* `MAX_CURR` not supplied
* `ALLOW_PERSIST` is on, but any of the subsequently required variables (`FAST_FILTER_VALUE`, `FILTER_VALUE`, `NPP`, `FAST_PERSISTENT_SETTLETIME`, `FAST_RATE`) are missing
* `USE_SWITCH` is on, but any of the subsequently required variables (`SWITCH_TEMP_PV`, `SWITHCH_HIGH`, `SWITCH_LOW`, `SWITCH_STABLE_NUMBER`, `HEATER_TOLERANCE`, `SWITCH_TIMEOUT`, `SWITCH_TEMP_TOLERANCE`, `HEATER_OUT`) are missing
* `USE_MAGNET_TEMP` is on, but any of the subsequently required variables (`MAGNET_TEMP_PV`, `MAX_MAGNET_TEMP`, `MIN_MAGNET_TEMP`) are missing
* `COMP_OFF_ACT` is on, but any of the subsequently required variables (`NO_OF_COMP`, `MIN_NO_OF_COMP`, `COMP_1_STAT_PV`, `COMP_2_STAT_PV`) are missing

Additionally, the asyn driver will initialise various variables and send several commandss to the PSU based on user provided macros:
* The Tesla-Amps conversion rate will be set to `T_TO_A`
* The maximum allowed current will be set to `MAX_CURR`
* The maximum allowed voltage will be set to `MAX_VOLT`
* The heater output will be set to `HEATER_OUT`

## Macros:
|Macro|Description|Defaults|
|-----|-----------|--------|
|`MAX_CURR`|Define the maximum current that is allowed||
|`T_TO_A`|The conversion value between Tesla and Amps for the system||
|`MAX_VOLT`|Set the maximum voltage for the system||
|`WRITE_UNIT`|Which unit to write to the PSU in|Amps|
|`DISPLAY_UNIT`|Which unit will be used when displaying the value from the PSU|Gauss|
|`RAMP_FILE`|

It initialises and waits in a `Ready` state, depending on things like switch status, temperatures, magnet mode, settle times, etc. `Ready` means that it is ready to drive its field (up or down). It is dangerous to ramp the magnet too fast, so the IOC uses 'ramp tables' which contain field strength-ramp rate pairs. i.e. the magnet can safely ramp up to the field strength at the ramp rate associated with it. Any higher and you risk quenching.

To prevent a quench, the IOC will, upon setting a setpoint, calculate the steps required to safely ramp to the new setpoint. It will then send pairs of values, one ramp rate and one ramp set point, which will start the PSU ramp. The ramp set point is always sent as a new mid setpoint (unless it is doing a ramp to 0). 

If all runs smoothly, the magnet will get up to the field you specify.

#### Pausing

The PSU can pause in the middle of a ramp. This stops ramp generator activity in the PSU and immediately responds with an acknowledge message. Subsequent ramp status queries will inform the IOC that the PSU is paused and holding at a certain current/field strength.

#### Ramping Through 0

The field can switch polarity, depending on the direction of the current driving it. The PSU keeps track of this using a 'direction' which is either +, -, or 0. 0 is only used for Low Field Option mode, see the manual's Appendix N for more. 

When the polarity is switched, i.e. when driving the field from 3T to -3T, the PSU will first ramp to 0, then switch polarity (this shorts the terminals and causes a voltage excursion for 5ms), then carry as it would normally and select appropriate ramp rates as it drives the magnet up to field. 

### Quenching

The magnet can quench if it is ramped too aggressively, or if its temperature drifts too high. If the PSU detects a quench, it report that it thinks the magnet has quenched. The IOC will interpret this and halt all queued actions. It will stay in this state until the IOC is restarted. 