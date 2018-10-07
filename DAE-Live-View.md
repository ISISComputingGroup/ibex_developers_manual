# Live View

## normal integral 2D detector live view
 
The DAE, when in event mode, can serve up an [AreaDetector](https://github.com/areaDetector/ADCore) image as a live view of the neutron data. This can be viewed using an ImageJ plugin or as an Intensity plot in CSS.

Using the liveview device screen you should be able to add a view with the DET macro as 1 or 2

You need to run the DAE in event mode, this will need an event mode wiring table and also defining a second time regime in the time channels section. 
 
Livewview PVs have a root at %MYPVPREFIX%DAE:AD1 and %MYPVPREFIX%DAE:AD2 for the two detector case

You first need to tell it the spectra to use for the liveview e.g.
```
caput %MYPVPREFIX%DAE:AD1:INTG:SPEC:START:SP 11
caput %MYPVPREFIX%DAE:AD1:INTG:SPEC:SIZEX:SP 80
caput %MYPVPREFIX%DAE:AD1:INTG:SPEC:SIZEY:SP 80
caput %MYPVPREFIX%DAE:AD1:SizeX 80
caput %MYPVPREFIX%DAE:AD1:SizeY 80
```
will tell it to start from spectrum 11 and use consecutive spectra in an 80x80 grid. Note that SPEC:SIZEX and SizeX should be set the same at this point, SizeX can be smaller and binning etc done here but we are going to use a region of interest later instead so just make them the same. 

Liveview is disabled by default, it is enabled with
```
caput %MYPVPREFIX%DAE:AD1:INTG:ENABLE:SP 1
```
depending on the number of spectra, MAX_ARRAY_BYTES may need adjusting

## 1D detector with TOF axis giving 2D view

In this case Y is the spectrum number and X is the time of flight bin. 

* SizeY is the number of spectra in the 1D detector
* SizeX is (number_of_time_channels + 1)
* SPEC:START:SP is (number_of_time_channels + 1) * (number_of_dae_spectra_to_skip_to_get_to_1D_detector_spectra).

You then need to put the live view into "TOFChannel" rather than "TOFSummed" mode with:
```
caput %MYPVPREFIX%DAE:AD1:INTG:DATAMODE:SP 1
```
