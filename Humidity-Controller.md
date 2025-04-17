> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Other](Other) > [Humidity Controller](Humidity-Controller)

This program is running on the `imat-messina-detect` pc, it reads the humidity via DDE and writes it into a user pv  `IN:IMAT:PARS:USER:R0`. If the `imat-messina-detect` pc reboots the program will need restarting, the procedure is:

- On `messina` PC open the directory  `c:\Instrument\Apps\EPICS`  in windows explorer
- Double click on `start_rhcontroller.bat`

This will create a new window with the program running inside it, this window can then be minimised

(NOTE: this was a temporary workaround and will be replaced by a proper WinDDE client solution #4065)