# Webserver

## NDAEXTWEB3

NDAEXTWEB3 is a central Windows 2019 server, which is hosted on the FIT Hyper-V cluster, that runs a number of the web services associated with IBEX. The login credentials for this are in sharepoint. The server holds:

* The [old IBEX web dashboard (JSON_Bourne)](/webdashboard/Web-Dashboard)
* The [Automation application](/processes/git_and_github/Automation-Application)
* [MCR news](https://www.isis.stfc.ac.uk/Pages/MCR-News.aspx)
* The central proxy created [here](https://github.com/ISISComputingGroup/IBEX/issues/5112)

Most of these services can be started and stopped by the [IIS Manager](https://www.iis.net/). To access the IIS Manager, select IIS in the Server Manager, then click on Manage in the top right hand corner of that screen. 

There should be 2 sites, Dataweb and WAP, which provide the above.

If a new server is setup, then ciphers and old TLS versions may need to be disabled e.g. tls 1.0 and 1.1 as per https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/manage-ssl-protocols-in-ad-fs


## NDAEXTWEB4

NDAEXTWEB4 is similar in that it also runs on the Hyper-V cluster. This currently hosts the [PVWS](#pvws) which is a PVWS instance for the IBEX web dashboard. 

## Shadow
    
Some web services run on Shadow - see [here](Shadow) for more information. 
