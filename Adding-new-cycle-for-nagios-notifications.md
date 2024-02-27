Nagios has a file that lists time periods that notifications will be emailed in, many are "all the time" but some are set to be within cycle only, particularly ones that notify scientists. The service will always go red in nagios web display, but not send an email alert unless the current time is within the linked timeperiod. So this file needs to be updated with new isis cycle dates as appropriate. To do this:  
* log onto control-mon.isis.cclrc.ac.uk linux machine
* cd /usr/local/nagios/etc/objects
* edit `timeperiods.cfg` with your favourite editor. At the bottom of the file, find the timeperiod called `isis_cycle` and add a new line in the same format as the rest. We use friday before start of user run for our start time - the web page https://www.isis.stfc.ac.uk/Pages/Beam-Status.aspx lists start of user run which is the tuesday, so count back 4 days from that  
* run `sudo service nagios reload` to load changes

