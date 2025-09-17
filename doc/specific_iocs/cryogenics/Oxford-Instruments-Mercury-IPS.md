# Mercury IPS

The Oxford Instruments Mercury IPS is a superconducting magnet power supply. It is the successor to the [IPS](Oxford-Instruments-IPS). Much of the information on the IPS wiki page also applies to the Mercury IPS.

Note: although the Mercury IPS is the successor to the "old" IPS, cryogenics prefer to run the older IPS units as they are more reliable.

## Hardware quirks (Legacy mode)

The following faults can be seen when operating the magnet fully from the front panel, but it is likely that software will also run into the same conditions:
  * The firmware will sometimes crash/freeze. To reset it, the whole power supply needs to be power-cycled. This is obviously undesirable for a magnet power supply, and cryogenics are chasing OI about this issue. It's not clear whether this issue is general to all Mercury IPS units or whether we have one faulty unit.
  * The switch heater occasionally reports that it's ON when it's actually OFF
  * The power supply reports a voltage of ~9000V which is incorrect (a sensible voltage for this power supply would be around ~8V while ramping)
  
## SCPI Protocol

The IPS IOC now supports the SCPI protocol, which is more feature rich than Legacy mode.
Effort was made to ensure that the top level EPICS interface was was changed as little as possible.
It was particularly important that the SNL state-machine logic was not altered.
This all required some careful designing of the new interface to provide PV compatibility with the legacy mode.
There is now significantly more diagnostic information available, along with support for daughter-boards, such as He and N level meters, pressure measurement, etc., all of which have necessitated additions to the user interface in the IBEX client.
The IOC can be configured to run with either legacy or SCPI protocols via a STREAMPROTOCOL macro ("SCPI" | "LEGACY"). The IOC publishes a new PV $(P)PROTOCOL, which reflects the configuration mode, allowing the user interface to hide or show attributes and controls relevant to SCPI or LEGACY modes.

As already mentioned, SCPI mode provides additional status reporting, much of which is based on the return string from the "READ:SYS:ALRM" command, which is poorly documented in the supplier's documentation. The status strings are assumed to all conform to the "Directory of Alarms" section (17.3) of the Operator's Manual (Issue 20, July 2018).
Whilst many of the system alarms that we could test, mostly conformed, some differences were noticed, along with additional, undocumented status, such as "Magnet Safety".
It has not been possible to test all alarm scenarios with the IPS unit and as such unable to fully ascertain that all the expected message strings are correct - they may need to be adjusted later on, if/when they arise.

The support module exports an aSub record subroutine to facilitate handling of the responses to READ:SYS:ALRM, which is not feasible with a StreamDevice protocol handler.

### CONTROL and CONTROL:SP
These records have been removed from the SCPI variant database
as the SCPI command set does not manage the panel lock in the same was as legacy and
Magnet Group advised to remove this feature, as they always want to be able to control
the IPS via the front panel.

### SYSTEM:HWFAULT status is derived from the status bits via a calc record.
This collates the various possible hardware faults into a single record,
which in the legacy protocol is a single value (Xm bit 4).

### SWEEPMODE:PARAMS and SWEEPMODE:SWEEP
These records have been removed as they are meaningless and underivable in SCPI protocol.

### _SWEEPMODE:SWEEP
In the legacy version, this used to be the readback from n of Mmn part of Examine command return.
0 output constant, 1, 2, 3 output changing
The SCPI protocol doesn't directly offer this, so it has to be derived via the ACTIVITY record (DEV:GRPZ:PSU:ACTN)
Direction from Alex Jones: "A response of HOLD or CLMP would be equivalent to n=0 in the response of the X command
in the old protocol. Responses of RTOS or RTOZ would be equivalent to n=1.
There is no equivalent for the m=0,1 fast/slow ramps, but we do not use this feature anyway."

### System Alarms
System alarms are derived by interrogating the IPS with the "READ:SYS:ALRM?" SCPI command.
This returns a comma-separated string of active alarms, or an empty string if no alarms are present.
The string is parsed by an aSub record, which sets the relevant bits in a binary register.
The bits are mapped to individual status records, which are then used to set the relevant alarms.
The precise protocol was determined empirically by sending the command and observing the response
directly from the instrument.
Discrete records are generated for each board type and each alarm by the
scpi_system_alarms_discrete.template and substitutions files.

The base response is: READ:SYS:ALRM: which may (or may not) be followed by a board identifier,
a tab character (9) an alarm string and a semicolon.

In ABNF:<br />
```
response      = "READ:SYS:ALRM:" *(error)
error         = board_id TAB error_message SEMICOLON

board_id      = 1*(ALPHA / DIGIT / ".")       ; e.g. MB1.T1
error_message = 1*(ALPHA / DIGIT / ".")       ; e.g. "Open circuit"
TAB           = %x09                          ; tab character
SEMICOLON     = %x3B                          ; semicolon ";"
```

The board identifiers are provided as macros:

| Macro |  Default |
|-------|----------|
| BOARDID_MAG    |   MB1.T1 |
| BOARDID_10TMAG |   DB8.T1 |
| BOARDID_PRESS  |   DB5.P1 |
| BOARDID_LEVEL  |   DB1.L1 |

## Development Notes:
Alex Jones has looked at some of the differences between the SCPI and legacy command set and has summarised some useful information, as quoted below:
For the quench and overheat status, these (and many other issues) are dealt with by “Alarms” for the SCPI protocol. See the Magnet board section on p. 162 in Issue 20. These are read by “READ:DEV::PSU:STAT” in some undefined hex format for just the magnet-related alarms, and READ:SYS:ALRM for a list of everything.

Some further information re UID naming:
The UIDs can be either the nickname for the card (which we can set to anything we want) or related to the slot number and signal type.
From the spreadsheet, the positional UID for the magnet temperature sensor will be MB1.T1, the UID for the level meter will be DB1.L1 and the UID for the magnet supply will be GRPZ for all 4 of the systems.
The 10T system will have an additional temperature sensor DB8.T1 and a pressure sensor DB5.P1.

It appears that:
devices connected to the motherboard are prefixed: MB1\
devices connected to a daughterboard are prefixed: DB<slot #>


Conversation between Chris Lawson and Robert Grzyb at Oxford Instruments (18 Feb 2025)
SCPI Equivalents:
Yes we are looking for the equivalent between Mercury iPS and iPS-120 control syntax. It may be some things are missing/changed, but wondered if there was a table of all of this somewhere internally.
I do not think we have a document which succinctly summarises differences between Mercury iPS and the IPS-120 in the context of their remote command sets.
 
Q: What are the new commands to use on the Mercury iPS which are equivalent to the commands from the old iPS-120 below?\
F17 (Trip Current)\
F19 (Trip Field)\
Xmn\
m = 1 quenched\
m = 2 overheated
 
Answer from Robert Grzyb at Oxford Instruments:\
<em>F17/F19\
I assume that you mean legacy commands R17 (Trip Current) and R19 (Trip Field).
This functionality is preserved when Mercury iPS remote interface is set to use legacy command set.
But when using "SCPI-style" command set, this exact information cannot be retrieved directly from the iPS.
Under certain (limited) circumstances R17/R19 are equivalent to DEV:<UID>:PSU:SIG:PCUR and DEV:<UID>:PSU:SIG:PFLD (note that UID must be a group, not an individual PSU).
 
Xmn
There is no equivalent for X (examine status) command in the "SCPI-style" command set.
As far as the first portion ("mn") of the reply to X command is concerned, certain "m" values correspond loosely to the bits of the status word in Mercury iPS group device (READ:DEV:<UID>:PSU:STAT).
The "n" part is not applicable to the Mercury iPS at all.
</em> 

Q: For Xmn, I note that these may be dealt with by alarms which can be read with READ:DEV:<UID>:PSU:STAT in some hex format which is not defined in the manual (p. 162 in Issue 20). Could this be clarified?\

Asnwer from Robert Grzyb at Oxford Instruments:\
<em>
READ:DEV:<UID>:PSU:STAT\
It is important to note that the STATus word should be examined at the group device level, not the individual PSU level.\
It is also very important to mask out (ignore) all other bits in this 32-bit word (i.e. ones  not defined in the list given below):\
</em>

| Status | Bit value |
| ------ | --------- |
| Switch Heater Mismatch | 00000001 |
| Over Temperature [Sense Resistor] | 00000004 |
| Over Temperature [Rundown Resistors] | 00000002 |
| Over Temperature [PCB] | 00000008 |
| Calibration Failure | 00000010 |
| MSP430 Firmware Error | 00000020 |
| Rundown Resistors Failed | 00000040 |
| MSP430 RS-485 Failure | 00000080 |
| Quench detected | 00000100 |
| Catch detected | 00000200 |
| Over Temperature [Sense Amplifier] | 00001000 |
| Over Temperature [Amplifier 1] | 00002000 |
| Over Temperature [Amplifier 2] | 00004000 |
| PWM Cutoff | 00008000 |
| Voltage ADC error | 00010000 |
| Current ADC error | 00020000 |

Q: Also, is it possible to read if the Mercury iPS has tripped due to a low helium level signal from the level card (something like the X command on the old iLM200 which has a low level flag at bit 5 of S)?
 
Answer:\
<em>
Low helium level

There is no direct indication of the fact that iPS has run the magnet down as a result of helium level dropping below a set threshold.\
It is possible to read both the helium level (DEV:<UID>:LVL:SIG:HEL) and the configured threshold for low helium alarm (DEV:<UID>:LVL:HEL:LOW).
</em>

## Compromises with SCPI command set and EPICS
STS:SYSTEM:LIMIT\
Is an mbbi and has has 5 possible values:\
- 0: "Normal"
- 1: "On +ve V Limit"
- 2: "On -ve V Limit"
- 4: "Current too -ve"
- 8: "Current too +ve"

The limit flags came from the legacy command: Xmn
with the index denoted by the 'n' value.
SCPI does not provide this information.

