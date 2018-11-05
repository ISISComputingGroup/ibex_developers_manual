> [Wiki](Home) > [Trouble-shooting](trouble-shooting-pages) > [Database](Database-Troubleshooting)

## What is generating all the data?

It is likely ADEL fields on some records are causing a lot of logging. You can run e.g.
```
python utils\archive_rates.py --host=ndximat
```
To see which PVs are doing this

## Is the Database Up

Look for mysqld.exe task running in task manager or for the service MQSQLXX (currently 57) running. If it is not running log files are in `...var\mysql\Data\XXX.err`. To start it as an admin start the services from the start menu then start the MYSQLXX service.

## Reducing database disc space

Database disc space is taken up by tables stored in `C:\Instrument\Var\mysql\data` the space can be regained by truncating the table. This could lose the data and will certainly remove it from the database so be careful. At various stages you will be prompted for the database password it is on the passwords page.

Run the script in:

```
<public share>\ibex_utils\installation_and_upgrade\truncate_database.bat
```

If you wish to do this manually:

1. First create a sql dump of the database:
    ```
    "c:\Program Files\MySQL\MySQL Server 5.7\bin\mysqldump.exe" -u root -p --all-databases --single-transaction --result-file=c:\data\old\ibex_backup_YYYY_MM_DD\ibex_db_sqldump_YYYY_MM_DD.sql
    ```
1. Check the file looks right and move it to the long term storage folder (`\\isis\inst$\backups$\stage-deleted\<inst>`). 
1. Truncate the tables with:
    ```
    "c:\Program Files\MySQL\MySQL Server 5.7\bin\mysql.exe" -u root -p --execute "truncate table msg_log.message;truncate table archive.sample"
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
1. Create a new service: `"C:\Program Files\MySQL\MySQL Server 5.7\bin\mysqld" --install MySQL57 --defaults-file=\"C:\Instrument\Var\mysql\my.ini\"
1. Set the user running the service: LogOn tab -> This account to `NETWORK SERVICE` no password (this removes the notes and when you click start adds them back in)
1. Start the service

