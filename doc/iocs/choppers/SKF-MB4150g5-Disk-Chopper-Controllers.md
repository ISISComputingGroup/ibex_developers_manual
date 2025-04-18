# SKF MB4150g5 Chopper

These controllers are a development of the [MB350g3](SKF-MB350g3-Chopper) previously used on LET for its disk choppers and now repurposed on EMMA for its Fermi.  The G5 is an Ethernet device using a MODBUS protocol to communicate, and are generally installed on the instrument private networks.  Spare/test controllers may exist on the ISIS network.

The IOC for this device is the **SKFCHOPPER**, this IOC has to have macros set in the globals.txt

## Current Installations

* **Six** controllers on LET (original single-disk choppers 3 & 4, and the previously Astrium double-disk choppers 1 & 5. Chopper 2 is an [ISIS MK3](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/MK3-Chopper))
* **Five** on IMAT (two double-disk choppers and a T0)
* **Two** on SANDALS (a single double-disk chopper)

## Addressing Schema on the instrument's private network

LET - These controllers have been allocated _static_ addresses in the range _xxx.xxx.xxx.8x_, which is under the control of the Experiment Controls Group.  Since installation, the addresses have been in the original range of xxx.xxx.xxx.18x, but problems were encountered when installing two additional controllers (see ticket [5033](https://github.com/ISISComputingGroup/IBEX/issues/5033) for details).

IMAT - These controllers are still in the original range of _xxx.xxx.xxx.18x_, but it is planned to reallocate them for consistency.

SANDALS - Also still in the original range of _xxx.xxx.xxx.18x_.

**N.B.** The address ranges and subnets on the private network haven't formally been divided between the various groups (Experiment Control, Electronics, Detectors) to date.  A coordinated effort is required to produce a document, ideally before any further use of the private network is made.

## Communications

The controllers use a MODBUS protocol to communicate over Ethernet.  Their IOCs use a small subset of the complete command set to provide the minimum functionality required for remote control by the scientists.  Due to differences in parameter definitions between SKF and ISIS, some interpretation (and trial and error) was needed to produce this reduced set of commands.

The MODBUS TCP protocol is used, which slightly differs to MODBUS RTU used by eurotherms and other serial devices. 
This means there are some extra fields in the header of MODBUS requests/responses, as well as MODBUS TCP using a `crc16` or similar checksum. 
A MODBUS TCP packet consists of an MBAP (Modbus Application) Header and a PDU (the same as MODBUS RTU)
The MBAP consists of: 

Transaction Identifier: 2 bytes
Protocol Identifier: 2 bytes
Length: 2 bytes
Unit Identifier: 1 byte

https://ipc2u.com/articles/knowledge-base/detailed-description-of-the-modbus-tcp-protocol-with-command-examples/ shows some examples of a MODBUS TCP request compared against MODBUS RTU. 

Some of the SKF chopper controllers at ISIS implement the transaction identifier part of the MBAP header incorrectly. We have catered for this in the MODBUS interpose framework, skipping the check for this ID can be done by setting the `SKIP_TRANSACTION_ID` macro in globals to `1`. 

