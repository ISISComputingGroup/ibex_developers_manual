{#controlsvcs}
# `control-svcs`

control-svcs.isis.cclrc.ac.uk

To log on use an SSH client such as Putty and see usual username/password page for credentials.

The machine runs various services, including: 
* EPICS gateways for running data between the halls
* ArchiveEngine for storing central data for beam currents etc. 
* Git repositories for storing configs etc. (see https://control-svcs.isis.cclrc.ac.uk/git/)
* [Experiment database populator](https://github.com/ISISComputingGroup/ExperimentDatabasePopulator)
* The [Alert Relay](control_svcs/Alert-Relay)
* [Isis info slack channel bots](/webdashboard/ISIS-Info-Slack)

None of these services are crucial for running instruments to continue taking data. The services log to `\home\var\` and can be restarted by killing the process as they run in procserv.

These run under the "epics" user id so 
```
sudo su - epics
```
and give your "isissupport" password when prompted

Depending on what you need to do, you may need to modify system init scripts to start services at boot time.  

## Troubleshooting

### Whole VM is down

The best bet at diagnosing/fixing this is to [download VM Manager console](https://stfc365.sharepoint.com/sites/ISISExperimentControls/_layouts/15/Doc.aspx?sourcedoc=%7B289EA683-832D-4CC5-936B-A409AB379AF7%7D&file=vmm%20console.docx&action=default&mobileredirect=true&DefaultItemOpen=1) - ask Facilities IT if you have problems. The machine has appeared to be down in the past (unable to ping etc.) but has actually been running OK (access via VM console) - this seems to happen if the VM is "live migrated" to a new node on the cluster. Facilities IT are now aware of this and should inform us first, after the migration we may need to reboot to restore network connectivity.   

### Webserver is down

Log onto control services and check if the webserver service is running using
```
sudo systemctl status httpd
```

If it is down, it can be restarted with the following standard commands (these commands are also used to start/auto-restart any other linux service, substituting `httpd` with the name of the appropriate service):
```
sudo systemctl start httpd
sudo systemctl enable httpd
```

If you need to stop the service first use
```
sudo systemctl stop httpd
```

The logs are located in `/var/log/httpd` which may be useful for troubleshooting if a simple restart does not solve the issue.

### Gateways unavailable / Beam Logger details not updating

If there is an issue with the gateway (i.e. Beam status PVs cannot not be found or are showing outdated values)

`ssh isissupport@control-svcs`

`ps -ux -U epics`

Depending on which gateway you are looking for, please look for the following where \<GATEWAY\> is either gateway_R55, gateway_R80 or gateway_R2.

`COMMAND: ../support/gateway/master/bin/linux-x86_64/gateway -pvlist /home/epics/EPICS/gateway/gwsite.pvlist -access /home/epics/EPICS/gateway/gwsite.acf -putlog /home/epics/var/logs/<GATEWAY>/putlog.log`

`sudo kill -9 <PID>`


## Further Information

```{toctree}
:glob:
:titlesonly:

control_svcs/*
```
