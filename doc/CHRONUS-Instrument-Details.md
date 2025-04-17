This page collects information that will be useful for the implementation of the IBEX control system on CHRONUS.

## Background & Timeline

CHRONUS is a muon spectroscopy instrument at ISIS, on TS1, as part of the RIKEN instruments. The [CHRONUS](https://www.isis.stfc.ac.uk/Pages/CHRONUS.aspx) web page describes the background to the instrument.

## Control Systems

CHRONUS is in the process of migrating to the IBEX control system alongside Argus as of May 2024, due to both be completed by the end of the year.

## CHRONUS Equipment

The Equipment listed below is used on CHRONUS. Please add new information (e.g. new items of equipment, new notes, information about drivers, etc. to this table).

Manufacturer | Model | Type | Connection | Driver | Notes
------------ | ------------ | ------------ | ------------ | ------------ | ------------------------------------------
ISIS | DAE 2 | Detector Electronics | Ethernet | | |
CAEN | V895 | Discriminator | ??? | support: CAENVME ioc: CAENV895| [See CAEN note](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/CHRONUS-Instrument-Details#caen-v895-note)|
CAEN | SY4527 | HV power supply | Ethernet | HVCAENx527 | |
Kepco | BOP | Bi-Polar Power Supply | RS-232 | KEPCO | [See Kepco note](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/CHRONUS-Instrument-Details#kepco-note)|
National Instruments | DAQmx | Magnetometer | Ethernet | ZFMAGFLD_01 | [See magnetometer note](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/CHRONUS-Instrument-Details#magnetometer-note)

# Notes

## CAEN V895 Note

The CHRONUS CAEN v895 IOC is connected to 3 crates. Two of the crates have 15 cards, numbered 0-14, plugged in, and the third has 8, numbered 0-7. There are therefore a total of 38 cards, and 608 channels as there are 16 channels per card.

A script exists in the muon instrument scripts repo to set all channels to a user's choice of a defined value, or an array of values specified in a file. 

## Kepco Note

There are 3 kepcos being used on CHRONUS, all of which for the zero-field system. The axis are aligned as follows:
 - X: Left - Right
 - Y: Up - Down
 - Z: Forward - Back

## Magnetometer Note

There are two magnetometers used on chronus, one fixed and used in the zero field controller, the other a removable probe.