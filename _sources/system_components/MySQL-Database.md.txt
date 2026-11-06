# MySQL database

```{toctree}
:glob:
:titlesonly:
:maxdepth: 1
:hidden:

mysql/*
```

```{seealso}
See also [troubleshooting notes](mysql/Database-Troubleshooting).
```

## General Command Line Commands
Using the MySQL Command Line Client

### List the databases available
```
show databases;
```

### Set the database to use
```
use database_name;
```

### List the tables in the current database
```
show tables;
```
### Display data from a table
```
select * from table_name;
```

## The Tables

### iocdb
* `ioc` - the list of all IOCs
* `iocenv` - lists the environment variables for each IOC
* `iocrt` - shows which IOCs are running
* `pvinfo` - information about each PV
* `pvs` - the list of PVs and their type

### exp_data
* `experiment`
* `experimentteams`
* `role`
* `user`

## Configuration

The mysql database runs as a service; details can be accessed by running `services.msc`. It will show in the properties of the service where the configuration file is. In general this should be in `C:\Instrument\var\mysql\my.ini` (however on some systems it is in `c:\ProgramData\MySQL\MySQL Server 5.6\my.ini`). The contents of this file should be for the `server_type=3` this sets up the memory etc to be of an acceptable value. The most telling parameter in this file for memory management is probably `innodb_buffer_pool_size=512M`.

To restart mysql right click on the service and click restart. Note that a running IBEX instrument seems to have some problems with this; so will also need to be restarted (block server said `Error executing command on database: Unable to get connection from pool: `).


## Change Password:

Update the sql server password using: "c:\Program Files\MySQL\MySQL Server 5.7\bin\mysqladmin.exe" -u root -p password
It will then prompt for the old password followed by the new password which is found in the passwords doc.

