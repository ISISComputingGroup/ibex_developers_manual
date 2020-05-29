> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [PLCs](PLCs) >

## Introduction

A PLC (programmable logic controller) is a device that is capable of doing near real-time control of a number of inputs and outputs. They're used throughout ISIS to do control that needs to happen very quickly or very reliably/safely e.g. if a vessel is under vacuum make sure it cannot move. In general IBEX doesn't need to worry about what logic the PLC is performing but just needs to read and write to various memory addresses on the device to make sure it performs the correct logic.

## Models

There are a number of different PLCs in use at ISIS:

* [Beckhoff](Beckhoff) - Mostly used for motion but are in fact generic PLCs
* [Omron FINS](PLCs#omron-fins)

## Omron FINS

The Omron FINS is a PLC controlled via a driver first written at Diamond, see [here](https://github.com/ISISComputingGroup/EPICS-FINS). The IOC works by loading an instrument specific `FINS_01.cmd` in `configurations/fins`, which will load an instrument specific `db` from `ioc/master/FINS/db`. The dbs in here are usually created from a number of templates matching specific memory addresses to PVs. Currently the following specific FINS PLC installations are supported in IBEX:

* IMAT FINS PLC
* LARMOR air PLC
* SANS2D vacuum PLC
* WISH vacuum PLC
* ZOOM vacuum PLC

# Testing the FINS IOC in devsim

If you want to test the IOC for a FINS PLC in devsim mode, you need to add the line ```$(IFDEVSIM) finsUDPInit("PLC", "$(PLCIP):$(EMULATOR_PORT=)", "TCPNOHEAD", 0, "$(PLCNODE=)")``` in the FINS_01.cmd file used by that specific FINS IOC. At the same time, the file should either not have any other finsUDPInit call for talking with the real PLC, or have ```$(IFNOTDEVSIM) $(IFNOTRECSIM)``` before that call.