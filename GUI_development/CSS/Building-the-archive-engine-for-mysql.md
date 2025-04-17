> [Wiki](Home) > [The GUI](The-GUI) > [CS Studio](GUI-CSS) > Building the archive engine for MySQL

# Setting up the MySql database

See mysql [installation for installing mysql](Installing-and-Upgrading-MySQL)

Create the database using the mysql_schema.txt in `...EPICS\CSS\master\ArchiveEngine` which originates from `org.csstudio.archive.rdb\dbd`

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

# Adding to EPICS Server

To add to epics server:

1. Get the latest build off the build server (e.g. `E:\Jenkins\workspace\ControlSystemStudio\org.csstudio.sns\repository\target\products`)
1. Place it in a folder called `css_archvive_engine`
1. Zip the folder and call it `css_archive_engine-win.x86_64.zip`
1. Copy this to ICP Binaries on to internal server
