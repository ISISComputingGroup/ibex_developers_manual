# Creating an IOC wrapper for a VI using lvDCOM

**NOTE:** Template XML and DB files can now be automatically generated from the VI - see [wiki:LVDCOMAutoGenerateXML here].

For this example the Agilent 53220A Front Panel VI is used (C:\LabVIEW Modules\Drivers\Agilent 53220A).

Copy the directory lvDCOM directory from your EPICS build (in the future we will be able to get this from the build server).
Rename the directory to match the VI, in this case Agilent_53220A. Note: no spaces allowed in directory name.

Copy Agilent_53220A/lvDCOMApp/src/examples/example_lvinput.xml to Agilent_53220A/iocBoot/ioclvDCOM and rename it to match the VI (no spaces), in this case: agilent53220A.

Open the XML file.
Check the path is correct for the external interface, it should be:

```
<extint path="c:/LabVIEW Modules/Common/External Interface/External Interface.llb/External Interface - Set Value.vi" />
```

Change the section name if you wish (for example: frontpanel) and set the VI path to point at the real VI:

```    
<vi path="C:/LabVIEW Modules/Drivers/Agilent 53220A/Agilent 53220A - System Functions.llb/Agilent 53220A - Front Panel.vi"> 
```

Add params for the controls you wish to expose. The target should be set to the name of the control or indicator (including case?):

```    
<param name="counts" type="float64"> 
    <read method="GCV" target="Counts" />  
</param>
	
<param name="counting" type="int32"> 
    <read method="GCV" target="Counting" />
</param>

<param name="start" type="int32"> 
    <read method="GCV" target="Start Counting" />  
    <set method="SCV" extint="true" target="Start Counting" /> 
</param>
      
<param name="stop" type="int32"> 
    <read method="GCV" target="Stop Counting" />  
    <set method="SCV" extint="true" target="Stop Counting" /> 
</param>
```
   
NOTE: where extint is set to true the external interface will be used.\\
        
Open lvDCOM.db in Agilent_53220A.db and edit it to match the XML file - any INP or OUT param should match a param name defined in the XML file:

```
record(ai, "$(P)COUNTS")
{
    field(DTYP, "asynFloat64")
    field(INP,  "@asyn(ex1,0,0)counts")
    field(PREC, "3")
    field(SCAN, ".1 second")
}

record(bi, "$(P)COUNTING")
{
    field(DTYP, "asynInt32")
    field(INP,  "@asyn(ex1,0,0)counting")
    field(ZNAM, "FALSE")
    field(ONAM, "TRUE")
    field(SCAN, ".1 second")
}

record(ao, "$(P)START")
{
    field(DTYP, "asynInt32")
    field(OUT,  "@asyn(ex1,0,0)start")
}

record(ao, "$(P)STOP")
{
    field(DTYP, "asynInt32")
    field(OUT,  "@asyn(ex1,0,0)stop")
}
```

Change directory to Agilent_53220A/iocBoot/ioclvDCOM\\
Open st.cmd for editing and change it to this:

```
#!../../bin/windows-x64/lvdcom

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/lvDCOM.dbd"
lvDCOM_registerRecordDeviceDriver pdbbase

cd ${TOP}/iocBoot/${IOC}

# Turn on asynTraceFlow and asynTraceError for global trace, i.e. no connected asynUser.
#asynSetTraceMask("", 0, 17)

## main args are:  portName, configSection, configFile, host, options (see lvDCOMConfigure() documentation in lvDCOMDriver.cpp)
##
## there are additional optional args to specify a DCOM ProgID for a compiled LabVIEW application 
## and a different username + password for remote host if that is required 
##
## the "options" argument is a combination of the following flags (as per the #lvDCOMOptions enum in lvDCOMInterface.h)
##    viWarnIfIdle=1, viStartIfIdle=2, viStopOnExitIfStarted=4, viAlwaysStopOnExit=8
lvDCOMConfigure("ex1", "frontpanel", "$(TOP)/iocBoot/ioclvDCOM/agilent53200A.xml", "", 6)
#lvDCOMConfigure("ex1", "example", "$(TOP)/lvDCOMApp/src/examples/example_lvinput.xml", "", 6, "LvDCOMex.Application")
#lvDCOMConfigure("ex1", "example", "$(TOP)/lvDCOMApp/src/examples/example_lvinput.xml", "ndxtestfaa", 6, "", "username", "password")

dbLoadRecords("$(TOP)/db/lvDCOM.db","P=INST:SE:AG53220A:")
#dbLoadRecords("$(ASYN)/db/asynRecord.db","P=ex1:,R=asyn1,PORT=ex1,ADDR=0,OMAX=80,IMAX=80")
#asynSetTraceMask("ex1",0,0xff)
asynSetTraceIOMask("ex1",0,0x2)

iocInit
```
    
Open the envPaths file and check all the environment variables are correct.\\ 
The TOP variable should be set to the location of the new IOC, for example: 

```
epicsEnvSet("TOP","c:/YOUR_PATH/Agilent_53220A")
```

Now run the IOC:

```
..\..\bin\windows-x64\lvDcom.exe st.cmd
```

The IOC should start with no errors and typing "dbl" will list the PVs.\\
Note: unless the VI was already open it will not be visible. If it is not visible, stop the IOC, load the VI and restart the IOC

From another command window it should be possible to use caget and caput to play with these PVs.

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