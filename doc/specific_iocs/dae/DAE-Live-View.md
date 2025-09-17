# Live View

## normal integral 2D detector live view
 
The DAE, when in [event mode](#dae_event_histogram_modes), can serve up an [AreaDetector](https://github.com/areaDetector/ADCore) image of the neutron data as a `detector live view` device screen. The data created by areaDetector canalso be viewed using an ImageJ plugin or as an Intensity plot in CSS.

Using the live view device screens you can add several views, the DET macro indicates a view number and starts at 1 and can go up to 10

Running the DAE in event mode works best (is quickest), this will need an event mode wiring table and also defining a second time regime in the time channels section. If you nede to run it in histogram mode it will be slower as it will have to download all histograms to integrate every time, in event mode these are pre-created for fast access. 
 
Live view PVs have a root prefix of `%MYPVPREFIX%DAE:AD1:` for detector view 1 etc

Open the live view settings page and then you need to specify a few items. Standard data is stored in the DAE as a set of spectra starting at nuber 1 (spectrum 0 is a special spectrum for unassigned data). The DAE has no knowledge of detector shape, however a contiguous block of spectrum numbers usually corresponds to rastering by row or column of a 2D detector. So for example you may have a detector sized 600x400 pixels - in the DAE this may be stored as 600 contiguous blocks of 400 elements, so you need to tell the view 
* starting spectrum number: at what spectrum number does the first detector pixel correspond to. This is usually not 1 as the first few spectra are usually assigned to monitors.
* x pixels and y pixels: size of the detector
The liveview dispay will then real xsize x ysize spectra and recreate the two dimensional structure. Other variables you can set are:  

* integral mode: see total counts so far, or counts since last poll
* integral trans mode: do you want to see plot of pure counts, logarithm of counts etc.
* scale to zero: is scale to use  `0 -> max counts` or `min counts` to `max counts`
* specify a region of interest (ROI) and binning, or just leave as as to see all
* spec mode: is the dae in event or [histogram mode](#dae_event_histogram_modes)
* data mode: noremally `TOFSummed`, `TOF channel` is a special mode for linear (1D) detectors, it uses the linear detector pixel number as one axes and the time of flight as the other giving a 2D view. Used on POLREF amnd INTER for example.
* rotation: is the image the right way round or needs to be flipped
* period: dae period number to display, or use 0 for current period 
* running: choose to enable or disable liveview.

depending on the number of spectra, EPICS `MAX_ARRAY_BYTES` may need adjusting - this would only be for a PCAS based server, so the gateway for example if you nede to view teh liveview off instrument.

## 1D detector with TOF axis giving 2D view (data mode: `TOF channel`)

In this case Y is the spectrum number and X is the time of flight bin. 

* `Y Pixels` is the number of spectra in the 1D detector
* `X Pixels` is (number_of_time_channels + 1)  
    - `number_of_time_channels` is shown on the DAE Run Information tab as `Time Channels` (this number will change if you change time channel boundaries)

## error on profile picture about not enough data for `dataWidth*height`

This is caused by the array pv being viewed not being large enough to contain all the data, this is determined by `NELEMENTS` in `liveview.cmd` in `ioc/isisdae`. It is set by the macro `LIVEVIEW_NELEMENTS` it needs to be at least `sizeX` x `sizeY`. In some cases `EPICS_CA_MAX_ARRAY_BYTES` could need increasing, but we have set this quite large now (and EPICS7 did away with it), so it would be gateway/pcaspy/CSS where it might have an effect. 
