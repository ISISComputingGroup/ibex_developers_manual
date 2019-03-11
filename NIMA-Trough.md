# NIMA Trough

The NIMA Trough is used to fabricate thin films of material. 

## Specifications

The implementation for IBEX uses an lvDCOM solution. The IOC connects to a VI interface to process set points and read back values. When the IOC is started, it attempts to boot the Labview VI. In general use, the VI will be open with its graphing view along side the IBEX client.

## Running the IOC

The NIMA Trough IOC is not compatible with versions of the VI that are older than 2019-02-15. Ensure you update and VI drivers you have locally from source safe. Updated drivers should be available on DEMO.