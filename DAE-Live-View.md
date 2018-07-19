# Live View

The DAE, when in event mode, can serve up an [AreaDetector](https://github.com/areaDetector/ADCore) image as a live view of the neutron data. This can be viewed using an ImageJ plugin or as an Intensity plot in CSS.

## Simulating the live view

Currently the live view, or a simulation, isn't in the standard DAE IOC. An area detector simulation exists [here](https://github.com/areaDetector/ADSimDetector) or, with a couple of ISIS specific modifications [here](https://github.com/ISISComputingGroup/EPICS-areaDetector/tree/master/ADSimDetector). To run this:
* Run the IOC located [here](https://github.com/ISISComputingGroup/EPICS-areaDetector/tree/master/ADSimDetector/iocs/simDetectorIOC/iocBoot/iocSimDetector)
* Start 'taking' data with `caput %MYPVPREFIX%DAE:cam1:Acquire 1`
* Data should now be available on `%MYPVPREFIX%DAE:image1:ArrayData`
* You can control the data update rate by writing to `%MYPVPREFIX%DAE:cam1:AcquireTime` (the DAE itself tends to update every ~1 second)