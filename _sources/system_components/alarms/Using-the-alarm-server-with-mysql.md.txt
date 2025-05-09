# Using the alarm server with MySQL

Inside the EPICS_PILOT repository, there are pre-built executables for the Alarm Configuration Tool and the Alarm Server.

Apache's ActiveMQ will need to be installed somewhere and be accessible. ActiveMQ provides the Java Message Service (JMS) used by CSS to communicate with the various parts of the system.

[ActiveMQ](/system_components/ActiveMQ)

## Creating a configuration

The Alarm Configuration Tool bundle includes two batch files: one for retrieving the current configuration; and, one for setting a new configuration.

The alarm_server_settings.ini file contains the database and JMS settings and may need to be altered depending on your setup.

There is a demonstration configuration file called alarm_config.xml which can be used as a starting point for your own configuration. 

Alternatively, you can use the get_config.bat file to retrieve the current settings, the bat file will need to be edited to set the correct root name to retrieve.

The root is essentially the name of the alarm configuration and is found in the first line of the configuration XML, it will look something like this <config name="test">

To send a configuration to the database, use the set_config.bat file.

This file will need to be edited to point at the correct root (currently set to test) and to use the correct configuration file (currently set to alarm_config.xml).

## Running the Alarm Server

Firstly, the JMS needs to be running; usually this is done by navigating to the bin folder in the ActiveMQ installation and running the batch file.

The alarm_server_settings.ini file contains the database and JMS settings and may need to be altered depending on your setup.

The Alarm Server is started using the run_alarm_server.bat file. When run it will spawn a command window.
This file will need to be edited to point at the correct root (currently set to test).

To stop the alarm server close the window that is spawned on startup.
