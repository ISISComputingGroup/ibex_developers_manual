# Mercury IPS

The Oxford Instruments Mercury IPS is a superconducting magnet power supply. It is the successor to the [IPS](Oxford-Instruments-IPS). Much of the information on the IPS wiki page also applies to the Mercury IPS.

Note: although the Mercury IPS is the successor to the "old" IPS, cryogenics prefer to run the older IPS units as they are more reliable.

## Hardware quirks (Legacy mode)

The following faults can be seen when operating the magnet fully from the front panel, but it is likely that software will also run into the same conditions:
  * The firmware will sometimes crash/freeze. To reset it, the whole power supply needs to be power-cycled. This is obviously undesirable for a magnet power supply, and cryogenics are chasing OI about this issue. It's not clear whether this issue is general to all Mercury IPS units or whether we have one faulty unit.
  * The switch heater occasionally reports that it's ON when it's actually OFF
  * The power supply reports a voltage of ~9000V which is incorrect (a sensible voltage for this power supply would be around ~8V while ramping)
  
## SCPI Prorocol

The IPS IOC now supports the SCPI protocol, which is more feature rich than Legacy mode.
Effort was made to ensure that the top level EPICS insterface was was changed as little as possible.
It was particularly important that the SNL state-machine logic was not altered.
This all required some careful shoe-horning of the new interface to provide PV compatibility with the legacy mode.
There is now siginificantly more diagnostic information available, along with support for daughter-boards, such as He and N leve meters, pressure measurement, etc., all of which have necessitated additions to the user interface in the IBEX client.
The IOC can be configured to run with either legacy or SCPI protocols via a STREAMPROTOCOL macro ("SCPI" | "LEGACY"). The IOC publishes a new PV $(P)PROTOCOL, which reflects the configuration mode, allowing the user interface to hide or show attributes and controls relevant to SCPI or LEGACY modes.

As already mentioned, SCPI mode provides additional status reporting, much of which is based on the return string from the "READ:SYS:ALRM" command, which is poorly documented in the supplier's documentation. The status strings are assumed to all conform to the "Directory of Alarms" section (17.3) of the Operator's Manual (Issue 20, July 2018).
Whilst many of the system alarms that we could test, mostly conformed, some differences were noticed, along with additional, undocumented status, such as "Magnet Safety".
It has not been possible to test all alarm scenarios with the IPS unit and as such unable to fully assertain that all the expected message strings are correct - they may need to be adjusted later on, if/when they arise.

The support module exports an aSub record subroutine to facilitate handling of the responses to READ:SYS:ALRM, which is not feasible with a StreamDevice protocol handler.

