# Helium Level Monitoring

```{note}
This is not a typical EPICS IOC. 

For details & background about the HLM Project as a whole, see [here](https://github.com/ISISNeutronMuon/HLM_PV_Import/wiki/Intro-to-the-HLM-Project).
```

```{toctree}
:glob:
:titlesonly:
:maxdepth: 1
:hidden:

hlm/*
```
 
**HLM PV Import** - service and manager for updating the [HLM Database](https://github.com/SampleEnvironment/He-Management/wiki#helium-level-monitoring-database) with PV data from the [Helium Recovery PLC](../plcs/Helium-Recovery-PLC) ([Omron FINS](../plcs/Omron-FINS)). 

**HLM View** - data display website running with Django on the HLM server machine (for more info check [deployment notes](hlm/HLM-Web-Server-deployment))



### Links
* [HLM PV Import Wiki](https://github.com/ISISNeutronMuon/HLM_PV_Import/wiki)
* [HLM GAM Database](https://github.com/SampleEnvironment/He-Management/wiki#helium-level-monitoring-database) - the gas management database PV values are being imported into as object measurements
* [Helium Recovery PLC](../plcs/Helium-Recovery-PLC) - [FINS PLC](../plcs/Omron-FINS) used for monitoring various parameters related to the helium gas recovery system
* [HLM Project Sharepoint](http://www.facilities.rl.ac.uk/isis/projects/heliummgmt/_layouts/viewlsts.aspx?BaseType=1) - project management docs and other useful info
* [HLM View](https://github.com/ISISNeutronMuon/HLM_View) - data display website repo

## Jenkins

Automated building & testing is running on the IBEX Jenkins instance as the ["HLM PV Import" multi-branch pipeline job](https://epics-jenkins.isis.rl.ac.uk/job/HLM%20PV%20Import/). 

It is running on **NDW1757** and using the Python in `C:/HLM_PV_Import/python.exe`. To update Python, manually download a newer version and install it in there.

The `Jenkinsfile` is in the project root, together with the `setup_jenkins_settings_file.py` script required (and called by the Jenkinsfile) when running the tests.

**Notes**: 
* In `requirements.txt`, make sure to keep `cryptography` at `3.1.1` to avoid build errors due to newly added Rust dependencies.
* Use `call "myvenv\\Scripts\\activate.bat"` instead of only `myvenv\\Scripts\\activate.bat` in the Jenkinsfile bat commands or it won't work.


