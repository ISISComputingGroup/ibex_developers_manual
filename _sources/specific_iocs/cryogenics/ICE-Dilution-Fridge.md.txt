# ICE Dilution Fridge

## Introduction

This dilution fridge is made by a company called ICE and is no longer supported.

This dilution fridge can not be compared to the Triton dilution fridge, and is the only one not controlled by Triton gas handling systems.

There is only one ICE dilution fridge which is used on MUSR mainly. It is available for EMU and I believe there is an expectation that it will be an option for the RIKEN beam lines also.

## Connection

The ICE dilution fridge itself is controlled through a LabView VI running on a PC called ICECube. That PC runs Windows XP and should absolutely not go on the ISIS network. That PC runs the VI that contains the complicated logic for making dilution happen. That PC is then controlled by an IOC running under IBEX, which replaces a much simpler VI found at `C:\LabVIEW Modules\Drivers\ICEOxford\ICECube` . The IOC talks to ICECube over a serial connection.

Settings:

1. Baud rate: 9600

### Command set

The complete command set for the ICE dilution fridge is detailed in the Remote Interface document on the share network folder.

**Note:** The IOC has been developed to have the same functionality as the ICECube VI. As a result, it only has the PVs and only supports the commands that are used by the VI (with one exception detailed in Gotchas). There are some commands in the Remote Interface that are never used by the VI and are thus not implemented in the IOC. These are: `IDN?`, `1KPUMP?`, `HE3PUMP?`, `ROOTS?`, `STATUS?`, `SVx?`, `Vx?`, `Px?` (where x is the number of the solenoid valve/valve/pressure), `T?`, `T-R?`, `cryo-r?`, `STILL-R?`, `1K-R?`, `1K`, `CLOSEALL`, `LOG=TRUE/FALSE`, `File Path`, `MC-PID`, `MC-TSET`, `MC-HTR-RGE`, `STILL_PWR`, `CRYO-HTR`.

The dilution fridge temperature at low temperatures is controlled via a Lakeshore 370 remotely. This can be found in the documentation command set and the two commands are `LS-DIRECT-SET` and `LS-DIRECT-READ`. These two commands will pass any command that you wish on to the Lakeshore 370 directly - as though you were talking to the device itself. This is probably the reason why the MC- commands listed above are not used, since those parameters are controlled via the LS 370. On the share network folder you can find the manual for the Lakeshore 370 and it gives detailed information about all the commands the Lakeshore accepts. 

The cryostat temperature control is via a CRYOCON 24C. There is a remote direct command also for this namely CRYO-DIRECT-SET and CRYO-DIRECT-READ. They are listed in the Remote Interface but never used by the LabView VI and thus not implemented in the IOC.

### Channels

The ICE dilution fridge has 4 distinct channels:

| Physical sensor location | Channel name | Notes |
| --- | --- | --- |
| Outer Cryostat | T1 | The T1 channel represents the temperature of the outer cryostat and is controlled through VTI Loop 1. VTI Loop 1 has been used by scientists regularly in the past, and is the main temperature on the VTI tab that the instrument scientists are interested in. |
| Auxiliary equipment | T4 | The T4 channel represents a temperature sensor that can be attached to any auxiliary equipment and is controlled by VTI Loop 2. VTI Loop 2 has been used by scientists rarely. |

The T2 and T3 channels are seldom if ever used, therefore the temperature sensors they monitor are almost always disconnected.


## Configuration

In order to run this IOC, you should have the ICECube remote PC running and connected via serial. No further configuration should be needed.

## Gotchas

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
