> [Wiki](Home) > [The GUI](The-GUI) > [CS Studio](GUI-CSS) > Building the alarm server for MySQL

# Setting up the JMS and the MySql Database

The Java Message Service is implemented using ActiveMQ

Download ActiveMQ from Apache.

Start ActiveMQ `bin\activemq.bat` - this needs to be running for the alarm server to work.

Use an new database or an existing one, configure the database using the ALARM_MYSQL.sql and MYSQL_USER.sql files in org.csstudio.alarm.beast\dbd

# Configuring the alarm handler

This is all assuming the presence of a PV record like:

```
record(ai, "simple:value1")
{
    field(VAL, 1)
    field(HIHI,18)
    field(HIGH,15)
    field(LOW,5)
    field(LOLO,2)
    field(HHSV,"MAJOR")
    field(HSV,"MINOR")
    field(LSV,"MINOR")
    field(LLSV,"MAJOR")
}
```

Create an XML file with a name like alarm_config.xml.

It should contain something like:

```
    <config name="mytestalarm">
        <component name="System1">
            <component name="Subsys1">
                <guidance>
                    <title>My Test Alarm</title>
                    <details>Some details here</details>
                </guidance>
                <pv name="simple:value1">
                    <description>Test PV alarm</description>
                    <annunciating>false</annunciating>
                </pv>
            </component>
        </component>
    </config>
```

Create a ini file with a name like alarm_settings.ini.

It should contain something like:   

```    
    org.csstudio.alarm.beast/rdb_url=jdbc:mysql://localhost/alarm
    org.csstudio.alarm.beast/rdb_user=alarm
    org.csstudio.alarm.beast/rdb_password=$alarm
    org.csstudio.alarm.beast/rdb_schema=

    # Logging preferences
    org.csstudio.logging/console_level=CONFIG
    org.csstudio.logging/jms_url=failover:(tcp://localhost:61616)
```

Where localhost may need to be replaced by your server(s) details.

In Eclipse, go to org.csstudio.alarm.beast.configtool and open `!AlarmConfigTool.product`.
Add the following settings to the "Launching" tab under "Program Arguments" and run as a normal RCP application:

```
    -pluginCustomization full_path/alarm_settings.ini -import -root mytestalarm -file full_path/alarm_config.xml
```

To remove use -delete mytestalarm (or what ever the config name is)

To modify use -modify

To retrieve the current settings use -export filename

Alternatively, export the configuration tool without the "Program Arguments" and pass everything as command line args.

Note: in Eclipse, export means creating a standalone executable file. 
    
# Running the Alarm Server

In Eclipse, go to org.csstudio.alarm.beast.server and open AlarmServer.product.

Add the following settings to the "Launching" tab under "Program Arguments" and run as a normal RCP application:

```
    -consoleLog -root mytestalarm -pluginCustomization full_path/alarm_settings.ini
```

There is an example ini file in org.csstudio.alarm.beast.server called plugin_customization.ini.

Alternatively, leave the "Program Arguments" blank and pass the arguments via the command line.

Either start the RCP application from Eclipse or export the alarm server and run it from the command line.
