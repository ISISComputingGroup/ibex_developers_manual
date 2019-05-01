> [Wiki](Home) ▸ [[BlockServer]] ▸ **BlockServer Structure**

> [Wiki](Home) ▸ [[High Level Architectural Design]] ▸ **BlockServer Structure**

This document is intended to outline the internal structure of the BlockServer for reference by future developers. Please be aware that the BlockServer is a work in progress and as such this document is liable to change.

# Overview

The BlockServer's main responsibility is to look after configurations and their associated files. It can be used to read/write
to both the active configuration on the instrument and other potential configurations in the filesystem. It also contains a
filewatcher to ensure that any manual changes to configurations are correctly handled. Below is an UML overview of the most 
significant parts:

![Full UML](backend_system/blockserver/images/Block-Server-Configuration-Rules/full_uml.png)

# Channel Access

The BlockServer uses the pcaspy Python module to implement channel access. There are two main means of implementing PVs in the
BlockServer, static PVs and dynamic PVs:

* Static PVs are created in a dictionary at startup and are intercepted by subclassing the Driver class and implementing the read()
  and write() methods. Most of the PVs the BlockServer uses are written like this and the method is well documented in the pcaspy 
  documentation_. Note that if you are monitoring this PV for changes, you need to call setParam() followed by updatePVs() in the blockserver to propagate this change to the monitors. You can check whether this is working properly by putting a `camonitor` on the PV in question and checking that it automatically updates when the PV value is changed.

.. _documentation: http://pcaspy.readthedocs.org/en/latest/

* Dynamic PVs are more complex and are required for serving PVs for each inactive configuration, the names of which are not known
  until startup. To do this we have created our own pcaspy server called CAServer that can be found in 
  inst_server\\server_common\\channel_access_server.py. This server has a number of simple methods to register new PVs within it's own 
  dictionary and pass them to channel access when requested. The server also assumes that all PVs will be in a string format, which is
  currently a good assumption. All dynamic PVs are created by the ConfigListManager as they relate to the inactive configs/components
  that are listed in that class. A simple diagram of this relationship is shown below:

![CA UML](backend_system/blockserver/images/Block-Server-Configuration-Rules/channel_access_uml.png)
   
A simple example of both the static and dynamic PVs is located in inst_server\\BlockServer\\blockserver_docs\\resources\\pcaspy_example.

# Configuration Servers

There are two Configuration Server Manager classes. The ActiveConfigHolder class holds the currently configuration and deals with the
JSON communication between the BlockServer PVs and what modifications to make for the configuration. It also controls the running of 
the IOCs. This class is a subclass of ConfigHolder which is used to hold the basic details about the configurations as
well as save/load them to disk. Most, if not all, of the individual get/set methods in the ConfigHolder are being replaced by catch-all
get_config_details() and set_config_details(). A reduced description of the classes is given below:

![Config Server UML](backend_system/blockserver/images/Block-Server-Configuration-Rules/config_servers_uml.png)
	
# Configurations

The ConfigHolder class does most of the implementation for the specifics of editing a configuration making sure that all parts of the 
configuration follow the correct rules. It holds a Configuration object which does very little other than contain all the relevant 
configuration details. There are also small container classes to hold separate Blocks, Groups, IOCs and MetaData.

The ConfigHolder also uses the methods from the static class ConfigurationFileManager, which deal with the specifics of the file system
including version control of configuration files. This FileManager class uses a ConfigurationXmlConverter object to help convert into 
the xml used for saving and loading.

![Configs UML](backend_system/blockserver/images/Block-Server-Configuration-Rules/configs_uml.png)
	
# Inactive Configs

The ConfigListManager class is responsible for the details of all of the configurations, both the active one and the inactive ones, 
on the file system. When the BlockServer is first started this class will search through the configurations folder and do the following
for each config:

1. Check folders hold the expected files
2. Check the xml files against the schema (using the static ConfigurationSchemaChecker class)
3. Load the files into a dummy InactiveConfigHolder
4. Create a PV name based on the configuration name but ensuring only valid chars
5. Create a PV for the configuration that gives all data on it
6. For each component the configurations that contain it are noted in a dictionary

When modifications are made to configurations through the BlockServer PVs these steps are repeated for the modified configuration.

The ConfigListManager is also responsible for ensuring that configurations are correctly deleted. When a configuration is deleted via 
the DELET_CONFIG or DELETE_COMP PVs there will be a check that the any active configurations/components are not being deleted. If the 
configuration is safe to delete the corresponding PVs are unregistered and the files are removed from both the file system and version 
control.

![Config List UML](backend_system/blockserver/images/Block-Server-Configuration-Rules/config_list_uml.png)
