> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Imaging Cameras](Imaging-Cameras) > [Pixelman](Pixelman)

## IOC

This IOC runs on a separate computer, **not on NDXIMAT**. 

The computer's name is `IMAT-UCB`, the password is listed on the passwords page. The PV Prefix is `MO:IMAT-MCP`.

To launch Pixelman you have to run a special batch script in `C:\Instrument\Apps\EPICS\support\pixelman\master\run`. The file is `run_pixelman.bat` You should see some log entries in the camera software and the Pixelman GUI will start itself as it loads the EPICS plugins. If the .exe is just double-clicked the camera software will look like it loaded OK but not publish any PVs.  If you get a message box suggesting you remove a line from a file, please click "NO"

For more information see the README file in `C:\Instrument\Apps\EPICS\support\pixelman\master\run`

## Setup

The PC is set up and looked after by FIT and the instrument scientists. The person from Berkley set up the camera software and network card; the scientists may have instructions about how to restart various components.

We installed the IBEX server **32-bit** into `c:\instrument\apps\epics` using the normal installer but for 32-bit (we literally only installed the server, no git, client, SQL or config). The server does **not** run, we just use the two programs detailed in IOC section.

To help with this we created two shortcuts on the desktop to start Pixelman and gateways as above.

## Troubleshooting

If you see errors on the IMAT screen from scripts that say things like connection failed to IMAT:...:SP: you may need to start the EPICS gateway.  To do this type `C:\Instrument\Apps\EPICS\gateway\start_gateways.bat`.  You may also need to restart the Pixelman software.

It seems that if the contents of `ShutterValues.txt` are not liked by Pixelman, then the program will not start with EPICS support and you either get nothing or a Microsoft C++ error box. If you run `pixelman.exe` and dismiss the errors about not being able to load `epics.dll` then Pixelman will start, but you have no EPICS PVs. If you use the desktop shortcut `run_pixelman.bat` it fails as described. The EPICS DLL does not read `ShutterValues.txt` so I am unsure of the reason behind this, we do not have the source code for Pixelman so I cannot debug this.

UPDATE: after investigation by camera developer, it looks like the maximum number of time slices is now lower than it used to be (now ~2900, previously 3100), which means previous working `ShutterValues.txt` files may fail. At the moment it is unclear what has caused this.
