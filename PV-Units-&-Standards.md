> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > PV units

DB Unit Checker
===============

The DBUnitChecker Python script is a helper file that checks a number of things are true about the PVs used within the project.

Current error checks are:

- PVs that are labelled as interesting and have type longin, longout, ai or ao must contain a unit field
- Description fields must contain less than 41 characters
- All units must conform to unit standards (see below)
- PVs that are labelled as interesting must have description fields
- The names of PVs that are labelled as interesting must be capitialised and contain only `A-Z 0-9 _ :`
- `calc` records that are marked as interesting must be have their access security group (`ASG`) set to `READONLY`.

Current warning are:

- PVs may not have multiple unit fields
- PVs that are labelled as interesting and have type longin, longout, ai or ao may not have blank fields

The checker is run at the end of a build on Jenkins and unit tests are failed if any of the error checks fail. Failed warnings will be noted and displayed in the test report but will not result in an unstable build.

Unit Standards
--------------

If the unit has a standard alphanumeric unit symbol that has been used. In the case where the usual symbol is not alphanumeric e.g. degree (°), angstrom (Å), the unit is written in full, lower case and singular.

Standard prefixes, [T|G|M|k|m|u|n|p|f], are accepted before all units.

Units can be constructed from a number of 'base' units using a space, forwardslash and caret for multiplication, division and powers respectively. For example a unit for work done could be "N m", a unit for velocity could be "m/s" and a unit for area "m^2". This is the same standard as used in [udunits](http://linux.die.net/man/3/udunits).

For PVs where the units are contestable, for example NUMSPECTRA, a blank units field is acceptable. This will give a warning, but not a failure, when a test is run and so can be discussed at a later date.

The units within the support/optics/ path are not checked as they contained a number of ambiguities and are rarely used.

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
* degree
* eV
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
* s
* torr
* step
* T
* V

