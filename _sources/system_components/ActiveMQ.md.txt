# ActiveMQ

[ActiveMQ](http://activemq.apache.org/) is a messaging broker that is used in a number of places throughout IBEX. Specifically it is used by:

* [The Alarm Server](Alarms)
* [The IOC Log Server](IOC-message-logging)

The GUI also hooks into ActiveMQ to read/write to all these components. Previously a version of ActiveMQ was bundled with each of these backend components. However, this was modified to be a single instance that is run through procserv when the instrument is first started. 

## Changing the ActiveMQ ports

The default ActiveMQ ports are:

* 39990 for the openwire protocol (used by JMS)
* 39991 for the STOMP protocol (used by script server)

Due to port conflicts these have been changed to those listed [here](#ibex_hard_coded_ports).

The ports used are hardcoded in a number of places so to change them they must be changed in:

* `EPICS\ISIS\ActiveMQ\master\conf\activemq.xml`
* `EPICS\CSS\master\AlarmServer\alarm_server_settings.ini`
* `EPICS\ISIS\IocLogServer\master\logserver_config.ini`
* `Client\base\uk.ac.stfc.isis.ibex.product\plugin_customization.ini`
* `Client\base\uk.ac.stfc.isis.ibex.activemq\src\uk\ac\stfc\isis\ibex\activemq\ActiveMQ.java`

It's hard to put these into a central macro as most of the configuration requires loading *.ini files.
