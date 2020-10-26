> [Wiki](Home) > [The Backend System](The-Backend-System) > [Creating and Basics of IOCs](IOCs) > [pcaspy ioc](ioc-pcaspy)

IOCs can be served via python using pycaspy. These let you create IOCs with PVs using channel access. They do not work quite like the normal EPICs so this the start of a guide to help create one.

## Main Loop

To Do

## Allow IBEX to start the IOC

The easiest way to let ibex start the pycaspy server (or in fact any python script) you need:

1. Create dir (use same [naming rules](IOC-Naming) as for other IOCs)
1. Add an empty makefile. Copy the one in LSICORR
1. Create the directory tree: `<ioc name>\iocBoot\ioc<ioc name>-IOC-01`
    1. Add a [standard `config.xml` to the folder](IOC-Finishing-Touches#7-macros-and-details)
    1. Add a `runIoc.bat` file which runs the pycas py server with options.
1. If needed create a similar tree for a second IOC.

## Registering IOC and PVs with IBEX

To make sure that IBEX knows both that your IOC has started and what PVs should be archived and interesting use:

```
sys.path.insert(2, os.path.join(os.getenv("EPICS_KIT_ROOT"), "ISIS", "inst_servers", "master"))
from server_common.helpers import register_ioc_start, get_macro_values

register_ioc_start(REFL_IOC_NAME, STATIC_PV_DATABASE, PREFIX)
```

where
- `STATIC_PV_DATABASE`: is a pv database used to construct the pv. To add a pv info field use entries in the pv for PV_INFO_FIELD_NAME. For example `{'pv name': {'info_field': {'archive': '', 'INTEREST': 'HIGH'}, 'type': 'float'}}` which will archive the val field and register the pv as high interest.
- `PREFIX`: is the prefix for the IOC e.g. `IN:NDXLARMOR:REFL_01`

## Accessing PVs

Most IOCs which need to access PVs use the `CaChannelWrapper` in `instservers` file `server_common/channel_access.py`. To do this:

```
import sys
import os
sys.path.insert(2, os.path.join(os.getenv("EPICS_KIT_ROOT"), "ISIS", "inst_servers", "master"))

ChannelAccess.caget("{}BLAH".format(mypvprefix))
```

## Accessing Macros on Start

If you want to access the macros on start of a pv then add the following to your runIOC.bat:

- `call dllPath.bat`: this adds the dll paths needed to run the icp config command. For example of this file see the reflectometry IOC.
- Nearer the end put the macros into an environment variable (`icpconfigGetMacros` is defined in [icpconfig](icpconfig)) 

    ```
        set "GETMACROS=C:\Instrument\Apps\EPICS\support\icpconfig\master\bin\%EPICS_HOST_ARCH%\icpconfigGetMacros.exe"
        set "MYIOCNAME=<IOC NAME>"

        if "%MACROS%"=="" (
            REM need this funny syntax to be able to set eol correctly - see google
            for /f usebackq^ tokens^=*^ delims^=^ eol^= %%a in ( `%GETMACROS% %MYIOCNAME%`  ) do ( set "MACROS=%%a" )
            echo Defining macros
        ) else (
            echo Macros already defined
        )

        echo Macro JSON is %MACROS%
    ```

- Inside the IOC you can access the macros with:

    ```
        from server_common.helpers import register_ioc_start, get_macro_values
        get_macro_values()
    ````
