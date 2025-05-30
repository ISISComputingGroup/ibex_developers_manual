# Adding new cycle for Nagios notifications

Nagios has a file that lists time periods that notifications will be emailed in, many are "all the time" but some are set to be within cycle only, particularly ones that notify scientists e.g. muon pulse width or kicker check. The service will always go red in nagios web display and say that notifications are enabled, but not send an email alert unless the current time is within the linked timeperiod (it actually queues up the email and sends it once a timeperiod starts, hence it claims they are enabled). So this file needs to be updated with new isis cycle dates as appropriate. To do this:  
* log onto control-mon.isis.cclrc.ac.uk linux machine
* cd /usr/local/nagios/etc/objects
* edit `timeperiods.cfg` with your favourite linux editor. At the bottom of the file there is a timeperiod called `isis_cycle` and add a new line to this in the same format as the rest of the define. We use Friday before start of user run for our start time - the web page https://www.isis.stfc.ac.uk/Pages/Beam-Status.aspx lists start of user run which is the Tuesday, so count back 4 days from that  
* run `sudo service nagios reload` to load changes - you will be prompted for the password of the account you are logged in as

