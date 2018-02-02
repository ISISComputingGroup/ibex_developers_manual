[Wiki](Home) > [Trouble-shooting](trouble-shooting-pages) > [GUI](GUI-Troubleshooting) > [IOC Start/Stop List not showing](IOC-Start/Stop-List-not-showing)

If the IOC Start/Stop list is blank when the instrument is running then there is a problem with the PV serving this. The PV serving it comes from the DBSRV ioc and ultimately comes from the MySQL database. Console to the BD server:

`console -M localhost DBSVR`

should not be producing errors (pressing return creates blank lines)

Next check that the [database is up](Database-Troubleshooting).