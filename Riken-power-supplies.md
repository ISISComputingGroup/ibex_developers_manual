> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Power Supplies](Power-Supplies) > [Riken power supplies](Riken-power-supplies)

# Setup

![](https://github.com/ISISComputingGroup/ibex_developers_manual/blob/master/images/riken_changeover.PNG?raw=true)

# Documentation

There is some documentation on the physical setup at `\\...\shares\ISIS_Experiment_Controls\Manuals\RIKEN_power_supplies\riken psu controls - issue C.ppt`

# Macros

The RIKEN power supplies are controlled by a number of daisy chained [Danfysik](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Danfysik) PSUs. Daisy chained PSUs are connected to each other in a chain with one PSU at the end connecting to the MOXA. This is done because on RIKEN a large number of PSUs are needed that would require a large number of RJ-45 ports otherwise, so daisy chaining is used to connect multiple PSUs to just one port. 

Macros are prefixed with (for example) `CHAIN1_`. Each chain of PSUs is talking on a completely independent COM port. This is configured using the `CHAIN1_PORT` macro.

For each power supply, the macros will be in the following format:
```
CHAIN1_ADR1=1
CHAIN1_ID1=RQ1
CHAIN1_FRV1=2
CHAIN1_FRI1=625/99990
CHAIN1_FWI1=9999/625
```

Because there are a huge number of macros, they cannot be set in the gui: they must be set via globals.txt

Where:
- `ADR` is the address on the daisy chain of the power supply
- `ID` is the human-friendly name of the power supply
- `FRV` is a scaling factor applied when reading voltage
- `FRI` is a scaling factor applied when reading current
- `FWI` is a scaling factor applied when writing current (note, for some power supplies this can be completely different from the reading scale factor)

Additionally, the IOC talks to DAQ MX to do some changeover logic, which is implemented in SNL inside the IOC.

To run this IOC you will need to install the DAQMX binaries - available on the national instruments website (it is a rather large installer so it is not installed by default).

A minimal globals.txt file which can boot the IOC and connect to the emulator contains:
```
RKNPS_01__CHAIN1_PORT=COM5
RKNPS_01__EMULATOR_PORT1=57677
RKNPS_01__EMULATOR_PORT2=57678
RKNPS_01__EMULATOR_PORT3=57679
RKNPS_01__EMULATOR_PORT4=57680

# GEC 200 volts 500 amps (but scales as 625A)
RKNPS_01__CHAIN1_ADR1=001
RKNPS_01__CHAIN1_ID1=RQ1
RKNPS_01__CHAIN1_FRV1=2
RKNPS_01__CHAIN1_FRI1=625/99990
RKNPS_01__CHAIN1_FWI1=9999/625

# GEC 200 volts 500 amps
RKNPS_01__CHAIN1_ADR2=002
RKNPS_01__CHAIN1_ID2=RB1
RKNPS_01__CHAIN1_FRV2=2
RKNPS_01__CHAIN1_FRI2=500/99990
RKNPS_01__CHAIN1_FWI2=9999/500

```

# Hardware notes / Changeover sequences

### RB2 mode change

- RB2 is a power supply that can be put into three distinct modes: BEND1 (beam goes one way), BEAM2 (the other way), and SEPTUM (beam splits both ways). RB2, although one physical supply, has two control boards. The first control board (called "RB2" in our system) supplies current for either BEND1, BEND2, or half of SEPTUM mode. The second control board ("RB2-2" in our system) is *only* used in SEPTUM mode and supplies the other half of the current.
- We check that BOTH RB2 and RB2-2 are powered off before allowing an RB2 mode change to take place.
- Currently IBEX does not know the state of the changeover switches; only that a switch has been requested. This information is available from the PLC but not currently read.

### Port 3/4 changeover

- The port 3/4 changeover sequence is similar in that RQ18, 19 and 20 power supplies must be OFF before the  sequence can complete. There are three sets of rotary switches that each have 3 positions - Ports 3, 4, and 5 (port 5 does not exist - it is a dummy port).
- These switches redirect power supplies to different magnets based on the mode. RQ 18, 19 and 20 get redirected to RQ 21, 22 and 23 respectively. The underlying power supply stays the same. The switches are controlled by the PLC which drives the changeover logic. 
- Currently IBEX does not know the state of the changeover switches; only that a switch has been requested. This information is available from the PLC but not currently read. Therefore, the driver does not "disable" the power supplies for the "other" mode. For example, RQ18 and RQ21 will always read the same, regardless of the state of the changeover switches. This will be addressed in https://github.com/ISISComputingGroup/IBEX/issues/3490
- It is possible for these switches to get out of sync with each other - see debugging section below
- The switches are located behind a grille, in a corner between port 3 and 4, near some servers and HV power supplies. There are LEDs to say which mode each switch is currently in, which are visible through the grille. To access the switches physically you need a permit - contact Tim Carter.

# Debugging

### Whole chain of PSUs won't talk
- Double check that the moxa port is set to RS-422 mode. **This setting needs to be done in the moxa itself (via the webpage) - IBEX can't do it!**

### Individual PSU won't talk at all

Check the comms cable - it can become loose. It is inside the danfysik unit, you will need the power supplies section to take the front off.

### Individual PSU is talking but does not accept setpoints
Check whether the `.DISP` field is set on records that do not accept values written to them. If yes, it is likely that the instrument thinks it is in changeover (this is the default assumption e.g. if the DAQmx box is not talking to the IOC). You may have to power cycle the DAQmx. There are some pictures on [sharepoint](https://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Forms/AllItems.aspx?RootFolder=%2Fisis%2Fcomputing%2FICPdiscussions%2FRIKEN%20FE&FolderCTID=0x01200027AD8F05966A2748B3B04C98BB5B442B&View={F2C33C51-70E6-4343-B937-2C59A2568306}&InitialTabId=Ribbon%2EDocument&VisibilityContext=WSSTabPersistence) that show what the DAQmx looks like and where it is located on the RIKEN beamline.

### Individual PSU won't talk sensibly / I get interleaved replies / I get delayed replies

This can happen, we are not sure why. The PSU seems to get into a communications mode where it is using a different terminator (I think it's terminator when it gets into this state is `\n\r\n\r\n\r`, and no, that isn't a typo...).

The only (known) way to get out of this state is to power-cycle the power supply at it's main switch.

### I get intermittent communications failures on various PVs, across all of the power supplies

There is a short wait in the protocol file (10ms) between each command to try to overcome this problem. If it re-occurs, the delay may need increasing slightly. If it is increased, the scan rate may need to be decreased so that the serial line can cope with the overall message rate.

### Changeover sequence won't start - PLC indicates "waiting for IBEX to respond".

IBEX will only let the changeover sequence proceed if it gets "off" readings WITHOUT ALARMS from the power supplies it cares about. For RB2 mode change these are "RB2" and "RB2-2", for port 3/4 change these are RQ18, RQ19 and RQ20.

### Changeover sequence won't finish

RB2 mode change:
- Sometimes RB2 does not properly acknowledge the request to change from the PLC. The PLC will then sit there in it's changeover state waiting for the PSU to be in the correct state. To fix this, need to go down in person to RB2 and press the button on the front panel to put it into the mode the PLC expects (it will then detect this and the changeover will finish)

Port changeover:
- The port changeover depends on three rotary switches which are located in the corner between ports 3 and 4 (near some HV power supplies). These switches can, and often do, get out of sync with each other. To fix this state, the misbehaving switch has to be manually forced back into place. The switches are interlocked and you will need a permit to access them. Contact Tim Carter in the first instance.

# Magnet troubleshooting 

This section is from a document by James Lord; the original document on the manuals shared drive

### RQ19 (also known as RQ22)
This magnet supply (Ports 3,4) has an internal reversing switch but no motor to drive it. So if the computer asks for the polarity to change, the control board tries to move the switch but nothing further happens until someone manually changes it – it won’t even accept a request to go back to the polarity it was at before. Normally a polarity change is only required if port 3 or 4 is being switched between positive and negative muons, so this would be at an experiment change over in working hours.
The inst.set_beamline() command is set up to detect if this magnet needs its polarity changing, and will not set any new values – it will return an error similar to that if RB2 had been in the wrong mode. Instead, ask the electrical engineers to turn the supply off, open it up, change the polarity switch, close and turn on the mains power again. Then re-run inst.set_beamline(…,polarity=x,…). This time it will complete successfully as the supply is already set to the required polarity.
You might want to change over the polarity switch at a convenient time while positive muons are going to only ports 1 or 2, in anticipation of changing to using negative muons in port 3 or 4 over a weekend. inst.set_beamline() doesn't care about the polarity of power supplies that it is not using, and that are supposed to be off. There is no need to execute any commands at the time the supply is changed over, just use inst.set_beamline(ports=4,decay=True,polarity=-1,…) once you are ready to use the negative muons.

### RB2
Sometimes RB2-2 reads back implausible numbers such as 75000A. RB2 may also be wrong by a factor of 2. This is often because the IOC (or all of IBEX) has been restarted and the calibration factors for the power supply have been reset to default (which now corresponds to SEPTUM). You might also see this if the RB2 mode has been changed without telling IBEX.
- Run inst.set_RB2_mode(mode,”CAL”) with the mode that RB2 is in now.
- Run inst.set_beamline() to re-send the setpoints.
Note that this procedure may briefly change the value of RB2, so it is best to pause any runs in progress. The restart of IBEX itself would not have affected the magnets.

### RQ2 and RB1
These supplies sometimes don’t turn back on after a polarity change. Usually re-running inst.set_beamline() re-sends the setpoints and they start working eventually.
