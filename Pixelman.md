# IOC

This IOC runs on a separate computer, **not on NDXIMAT**. 

The computer's name is `IMAT-UCB-DETECT`, the password is listed on the passwords page.

To launch pixelman have to run a special batch script in `support/pixelman/run`. You should see some log entries in the camera software as it loads the EPICS plugins. If the .exe is just double clicked the camera software will look like it loaded ok but not publish any PVs

For more information see the README file in `C:\Instrument\Apps\EPICS\support\pixelman\master\run`