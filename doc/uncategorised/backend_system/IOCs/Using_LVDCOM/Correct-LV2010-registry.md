> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Using LVDCOM](Using-LVDCOM) > Connecting to LV2010 registry

# Fixing LabVIEW 2010's Registry settings to allow remote DCOM access

It appears that when LabVIEW 2010 is installed it does not regisiter itself correctly in the Windows Registry. This means that it ignores any DCOM settings applied to it via dcomcnfg (see note below); as a result, it uses the general default settings instead.

Note: dcomcnfg is the DCOM configuration tool which can be launched by typing "dcomcnfg" at the command prompt.

Without the correction to the Registry, connecting to the machine from a remote lvDCOM IOC starts a second instance of LabVIEW rather than connecting to the existing instance - this is NOT what is wanted.

1. Find the CLSID of LabVIEW - you can use dcomcnfg for this or search the registry.

1. Under `HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID`, find the `LabVIEW.exe` and copy the `AppId`

1. Under `HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID\{LabVIEW GUID from step 1}`, add a string called `!AppId` and set the value to the `AppId` from above.

1. Open dcomcnfg as Administrator, locate LabVIEW and click properties. Under Identity, set it to launching user then click OK.
