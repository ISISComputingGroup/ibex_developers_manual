> [Wiki](Home) > [The Backend System](The-Backend-System) > [System components](System-components) > [ActiveMQ](ActiveMQ)

[ActiveMQ](http://activemq.apache.org/) is a messaging broker that is used in a number of places throughout IBEX. Specifically it is used by:

* [The Alarm Server](Alarms)
* [The IOC Log Server](Ioc-message-logging)
* [The Script Server Proxy](ISIS-Proxy) _(OUTDATED: Nicos has been updated to use ZeroMQ. These changes have been merged into our latest ISIS Nicos repository, which eliminates the need for an ISIS proxy.)_

The GUI also hooks into ActiveMQ to read/write to all these components. Previously a version of ActiveMQ was bundled with each of these backend components. However, this was modified to be a single instance that is run through procserv when the instrument is first started. 

# Changing the ActiveMQ ports

The default ActiveMQ ports are:

* 61616 for the openwire protocol (used by JMS)
* 61613 for the STOMP protocol (used by script server)

Due to port conflicts these have been changed to:

* 39990 for openwire
* 39991 for STOMP

The ports used are hardcoded in a number of places so to change them they must be changed in:

* EPICS\ISIS\ActiveMQ\master\conf\activemq.xml
* EPICS\CSS\master\AlarmServer\alarm_server_settings.ini
* EPICS\ISIS\IocLogServer\master\logserver_config.ini
* EPICS\ISIS\ScriptServer\nicos-core\master\ISIS_script_server\client_connection\Stomp\stomp_connection.py
* Client\base\uk.ac.stfc.isis.ibex.product\plugin_customization.ini
* Client\base\uk.ac.stfc.isis.ibex.activemq\src\uk\ac\stfc\isis\ibex\activemq\ActiveMQ.java

It's hard to put these into a central macro as most of the configuration requires loading *.ini files.
