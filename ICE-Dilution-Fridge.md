> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Cryogenics](Cryogenics) > [ICE Dilution Fridge](ICE Dilution Fridge)

# Introduction

This dilution fridge is made by a company called ICE and is not longer supported.

This dilution fridge can not be compared to the Triton dilution fridge, and is the only one not controlled by Triton gas handling systems.

There is only one ICE dilution fridge which is used on MUSR mainly. It is available for EMU and I believe there is an expectation that it will be an option for the RIKEN beam lines also.

# Connection

The ICE dilution fridge itself is controlled through a LabView VI running on a PC called ICECube. That PC runs Windows XP and should absolutely not go on the ISIS network. That PC runs the VI that contains the complicated logic for making dilution happen. That PC is then controlled by an IOC running under IBEX, which raplaces a much simpler VI found at C:\LabVIEW Modules\Drivers\ICEOxford\ICECube . The IOC talks to ICECube over a serial connection.

Settings:

1. COM port : 57677

1. Baud rate: 9600

### Command set

The complete command set for the ICE dilution fridge is detailed in the Remote Interface document on the share network folder.

**Note:** The IOC has been developed to have the same functionality as the ICECube VI. As a result, it only has the PVs and only supports the commands that are used by the VI (with one exception detailed in Gotchas). There are some commands in the Remote Interface that are never used by the VI and are thus not implemented in the IOC. These are: IDN?, 1KPUMP?, HE3PUMP?, ROOTS?, STATUS?, SVx?, Vx?, Px? (where x is the number of the solenoid valve/valve/pressure), T?, T-R?, cryo-r?, STILL-R?, 1K-R?, MC-R?, 1K, CLOSEALL, LOG=TRUE/FALSE, File Path, MC-PID, MC-TSET, MC-HTR-RGE, STILL_PWR, CRYO-HTR.

The dilution fridge temperature at low temperatures is controlled via a Lakeshore 370 remotely. This can be found in the documentation command set and the two commands are LS-DIRECT-SET and LS-DIRECT-READ. These two commands will pass any command that you wish on to the Lakeshore 370 directly - as though you were talking to the device itself. This is probably the reason why the MC- commands listed above are not used, since those parameters are controlled via the LS 370. On the share network folder you can find the manual for the Lakeshore 370 and it gives detailed information about all the commands the Lakeshore accepts. 

The cryostat temperature control is via a CRYOCON 24C. There is a remote direct command also for this namely CRYO-DIRECT-SET and CRYO-DIRECT-READ. They are listed in the Remote Interface but never used by the LabView VI and thus not implemented in the IOC.

### Channels

The ICE dilution fridge reads data from 3 distinct channels:

| Physical sensor location | Channel name  | Notes |
| --- | --- | --- |
| He3 Pot | `HelioxX` | This is the "main" heliox control channel. According to the OI manual this is the only channel which we should need to use to control the heliox's temperature. In the IOC and LabVIEW driver, this is the only channel on which we allow setting setpoints. It is a hardware alias of either `HeHigh` or `HeLow` depending on temperature (see below). |
| He3 Sorption pump | `He3Sorb` | Dedicated channel for the (helium-3) sorption pump. Monitoring only. Note: the He3 sorption pump and the He3 Pot are not the same! | 
| He4 Pot | `He4Pot` | Dedicated channel for the (helium-4) 1K-pot cooling stage. Monitoring only. Note: the way that ISIS run the Mercury Heliox systems means that this channel will read a constant value all the time, as there is no actual hardware present on the heliox to read this. This hardware would only be present if a single Mercury ITC unit was used to control both the main cryostat and the sorption stage. | 
| He3 Pot (high sensor) | `HeHigh` | Monitoring only. This is a "high" (~2-80K) temperature thermocouple, used for measuring the temperature of the He3 Pot when the temperature is in it's range of validity. This channel will give invalid temperatures if the heliox is running at "low" temperature. | 
| He3 Pot (low sensor) | `HeLow` | Monitoring only. This is a "low" (~0.2-2K) temperature thermocouple, used for measuring the temperature of the He3 Pot when the temperature is in it's range of validity. This channel will give invalid temperatures if the heliox is running at "high" temperature. | 

Because the channel names vary between the Muon Heliox and the LET heliox, they must be supplied as IOC macros.

If a new heliox turns up on another beamline, the following is the process to figure out the required channel names:
- Connect to the device via your favourite terminal emulator (HTerm/PuTTY/HyperTerminal/etc).
- Issue the command `READ:SYS:CAT` (terminated with a line feed, `\n`)
- This will respond with a string like `STAT:SYS:CAT:DEV:<device 1 id>:<device 1 type>:DEV:<device 2 id>:<device 2 type>:...`. 
  * The IDs should look something like `DB1.H1` (meaning: daughter board 1, heater 1)
  * The device type could be one of `TEMP` (temperature), `PRES` (pressure), `HTR` (heater) or `AUX` (auxiliary output).
- For each of the devices in the catalog response, issue the command `READ:DEV:<device id>:<device type>:NICK` (terminated with a line feed)
- The device will respond with a string that looks like `STAT:DEV:MB1.T1:TEMP:NICK:MB1_He3_Sorb`
- The last part of this response (`MB1_He3_Sorb` in this example) is the string that the IOC will need as a macro
- If it's not immediately obvious which channel name corresponds to which item in the table above, consult cryogenics for advice about how the channels have been named.

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

As of https://github.com/ISISComputingGroup/IBEX/issues/3993 this mapping should have been set on all of the fridges by cryogenics section.

# Gotchas

- Oxford software running on the remote PC can occasionally crash. If this happens, you need to VNC to the remote computer using the credentials on the passwords sharepoint page and manually restart the software.
- Some commands take a very long time to generate a reply (can be in the region of 10+ seconds before the reply comes through). This is particularly noticeable for setting values, especially setting closed loop mode on or off.
- [Older versions of Triton software only - see IBEX issue #3030] There are some indexing errors in the Oxford software. Therefore, if you want to read values relating to channel `T3`, you may need to query the device for some variables using `T3` as expected and for other variables using `T2`.
- Sample channel - if this comes back as `T0`, this indicates that it is running on a dedicated control channel, and is newer hardware.
- Beware of things coming back as strings when you expect numbers. For example many commands will respond with `NONE` or `NOT_FOUND` where you would usually expect a numeric response.
- Because the device responds to some commands very slowly, need to be quite careful about the overall command rate - ensure that the device can actually keep up with all the commands being sent.
- Switching "closed loop" on can change the setpoint temperature - I think it changes the setpoint to match the current temperature. This is usually not desirable. See https://github.com/ISISComputingGroup/IBEX/issues/4103 for more details.
  * The workaround is to set the temperature setpoint, wait 500ms, change closed loop mode, wait 500ms, then set the temperature setpoint again.
- Sometimes the channel mapping will appear to be correct from the Oxford software, but will not report correctly from the remote interface. For example, the fridge may report it has no `SORB` channel, even if one is correctly configured. This is a bug in the oxford instruments software running on the triton control PC. To get out of this state, the triton software (on the OI pc) must be restarted. **Check with cryogenics before doing this!**
