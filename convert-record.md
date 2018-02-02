> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > convert record

The convert record is used to convert values when you have a lookup table or formulae. The details for the record can be found at http://www-csr.bessy.de/control/SoftDist/csm/cvtRecord.html. These can be a little sketchy so these are some extra notes.

I (John) used the record in the barndoors support modules (..\EPICS\support\barndoors\master), Kathryn has used it on the Eurotherm.

To use this record in an IOC you must include in the build.mak file the following:

1. `$(APPNAME)_DBD += cvtRecord.dbd` in the dbd section
1. `$(APPNAME)_LIBS += cvtRecord csmbase` in the libraries section

If you are using a calibration file both the base path (`TDIR` field) and the filename (`SPEC` field) must be less than 40 characters; If you really need an extra 40 characters the `BDIR` field can also be used. You should use the standard name for these macros of `CALIB_PATH` and `CALIB_FILE` (see (Macro-Naming)). The suggested location for calibration files is `C:\Instrument\Settings\calib\<device type>`. Place an example in your IOC that can be copied  in settings.

The convert records will load calibration data when it is initialised. To reload the calibration data use:

    caput %MYPVPREFIX%<record name>.INIT 1

## Tips, Tricks and Gotchas

1. The record will linearly interpolate the value this includes at either end of the record so make sure you set `DRVH` and `DRVL` if you want to avoid this.
1. Make sure your calibration (in the way in the direction you are using it) has only one value per input otherwise it is not always clear what the answer will be. For example in the barn doors I have two calibration file one represents the gap for a given response (this includes inwards and outwards swing which have the same gap measurement) and one file which is just inward swing for when I am converting a gap to a motor movement.
