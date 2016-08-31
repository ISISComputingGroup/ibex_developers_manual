> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs)

These are instructions for creating an IOC wrapper for a VI using lvDCOM. It assumes you want to create a "support" type module for lvdcom in ISIS. The Mercury ITC is an example where the below was followed and then an IOC was created using the this as a support module.

## 1. Create ISIS IOC

I plan to make these into a template (so you will just need to run makeBaseApp.pl and not do the edits), but for now this is the manual way.

Please take note of the [IOC naming convention](IOC-Naming) before proceeding.

1. Create a public repository to work in called EPICS-\<device>.
1. In the `EPICS\ISIS` directory create a directory called \<device>
1. Clone the repository into this directory and call that clone master
1. Copy a standard makefile into this directory

Create the IOC in master with (from an EPICS terminal)

```
 makeBaseApp.pl –t ioc <myname>
 makeBaseApp.pl –i –t ioc <myname>
```

Edit `mynameApp/src/build.mak` add dbd file

```
$(APPNAME)_DBD += lvDCOM.dbd
```

and libraries

```
$(APPNAME)_LIBS += lvDCOM 
$(APPNAME)_LIBS += asyn
```

and system library 

```
$(APPNAME)_SYS_LIBS_WIN32 += msxml2
```

Add the IOC to the makefile in `EPICS\ISIS\Makefile` e.g.

```
ATLDIRS += <device>
```

## 2. Create the xml configuration file

This is a summary of [[more general LvDCOM instructions|LVDCOM-auto-generate-xml]].

1. Open the VI in lab view.
1. Export strings from the labview panel (In different version of labview this is different)
     1. 2010:  Go to Tools menu, Advanced, Export Strings... and uncheck the wizard option for "block diagram strings" and save the export results to a text file e.g. controls.txt (Note: you may need write access to the VI itself to do this, so might have to make a local copy of the VI first)
     1. 2014: 
         1. Menu -> Tools -> Advanced -> Export Strings... 
         1. Then save file to (\<device>/protocol/controls.txt)
         1. Yes to "Export captions for controls without captions?"
         1. No to "Export block diagram strings?"
1. Generate a corrected xml file. In an epics terminal run in the protocol directory:
   ```
    C:\Instrument\Apps\EPICS\ISIS\lvDCOM\master\lvDCOMApp\src\fix_xml.cmd
"controls.txt" "controls.xml"
    ```
1. Generate lvcom file:
    ```
    xsltproc C:\Instrument\Apps\EPICS\ISIS\lvDCOM\master\lvDCOMApp\src\lvstrings2input.xsl "controls.xml" > lv_controls.xml
    ```
1. Edit lv_controls.xml (see below for example)
    1. Check the path is correct for the external interface, it should be:`<extint path="$(LVDCOM)/lvDCOMApp/src/extint/Main/Library/External Interface - Set Value.vi"/>`
    1. Path in vi element needs path to be vi in the llb containing the vi e.g. `C:/LabVIEW Modules/Drivers/Oxford Instruments/Mercury/Mercury - Temperature.llb/<name of vi>`
    1. Look at TODOs in this file
    1. remove unneeded controls or states of those controls (e.g. write for read only values)
    1. If the value is controlled by an event the `extint` value of set contols should be set to `"true"`. This will make it process the value. If one of the value is true you might as well set them all to be true the only advantage is if the are all false it does not need to load the external interface.
1. Add protocol file to `ISIS/<iocname>App/protocol/Makefile` as

    ```
    DATA += lv_controls.xml
    ```

## 3. Generate the DB File      

1. generate db file from an epics terminal in protocol
    ```
    xsltproc C:\Instrument\Apps\EPICS\ISIS\lvDCOM\master\lvDCOMApp\src\lvinput2db.xsl lv_controls.xml > ..\Db\controls.db
    ```
1. Add db file to `ISIS\<iocname>App\Db\Makefile`

   ```
   DB += controls.db
   ```
1. Edit the DB file. I found I wanted many `_RBV` to be `:RBV` and to get rid of some of the records (see below for example)

## 4. Edit to st.cmd

1. Add `lvDCOMConfigure("lvfp", "frontpanel", "${TOP}/data/lv_controls.xml")` before load common record. 
    * Main args are:  portName, configSection, configFile, host, options (see lvDCOMConfigure() documentation in lvDCOMDriver.cpp)
    * Additional optional args to specify a DCOM ProgID for a compiled LabVIEW application and a different username + password for remote host if that is required. e.g `lvDCOMConfigure("ex1", "example", "$(TOP)/lvDCOMApp/src/examples/example_lvinput.xml", "ndxtestfaa", 6, "", "username", "password")`
1. Add db load record

## 5. Run the IOC

Run the IOC as normal. The IOC should start with no errors and typing "dbl" will list the PVs. Note: unless the VI was already open it will not be visible. If it is not visible, stop the IOC, load the VI and restart the IOC

## 6. Finish the Workflow

Now return to the IOC workflow to finishing adding things like units, PVs of interest and macros.
Once the ISIS IOC works you should probably now create an IOC linked to this one in ioc follow a similar pattern to a support modules. Remember that if you do this add your new ioc to the Makefile `IOCDIRS` and it does not build if there is no ATL so add it to this list too, i.e. edit `EPICS\ioc\master\Makefile` add to the line:

    ifneq ($(HAVE_ATL),YES)  
    DIRS_NOTBUILD += ISISDAE MERCURY_ITC STPS350 AG53220A STSR400 DELFTSHEAR DELFTDCMAG DELFTARDUSTEP LVTEST
    endif



# Example XML control definitions

A numeric indicator:

```
<param name="ind1" type="float64"> 
    <read method="GCV" target="Some Indicator" />  
</param>
```
            
A numeric control:

```
<param name="cont1" type="float64">
    <read target="Some Control" method="GCV"/>
    <set target="Some Control" method="SCV" extint="false"/>
</param>
```

A boolean indicator:

```
<param name="bool_ind" type="int32"> 
    <read method="GCV" target="Some boolean indicator" />
</param>
```
          
A string control:

```
<param name="strcont1" type="string">
    <read target="Some String" method="GCV"/>
    <set target="Some String" method="SCV" extint="false"/>
</param>
```

An array indicator:

```     
<param name="arrayind1" type="float64array">
    <read target="Some Array" method="GCV"/>
</param>
```

# Example records

A numeric indicator:
```
record(ai, "$(P)NUM_IND")
{
    field(DTYP, "asynFloat64")
    field(INP,  "@asyn(ex1,0,0)param_name_from_xml")
    field(PREC, "3")
    field(SCAN, ".1 second")
}
```

A numeric control:

```
record(ao, "$(P)NUM_CON")
{
    field(DTYP, "asynFloat64")
    field(OUT,  "@asyn(ex1,0,0)param_name_from_xml")
    field(PREC, "3")
}
```
    
A boolean indicator:

```
record(bi, "$(P)BOOL_IND")
{
    field(DTYP, "asynInt32")
    field(INP,  "@asyn(ex1,0,0)param_name_from_xml")
    field(ZNAM, "FALSE")
    field(ONAM, "TRUE")
    field(SCAN, ".1 second")
}
```
        
A string control (two records - one for readback and one for writing):

```
record(stringin, "$(P)STR")
{
    field(DTYP, "asynOctetRead")
    field(INP,  "@asyn(ex1,0,0)param_name_from_xml")
    field(SCAN, ".1 second")
}

record(stringout, "$(P)STRW")
{
    field(DTYP, "asynOctetWrite")
    field(OUT,  "@asyn(ex1,0,0)param_name_from_xml")
}
```

A numeric array indicator:

```
record(waveform, "$(P)ARRAY_IND")
{
   field(DTYP, "asynFloat64ArrayIn")
   field(INP,  "@asyn(ex1,0,0)param_name_from_xml")
   field(PREC, "3")
   field(SCAN, ".1 second")
   field(NELM, "10")
   field(FTVL, "DOUBLE")
}
```

