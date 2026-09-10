# Gamry

The Gamry IOC controls and in-house developed device. This device controls a Gamry potentiostat via its interface communication port. This is used on IMAT and work can be seen in the following issue: [#2642](https://github.com/ISISComputingGroup/IBEX/issues/2642)  

Currently there is no specific device driver for the potentiostat itself; instead, IBEX talks to a box developed by ISIS Electronics Group using the `GAMRY` ioc (via serial, 9-way, no null modem), that box then sends trigger pulses to the actual potentiostat control box.

Electronics' documentation for this system is [here](https://stfc365.sharepoint.com/:w:/s/ElectronicsUserSupport/IQCELTEsFEMVRqC6uTdYBPfEARrMBGvFkVqeUZ35h2fsg6A?CID=5C0A3560-B943-4887-9E61-3F103BE4ADFB&wdLOR=cA3886F77-7D88-4E15-931D-115DF1AEBFE1).
