> [Wiki](Home) > [The Backend System](The-Backend-System) > [System components](System-components) > The MySQL database 

# General Command Line Commands
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

# The Tables

### iocdb
* ioc - the list of all IOCs
* iocenv - lists the environment variables for each IOC
* iocrt - shows which IOCs are running
* pvinfo - information about each PV
* pvs - the list of PVs and their type

### exp_data
* experiment
* experimentteams
* role
* user