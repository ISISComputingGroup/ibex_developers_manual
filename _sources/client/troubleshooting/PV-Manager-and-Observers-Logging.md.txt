# PVManager & Observers Logging

To help debug the PVObserver and lower levels you can build a version of the GUI which includes logging and the code for PV manager.

1. Checkout [csstudio repository](https://github.com/ISISComputingGroup/CSStudio_3_3) to somewhere accessible (probably c:\instrument\Dev)
1. Switch to the Logging_for_PV_connections branch
    - NB the JCA and caj code has been copied from the caj and jca project to org.csstudio.platform.libs.epics and the jar deleted in this project. If you need to update this code create a new copy.
1. Switch the gui branch to Logging_for_PV_connections 
1. Import all projects (including nested projects) from this directory into Eclipse 
1. Clean and build - not all projects will build but all the ones needed should build.
1. Run with the following plugins from the workspace instead of the P2 repository. To do this select Run -> Run configuration. On the plug-ins tab type the plugin name and deselect target platform and select workspace:
    - org.csstudio.logging
    - org.csstudio.platform.libs.epics
    - org.csstudio.utilities.pvmanager
    - org.csstudio.utilities.pvmanager.epics
1. This will now print out debug statements all containing the text Ticket2162
1. The logs can be filtered using a python program below (this program is very rough, don't forget to change the date)
1. This can be combined with Wireshark to analyse traffic if needed

Example log output from disconnection to reconnection

```
:NDW1407:CS:SB:TEMP1 = 13:52:47.265000: CAJChannel connect changegov.aps.jca.Channel$ConnectionState[DISCONNECTED=1]
:NDW1407:CS:SB:TEMP1 = 13:52:47.265000: MultiplexChannelHandler connect changeJCAConnection [connected: false writeConnected: false channel: CAJChannel = { name = TE:NDW1407:CS:SB:TEMP1, connectionState = DISCONNECTED }]
:NDW1407:CS:SB:TEMP1 = 13:52:47.265000: ConnectionCollector connect changefalse
:NDW1407:CS:SB:TEMP1 = 13:52:47.266000: PVDirector connected or exception event false
:NDW1407:CS:SB:TEMP1 = 13:52:47.266000: PVReaderImpl connection
:NDW1407:CS:SB:TEMP1 = 13:52:47.266000: PVManagerObservable connection false
:NDW1407:CS:SB:TEMP1 = 13:52:47.266000: DisplayBlock connection false
:NDW1407:CS:SB:TEMP1 = 13:52:47.266000: ChannelSearchManager Moved channel search to timer with delay 32
:NDW1407:CS:SB:TEMP1 = 13:52:47.276000: CAJChannel generate search request
:NDW1407:CS:SB:TEMP1 = 13:52:47.276000: Search requests generate search request
:NDW1407:CS:SB:TEMP1 = 13:52:47.276000: ChannelSearchManager request sent? true
:NDW1407:CS:SB:TEMP1 = 13:52:47.309000: ChannelSearchManager Moved channel search to timer with delay 64
                 all = 13:52:47.309000: ChannelSearchManager no work to do not restarting timer. period32
:NDW1407:CS:SB:TEMP1 = 13:52:47.319000: CAJChannel generate search request
:NDW1407:CS:SB:TEMP1 = 13:52:47.319000: Search requests generate search request
:NDW1407:CS:SB:TEMP1 = 13:52:47.319000: ChannelSearchManager request sent? true
:NDW1407:CS:SB:TEMP1 = 13:52:47.366000: PVReaderImpl valueChange
:NDW1407:CS:SB:TEMP1 = 13:52:47.366000: PVManagerObservable valueChange false
:NDW1407:CS:SB:TEMP1 = 13:52:47.383000: ChannelSearchManager Moved channel search to timer with delay 128
                 all = 13:52:47.383000: ChannelSearchManager no work to do not restarting timer. period64
:NDW1407:CS:SB:TEMP1 = 13:52:47.393000: CAJChannel generate search request
:NDW1407:CS:SB:TEMP1 = 13:52:47.393000: Search requests generate search request
:NDW1407:CS:SB:TEMP1 = 13:52:47.393000: ChannelSearchManager request sent? true
:NDW1407:CS:SB:TEMP1 = 13:52:47.521000: ChannelSearchManager Moved channel search to timer with delay 256
                 all = 13:52:47.521000: ChannelSearchManager no work to do not restarting timer. period128
:NDW1407:CS:SB:TEMP1 = 13:52:47.531000: CAJChannel generate search request
:NDW1407:CS:SB:TEMP1 = 13:52:47.531000: Search requests generate search request
:NDW1407:CS:SB:TEMP1 = 13:52:47.531000: ChannelSearchManager request sent? true
:NDW1407:CS:SB:TEMP1 = 13:52:47.787000: ChannelSearchManager Moved channel search to timer with delay 512
                 all = 13:52:47.787000: ChannelSearchManager no work to do not restarting timer. period256
:NDW1407:CS:SB:TEMP1 = 13:52:47.797000: CAJChannel generate search request
:NDW1407:CS:SB:TEMP1 = 13:52:47.797000: Search requests generate search request
:NDW1407:CS:SB:TEMP1 = 13:52:47.797000: ChannelSearchManager request sent? true
:NDW1407:CS:SB:TEMP1 = 13:52:48.309000: ChannelSearchManager Moved channel search to timer with delay 1024
                 all = 13:52:48.309000: ChannelSearchManager no work to do not restarting timer. period512
:NDW1407:CS:SB:TEMP1 = 13:52:48.319000: CAJChannel generate search request
:NDW1407:CS:SB:TEMP1 = 13:52:48.319000: Search requests generate search request
:NDW1407:CS:SB:TEMP1 = 13:52:48.319000: ChannelSearchManager request sent? true
:NDW1407:CS:SB:TEMP1 = 13:52:49.343000: ChannelSearchManager Moved channel search to timer with delay 2048
                 all = 13:52:49.343000: ChannelSearchManager no work to do not restarting timer. period1024
:NDW1407:CS:SB:TEMP1 = 13:52:49.353000: CAJChannel generate search request
:NDW1407:CS:SB:TEMP1 = 13:52:49.353000: Search requests generate search request
:NDW1407:CS:SB:TEMP1 = 13:52:49.353000: ChannelSearchManager request sent? true
:NDW1407:CS:SB:TEMP1 = 13:52:51.401000: ChannelSearchManager Moved channel search to timer with delay 4096
                 all = 13:52:51.401000: ChannelSearchManager no work to do not restarting timer. period2048
:NDW1407:CS:SB:TEMP1 = 13:52:51.411000: CAJChannel generate search request
:NDW1407:CS:SB:TEMP1 = 13:52:51.411000: Search requests generate search request
:NDW1407:CS:SB:TEMP1 = 13:52:51.411000: ChannelSearchManager request sent? true
:NDW1407:CS:SB:TEMP1 = 13:52:55.508000: ChannelSearchManager Moved channel search to timer with delay 8192
                 all = 13:52:55.508000: ChannelSearchManager no work to do not restarting timer. period4096
:NDW1407:CS:SB:TEMP1 = 13:52:55.518000: CAJChannel generate search request
:NDW1407:CS:SB:TEMP1 = 13:52:55.518000: Search requests generate search request
:NDW1407:CS:SB:TEMP1 = 13:52:55.518000: ChannelSearchManager request sent? true
                 all = 13:52:58.123000: ChannelSearchManager no work to do not restarting timer. period16384
:NDW1407:CS:SB:TEMP1 = 13:53:03.711000: ChannelSearchManager Moved channel search to timer with delay 16384
                 all = 13:53:03.711000: ChannelSearchManager no work to do not restarting timer. period8192
:NDW1407:CS:SB:TEMP1 = 13:53:03.721000: CAJChannel generate search request
:NDW1407:CS:SB:TEMP1 = 13:53:03.721000: Search requests generate search request
:NDW1407:CS:SB:TEMP1 = 13:53:03.721000: ChannelSearchManager request sent? true
                 all = 13:53:05.425000: ChannelSearchManager no work to do not restarting timer. period32
                 all = 13:53:05.788000: ChannelSearchManager no work to do not restarting timer. period128
                 all = 13:53:06.224000: ChannelSearchManager no work to do not restarting timer. period256
                 all = 13:53:08.641000: ChannelSearchManager no work to do not restarting timer. period128
:NDW1407:CS:SB:TEMP1 = 13:53:20.534000: ChannelSearchManager Moved channel search to timer with delay 32768
                 all = 13:53:20.534000: ChannelSearchManager no work to do not restarting timer. period16384
:NDW1407:CS:SB:TEMP1 = 13:53:20.830000: CAJChannel generate search request
:NDW1407:CS:SB:TEMP1 = 13:53:20.830000: Search requests generate search request
:NDW1407:CS:SB:TEMP1 = 13:53:20.831000: ChannelSearchManager request sent? true
                 all = 13:53:38.603000: ChannelSearchManager no work to do not restarting timer. period32
                 all = 13:53:39.815000: ChannelSearchManager no work to do not restarting timer. period64
                 all = 13:53:39.954000: ChannelSearchManager no work to do not restarting timer. period128
                 all = 13:53:46.211000: ChannelSearchManager no work to do not restarting timer. period16384
                 all = 13:53:50.802000: ChannelSearchManager no work to do not restarting timer. period256
:NDW1407:CS:SB:TEMP1 = 13:54:10.818000: CAJChannel generate search request
:NDW1407:CS:SB:TEMP1 = 13:54:10.818000: Search requests generate search request
:NDW1407:CS:SB:TEMP1 = 13:54:10.819000: ChannelSearchManager request sent? false
                 all = 13:54:11.286000: ChannelSearchManager no work to do not restarting timer. period512
:NDW1407:CS:SB:TEMP1 = 13:54:43.587000: CAJChannel generate search request
:NDW1407:CS:SB:TEMP1 = 13:54:43.587000: Search requests generate search request
:NDW1407:CS:SB:TEMP1 = 13:54:43.587000: ChannelSearchManager request sent? true
:NDW1407:CS:SB:TEMP1 = 13:54:43.589000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 22
:NDW1407:CS:SB:TEMP1 = 13:54:43.589000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 18
:NDW1407:CS:SB:TEMP1 = 13:54:43.591000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 22
:NDW1407:CS:SB:TEMP1 = 13:54:43.591000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 18
:NDW1407:CS:SB:TEMP1 = 13:54:43.591000: CAJChannel connect complete changegov.aps.jca.Channel$ConnectionState[DISCONNECTED=1]
:NDW1407:CS:SB:TEMP1 = 13:54:43.591000: CATransport resubscribe subscriptions request
:NDW1407:CS:SB:TEMP1 = 13:54:43.591000: CATransport resubscribe subscriptions request
:NDW1407:CS:SB:TEMP1 = 13:54:43.591000: CAJChannel connect changegov.aps.jca.Channel$ConnectionState[CONNECTED=2]
:NDW1407:CS:SB:TEMP1 = 13:54:43.591000: MultiplexChannelHandler connect changeJCAConnection [connected: true writeConnected: false channel: CAJChannel = { name = TE:NDW1407:CS:SB:TEMP1, connectionState = CONNECTED }]
```

## Python to analysis the logs:

See `...ibex_utils\ibex_log_parser\parse.py`
