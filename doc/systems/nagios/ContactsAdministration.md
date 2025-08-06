# Nagios Contacts
## Viewing Nagios Contacts and contact groups
To view currently configured Nagios contacts:

1.  log into the Nagios web interface as `nagiosadmin`. 
2. On the left hand menu, select `Configuration` under `System`.  
3. Select either the `Contacts` Object Type to see configured contacts or `Contact Groups` to see the configured groups of contacts. 

## Editing Nagios Contacts
To edit contacts or contact groups:

1. SSH into the Nagios host using the login details available in Keeper
2. Nagios is in `/usr/local/nagios` with configuration of objects within `/usr/local/nagios/etc/objects/`
3. Within that directory, edit contacts.cfg 
4. restart the Nagios service:
    `sudo service nagios reload`
6. Check changes in the web interface as above
