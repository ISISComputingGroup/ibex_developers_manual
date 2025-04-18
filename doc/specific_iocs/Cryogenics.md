# Cryogenics

## IOCs

```{toctree}
:glob:
:titlesonly:
:maxdepth: 1

cryogenics/*
```

```{seealso}
See also [Temperature controllers](Temperature-Controllers) for other temperature controllers which may be used in cryogenic setups.
```

## Cryostats (T>1K)

### Closed Cycle Refrigerators (CCRs)
These are controlled using Eurotherms.  No need to communicate directly with the CCR itself.

### Orange Cryostats
These are controlled using Eurotherms.  No need to communicate directly with the Cryostat itself.

### Variox (Blue) Cryostats
These are manufactured by Oxford Instruments (OI).  They can be controlled by either: 
   * Oxford Instruments ITC503 (See [#1389](https://github.com/ISISComputingGroup/IBEX/issues/1389), [#3189](https://github.com/ISISComputingGroup/IBEX/issues/3189)) + Oxford Instruments ILM200 (See [#1390](https://github.com/ISISComputingGroup/IBEX/issues/1390))

or 
   * Oxford Instruments Mercury ITC (with level meter expansion card)

or
   * Oxford Instruments Mercury ITC + standalone level meter such as an Oxford Instruments ILM200

### ISISStat

Controlled by a Mercury ITC (See [#1199](https://github.com/ISISComputingGroup/IBEX/issues/1199))

Note: a "Mercury ITC" and an "ITC503" are two different devices (with different drivers). They are both manufactured by Oxford Instruments and control the temperature of a cryostat. The Mercury ITC is the newer model, the ITC503 is the older model. Mercury ITC controllers can take various expansion boards, which I do not believe ITC503 controllers are capable of.

Our support for Mercury ITC units is not yet fully complete:
* See [#1286](https://github.com/ISISComputingGroup/IBEX/issues/1286)
* See [#1287](https://github.com/ISISComputingGroup/IBEX/issues/1287)
* See [#1392](https://github.com/ISISComputingGroup/IBEX/issues/1392)

### Oxford Flow through Cryostats

EMU use a flow cryostat controlled by an ITC503 temperature controller. There is no special setup of ITC503 required from a computing perspective.

Other beamlines may use different setups, check with the scientists if unsure.

## Low temperature inserts (T<1K)

All of the inserts in this category are run in a "parasitic" fashion - i.e. they sit inside an outer cryostat which provides cooling to low temperature, and then the insert provides the final stage of cooling to very low temperature.

The outer cryostat for these inserts can be either a blue cryostat (see above for details) or a cryomagnet (see below for details)

### Mercury Heliox (He3 sorption refrigerator)

This insert is capable of reaching temperatures of ~300mK. The heliox and the outer cryostat use separate physical controllers, which need separate moxa connections and EPICS drivers.

For further details see [mercury heliox](cryogenics/Mercury-Heliox)

### Triton Dilution Fridge

Triton systems are dilution refrigerators capable of reaching ~30mK. They are controlled by a dedicated PC which sits in a rack. Cryogenics group do a significant amount of setup with these controllers when they arrive on a beamline.

See [Triton](cryogenics/Triton) for further details about the triton system

### ICE dilution fridge.

This dilution fridge is only used on muon beamlines - usually on MuSr, but occasionally borrowed by EMU. The RIKEN muon instruments (Argus/Chronus) may also use this fridge in the near future. This is currently the only dilution fridge at ISIS which is not controlled by an Oxford Instruments Triton controller.

For details see [ICE dilution fridge](cryogenics/ICE-Dilution-Fridge)

## Cryomagnets (cryogenically cooled superconducting magnets)

Most of the magnets in this section can be used instead of a cryostat when using a "parasitic" cooling insert (e.g. heliox, triton). This is because the magnets must be cooled to low temperatures anyway so that they superconduct, so they also act as the outer cryostat.

### 7.5T magnet

The 7.5T magnet is controlled by 3 devices:
   * [Intelligent Power Supply (IPS)](cryogenics/Oxford-Instruments-IPS) (See [#1391](https://github.com/ISISComputingGroup/IBEX/issues/1391)). It could also be controlled by a [Mercury IPS](cryogenics/Oxford-Instruments-Mercury-IPS) but cryogenics group are not using this option at present due to hardware issues with the Mercury IPS.
   * [Intelligent Temperature Controller (ITC503)](cryogenics/ITC-503) (See [#1389](https://github.com/ISISComputingGroup/IBEX/issues/1389), [#3189](https://github.com/ISISComputingGroup/IBEX/issues/3189)). A [Mercury ITC](cryogenics/MercuryiTC) may be used as a fallback if the ITC503 controller fails, but this is not usual. 
   * Intelligent Level Meter (ILM) (See [#1390](https://github.com/ISISComputingGroup/IBEX/issues/1390))

For details including configuration settings, see [Oxford Instruments IPS](cryogenics/Oxford-Instruments-IPS).

See note at the bottom of this page for differences between IBEX and SECI in terms of how this device must be connected.

### 9T "chopper" magnet 

This system appears to IBEX exactly like the 7.5T magnet discussed above, but with a different maximum field. It is currently dedicated to LET (but not permanently installed). 

Please see the documentation and notes linked above for further details.

### 2T 3D Vector magnet 

This is primarily used on SANS and reflectometry beamlines.

The 2T 3D vector magnet is manufactured by Scientific Magnetics. It has its own control system for which the manufacturer has provided LabVIEW VIs. We interface with these via lvDCOM (See [#1398](https://github.com/ISISComputingGroup/IBEX/issues/1398)).  Detailed information [here](cryogenics/2T-3D-Vector-magnet).

### 5T HIFI magnet

This is a dedicated system permanently installed on HiFi.

See [here](cryogenics/Cryogenic-SMS-PSU) and [here](/processes/instrument_details/HIFI_CRYOMAG-Instrument-Details) for details

This magnet does *not* act as an outer cryostat for any other sample environment that may be used.

### 17T "Birmingham" magnet

This is a cryomagnet owned by the University of Birmingham, which occasionally travels to various scattering facilities, including ISIS.

IBEX does not have support for this device at present. Ticket [#4523](https://github.com/ISISComputingGroup/IBEX/issues/4523) contains some details about this device.

From a brief look at the command set and manual, it appears that all of the magnet control logic occurs in the Birmingham computer, and we simply send it ascii-formatted commands to go to a field. In theory this may be controllable via SDTEST (although a dedicated driver would of course be better).

### 4T "E18" dilution fridge/magnet combination

This system is a combination of a Oxford Instruments [triton dilution fridge](cryogenics/Triton) and a 4T cryomagnet driven by a [Mercury IPS](cryogenics/Oxford-Instruments-Mercury-IPS). Similar to the distinction between an old-style Oxford instruments ITC503 and a Mercury ITC, the Mercury IPS is the newer model. It is a physically different device to the old-style IPS, but performs the same task.

For details of the Mercury IPS, see [Mercury IPS](cryogenics/Oxford-Instruments-Mercury-IPS). Some further details are also in [#4339](https://github.com/ISISComputingGroup/IBEX/issues/4339).

## Level meters

### Helium Level Gauge
Does what it says on the tin - measures the level of helium in a cryostat.
   * support for Cryogenics Ltd He Level Gauge  - See [#2350](https://github.com/ISISComputingGroup/IBEX/issues/2350)

### Oxford Instruments Intelligent Level Meter (ILM200)

This is another type of level meter, manufactured by Oxford instruments. It is often used in conjunction with ITC503 temperature controllers. It has two channels which can be set up to independently measure Helium and Nitrogen levels.

Note: the ILM200 only physically measures the levels every 30 minutes, so if looking at the log plotter, there will be steps rather than a smooth downward curve - this is expected.

See note at the bottom of this page for differences between IBEX and SECI in terms of how this device must be connected.

## Note about Oxford Instruments ITC/ILM/IPS controllers

These controllers used to be run in a rack with a single serial connection under SECI (this used an ISIS isobus expander crate to split the signals). This is because, in SECI, there was only one process which talked to all of the pieces of equipment (in various combinations).

In IBEX, support for the individual devices has been written into separate IOCs to increase the flexibility of the drivers. Under Windows, this means that they cannot talk to the same COM port (because each IOC has exclusive access to the port). Therefore, under IBEX, separate connections from the moxa to each bit of kit are required.

The kit takes 25-way serial cables.
