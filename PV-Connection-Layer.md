> [Wiki](Home) > [The GUI](The-GUI) > [CS Studio](GUI-CSS) > [PV Connection Layer](PV-Connection-Layer)

This is what I think I know about how the layers under PVMAnagerObservable work to reconnect to a PV. This was part of the [logging ticket](https://github.com/ISISComputingGroup/IBEX/issues/2162) and led to a logging build [PV Manager and Observers Logging](PV-Manager-and-Observers-Logging).

On disconnect the log is:

```
:NDW1407:CS:SB:TEMP1 = 13:52:47.265000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 27
:NDW1407:CS:SB:TEMP1 = 13:52:47.265000: CAJChannel connect changegov.aps.jca.Channel$ConnectionState[DISCONNECTED=1]
:NDW1407:CS:SB:TEMP1 = 13:52:47.265000: MultiplexChannelHandler connect changeJCAConnection [connected: false writeConnected: false channel: CAJChannel = { name = TE:NDW1407:CS:SB:TEMP1, connectionState = DISCONNECTED }]
:NDW1407:CS:SB:TEMP1 = 13:52:47.265000: ConnectionCollector connect changefalse
:NDW1407:CS:SB:TEMP1 = 13:52:47.266000: PVDirector connected or exception event false
:NDW1407:CS:SB:TEMP1 = 13:52:47.266000: PVReaderImpl connection
:NDW1407:CS:SB:TEMP1 = 13:52:47.266000: PVManagerObservable connection false
:NDW1407:CS:SB:TEMP1 = 13:52:47.266000: DisplayBlock connection false
```

The channel then is searched for:

```
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
```

You can see that as the channel is not found it is sent to progressively longer period searches. Until is reaches the 16s one I have seen it up to a 64s delay.

Then we reconnect the IOC and we get:

```
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
:NDW1407:CS:SB:TEMP1 = 13:54:43.591000: ConnectionCollector connect changetrue
:NDW1407:CS:SB:TEMP1 = 13:54:43.591000: PVDirector connected or exception event true
:NDW1407:CS:SB:TEMP1 = 13:54:43.591000: PVReaderImpl connection
:NDW1407:CS:SB:TEMP1 = 13:54:43.591000: PVManagerObservable connection true
:NDW1407:CS:SB:TEMP1 = 13:54:43.591000: DisplayBlock connection true
```

The GUI gets access rights (22) then a connection (18). I have seen it get a version number too not sure whether this is only on first connect. Then we register for value changes I think.

```
:NDW1407:CS:SB:TEMP1 = 13:54:43.591000: CreateChannel connect complete
:NDW1407:CS:SB:TEMP1 = 13:54:43.591000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 22
:NDW1407:CS:SB:TEMP1 = 13:54:43.592000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 18
:NDW1407:CS:SB:TEMP1 = 13:54:43.592000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 13:54:43.592000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 13:54:43.592000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 13:54:43.592000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 13:54:43.593000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 13:54:43.593000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 13:54:43.593000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 13:54:43.593000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 13:54:43.593000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 13:54:43.593000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 15
:NDW1407:CS:SB:TEMP1 = 13:54:43.593000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 13:54:43.593000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 13:54:43.593000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 13:54:43.602000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 13:54:43.602000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 13:54:43.602000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 13:54:43.602000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 13:54:43.602000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 15
:NDW1407:CS:SB:TEMP1 = 13:54:43.692000: PVReaderImpl valueChange
:NDW1407:CS:SB:TEMP1 = 13:54:43.692000: PVManagerObservable valueChange true
```


So I think the way it works is that there is a ladder of timers which send a search response for requested PVs onto the network (max delay appears to be 132s). If a connection is established the search is no longer requested if it isn't then it is moved down the ladder. Once the IOC replies the handshake is done and a connection is established the timing for this seems short so I don't think this is the problem.

The logic of sending the search request seems complicated maybe the problem is in here (ChannelSearchManager.timeout) or maybe if there are many items in this list it fills up the send buffer so it takes a while for it to reconnect along with the delay.
Also we found that if the system gets to many responses it tell the system to stop sending flow control (CATransport.enableFlowControl). This may also cause a problem if this search is ignored because flow control is on and then it has to wait to send it again. Maybe this along with the large number of PVs might explain slow re-connection. I have created another ticket for someone else to look.





