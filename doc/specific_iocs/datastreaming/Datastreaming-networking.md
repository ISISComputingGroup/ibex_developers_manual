# Data streaming: networking

The data streaming system requires several items to be on the same network:
- `kafka_dae_control` (speaks UDP to streaming control board)
- `event_udp_to_kafka` (recieves UDP from detector modules, converts and forwards them to Kafka)
- Streaming control board
  - Control port which `kafka_dae_control` communicates with
  - Status packet port which UDP headers come out of (which get processed by `event_udp_to_kafka`)
- Monitors
- Detectors

The current standard for network addressing is:
- `192.168.1.1` is the address of the streaming server, which will currently host both `kafka_dae_control` and `event_udp_to_kafka` processes
  - It is possible, in future, that these two processes may run on different servers and therefore with different IPs
- `192.168.1.250` to be the streaming control board's control port
- `192.168.1.251` to be the streaming control board's status-packet port
- `192.168.1.252` to be streaming monitors
- The rest of the range to be streaming detectors

:::{note}
All of these IP addresses are on a private network which is **NOT** the same as the usual NDX/NDH private network.
This is a private network only used by the streaming server and streaming hardware. It therefore does not conflict with IP addresses on the NDX/NDH instrument private network.
:::
