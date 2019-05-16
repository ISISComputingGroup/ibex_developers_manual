> [Wiki](Home) > [The Backend System](The-Backend-System) > [Creating and Basics of IOCs](IOCs) > [IOC Startup](IOC-Startup)

In the vast majority of cases an IOC should start up and not set values on the device. Values should only be set when the set point PV is processed. Exceptions to this are:

- Remote/local mode: IOC should switch a device to remote mode when started
- Format: if multiple formats can be specified the format returned can be set on startup
    - This may alternatively be done in a mismatch handler
