NDAEXTWEB is a central Windows 2019 server that runs a number of the web services associated with IBEX and SECI. The login credentials for this are in sharepoint. The server holds:

* The [IBEX web dashboard](Web-Dashboard)
* The [Automation application](Automation-Application)
* [MCR news](https://www.isis.stfc.ac.uk/Pages/MCR-News.aspx)
* The SECI web dashboard
* The central proxy created [here](https://github.com/ISISComputingGroup/IBEX/issues/5112)
* WAP access to SECI web dashboard


Most of these services can be started and stopped by the [IIS Manager](https://www.iis.net/). To access the IIS Manager, select IIS in the Server Manager, then click on Manage in the top right hand corner of that screen. 

There should be 2 sites, Dataweb and WAP, which provide the above.

If a new server is setup, then ciphers and old TLS versions may need to be disabled e.g. tls 1.0 and 1.1 as per https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/manage-ssl-protocols-in-ad-fs

 