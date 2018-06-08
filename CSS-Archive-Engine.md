> [Wiki](Home) > [The Backend System](The-Backend-System) > [System components](System-components) > [CSS Archive Engine](CSS-Archive-Engine)

# Archive Engine

The Archive Engine is part of CSS and is used to archive PV values. Note that most facilities use the [Archive Appliance](https://slacmshankar.github.io/epicsarchiver_docs/index.html) as the Archive Engine (specifically MySQL) was found to be slow at millions of PVs. As we don't have that many PVs we have continued to use the Archive Engine.

The code for the Archive Engine is [here](https://github.com/ControlSystemStudio/cs-studio/tree/master/applications/archive). We have our own fork of this [here](https://github.com/ISISComputingGroup/cs-studio) but in general the two should be in sync as much as possible as [discussed](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/GUI-CSS#source-code).

We have a built version of the ArchiveEngine at `\\shadow.isis.cclrc.ac.uk\ICP_Binaries$\CSS` which gets copied into `EPICS\CSS\master\css-win.x86_64` during the build. The built version is manually updated to keep it in line with the cs-studio version, see [updating the archive engine](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/CSS-Archive-Engine#updating-the-archive-engine).

We actually run two archive engines on each instrument:

1. Block archive, this just archives blocks and is restarted whenever the configuration (and blocks) change.
1. Instrument archive, this is just started once and archives all PVs marked with the archive info setting which are in the database. See [configuration](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/CSS-Archive-Engine#configuration).

To run these archive engines there are two batch files in `EPICS\CSS\master\ArchiveEngine` called `start_block_archiver` and `start_inst_archiver`. They can also both be accessed via procserv as **ARBLOCK** and **ARINST**.

Each Archive Engine can be accessed via a web browser when running. This is what the [web dashboard](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Web-Dashboard) is based on.

# Prerequisites

The archive engine stores values in a MySQL database. To set the database up see [here](Installing-and-Upgrading-MySQL).

Create the database using the mysql_schema.txt in `...EPICS\CSS\master\ArchiveEngine` which originates from `org.csstudio.archive.rdb\dbd`

# Configuration



# The Archive Configuration Tool
The startup for `arinst` and `arblock` create configs for the archive engine which look like:

```
    <engineconfig>
        <group>
             <name>Testing</name>
                 <channel>
                     <name>test:rand</name>
                     <period>1.0</period>
                     <monitor/>
                 </channel>
        </group>
    </engineconfig>
```

There are settings in mysql_settings_block.ini in `EPICS\CSS\master\ArchiveEngine` and similar for the instrument archiver. If running from Eclipse set these in org.csstudio.archive.config.rdb and open ArchiveConfigTool.product.

Add the following settings to the "Launching" tab under "Program Arguments" and run as a normal RCP application:

```
    -engine my_engine -pluginCustomization full_path_here\my_settings.ini -config full_path_here\my_config.xml -import
```

Or export the configuration tool without the "Program Arguments" and pass everything as command line args.

Note: in Eclipse, export means creating a standalone executable file.

List of args:

```
    -engine my_engine        : Engine Name
    -config my_config.xml    : XML Engine config file
    -export                  : export configuration as XML
    -import                  : import configuration from XML
    -delete_config           : Delete existing engine config
    -description 'My Engine' : Engine Description
    -host my.host.org        : Engine Host
    -port 4812               : Engine Port
    -replace_engine          : Replace existing engine config, or stop?
    -steal_channels          : Steal channels from other engine
    -rdb_url jdbc:...        : RDB URL
    -rdb_user user           : RDB User
    -rdb_password password   : RDB Password
    -rdb_schema schema       : RDB schema (table prefix), ending in '.'
```

When replacing an existing configuration on the server it is necessary to add `-replace_engine -steal_channels`

# Updating the Archive Engine

As our version of the Archive Engine is no different to CSS we can just copy their builds to get the latest version. To do this:

1. Download the build from [CSS](https://ics-web.sns.ornl.gov/css/nightly/). 
1. Place it in a folder called `css_archvive_engine`
1. Zip the folder and call it `css_archive_engine-win.x86_64.zip`
1. Copy this to ICP Binaries on to internal server

## Editing the Archive Engine

In some cases we may want to build the archive engine ourselves. For example, if we want to edit the code. To do this:

# The Archive Engine

In Eclipse, go to org.csstudio.archive.engine and open `ArchiveEngine.product`.

Add the following settings to the "Launching" tab under "Program Arguments" and run as a normal RCP application:

```
    -engine my_engine -pluginCustomization full_path_here\my_settings.ini
```

The CS-Studio manual says that the port is required for consistency tests but I have found this to cause problems.

Alternatively, leave the "Program Arguments" blank and edit the plugin_customization.ini in the project to contain the settings.

If creating a standalone executable, leave "Program Arguments" blank and use command line arguments instead. 

By using the MySQL command line it should be possible to see the database filling up (it appears the update rate is ~30 seconds, so you might  not see any changes initially).

```
    mysql> use archive;
    mysql> select * from sample;
```

# Connecting from CS-Studio GUI
If you are using a pre-built package, say from the SNS, then in a running instance, go to "Edit->Preferences->CSS Applications->Trends->Data Browser" and add your server.

If you are creating your own CS-Studio application, then you probably need to do something like the following:

* Include org.csstudio.archive.reader.rdb and its dependencies in your CS-Studio product.

* Create an ini file called plugin_customization.ini and add it to your "product" workspace. It will need to contain something like the following:

```
    org.csstudio.archive.reader.rdb/url=jdbc:mysql://localhost/archive
    org.csstudio.archive.reader.rdb/user=report
    org.csstudio.archive.reader.rdb/password=$report
    org.csstudio.archive.reader.rdb/schema=

    org.csstudio.trends.databrowser2/url=jdbc:mysql://localhost/archive
    org.csstudio.trends.databrowser2/archives=RDB|1|jdbc:mysql://localhost/archive
```

* In the main product file (for example: CSS_ISIS.product) click on the "Launching" tab under "Program Arguments" put:

```
    -engine my_engine
```

* Run as a normal RCP application.

# Creating a configuration

The Archive Configuration Tool bundle includes two batch files: one for retrieving the current configuration; and, one for setting a new configuration.

The mysql_settings.ini file contains the database settings and may need to be altered depending on your setup.

There is a demonstration configuration file called icap_test_config.xml which can be used as a starting point for your own configuration. 

Alternatively, you can use the get_config.bat file to retrieve the current settings, the bat file will need to be edited to set the correct engine name to retrieve.

To send a configuration to the database, use the set_config.bat file.

This file will need to be edited to point at the correct engine (currently set to icap_test_engine) and to use the correct configuration file (currently set to icap_test_config.xml).
