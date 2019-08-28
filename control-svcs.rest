control-svcs.isis.cclrc.ac.uk

To log on, see usual username/password page

The machine runs various services, such as epics gateways. These run under the "epics" user id so 
```
sudo su - epics
```
and give your "isissupport" password when prompted

Depending on what you need to do, you may need to modify system init scripts to start services at boot time.  

# Webserver is down

If the webserver serving [http://control-svcs.isis.cclrc.ac.uk/](http://control-svcs.isis.cclrc.ac.uk/) is down, it can be restarted with the following standard commands (these commands are also used to start/auto-restart any other linux service, substituting `httpd` with the name of the appropriate service):
```
sudo systemctl start httpd
sudo systemctl enable httpd
```

If you need to stop the service first use
```
sudo systemctl stop httpd
```