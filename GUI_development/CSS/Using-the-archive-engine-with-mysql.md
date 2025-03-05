> [Wiki](Home) > [The GUI](The-GUI) > [CS Studio](GUI-CSS) > Using the archive engine with MySQL

Inside the EPICS_PILOT repository, there are pre-built executables for the Archive Configuration Tool and the Archive Engine.

# Creating a configuration

The Archive Configuration Tool bundle includes two batch files: one for retrieving the current configuration; and, one for setting a new configuration.

The mysql_settings.ini file contains the database settings and may need to be altered depending on your setup.

There is a demonstration configuration file called icap_test_config.xml which can be used as a starting point for your own configuration. 

Alternatively, you can use the get_config.bat file to retrieve the current settings, the bat file will need to be edited to set the correct engine name to retrieve.

To send a configuration to the database, use the set_config.bat file.

This file will need to be edited to point at the correct engine (currently set to `icap_test_engine`) and to use the correct configuration file (currently set to `icap_test_config.xml`).

# Running the Archive Engine
The Archive Engine bundle contains two batch files: one for starting the engine; and, one for stopping the engine.

The `mysql_settings.ini` file contains the database settings and may need to be altered depending on your setup.

To run the archive engine use the `run_archive_engine.bat` file.

This file will need to be edited to point at the correct engine (currently set to icap_test_engine).

To stop the archive engine use the `kill_archive_engine.bat` file.

Note: sometimes the archive engine disappears from task manager but still appears to be running.
If this happens then it is necessary to kill the associated `javaw.exe` process.
