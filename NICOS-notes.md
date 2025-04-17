> [Wiki](Home) > [The Backend System](The-Backend-System) > [Nicos](Nicos) > [Nicos notes](NICOS-notes)

# Periodic git pop-up while client is running

If Nicos is not correctly up-to-date and working it has been seen that periodically a git.exe cmd pops up on screen. This is associated with the following log message in the GUI:
```
*2020-02-26 14:31:01.578 [Worker-9: NICOSConnection] INFO  uk.ac.stfc.isis.ibex.nicos.comms.ZMQWrapper - Opening ZMQ connection to NICOS
*2020-02-26 14:31:01.581 [Worker-9: NICOSConnection] INFO  uk.ac.stfc.isis.ibex.nicos.comms.ZMQSession - Connected to NICOS at tcp://localhost:1301
*2020-02-26 14:31:03.085 [Worker-9: NICOSConnection] WARN  uk.ac.stfc.isis.ibex.nicos.comms.ZMQSession - No response from server after sending uk.ac.stfc.isis.ibex.nicos.messages.GetBanner@586e968c
*2020-02-26 14:31:03.085 [Worker-9: NICOSConnection] ERROR uk.ac.stfc.isis.ibex.nicos.NicosModel - NICOS error: The connection to the script server failed, 
*2020-02-26 14:31:03.085 [Worker-9: NICOSConnection] ERROR uk.ac.stfc.isis.ibex.nicos.NicosModel - No data received from NICOS
```
Nicos is (most likely) spawning a shell which in turn creates a git instance but fails to start the full server. To remedy this, first console into the NICOS server: `console -M localhost` and `Ctrl-T` + `Ctrl-X` to stop auto-restart and kill the process. Then re-install NICOS using: 
```
%python3% -m pip install --upgrade --extra-index-url https://forge.frm2.tum.de/simple nicos-pyctl
``` 
Once it has installed successfully it's advised you also pull EPICS top directory. Finally you can `Ctrl-T` + `Ctrl-X`, once more in the NICOS console session to re-enable auto-restart and restart the server. You should then see the client connect to the NICOS server successfully:
```
*2020-02-26 14:32:52.322 [Worker-6: NICOSConnection] INFO  uk.ac.stfc.isis.ibex.nicos.comms.ZMQWrapper - Opening ZMQ connection to NICOS
*2020-02-26 14:32:52.325 [Worker-6: NICOSConnection] INFO  uk.ac.stfc.isis.ibex.nicos.comms.ZMQSession - Connected to NICOS at tcp://localhost:1301
```
and the pop up should stop.

