The three NGS power supplies for the muon front end are controlled via TCPIP but hidden behind a dLink firewall box located in the cabinet to the left. Two of the supplies control SEPTUMA and SEPTUMC, with one (currently the one in the middle) the spare. All the power supplies are accessed on the private network on the same IP port (10001), but the firewall box port forwards so they appear externally under ports 10001,10002,10003 The firewall only allows access from MUONFE to the supplies. The firewall has a web interface for management. Login details for the firewall box are on the sharepoint access page

From top to bottom the supplies are

|Supply | Internal IP  |   gateway     |      external port| external IP |
|------ | ------------- | -----------| -------------|    --------|
|SEPTUMA | 192.168.10.10  |  192.168.10.1  |   10001| firewall IP |
|SPARE | 192.168.10.11  |  192.168.10.1   |  10002| firewall IP |
|SEPTUMC | 192.168.10.12 |   192.168.10.1  |   10003| firewall IP |

# Swapping a power supply

If the spare is used, you could either change its IP address to that of the replaced supply (no IOC changes required) or change the port number used by the IOC whichever is easier. Changing IP address is in the advanced network menu and you need to rotate the control to move numbers up and down.  
