> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > convert record

The convert record is used to convert values when you have a lookup table or formulae. The details for the record can be found at http://www-csr.bessy.de/control/SoftDist/csm/cvtRecord.html. These can be a little sketchy so these are some extra notes.

I (John) used the record in the barndoors support modules (..\EPICS\support\barndoors\master), Kathryn has used it on the Eurotherm.

To use this record in an IOC you must include in the build.mak file the following (both in support and the ioc):

1. `$(APPNAME)_DBD += cvtRecord.dbd` in the dbd section
1. `$(APPNAME)_LIBS += cvtRecord csmbase` in the libraries section
1. `CSM=$(SUPPORT)/csm/master` in the RELEASE file in configuration directory

If you are using a calibration file both the base path (`TDIR` field) and the filename (`SPEC` field) must be less than 40 characters; If you really need an extra 40 characters the `BDIR` field can also be used. You should use the standard name for these macros of `CALIB_PATH` and `CALIB_FILE` (see (Macro-Naming)). The suggested location for calibration files is `C:\Instrument\Settings\calib\<device type>`. Place an example in your IOC that can be copied  in settings.

The convert records will load calibration data when it is initialised. To reload the calibration data use:

    caput %MYPVPREFIX%<record name>.INIT 1

## Spline hack

A hack is being introduced into `csmbase` and the convert record to allow developers to use bespoke conversion routines along with (1D) lookup tables. The way this is currently implemented is to write a conversion function (in C or C++) in the support directory and name it `User1DTableSub`. It must be named this due to a limitation in the convert record wherein a developer cannot specify _both_ a user defined subroutine name _and_ and a lookup table. Hence the way that the function is located by the convert record is to search the epics function registry for a function called `User1DTableSub`.

This is currently only in use with the Keithley 2700 as used for the HIFI Cryomag. The user defined subroutine uses the `gsl` library's cubic spline implementation to interpolate from a resistance measurement provided by a 4 wire carbon RTD to a temperature in Kelvin (in the range 0-200 or so).  

## Tips, Tricks and Gotchas

1. The record will linearly interpolate the value this includes at either end of the record so make sure you set `DRVH` and `DRVL` if you want to avoid this.
1. Make sure your calibration (in the way in the direction you are using it) has only one value per input otherwise it is not always clear what the answer will be. For example in the barn doors I have two calibration file one represents the gap for a given response (this includes inwards and outwards swing which have the same gap measurement) and one file which is just inward swing for when I am converting a gap to a motor movement.
1. The spline hack uses gsl, and the spline interpolation implementation allocated memory for the fit and an accelerator. This should normally be freed, but in the spline hack implementation is it not because of the way that an evaluation is called. If the convert record (when using a spline hack) develops a memory leak, this could be why.
