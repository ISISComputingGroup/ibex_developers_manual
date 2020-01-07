> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC)

# Individual devices

- [Muon Separator Power Supply](muon-separator-power-supply)
- [Zero field Magnetometer](Zero-Field-Magnetometer-IOC)

# General

If a DAQ unit is power cycled, it may need to be reconnected from the National Instruments "MAX" (measurement and automation explorer) software. To do this, open MAX, expand "network devices", right click the relevant device, and use the "self-test" option, then try reconnecting from IBEX.

# Connecting to a cDAQ using DAQmx and NI-MAX
You will need:
- Latest version of NI-MAX
- DAQmx driver installed (see "Device support in NI-DAQmx" section of DAQmx readme for compatibility with cDAQ devices)

To connect to the device from the instrument/your machine see the [National Instruments documentation](https://www.ni.com/getting-started/set-up-hardware/data-acquisition/compactdaq#Configuring%20NI-DAQmx%20for%20CompactDAQ%20Ethernet%20Chassis)

Notes:
- Opening "Devices and Interfaces" in the sidebar typically takes several minutes on a computer connected to the RAL network. This is possibly because of the amount of NI hardware on the network.
- You will need to know the hostname of the cDAQ for the "Find Network NI-DAQmx Devices" dialogue