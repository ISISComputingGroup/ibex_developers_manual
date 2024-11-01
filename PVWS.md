# PVWS
(PV Web socket)

we run a PVWS instance on NDAEXTWEB3 for the [Web Dashboard](https://github.com/ISISComputingGroup/WebDashboard)

this is done with a native tomcat service following the [PVWS instructions](https://github.com/ornl-epics/pvws?tab=readme-ov-file#running-under-tomcat)

Updating
tomcat installer from https://tomcat.apache.org/download-90.cgi installed in C:\Program Files\Apache Software Foundation\Tomcat 9.0 
pvws https://github.com/ornl-epics/pvws - we are using the latest nightly .war as of 01/11/24 - to update download this and place in the tomcat dir\webapps folder and restart the service
jdk 21 from https://adoptium.net/en-GB/ installed in C:\Program Files\Eclipse Adoptium\jdk-21.0.5.11-hotspot 

