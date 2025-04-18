# Networking tools

## View Network Traffic using Wireshark

To see packets to and from the machine simply install wireshark and use. To look at packets on localhost. Install npcap (https://nmap.org/npcap/) with compatible for winpcap. Then afterwards install wireshark it should recognise ncap.
To capture network traffic:

1. Start Wireshark
1. Select capture interface (for localhost use Npcap Loopback Adapter)
1. Click the fin to start, stop button to stop and fin with reload to restart.
1. It is often useful to filter your traffic. Filters I have used:

    - `(data.data contains "TE:NDW1407:CS:SB" || data.data contains 00:06:00:08)` look at all packets containing block on my machine or the EPICS search for channel message
    - `udp.dstport == 55691 || udp.srcport == 55691` get all UDP data from and to port 55691
    - `tcp.srcport == 51679` get all tcp data from port 51679

## Look at Open Ports

To see open ports as an admin type:
```
    netstat -abon
```