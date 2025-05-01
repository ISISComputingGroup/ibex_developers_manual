# Live View

## normal integral 2D detector live view
 
The DAE, when in [event mode](#dae_event_histogram_modes), can serve up an [AreaDetector](https://github.com/areaDetector/ADCore) image as a live view of the neutron data. This can be viewed using an ImageJ plugin or as an Intensity plot in CSS.

Using the live view device screen you should be able to add a view with the DET macro as 1 or 2

You need to run the DAE in event mode, this will need an event mode wiring table and also defining a second time regime in the time channels section. 
 
Live view PVs have a root at `%MYPVPREFIX%DAE:AD1` and `%MYPVPREFIX%DAE:AD2` for the two detector case

You first need to tell it the spectra to use for the live view e.g.
```
caput %MYPVPREFIX%DAE:AD1:INTG:SPEC:START:SP 11
caput %MYPVPREFIX%DAE:AD1:INTG:SPEC:SIZEX:SP 80
caput %MYPVPREFIX%DAE:AD1:INTG:SPEC:SIZEY:SP 80
```
will tell it to start from spectrum 11 and use consecutive spectra in an 80x80 grid. Setting `SPEC:SIZEX` sets the underlying area detector `SizeX` and `MaxSizeX`. Though `SizeX` can be smaller, we do binning and size changes etc using a region of interest plugin later so they should always be the same here. 

Live view is disabled by default, it is enabled with
```
caput %MYPVPREFIX%DAE:AD1:INTG:ENABLE:SP 1
```
depending on the number of spectra, MAX_ARRAY_BYTES may need adjusting

## Live view in histogram mode

It is possible to use liveview in [histogram mode](#dae_event_histogram_modes), but this is slower and puts more load on the DAE unless a separate integrating detector card is used (such as on LOQ or SANS2D). Use the parameters to define spectrum numbers etc. as above and then enable this way with:
```  
caput %MYPVPREFIX%DAE:AD1:INTG:SPEC:MODE:SP 1
```

## 1D detector with TOF axis giving 2D view

In this case Y is the spectrum number and X is the time of flight bin. 

* `SIZEY` is the number of spectra in the 1D detector
* `SIZEX` is (number_of_time_channels + 1)  
    - `number_of_time_channels` is shown on the DAE Information tab as `Time Channels`
* `SPEC:START:SP` is number_of_dae_spectra_to_skip_to_get_to_1D_detector_spectra

Typically `number_of_dae_spectra_to_skip_to_get_to_1D_detector_spectra` will be the number of monitor spectra if they occur first in the spectra order, but on a multiple detector instrument it could be larger.  

You then need to put the live view into "TOFChannel" rather than "TOFSummed" mode either on the OPI or with:
```
caput %MYPVPREFIX%DAE:AD1:INTG:DATAMODE:SP 1
```
`number_of_time_channels` is displayed on the DAE Run Information tab as "time channels". Note that this value will change if they ever change their time channel boundaries.     

## error on profile picture about not enough data for `dataWidth*height`

This is caused by the array pv being viewed not being large enough to contain all the data, this is determined by `NELEMENTS` in `liveview.cmd` in `ioc/isisdae`. It is set by the macro `LIVEVIEW_NELEMENTS` it needs to be at least `sizeX` x `sizeY`. In some cases `EPICS_CA_MAX_ARRAY_BYTES` could need increasing, but we have set this quite large now (and EPICS7 did away with it), so it would be gateway/pcaspy/CSS where it might have an effect. 