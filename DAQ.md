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

# Data bottlenecking in the DAQmxBase driver (Monster mode)
When developing the zero field magnetometer IOC we found that there are significant overheads in the EPICS DAQmx driver when running it in one shot and continuous modes. In these modes the NI task used to take the data is started and stopped with every point/array of data requested (as applicable). This means that each point/array takes ~150 ms to acquire, around 100ms of this is from starting the task and ~50ms to actually take the data.

We addressed this issue for the zero field magnetometer (which needed consecutive readings very close to each other) by running in 'monster' mode. In monster mode the NI data acquisition task is never closed, so the data can be captured at a much faster rate. However, if the requested data rate is too high this can cause a buffer overflow. For the zero field magnetometer on a developer's machine this occurred at ~100000 data points/second.

Unlike the other two modes, monster mode appears to need a call to `DAQmxStart(portname)` at the end of the st.cmd file for the IOC, see the ZFMAGFLD st.cmd for a reference.

### Common errors

```
### DAQmx ERROR (CreateAI): Device cannot be accessed.  Possible causes:
Device is no longer present in the system.
Device is not powered.
Device is powered, but was temporarily without power.
Device and/or chassis driver support may have been removed.
```
If this happens immediately on IOC boot, check if the DAQ is connected in NI-MAX. Check the device is reserved in NI-MAX and can be reached over the network.