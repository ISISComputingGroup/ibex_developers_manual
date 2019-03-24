> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Cryogenics](Cryogenics) > [Triton](Triton)

# Connection

The Triton software runs on a dedicated PC that follows each fridge around. The IBEX control system makes a connection over TCP to issue commands to that software.

Settings:
1. Hostname : For the definitive answer, type `hostname` at a command prompt on the Triton control PC.  The list of Triton hostnames is available on the sharepoint.
1. TCP port : 33576

* If communication cannot be established and you are certain that the correct hostname has been entered, then try the IP address instead.  This can be determined by typing `ipconfig` at a command prompt on the Triton control PC and looking for "IPv4 Address" in the output. 
* Not all the Triton computers respond to a ping.
* Only one connection can be made at any time, additional connections are refused.

There are various generations of Triton systems in use at ISIS. There are sometimes differences in the protocol between different versions of the software (see for example IBEX issue #3030).

# Temperature control

Temperature control in the triton systems is achieved by multiple cooling stages:
- Outer cryostat - usually a eurotherm, ITC503 or lakeshore. This cryostat will typically be able to cool the dilution fridge and sample to a few degrees Kelvin (1-5). 
- Mixing chamber - this is where dilution cooling occurs, which brings the sample down towards base temperature (roughly 20-40mK). Dilution cooling only starts to work around 1K, hence the need for the outer cryostat. Dilution provides a constant amount of cooling power, so for temperature control the mixing chamber is fitted with a small heater which warms up the dilution to the desired temperature.
- There are a number of intermediate stages to bridge the gap between the outer cryostat and dilution. They are not always all present (depending on which fridge is used and experimental setup). In no particular order, there may be: J-T heat exchanger, 4K heat exchanger, sorb, still. The IOC monitors these temperatures if available from the Triton system, but they are not usually of interest to us (they are of interest to cryogenics).

The "base" temperature refers to the lowest achievable temperature in a given setup. This will vary based on which fridge is used and the sample, but is typically in the region of 20-40mK.

| Mode | Temperature range | Notes |
| --- | --- | --- |
| Base temperature | base (*) | In this mode the fridge is using dilution cooling without the heater on: the temperature drops towards base temperature. The heater is not used so PID settings and closed loop mode are irrelevant |
| Temperature control, in dilution | `base<T<~1K` | In this mode the fridge is in dilution, which would normally cool the mixing chamber to base temperature. A heater is then switched on to raise the temperature of the mixing chamber. In this mode, "closed loop" control should be ON,appropriate PID settings should be entered, and the heater range must be large enough to warm the sample to the desired temperature (*). Consult cryogenics if unsure about suitable values. |
| Temperature control, no dilution | `T>~1K` | In this mode the fridge is not using dilution cooling at all: the temperature is controlled by the outer cryostat. The heater is not used so PID settings and closed loop mode are irrelevant |

(*) - The driver has a PID table which looks up appropriate PID settings and heater ranges from a file, based on the temperature setpoint readback. This can be set permanently via IOC macros (if entered manually, it will not be remembered on next IOC restart).

**Note: the IOC does not bring a fridge into/out of dilution. This is a manual process that cryogenics group perform.**

# Configuration

The Triton IOC reads it's configuration (sensor <-> name mapping) from the triton control PC. However, the name <-> channel mapping is hard-coded in the triton IOC, which expects the following mapping:
- Stage 1 (PT1) : J-T heat exchanger
- Stage 2 (PT2) : 4K heat exchanger
- Sorb : Sorb
- Stil : Stil
- Mixing chamber : mixing chamber
- Cooling channel : **not read or used by IOC**

We have a ticket https://github.com/ISISComputingGroup/IBEX/issues/3993 to discuss whether this is actually a valid assumption as we have seen some fridges leave PT1 and PT2 undefined and link the "Cooling channel" to the 4K Heat Exchanger.

# Gotchas

- Oxford software running on the remote PC can occasionally crash. If this happens, you need to VNC to the remote computer using the credentials on the passwords sharepoint page and manually restart the software.
- Some commands take a very long time to generate a reply (can be in the region of 10+ seconds before the reply comes through). This is particularly noticeable for setting values, especially setting closed loop mode on or off.
- [Older versions of Triton software only - see IBEX issue #3030] There are some indexing errors in the Oxford software. Therefore, if you want to read values relating to channel `T3`, you may need to query the device for some variables using `T3` as expected and for other variables using `T2`.
- Sample channel - if this comes back as `T0`, this indicates that it is running on a dedicated control channel, and is newer hardware.
- Beware of things coming back as strings when you expect numbers. For example many commands will respond with `NONE` or `NOT_FOUND` where you would usually expect a numeric response.
- Because the device responds to some commands very slowly, need to be quite careful about the overall command rate - ensure that the device can actually keep up with all the commands being sent.
- Switching "closed loop" on can change the setpoint temperature - I think it changes the setpoint to match the current temperature. This is usually not desirable. See https://github.com/ISISComputingGroup/IBEX/issues/4103 for more details.
