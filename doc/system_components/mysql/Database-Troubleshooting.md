# Database Troubleshooting

## What is generating all the data?

It is likely ADEL fields on some records are causing a lot of logging. You can run e.g.
```
python utils\archive_rates.py --host=ndximat
```
To see which PVs are doing this

## Is the Database Up

Look for mysqld.exe task running in task manager or for the service MYSQLXX (currently 80) running. If it is not running log files are in `...var\mysql\Data\XXX.err`. To start it as an admin start the services from the start menu then start the MYSQLXX service.

{#database_troubleshooting_reduce_space}
## Reducing database disc space (Database truncate)

The database resides on the `Var` instrument disk volume, so can be responsible for this looking full; however there are also IOC log files on this volume that may instead be, or also be, the cause.

[Always do instruments that are in warning in this Nagios list for their Archive Db](https://control-mon.isis.cclrc.ac.uk/nagios/cgi-bin/status.cgi?servicegroup=mysql_db&style=detail)

First check with the scientists it is OK to go ahead - send an email to the `instrument-` specific contact list from https://sparrowhawk.nd.rl.ac.uk/footprints/contacts.html#instemail with something like
```
Subject: Archiving of old logging information on NDX<instrument> to free up disk space

Dear <instrument>,

We would like to do a bit of system maintenance on NDX<instrument> – this is to backup and then archive some diagnostic information in databases that has started to occupy a lot of space. It takes around half an hour to an hour to do this, though we don’t necessarily need to shutdown IBEX during this process, but as the system will pause logging blocks etc. during the time it is best that either:
- we shutdown ibex for the duration of the backup, or
- the instrument is in SETUP state and not logging anything critical

Please let us know:
- when it would be convenient to do this backup
- if it is OK to shutdown IBEX and then restart afterwards
- if the instrument is currently RUNNING, any specific instructions e.g. end() run and then begin() a new one after backup 

Regards,

ISIS Experiment Controls
```
 
Database disc space is taken up by tables stored in `C:\Instrument\Var\mysql\data` the space can be regained by truncating the table. This could lose the data and will certainly remove it from the database so be careful. At various stages you will be prompted for the database password it is on the passwords page. This can be done while the EPICS back-end on the instrument is up, but should not be done while data is being collected as some data points may get lost during the process.

Run the script in:

```
<public share>\ibex_utils\installation_and_upgrade\truncate_database.bat
```

Note that you may need the full name of the public share root.

## _If you wish to do this manually:_

1. First create a folder in `\\isis\inst$\Backups$\stage-deleted\<inst>\YYYY_MM_DD` - you need to do this from a cmd window not from windows explorer, this is because the file permissions allow create but not delete, but the way windows explorer creates a directory involves a delete. e.g. for LET
```
md  \\isis\inst$\Backups$\stage-deleted\ndxLET\ibex_backup_2023_09_04
```
1. Now create an SQL dump of the database:
    ```
    "c:\Instrument\Apps\MySQL\bin\mysqldump.exe" -u root -p --all-databases --single-transaction --result-file=\\isis\inst$\Backups$\stage-deleted\<inst>\ibex_backup_YYYY_MM_DD\ibex_db_sqldump_YYYY_MM_DD.sql
    ```
1. Truncate the tables with:
    ```
    "c:\Instrument\Apps\MySQL\bin\mysql.exe" -u root -p --execute "truncate table msg_log.message;truncate table archive.sample"
    ```

NB Originally this was the message and sample tables bumped to a directory in here, if you are looking for older data.

## Moving the Table Data Files

If the tables data file were created in the wrong place they can be moved using the following.

1. Open services.msc
1. Ensure that the mysql service is running under `NETWORK SERVICE` and copy the command line
1. Stop mysql service
1. Open command line in admin mode
1. Remove the old service: `"C:\Program Files\MySQL\MySQL Server 5.7\bin\mysqld" --remove MySQL57`
1. Move the data file from `C:\ProgramData\MySQL\data` to `C:\Instrument\Var\mysql\data`
1. Copy the my.ini file into `C:\Instrument\Var\mysql\` from `EPICS\SystemSetup`
1. Create a new service: `"C:\Instrument\Apps\MySQL\bin\mysqld" --install MySQL80 --defaults-file=\"C:\Instrument\Var\mysql\my.ini\"
1. Set the user running the service: LogOn tab -> This account to `NETWORK SERVICE` no password (this removes the notes and when you click start adds them back in)
1. Start the service

## Database fails to start I need to Recreate it

The commands for recreating the database are in the ibex [install script in the task `_install_latest_mysql8`](https://github.com/ISISComputingGroup/ibex_utils/blob/master/installation_and_upgrade/ibex_install_utils/install_tasks.py) this is the source. The rough steps are:

1. Stop mysqld processes
1. Move the database `../instrument/var/mysql` to `old`
1. create an empty  `c:/instrument/var/mysql` directory 
1. Recreate the database files: `c:\Instrument\Apps\MySQL\bin\mysqld.exe --datadir="c:/instrument/var/mysql/data" --initialize-insecure --console --log-error-verbosity=3`
1. Start the mysql service.
1. Set the database password with: `c:\Instrument\Apps\MySQL\bin\mysql.exe -u root -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '<password>';FLUSH privileges;"`
1. Run the schema setup in an epics terminal: `c:\instrument\Apps\EPICS\systemsetup\config_mysql.bat`
1. Restart the epics server
