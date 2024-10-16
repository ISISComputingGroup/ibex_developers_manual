> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > IOC Finishing Touches

This page documents the finishing touches to make to your IOC to make it function within the IBEX environment.

## 1. Interesting PVs

To have a PV appear in the interest list in IBEX Configurations add the following to the PV record:

    info(INTEREST, "<LEVEL>")

where the level is HIGH, MEDIUM, LOW.

For records that are of no "interest" do not add an interest info field. For example, intermediate CALC records, SIM records etc.

Any calc record which is interesting needs `field(ASG, "READONLY")` added so it cannot be set by accident.

## 2. Archive PVs

To have a PV automatically archived add the following to the PV record

    info(archive, "VAL")

This will archive the value of the `VAL` field once per second. The general form is 

    info(archive, "<period> <field>")

Where

    * period (defaults to 1):
        * when +ve - sign up to monitor the pv use the period field to determine a typical delay between samples in seconds 
        * when -ve - monitor the value the value is the deadband for the system
    * field: the field to monitor on the record

Find more information at [Logging from the archive](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Logging-from-the-archive).

## 3. Alarm PVs

If you want a PV to appear in the alarm view (and there should be at least one per IOC so that it can show disconnected) then add:

    info(alarm, "<name of IOC (not including _0X)>")

## 4. Autosave PVs

PVs can be autosaved so that they save their values and are reloaded when the IOC starts. The value is set before the record is initialised so is only processed using this value if `PINI` is Yes; although waveform records do this differently and will process the record. To do this mark the field with the following info line:

    info(autosaveFields, "VAL")

The second argument is the field which is autosaved within the record.

## 5. Disable records

It is very useful to be able to turn an IOC on and off by simply writing to a special PV, as it is a lot faster and more convenient than actually restarting the whole IOC. The instructions can be found [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Disable-records) .

## 6. PVs Have Essential Fields

All PVs should have if appropriate:

* Description (`DESC` field)
* Unit fields if representing a value (`EGU` field) which may be blank
    * Units must be in ...
* Precision (`PREC`) for records with floating point numbers - is this set correctly for what a user/technician requires 

## 7. Initialising Setpoints

Setpoint pvs should have "undefined field" initialised by adding the following record to the PV:

    `field(UDFS, "NO_ALARM")` 

This means that they can have alarm sensitive borders but will not alarm if they have never been set.

## 8. Compliance with DBChecker

The build in Jenkins will fail if the rules of the [DBChecker](PV-Units-&-Standards) script are not satisfied. You might as well check them beforehand to save yourself time later. See linked page for additional information & instructions.

## 9. Macros and Details

Macros where possible should follow the [standard names](Macro-Naming). If a macro can be set as part of the IOC (and can be reasonably set in the GUI) then a config file should be added to the run directory which contains a list of macros (i.e. `..\EPICS\ioc\master\<IOC Name>\iocBoot\<IOC Instance Name>\config.xml`). Common macros should be included from `..\EPICS\ioc\common\`.The file is of the form:

```xml
<?xml version="1.0" ?>
<ioc_config xmlns:xi="http://www.w3.org/2001/XInclude">
<config_part>
<ioc_desc>Eurotherm temperature controller</ioc_desc>
<macros>
  <xi:include href="../../../COMMON/PORT.xml" />
  <macro name="BAUD" pattern="^[0-9]+$" description="Serial communication baud rate, defaults to 9600." defaultValue="9600" hasDefault="YES" />
  <macro name="BITS" pattern="^[0-9]$" description="Serial communication number of bits, defaults to 7." defaultValue="7" hasDefault="YES" />
  <macro name="PARITY" pattern="^(even)|(odd)|(none)$" description="Serial communication parity, defaults to even." defaultValue="even" hasDefault="YES" />
  <macro name="STOP" pattern="^[0-9]$" description="Serial communication stop bit, defaults to 1." defaultValue="1" hasDefault="YES" />

  <macro name="ADDR_1" pattern="^[0-9]{1,2}$" description="Address for the 1st Eurotherm on this port e.g. 01. Blank for do not use." hasDefault="UNKNOWN" />

  <macro name="LOCAL_CALIB" pattern="^(yes)|(no)$" description="Use local instrument calibration directory instead of common one? Default is no." defaultValue="no" hasDefault="YES" />
</macros>
</config_part>
</ioc_config>
```

where
- `ioc_desc` is a short description of the IOC e.g Lakeshore 218 for LKSH218. This field is shown alongside the IOC name in the GUI when adding or editing IOCs.
- `ioc_details` is more details about the IOC, e.g. link to docs.
- `macro` describes a macro settable by a user. 
    - containing `name`, is the name of the macro;  
    - `pattern`, the regex for the macro's value; Useful regex for macros:
        - `^-?[0-9]+\.?[0-9]*$`: float with sign
        - `^[0-9]+\.?[0-9]*$`: float no sign
        - `^[0-9]+$`: integer no sign
    - `description`, a plain text description which is shown to the user.
    - `defaultValue`, the default value of the macro, if it exists (this attribute is not required)
    - `hasDefault`, if the macro has a default, either `"YES"`, `"NO"`, or `"UNKNOWN"`. (Note that `UNKNOWN` exists for legacy reasons, new IOCs should not use it)

`config.xml` support include so if you have several iocs with the same set of macros you don't need to repeat the file contents. Example GALIL02 (see below) uses GALIL01's config:

```xml
<?xml version="1.0" ?>
<ioc_config xmlns:xi="http://www.w3.org/2001/XInclude">
<xi:include href="../iocGALIL-IOC-01/config.xml"  />
</ioc_config>
```

Either a full make of the server or running `make iocstartups` from the EPICS folder will then make the contents of these XML files available to the GUI (after restarting the instrument).

**Tips**
* If you want a macro that restricts input to be a byte, so 0-255, then you can use ^$|^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$ . You can change this so it allows any range of integers of you desire. [This website](https://regex101.com/) is a good resource for checking regex expressions.

## 10. PV Limits

If a limit on a set point is well defined (i.e., given by a device manual) then the fields `DRVH` "Drive High" and `DRVL` "Drive Low" should be used to constrain the PV set point. The behaviour of these fields is that if a limit is 10.0 and a user inputs 11.0, then the PV will constrain the input to 10.0 and process that value. Records that use limits should also be robustly tested to ensure the behave as expected. An example test:

```python
    @parameterized.expand([
        ("lt_low_limit", CURR_LOW_LIMIT-1, "low_limit", CURR_LOW_LIMIT),
        ("gt_high_limit", CURR_HIGH_LIMIT+1, "high_limit", CURR_HIGH_LIMIT)])
    @skip_if_recsim("Behaviour cannot be simulated in Recsim")
    def test_WHEN_voltage_setpoint_is_set_outside_max_limits_THEN_setpoint_within(self, case, case_value, limit, limit_value):
        self.ca.set_pv_value("CURRENT:SP", case_value)
        self.ca.assert_that_pv_is("CURRENT:SP", limit_value)
```

## 11. Directories added to Makefiles
Type
```
make checkdirs
```
at EPICS top level and make sure it completes ok
 
## 12. Add IOC to EPICS hardware list

Once the IOC is reviewed and tested with hardware, [add it to the EPICS hardware list](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Add-ioc-to-epics-hardware-list)

