# MAPS Vacuum System
MAPS vacuum system is set up as two TPGs communicating via a single OMRON [OPC UA](OPCUA) PLC

## OPI
As this system is two TPG300s, one to measure the pressure tank, and another for other miscellaneous readings, the OPI for this system is two linking containers to a modified TPG300 OPI. Sunil Patel, the vacuum specialist, made a requirement that TPG (and likely other pressure controllers) cannot have their pressure, nor any other setpoint, set by the OPI. This means that for this OPI, those changes have already been made, and all values are read-only, except for the units which can be set between mbar, Torr, and Pa.

## Contacts
The main contact for information about this system is the Instrumentation and Control Systems Group, under Tim Carter