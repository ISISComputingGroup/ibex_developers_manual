This is what I think I know about how the layers under PVMAnagerObservable work to reconnect to a PV. This was part of the [logging ticket](https://github.com/ISISComputingGroup/IBEX/issues/2162) and led to a logging build [PV Manager and Observers](PV-Manager-and-Observers).

Logged re connections look like:

```
:NDW1407:CS:SB:TEMP1 = 16:51:54.837000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 0
:NDW1407:CS:SB:TEMP1 = 16:51:54.837000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 22
:NDW1407:CS:SB:TEMP1 = 16:51:54.837000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 18
:NDW1407:CS:SB:TEMP1 = 16:51:54.837000: CAJChannel connect complete changegov.aps.jca.Channel$ConnectionState[DISCONNECTED=1]
:NDW1407:CS:SB:TEMP1 = 16:51:54.837000: CATransport resubscribe subscriptions request
:NDW1407:CS:SB:TEMP1 = 16:51:54.838000: CAJChannel connect changegov.aps.jca.Channel$ConnectionState[CONNECTED=2]
:NDW1407:CS:SB:TEMP1 = 16:51:54.838000: MultiplexChannelHandler connect changeJCAConnection [connected: true writeConnected: false channel: CAJChannel = { name = TE:NDW1407:CS:SB:TEMP1, connectionState = CONNECTED }]
:NDW1407:CS:SB:TEMP1 = 16:51:54.838000: ConnectionCollector connect changetrue
:NDW1407:CS:SB:TEMP1 = 16:51:54.838000: PVDirector connected or exception event true
:NDW1407:CS:SB:TEMP1 = 16:51:54.838000: PVReaderImpl connection
:NDW1407:CS:SB:TEMP1 = 16:51:54.838000: PVManagerObservable connection true
:NDW1407:CS:SB:TEMP1 = 16:51:54.838000: DisplayBlock connection true
:NDW1407:CS:SB:TEMP1 = 16:51:54.838000: CreateChannel connect complete
:NDW1407:CS:SB:TEMP1 = 16:51:54.839000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 22
:NDW1407:CS:SB:TEMP1 = 16:51:54.839000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 18
:NDW1407:CS:SB:TEMP1 = 16:51:54.839000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 22
:NDW1407:CS:SB:TEMP1 = 16:51:54.839000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 18
:NDW1407:CS:SB:TEMP1 = 16:51:54.840000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 16:51:54.840000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 16:51:54.840000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 16:51:54.841000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 15
:NDW1407:CS:SB:TEMP1 = 16:51:54.841000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 16:51:54.841000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 16:51:54.841000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 16:51:54.841000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 16:51:54.841000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 16:51:54.841000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 16:51:54.842000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 16:51:54.850000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 15
:NDW1407:CS:SB:TEMP1 = 16:51:54.850000: CAResponseHandler id (18 is connection, 23 response, 1 reconnect) 1
:NDW1407:CS:SB:TEMP1 = 16:51:54.939000: PVReaderImpl valueChange
:NDW1407:CS:SB:TEMP1 = 16:51:54.939000: PVManagerObservable valueChange true
```

The GUI gets a version message (0), followed by access rights (22) then a connection (18).