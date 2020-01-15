> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Cryogenics](Cryogenics) > [ICE Dilution Fridge](ICE-Dilution-Fridge)

# Introduction

This dilution fridge is made by a company called ICE and is no longer supported.

This dilution fridge can not be compared to the Triton dilution fridge, and is the only one not controlled by Triton gas handling systems.

There is only one ICE dilution fridge which is used on MUSR mainly. It is available for EMU and I believe there is an expectation that it will be an option for the RIKEN beam lines also.

# Connection

The ICE dilution fridge itself is controlled through a LabView VI running on a PC called ICECube. That PC runs Windows XP and should absolutely not go on the ISIS network. That PC runs the VI that contains the complicated logic for making dilution happen. That PC is then controlled by an IOC running under IBEX, which replaces a much simpler VI found at C:\LabVIEW Modules\Drivers\ICEOxford\ICECube . The IOC talks to ICECube over a serial connection.

Settings:

1. Baud rate: 9600

### Command set

The complete command set for the ICE dilution fridge is detailed in the Remote Interface document on the share network folder.

**Note:** The IOC has been developed to have the same functionality as the ICECube VI. As a result, it only has the PVs and only supports the commands that are used by the VI (with one exception detailed in Gotchas). There are some commands in the Remote Interface that are never used by the VI and are thus not implemented in the IOC. These are: `IDN?`, `1KPUMP?`, `HE3PUMP?`, `ROOTS?`, `STATUS?`, `SVx?`, `Vx?`, `Px?` (where x is the number of the solenoid valve/valve/pressure), `T?`, `T-R?`, `cryo-r?`, `STILL-R?`, `1K-R?`, `1K`, `CLOSEALL`, `LOG=TRUE/FALSE`, `File Path`, `MC-PID`, `MC-TSET`, `MC-HTR-RGE`, `STILL_PWR`, `CRYO-HTR`.

The dilution fridge temperature at low temperatures is controlled via a Lakeshore 370 remotely. This can be found in the documentation command set and the two commands are `LS-DIRECT-SET` and `LS-DIRECT-READ`. These two commands will pass any command that you wish on to the Lakeshore 370 directly - as though you were talking to the device itself. This is probably the reason why the MC- commands listed above are not used, since those parameters are controlled via the LS 370. On the share network folder you can find the manual for the Lakeshore 370 and it gives detailed information about all the commands the Lakeshore accepts. 

The cryostat temperature control is via a CRYOCON 24C. There is a remote direct command also for this namely CRYO-DIRECT-SET and CRYO-DIRECT-READ. They are listed in the Remote Interface but never used by the LabView VI and thus not implemented in the IOC.

### Channels

The mercury ITC driver essentially reads data from 5 distinct channels:

| Physical sensor location | Channel name on LET heliox | Channel name on Muon heliox | Notes |
| --- | --- | --- | --- |
| He3 Pot | `HelioxX` | `HelioxX` | This is the "main" heliox control channel. According to the OI manual this is the only channel which we should need to use to control the heliox's temperature. In the IOC and LabVIEW driver, this is the only channel on which we allow setting setpoints. It is a hardware alias of either `HeHigh` or `HeLow` depending on temperature (see below). |
| He3 Sorption pump | `He3Sorb` | `MB1_He3_Sorb` | Dedicated channel for the (helium-3) sorption pump. Monitoring only. Note: the He3 sorption pump and the He3 Pot are not the same! | 
| He4 Pot | `He4Pot` | `DB6_He4Pot` | Dedicated channel for the (helium-4) 1K-pot cooling stage. Monitoring only. Note: the way that ISIS run the Mercury Heliox systems means that this channel will read a constant value all the time, as there is no actual hardware present on the heliox to read this. This hardware would only be present if a single Mercury ITC unit was used to control both the main cryostat and the sorption stage. | 
| He3 Pot (high sensor) | `HeHigh` | `DB7_He3_Pot_CRN` | Monitoring only. This is a "high" (~2-80K) temperature thermocouple, used for measuring the temperature of the He3 Pot when the temperature is in it's range of validity. This channel will give invalid temperatures if the heliox is running at "low" temperature. | 
| He3 Pot (low sensor) | `HeLow` | `DB8_He3_Pot_Low` | Monitoring only. This is a "low" (~0.2-2K) temperature thermocouple, used for measuring the temperature of the He3 Pot when the temperature is in it's range of validity. This channel will give invalid temperatures if the heliox is running at "high" temperature. | 

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

# Configuration

In order to run this IOC, you should have the ICECube remote PC running and connected via serial. No further configuration should be needed.

# Gotchas

- Some PVs are set to scan every second, some every 5 seconds and some every 10 seconds. Because of this, some of the readbacks in the OPI take a bit to update after you set the setpoint. Because there are a lot of read requests since the IOC has many PVs, sometimes it takes even longer for the pv to update, up to 8 seconds for 5 second scan PV and up to 12 seconds for a 10 second scan pv. There are forward links in the setpoint corresponding to these PVs so that the readback is updated immediately after changing the setpoint, but the command is queued among others so it does not help much.
- There are some graphical elements in the VI code that are hidden and that do not appear during use of the VI as far as we know. This is a readback for 1K (different from readback of 1K stage, uses the 1K? command), a readback for the state of the device (that is in included in the diagnostics tab of the OPI) and proportional valve 4. Proportional valve 4 is implemented in the IOC but does not appear in the OPI. The 1K readback has not been implemented because we looked through the blocks on the configurations of MUSR and EMU on SECVI and found no block on 1K, so we assumed it was not important.
- The roots pump indicator and button do not show up in the VI when not running, but appear once you run it against an emulator.
- When you send a set command, the ICECube PC sends back a reply of "OK". The exception is for any set commands sent to the Lakeshore 370 directly, where it replies with "Set LakeShore 370".
- When you set the temperature setpoint for the mixing chamber in the Lakeshore OPI tab, it also sets the scan and cmode Lakeshore 370 settings. If the setpoint is zero, scan is set has arguments 6 and 1, and cmode is set to 4. If it is not zero, scan receives arguments 6 and 0 and cmode is set to 1.
- When setting the Lakeshore MC PID values, you need to set all of them at once. The IOC does this by updating all MC PID readbacks then sending the values replacing one of them with the new setpoint.
- The Lakeshore MC Integral and Derivative are always integers. The ICECube sends them back when reading the PID values as integers and not as floats.
- When reading the voltage range the device sends 5 values. The second is the voltage range, and the last three are ignored when reading for the readback of the voltage range of a channel. But when you want to set the voltage range setpoint, you need to send the device 6 values, the last three being the Voltage Range Resistance Range, the Voltage Range auto-range mode and voltage range CS-Off mode. Therefore, when you change the setpoint, the IOC first reads the voltage range and saves those three values to some private PVs. Those are then used for the set command sent to the Lakeshore 370.
- The Proportional and Needle Valves' OPI images are either green or red depending on whether or not their value is more than zero, or zero respectively. This is done through a calc record for each valve that checks if the readback is greater than zero.
- On the Mimic tab of the ICECube Client vi, the M/C(K) readback displays one of two different values. It displays the mixing chamber temperature if that is over or equal to 0.051 K. If it is under 0.051 K, it displays the readback of the Mixing Chamber Resistance. Initially, this was also implemented in the IOC and OPI. However, after testing it with the instrument scientist we decided that it was a bit confusing. As a result, we agreed to always display the two readbacks separately on the Mimic tab of the OPI.
- During testing with the hardware, we discovered that the Mixing Chamber Resistance readback was 1000 times higher than the readback on the ICECube. No division is done in the ICECube client vi, so we assume it is done in the ICECube vi. A calc record was added to divide the readback by 1000 and that calc record value is shown in the OPI.
- On the mimic tab, the "Temperature set" setpoint is sent to the device only when you press Start and if the Sequence is set to Temperature Control.
- The sequence dropdown ad the Start, Stop and Skip buttons are only enabled when the Mode is set to Semi Automatic.
- The ICECube Client does not read or set the mode. The Remote Interface of ICECube has no commands to read or set the mode of the dilution fridge. The mode drop down on the OPI only enables or disables the Start/Stop/Skip buttons. The OPI drop down is Alarm sensitive to make it clear that in the beginning the value in the drop down does not reflect what the hardware does.
