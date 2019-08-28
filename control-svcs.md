control-svcs.isis.cclrc.ac.uk

To log on, see usual username/password page

The machine runs various services, such as epics gateways. These run under the "epics" user id so 
```
sudo su - epics
```
and give your "isissupport" password when prompted

Depending on what you need to do, you may need to modify system init scripts to start services at boot time.  

# Webserver is down

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