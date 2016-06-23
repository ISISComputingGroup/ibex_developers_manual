This page documents the finishing touches to make to your IOC to make it function within the IBEX environment.

## 1. Interesting PVs

To have a PV appear in the interest list in IBEX Configurations add the following to the PV record:

    info(INTEREST, "<LEVEL>")

where level is HIGH, MEDIUM, LOW

## 2. Archive PVs

To have a PV automatically archived add the following to the PV record

    info(archive, "VAL")

## 3. PVs Have Essential Fields

All PVs should have if appropriate:

* Description (`DESC` field)
* Unit fields if representing a value (`EGU` field) which may be blank
    * Units must be in ...

## 4. Macros

If a macro can be set as part of the IOC (and can be reasonably set in the GUI) then a config file should be added to the run directory which contains a list of macros (i.e. `..\EPICS\ioc\master\<IOC Name>\iocBoot\<IOC Instance Name>\config.xml). The file is of the form:

```
<?xml version="1.0" ?>
<ioc_config xmlns:xi="http://www.w3.org/2001/XInclude">
<config_part>
<macros>
<macro name="VI_TEMP_1" pattern="^[A-Z0-9]+$" description="Suffix of the vi temperature panel, usually '1' or blank for no controller." />
<macro name="VI_TEMP_2" pattern="^[A-Z0-9]+$" description="Suffix of the vi temperature panel, usually '2' or blank for no controller." />
<macro name="VI_TEMP_3" pattern="^[A-Z0-9]+$" description="Suffix of the vi temperature panel, usually '3' or blank for no controller." />
<macro name="VI_TEMP_4" pattern="^[A-Z0-9]+$" description="Suffix of the vi temperature panel, usually '4' or blank for no controller." />
</macros>
</config_part>
</ioc_config>
```

where `name` is the name of the macro,  pattern is the regex for the macro's value and description is a plain text description which is shown to the user. 
`config.xml` support xinclude so if you have several iocs with the same set of macros you don't need to repeat the file contents. Example GALIL02 (see below) uses GALIL01's config:

```
<?xml version="1.0" ?>
<ioc_config xmlns:xi="http://www.w3.org/2001/XInclude">
<xi:include href="../iocGALIL-IOC-01/config.xml"  />
</ioc_config>
```

Either a full make of the server, or running `make iocstartups` will then make the contents of these xml files available to the GUI (after restarting the instrument)