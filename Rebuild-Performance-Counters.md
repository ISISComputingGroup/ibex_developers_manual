If nagios was working OK and then suddenly you get lots of errors similar to : 
```
UNKNOWN - The WMI query had problems. You might have your username/password wrong or 
the user's access level is too low. Wmic error text on the next line.
[wmi/wmic.c:196:main()] ERROR: Login to remote object.
NTSTATUS: NT_STATUS_ACCESS_DENIED - Access denied
```
You may need to rebuild the performance counters on the machine that cannot be queried.

This is detailed on https://support.microsoft.com/en-us/help/2554336/how-to-manually-rebuild-performance-counters-for-windows-server-2008-6 but to summarise:

1. Open a administrator CMD window
1. Rebuild the counters:
    ```
    cd c:\windows\system32
    lodctr /R
    cd c:\windows\sysWOW64
    lodctr /R
    ```
1. Resync the counters with Windows Management Instrumentation (WMI):
    ```
    WINMGMT.EXE /RESYNCPERF
    ```
1. Stop and restart the Performance Logs and Alerts service (only if it is running)
1. Stop and restart the Windows Management Instrumentation service (this should always be running)


If all this fails, you may have to reboot

You can check WMI is working remotely by using the WMIC from your own computer e.g. to check `ndxvesuvio`
```
wmic /node:"ndxvesuvio" /user:"ndxvesuvio\the_admin_account" os get name
```
Replacing  the_admin_account  with our usual admin account


