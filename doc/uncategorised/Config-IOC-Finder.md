Print all IOCs over all configs and components on an instrument or list instruments with a given IOC. 

To use first check out the [config checker repository](https://github.com/ISISComputingGroup/ConfigChecker).

To list all IOCs on all instruments use:

    get_ioc_usage.bat

To list all IOCs on a limited number of instruments:

    get_ioc_usage.bat --instrument <inst1> <inst2>

To list all instruments with a IOC starting with `<ioc>`:

    get_ioc_usage.bat  --ioc <ioc>
