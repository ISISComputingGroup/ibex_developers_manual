# Mercury IPS

The Oxford Instruments Mercury IPS is a superconducting magnet power supply. It is the successor to 
the [IPS](Oxford-Instruments-IPS). Much of the information on the IPS wiki page also applies to the Mercury IPS.


## SCPI Protocol

The IPS IOC now supports the SCPI protocol, which is more feature rich than Legacy mode.

SCPI mode keeps the same PV interface used by the older IPS units wherever possible, to minimise the
changes required to instrument python scripts when swapping between old & new controllers.
The SNL state machine logic is identical between SCPI & legacy mode.

As already mentioned, SCPI mode provides additional status reporting, much of which is based on the 
return string from the `READ:SYS:ALRM` command, which is poorly documented in the supplier's
documentation. The status strings are assumed to all conform to the "Directory of Alarms" section 
(17.3) of the Operator's Manual (Issue 20, July 2018).
Whilst many of the system alarms that we could test, mostly conformed, some differences were
noticed, along with additional, undocumented status, such as "Magnet Safety".
It has not been possible to test all alarm scenarios with the IPS unit. Some messages are 
undocumented and were 'discovered'. Our best guess is that the IPS Manual presents some level of
truth, but as such it has not been possible to fully ascertain that all the expected message 
strings are correct - they may need to be adjusted later on, if/when they arise.

Tested and verified to date:
- PSU board open circuit
- PSU board short circuit
- Temperature board open circuit
- Temperature board short circuit

The support module exports an aSub record subroutine to facilitate handling of the responses to 
`READ:SYS:ALRM`, which is not feasible with a StreamDevice protocol handler.
See the section on [System Alarms](#system-alarms) below for more details.

### CONTROL and CONTROL:SP
These records have been removed from the SCPI variant database
as the SCPI command set does not manage the panel lock in the same was as legacy and
Magnet Group advised to remove this feature, as they always want to be able to control
the IPS via the front panel.

### SYSTEM:HWFAULT status is derived from the status bits via a calc record.
This collates the various possible hardware faults into a single record,
which in the legacy protocol is a single value (`Xm` bit 4).

### SWEEPMODE:PARAMS and SWEEPMODE:SWEEP
These records have been removed as they are meaningless and underivable in SCPI protocol.

### _SWEEPMODE:SWEEP
In the legacy version, this used to be the readback from `n` of `Mmn` part of Examine command 
return.
- 0 output constant
- 1, 2, 3 output changing

The SCPI protocol doesn't directly offer this, so it has to be derived via the `ACTIVITY` record 
(`DEV:GRPZ:PSU:ACTN`)\
Direction from Alex Jones: "A response of `HOLD` or `CLMP` would be equivalent to `n=0` in the 
response of the `X` command in the old protocol. Responses of `RTOS` or `RTOZ` would be equivalent to
`n=1`.
There is no equivalent for the `m=0,1` fast/slow ramps, but we do not use this feature anyway."

### System Alarms
System alarms are derived by interrogating the IPS with the `READ:SYS:ALRM?` SCPI command.
This returns a comma-separated string of active alarms, or an empty string if no alarms are present.
The string is parsed by an aSub record, which sets the relevant bits in a binary register.
The bits are mapped to individual status records, which are then used to set the relevant alarms.
The precise protocol was determined empirically by sending the command and observing the response
directly from the instrument.
Discrete records are generated for each board type and each alarm by the
`scpi_system_alarms_discrete.template` and substitutions files.

The base response is: `READ:SYS:ALRM:` which may (or may not) be followed by a board identifier,
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
Alex Jones has looked at some of the differences between the SCPI and legacy command set and has 
summarised some useful information, as quoted below:
For the quench and overheat status, these (and many other issues) are dealt with by “Alarms” for 
the SCPI protocol. See the Magnet board section on p. 162 in Issue 20. These are read by 
`READ:DEV::PSU:STAT` in some undefined hex format for just the magnet-related alarms, and 
`READ:SYS:ALRM` for a list of everything.

### Some further information re UID naming:
The UIDs can be either the nickname for the card (which we can set to anything we want) or related 
to the slot number and signal type. From the spreadsheet, the positional UID for the magnet 
temperature sensor will be `MB1.T1`, the UID for the level meter will be `DB1.L1` and the UID for 
the magnet supply will be `GRPZ` for all 4 of the systems.
The 10T system will have an additional temperature sensor `DB8.T1` and a pressure sensor `DB5.P1`.

Devices connected to the motherboard are prefixed: `MB1`\
Devices connected to a daughter-board are prefixed: `DB<slot #>`

### A comparison of availability of legacy vs SCPI features
| Function                        | Legacy | SCPI          |
|---------------------------------|--------|---------------|
| Trip current readback           | `F17`  | Not available |
| Trip field readback             | `F19`  | Not available |
| Ramp mode reporting (fast/slow) | Yes    | Not available |
| Status reporting                | Yes    | Detailed      |
| He Level reporting              | No     | Yes           |
| N2 Level reporting              | No     | Yes           |
| Pressure reporting              | No     | Yes           |
| Front panel control lock        | Yes    | No            |
 
 

### PSU Status:
Using the SCPI command: `READ:DEV:<UID>:PSU:STAT`\
It is important to note that the STATus word should be examined at the group device level, 
not the individual PSU level.\
It is also very important to mask out (ignore) all other bits in this 32-bit word (i.e. ones 
not defined in the list given below):\

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


### Compromises with SCPI command set and EPICS
`STS:SYSTEM:LIMIT`\
Is an `mbbi` and has has 5 possible values:\
- 0: "Normal"
- 1: "On +ve V Limit"
- 2: "On -ve V Limit"
- 4: "Current too -ve"
- 8: "Current too +ve"

The limit flags came from the legacy command: `Xmn`
with the index denoted by the `n` value.
SCPI does not provide this information.

## IOC Test Framework:
With support for the new SCPI based IPS command set, there are now two sets of StreamDevice 
protocols. The appropriate protocol is implemented by use of a macro 
(`PROTOCOL` = `SCPI` | `LEGACY`) defined prior to running the IOC.

The test framework has been adapted by splitting the existing legacy tests into common tests 
and tests specific to either control interface. For instance, the legacy command set knows 
nothing about cryogen levels, which the SCPI command set does.

The IOC support provides two protocol files: 
- Legacy: OxInstIPS.protocol
- SCPI: OxInstIPS_SCPI.protocol

The lewis emulator and IOC test framework for the Mercury IPS is located within the IPS support
module. Manually running the tests is achievable using the following approach:
1. `cd` to `C:\Instrument\Apps\EPICS\support\IPS\master\system_tests`
2. `run_tests.bat -t ips_scpi -a -f` - this will run all the SCPI specific tests
3. `run_tests.bat -t ips -a -f` - this will run all the legacy specific tests
4. To run a specific test, use something like: `run_tests.bat -t ips_scpi.test_WHEN_inductance_set_via_backdoor_THEN_value_in_ioc_updates_0__0_12345 -a -f`
- Note that the -a flag simply prompts as to whether to run tests or simply run the emulator.
- The -f flag forces a fast fail on error and no further tests are run.


## Related Documentation:
[Oxford Instruments IPS](https://isiscomputinggroup.github.io/ibex_developers_manual/specific_iocs/cryogenics/Oxford-Instruments-IPS.html)

