> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > PV units

DB Checker
===============

The DBChecker Python script is a helper file that checks a number of things are true about the PVs used within the project and that the correct syntax is used in db files.

### Usage

From an EPICS terminal in `C:\Instrument\Apps\EPICS\ISIS\DbChecker\master`, run:
```
%python3% check_db_file.py -d <directory to check> -r
```

### Capabilities

Current pv error checks are:

- PVs that are labelled as interesting and have type longin, longout, ai or ao must contain a unit field
- Description fields must contain less than 41 characters
- All units must conform to unit standards (see below)
- PVs that are labelled as interesting must have description fields
- The names of PVs that are labelled as interesting must be capitalised and contain only `A-Z 0-9 _ :`
- `calc` records that are marked as interesting must have their access security group (`ASG`) set to `READONLY`. This is because if you were to set it directly, the record would not execute its calculation, which is not what we want.

Current pv warning are:

- PVs may not have multiple unit fields
- PVs that are labelled as interesting and have type longin, longout, ai or ao may not have blank fields

Current syntax errors are:

- Colons not used as main separator
- Names use characters that are not alphanumeric, an underscore or colon
- Does not adhere to :SP and SP:RBV format
- If DUMMYPV and DUMMYPV:SP exists without DUMMYPV:SP:RBV (at least as an alias).
- If DUMMYPV:SP exists on its own but does not have a SP:RBV alias for DUMMYPV
- Underscores must not be used in place of : i.e. DUMMYPV_SP

Current syntax warnings are:

- Names not in uppercase



The checker is run at the end of a build on Jenkins and unit tests are failed if any of the error checks fail. Failed warnings will be noted and displayed in the test report but will not result in an unstable build. Syntax errors are currently treated as warnings as some files currently contain large numbers of them.

Unit Standards
--------------

The unit standards apply to both DB files and [calibration files](Calibration-Files).

If the unit has a standard alphanumeric unit symbol that has been used. In the case where the usual symbol is not alphanumeric e.g. degree (°), angstrom (Å), the unit is written in full, lower case and singular. The unit may be shortened because CSS will only display 8 characters worth of unit so `degree/s^2` is to long.

Standard prefixes, [T|G|M|k|m|u|n|p|f], are accepted before all units.

Units can be constructed from a number of 'base' units using a space, forwardslash and caret for multiplication, division and powers respectively. For example a unit for work done could be "N m", a unit for velocity could be "m/s" and a unit for area "m^2". This is the same standard as used in [udunits](http://linux.die.net/man/3/udunits).

For PVs where the units are contestable, for example NUMSPECTRA, a blank units field is acceptable. This will give a warning, but not a failure, when a test is run and so can be discussed at a later date.

The units within the `support/optics/` path are not checked as they contained a number of ambiguities and are rarely used.

Supported Units
---------------

The project currently contains the following base units:

* A
* angstrom
* bar
* bit
* byte
* C
* cm
* count
* degree or deg for short
* eV
* event
* frame
* hour
* Hz
* inch
* interrupt
* K
* L
* m
* min
* minute
* ohm
* Oersted
* %
* Pa
* photon
* pixel
* radian
* rpm
* s
* torr
* step or stp for short
* T
* V
