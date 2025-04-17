<html><body>
<!--StartFragment--><p>These are used to power the HIFI Cryomag. There are four, one (higher
 max current) controls the main switched cryomagnet, the other three 
(lower max current) control the X, Y, and Z 'shim' coil magnets. They 
are capable of driving the main cryomagnet up to a field of ~4.9 Tesla.</p>
<p>Magnet cool downs typically take several days, warm ups take a 
similar length of time. It usually sits at 3-4K, the temperature is 
monitored by a <a href="https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Keithley-2700">Keithley 2700</a>.</p>
<p>They are connected via USB to serial RS-232 directly to the NDXHIFI_CRYOMAG PC.</p>
<p>All commands have a longhand and a shorthand version which can be 
found in the manual on our network share. The emulator has been made 
such that it can deal with the longhand or the shorthand, since it must 
be tested against the VI for compatibility, and the VI uses shorthand 
commands (vs the IOC which, in its current state in July 2019, uses 
longhand. This is likely to change).</p>
<p>Commands can reply with a myriad of options. Some of these are time 
stamped, some are not. These are also listed in the manual on the 
network share.</p>
<h3>
<a id="user-content-emulator" class="anchor" href="https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Cryogenic-SMS-PSU#emulator" aria-hidden="true"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"></svg></a></h3>
<h3>
<a id="user-content-ioc" class="anchor" href="https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Cryogenic-SMS-PSU#ioc" aria-hidden="true"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"></svg></a></h3><h3>IOC</h3>
<p>An IOC exists for this PSU, named 
CRYOSMS. In order to prevent users from negligently sending commands to 
the PSU which could damage the cryomagnet (e.g. manually setting an 
incorrect ramp rate, sending values in wrong units), this IOC has a very
 non-standard communication system. Users are able to enter values into a
 large number of PVs as normal, however no use-facing setpoint PVs send 
commands to the device. Instead, writes triggered by users are sent to 
an asyn Port Driver, which handles the complex logic associated with 
ramping, handling quenches, etc. and feeds back values into a set of PVs
 with the HIDDEN access security group. Users are completely unable to 
interact or even view the contents of these PVs, the most they can do is
 confirm their existence. Finally, these hidden PVs send commands to the
 PSU through streamDevice, which is necessary due to the difficult 
syntax of certain responses. For reads from the device, the user-facing 
PVs interact directly with the PSU through streamDevice.</p>
<h3>
<a id="user-content-operation" class="anchor" href="https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Cryogenic-SMS-PSU#operation" aria-hidden="true"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"></svg></a></h3><h3>Operation</h3>
<p>The IOC will handle initialisation in asyn, where it will check 
various macros do determine whether certain modes should be 
enabled/disabled:</p>
<p>All writes to the device will be disabled in any of these situations:</p>
<ul>
<li>
<code>T_TO_A</code> not supplied</li>
<li>
<code>MAX_CURR</code> not supplied</li>
<li>
<code>ALLOW_PERSIST</code> is on, but any of the subsequently required variables (<code>FAST_FILTER_VALUE</code>, <code>FILTER_VALUE</code>, <code>NPP</code>, <code>FAST_PERSISTENT_SETTLETIME</code>, <code>FAST_RATE</code>) are missing</li>
<li>
<code>USE_SWITCH</code> is on, but any of the subsequently required variables (<code>SWITCH_TEMP_PV</code>, <code>SWITHCH_HIGH</code>, <code>SWITCH_LOW</code>, <code>SWITCH_STABLE_NUMBER</code>, <code>HEATER_TOLERANCE</code>, <code>SWITCH_TIMEOUT</code>, <code>SWITCH_TEMP_TOLERANCE</code>, <code>HEATER_OUT</code>) are missing</li>
<li>
<code>USE_MAGNET_TEMP</code> is on, but any of the subsequently required variables (<code>MAGNET_TEMP_PV</code>, <code>MAX_MAGNET_TEMP</code>, <code>MIN_MAGNET_TEMP</code>) are missing</li>
<li>
<code>COMP_OFF_ACT</code> is on, but any of the subsequently required variables (<code>NO_OF_COMP</code>, <code>MIN_NO_OF_COMP</code>, <code>COMP_1_STAT_PV</code>, <code>COMP_2_STAT_PV</code>) are missing</li>
</ul>
<p>Additionally, the asyn driver will initialise various variables and 
send several commands to the PSU based on user provided macros:</p>
<ul>
<li>The Tesla-Amps conversion rate will be set to <code>T_TO_A</code>
</li>
<li>The maximum allowed current will be set to <code>MAX_CURR</code>
</li>
<li>The maximum allowed voltage will be set to <code>MAX_VOLT</code>
</li>
<li>The heater output will be set to <code>HEATER_OUT</code>
</li>
<li>The ramp rate will be set to an appropriate value read from <code>RAMP_FILE</code> based on the current value of the field</li>
</ul>
<h2>
<a id="user-content-macros" class="anchor" href="https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Cryogenic-SMS-PSU#macros" aria-hidden="true"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"></svg></a></h2><h2>Macros:</h2>


Macro | Description | Defaults
-- | -- | --
MAX_CURR | Define the maximum current that is allowed |  
T_TO_A | The conversion value between Tesla and Amps for the system |  
MAX_VOLT | Set the maximum voltage for the system |  
WRITE_UNIT | Which unit to write to the PSU in | Amps
DISPLAY_UNIT | Which unit will be used when displaying the value from the PSU | Gauss
RAMP_FILE | Location of file containing ramp rates |  
ALLOW_PERSIST | Whether or not to allow setting of persistent values | No
USE_SWITCH | Whether or not to monitor and set switches on and off | No
SWITCH_TEMP_PV | PV address of switch temperature |  
SWITCH_HIGH | The value at which the switch will be considered warm | 3.7
SWITCH_LOW | The value at which the switch will be considered cold | 3.65
`SWITCH_STABLE_NUMBER | The number of readings past a threshold needed before the switch can be considered warm/cold | 10
HEATER_TOLERANCE | The tolerance between the magnet and lead currents before considering them as close enough to allow the leads to warm | 0.2
SWITCH_TIMEOUT | The time to allow for the switch to warm or cold after turning the  heater on/off before considering there to be an error situation | 300
SWITCH_TEMP_TOLERANCE | needs clarification |  
HEATER_OUT | The heater output to be used |  
USE_MAGNET_TEMP | Whether to act if the Magnet Temperature is out of range | No
MAGNET_TEMP_PV | The PV address of the magnet temperature |  
MAX_MAGNET_TEMP | Maximum allowed temperature of magnet | 5.5
MIN_MAGNET_TEMP | Temperature below which there is potentially an error reading temperature from the magnet | 1
COMP_OFF_ACT | Whether to act if magnet temperature is out of range | No
NO_OF_COMP | Number of compressors in the system | 2
COMP_1_STAT_PV | The PV address for the status of the first compressor |  
COMP_2_STAT_PV | The PV address for the status of the second compressor |  
FAST_RATE | The ramp rate to use for the fast ramps | 0.5
FAST_PERSISTENT_SETTLETIME | The number of seconds to settle after a ramp fast to persist | 5
PERSISTENT_SETTLETIME | The number of seconds to settle after a ramp to persist | 60
FILTER_VALUE | The value to use to filter the target reached calculation | 0.1
FAST_FILTER_VALUE | The value to use to filter the target reached calculation when ramping fast to a target | 1
NPP | The npp value when calculating whether or not the target has been reached |  


<p>It initialises and waits in a <code>Ready</code> state, depending on things like switch status, temperatures, magnet mode, settle times, etc. <code>Ready</code>
 means that it is ready to drive its field (up or down). It is dangerous
 to ramp the magnet too fast, so the IOC uses 'ramp tables' which 
contain field strength-ramp rate pairs. i.e. the magnet can safely ramp 
up to the field strength at the ramp rate associated with it. Any higher
 and you risk quenching.</p>
<p>To prevent a quench, the IOC will, upon setting a setpoint, calculate
 the steps required to safely ramp to the new setpoint. It will then 
send pairs of values, one ramp rate and one ramp set point, which will 
start the PSU ramp. The ramp set point is always sent as a new mid 
setpoint (unless it is doing a ramp to 0).</p>
<p>If all runs smoothly, the magnet will get up to the field you specify.</p>
<h3>
<a id="user-content-queued-state-machine" class="anchor" href="https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Cryogenic-SMS-PSU#queued-state-machine" aria-hidden="true"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"></svg></a></h3><h3>Queued State Machine</h3>
<p>The IOC makes use of a queued state machine, based upon the meta 
state machine library from boost. Possible states, events (things that 
prompt state changes) and actions (code to perform on given state 
transitions) are defined in this state machine, alongside a table of 
possible transitions and actions to perform on them. Inside the driver, a
 double-ended queue is used to store future transitions to be executed 
(e.g. when the device starts ramping it can queue the next event to be 
reaching the target). Within this queue individual events are stored 
inside <code>variant</code> objects from the boost variant library in 
order to preserve typing (boost msm fires events based on the typing of 
the object being passed to it). A separate thread is run by the driver 
which continually attempts to process the forwardmost item in the queue 
by applying a visitor to it which sends the event to the QSM and deletes
 it from the queue.</p>
<h4>
<a id="user-content-pausing" class="anchor" href="https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Cryogenic-SMS-PSU#pausing" aria-hidden="true"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"></svg></a></h4><h4>Pausing</h4>
<p>The PSU can pause in the middle of a ramp. This stops ramp generator 
activity in the PSU and immediately responds with an acknowledge 
message. Subsequent ramp status queries will inform the IOC that the PSU
 is paused and holding at a certain current/field strength.</p>
<h4>
<a id="user-content-ramping-through-0" class="anchor" href="https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Cryogenic-SMS-PSU#ramping-through-0" aria-hidden="true"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"></svg></a></h4><h4>Ramping Through 0</h4>
<p>The field can switch polarity, depending on the direction of the 
current driving it. The PSU keeps track of this using a 'direction' 
which is either +, -, or 0. 0 is only used for Low Field Option mode, 
see the manual's Appendix N for more.</p>
<p>When the polarity is switched, i.e. when driving the field from 3T to
 -3T, the PSU will first ramp to 0, then switch polarity (this shorts 
the terminals and causes a voltage excursion for 5ms), then carry as it 
would normally and select appropriate ramp rates as it drives the magnet
 up to field.</p>
<h3>
<a id="user-content-quenching" class="anchor" href="https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Cryogenic-SMS-PSU#quenching" aria-hidden="true"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"></svg></a></h3><h3>Quenching</h3>
<p>The magnet can quench if it is ramped too aggressively, or if its 
temperature drifts too high. If the PSU detects a quench, it report that
 it thinks the magnet has quenched. The IOC will interpret this and halt
 all queued actions. It will stay in this state until the IOC is 
restarted.</p><!--EndFragment-->
</body>
</html>