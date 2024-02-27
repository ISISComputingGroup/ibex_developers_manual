Nagios has a file that lists time periods that notifications will be emailed in, many are "all the time" but some are set to be within cycle only, particularly ones that notify scientists. The service will always go red in nagios web display, but not send an email alert unless the current time is within the linked timeperiod. So this file needs to be updated with new isis cycle dates as appropriate. To do this:  
* log onto control-mon.isis.cclrc.ac.uk linux machine
* cd /usr/local/nagios/etc/objects
* edit `timeperiods.cfg` with your favourite editor. At the bottom of the file, find the timeperiod called `isis_cycle` and add a new line in teh same format as the rest. We add friday before start of cycle for start and end of cycle for end of timeperiod. 
* run `sudo service nagios reload` to load changes

