> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > IOC Finishing Touches

This page documents the finishing touches to make to your IOC to make it function within the IBEX environment.

## 1. Interesting PVs

To have a PV appear in the interest list in IBEX Configurations add the following to the PV record:

    info(INTEREST, "<LEVEL>")

where level is HIGH, MEDIUM, LOW.

For records that are of no "interest" do not add an interest info field. For example: intermediate CALC records, SIM records etc.

## 2. Archive PVs

To have a PV automatically archived add the following to the PV record

    info(archive, "VAL")

## 3. PVs Have Essential Fields

All PVs should have if appropriate:

* Description (`DESC` field)
* Unit fields if representing a value (`EGU` field) which may be blank
    * Units must be in ...

## 4. Compliance with DBUnitChecker

The build in Jenkins will fail if the rules of the [DBUnitChecker](PV-Units) script are not satisfied. You might as well check them before hand to save yourself time later. From an epics terminal in your ioc's app db directory 

    python C:\Instrument\Apps\EPICS\ISIS\DbUnitChecker\master\db_checker.py -i .

To check it will not fail the build.

## 5. Macros

Macros where possible should follow the [standard names](Macro-Naming). If a macro can be set as part of the IOC (and can be reasonably set in the GUI) then a config file should be added to the run directory which contains a list of macros (i.e. `..\EPICS\ioc\master\<IOC Name>\iocBoot\<IOC Instance Name>\config.xml). The file is of the form:

```
<?xml version="1.0" ?>
<ioc_config xmlns:xi="http://www.w3.org/2001/XInclude">
 <config_part>
  <ioc_desc>SKF Chopper</ioc_desc>
  <ioc_details>SKF Choppers</ioc_details>
  <macros>
    <macro name="VI_TEMP_1" pattern="^[A-Z0-9]+$" description="Suffix of the vi temperature panel, usually '1' or blank for no controller." />
    <macro name="VI_TEMP_2" pattern="^[A-Z0-9]+$" description="Suffix of the vi temperature panel, usually '2' or blank for no controller." />
    <macro name="VI_TEMP_3" pattern="^[A-Z0-9]+$" description="Suffix of the vi temperature panel, usually '3' or blank for no controller." />
    <macro name="VI_TEMP_4" pattern="^[A-Z0-9]+$" description="Suffix of the vi temperature panel, usually '4' or blank for no controller." />
  </macros>
 </config_part>
</ioc_config>
```

where
> `macro` describes a macro setable by a user. containing `name`, is the name of the macro;  `pattern`, the regex for the macro's value; and `description`, a plain text description which is shown to the user. 

> `ioc_desc` is a short description of the IOC e.g Lakeshore 218 fro LKSH218

> `ioc_details` is more details about the IOC, e.g. link to docs.

`config.xml` support xinclude so if you have several iocs with the same set of macros you don't need to repeat the file contents. Example GALIL02 (see below) uses GALIL01's config:

```
<?xml version="1.0" ?>
<ioc_config xmlns:xi="http://www.w3.org/2001/XInclude">
<xi:include href="../iocGALIL-IOC-01/config.xml"  />
</ioc_config>
```

Either a full make of the server, or running `make iocstartups` will then make the contents of these xml files available to the GUI (after restarting the instrument)