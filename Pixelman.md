# IOC

This IOC runs on a separate computer, **not on NDXIMAT**. 

The computer's name is `IMAT-UCB-DETECT`, the password is listed on the passwords page.

To launch pixelman you have to run a special batch script in `C:\Instrument\Apps\EPICS32\support\pixelman\master\run`. The file is `run_pixelman.bat` You should see some log entries in the camera software and the pixelman GUI will start itself as it loads the EPICS plugins. If the .exe is just double clicked the camera software will look like it loaded ok but not publish any PVs.  If you get a message box suggesting you remove a line from a file, please click "NO"

IF you see errors on the IMAT screen from scripts that say things like connection failed to IMAT:...:SP: you may need to start the EPICS gateway.  To do this type

`C:\Instrument\Apps\EPICS32\gateway\start_gateways.bat`

For more information see the README file in `C:\Instrument\Apps\EPICS32\support\pixelman\master\run`

# Troubleshooting

It seem that if the contents of ShutterValues.txt are not liked by pixelman, then the program will not start with EPICS support and you either get nothing or a microsoft c++ error box. If you run pixelman.exe and dismiss the errors about not being able to load epics.dll then pixelman will start, but you have no epics PVs. If you use the desktop shortcut/run_pixelman.bat it fails as described.
