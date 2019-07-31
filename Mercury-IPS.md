> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Power Supplies](Power-Supplies) > [Oxford Instruments Mercury IPS](Oxford-Instruments-Mercury-IPS)

# Mercury IPS

The oxford instruments mercury IPS is a superconducting magnet power supply. It is the successor to the [IPS](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/OxfordInstrumentsIPS). Much of the information on the IPS wiki page also applies to the Mercury IPS.

Note: although the Mercury IPS is the successor to the "old" IPS, cryogenics prefer to run the older IPS units as they are more reliable. There is a long-term plan to replace both the "old" IPS units and the "Mercury" IPS units with something developed in-house (this is a project with the sample environment team).

# Hardware quirks

- The following faults can be seen when operating the magnet fully from the front panel, but it is likely that software will also run into the same conditions:
  * The firmware will sometimes crash/freeze. To reset it, the whole power supply needs to be power-cycled. This is obviously undesirable for a magnet power supply, and cryogenics are chasing OI about this issue. It's not clear whether this issue is general to all Mercury IPS units or whether we have one faulty unit.
  * The switch heater occasionally reports that it's ON when it's actually OFF
  * The power supply reports a voltage of ~9000V which is incorrect (a sensible voltage for this power supply would be around ~8V while ramping)