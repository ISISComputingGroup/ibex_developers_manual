> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Cryogenics](Cryogenics) > [ICE Dilution Fridge](ICE Dilution Fridge)

# Introduction

This dilution fridge is made by a company called ICE and is not longer supported.

This dilution fridge can not be compared to the Triton dilution fridge, and is the only one not controlled by Triton gas handling systems.

There is only one ICE dilution fridge which is used on MUSR mainly. It is available for EMU and I believe there is an expectation that it will be an option for the RIKEN beam lines also.

# Connection

The ICE dilution fridge itself is controlled through a LabView VI running on a PC called ICECube. That PC runs Windows XP and should absolutely not go on the ISIS network. That PC runs the VI that contains the complicated logic for making dilution happen. That PC is then controlled by an IOC running under IBEX, which raplaces a much simpler VI found at C:\LabVIEW Modules\Drivers\ICEOxford\ICECube . The IOC talks to ICECube over a serial connection.

Settings:

1. Baud rate: 9600

### Command set

The complete command set for the ICE dilution fridge is detailed in the Remote Interface document on the share network folder.

**Note:** The IOC has been developed to have the same functionality as the ICECube VI. As a result, it only has the PVs and only supports the commands that are used by the VI (with one exception detailed in Gotchas). There are some commands in the Remote Interface that are never used by the VI and are thus not implemented in the IOC. These are: IDN?, 1KPUMP?, HE3PUMP?, ROOTS?, STATUS?, SVx?, Vx?, Px? (where x is the number of the solenoid valve/valve/pressure), T?, T-R?, cryo-r?, STILL-R?, 1K-R?, MC-R?, 1K, CLOSEALL, LOG=TRUE/FALSE, File Path, MC-PID, MC-TSET, MC-HTR-RGE, STILL_PWR, CRYO-HTR.

The dilution fridge temperature at low temperatures is controlled via a Lakeshore 370 remotely. This can be found in the documentation command set and the two commands are LS-DIRECT-SET and LS-DIRECT-READ. These two commands will pass any command that you wish on to the Lakeshore 370 directly - as though you were talking to the device itself. This is probably the reason why the MC- commands listed above are not used, since those parameters are controlled via the LS 370. On the share network folder you can find the manual for the Lakeshore 370 and it gives detailed information about all the commands the Lakeshore accepts. 

The cryostat temperature control is via a CRYOCON 24C. There is a remote direct command also for this namely CRYO-DIRECT-SET and CRYO-DIRECT-READ. They are listed in the Remote Interface but never used by the LabView VI and thus not implemented in the IOC.

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
