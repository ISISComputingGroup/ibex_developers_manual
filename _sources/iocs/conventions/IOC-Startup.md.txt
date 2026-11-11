# IOC Startup

In the vast majority of cases an IOC should start up and not set values on the device. Values should only be set when the set point PV is processed. Exceptions to this are:

- Format: if multiple formats can be specified the format returned can be set on startup
    - This may alternatively be done in a mismatch handler
