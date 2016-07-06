> [Wiki](Home) > [The Backend System](The-Backend-System) > [Nicos](Nicos) > Running Nicos

Nicos is set to start/stop running as part of the entire instrument in the `start_inst.bat` file.

If you want to start/stop the Nicos script server (i.e. the Nicos daemon) in isolation you have two options:
* You can use the `start_nicos_daemon.bat` and `stop_nicos_daemon.bat` files in the root Nicos directory. This will start the Nicos process within procServ. Note that Nicos needs in its root directory a file called `nicos.conf` to know which instrument settings to use (instrument settings are located in `custom/`); the startup bat script will generate this file for you.
* You can navigate to the `bin/` directory and run `python nicos-daemon`. If no `nicos.conf` file is found, Nicos will run the `demo` instrument by default. Details on hown to specify which instrument to run can be found in the [Running an Instrument](Configuring-and-Running-a-New-Nicos-Instrument) section of the developer's manual. Note that for Nicos to be able to talk channel access through the genie_python commands, you need to launch it from within an EPICS terminal, so the necessary macros are set.

At the time of writing the IBEX GUI is not setup to communicate with Nicos. For testing purposes you can start the Nicos GUI by navigating to the `bin/` directory and run `python nicos-gui`.