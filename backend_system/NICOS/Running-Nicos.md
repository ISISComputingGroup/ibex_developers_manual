> [Wiki](Home) > [The Backend System](The-Backend-System) > [Nicos](Nicos) > Running Nicos

Nicos is set to start/stop running as part of the instrument in the `start_ibex_server_full.bat` file, but the code is commented out for now to speed things up as the script server is not ready for use. To start Nicos with the IBEX server, simply uncomment the lines:
```
 if "%ISIS_INSTRUMENT%" == "1" (
    @echo NICOS Script Server not ready to start on real instrument
 ) else (
    if not "%COMPUTERNAME%" == "NDWRENO" (
	    call %STARTINSTDIR%ISIS\ScriptServer\nicos-core\master\start_script_server.bat
	)
 )
```

If you want to start/stop the Nicos script server (i.e. the Nicos daemon) in isolation you have two options:
* You can use the `start_nicos_daemon.bat` and `stop_nicos_daemon.bat` files in the root Nicos directory. This will start the Nicos process within procServ. Note that Nicos needs in its root directory a file called `nicos.conf` to know which instrument settings to use (instrument settings are located in `custom/`); the startup bat script will generate this file for you.
* You can navigate to the `bin/` directory and run `python nicos-daemon`. If no `nicos.conf` file is found, Nicos will run the `demo` instrument by default. Details on how to specify which instrument to run can be found in the [Running an Instrument](Configuring-a-New-Nicos-Instrument) section of the developer's manual. Note that for Nicos to be able to talk channel access through the genie_python commands, you need to launch it from within an EPICS terminal, so the necessary macros are set.

To test the script server is working, open the "Nicos Scripting" perspective in the ibex client. Check that the connection status label says "connected". Write a simple script and send it to the server. You should be able to see the output from NICOS in the output text field.

For testing purposes you can also start the Nicos GUI by navigating to the `bin/` directory and run `python nicos-gui` and connect to the local daemon. However, as the NICOS GUI does not use ZeroMQ you will have to comment out `servercls='nicos.services.daemon.proto.zeromq.Server'` in `nicos-core/master/custom/demo/setups/special`. Both `nicos-daemon` and `nicos-gui` need to be restarted for this change to take effect.