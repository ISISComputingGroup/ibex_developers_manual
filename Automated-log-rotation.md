# Automated log rotation

IBEX logs are rotated by a script called `logrotate.py` in `C:\instrument\apps\epics\utils\logrotate.py`. This script is called nightly by a windows scheduled task. 

Currently, for all files not modified within the last 10 days, it:
- Deletes them if they are console logs
- Moves them to `stage-deleted` otherwise


The scheduled task is added/recreated as an install step in `ibex_utils` under `server_tasks`.

A nagios check will use the same script, but in dry-run mode and with a cutoff of 14 days, to notify us if the log rotation stops working.


# Automated periodic database message log truncation
Console logs are written to a `msg_log` database. After a while, the number of messages can become huge, especially if the console logging frequency is high. To mitigate this, an automated message log truncation procedure has been created. A scheduled SQL event calls a procedure to truncate the database `message` table to retain just those records spanning a predefined retention period.
The table's primary key is just the ID number, so searching on the createTime column for the row at the retention period threshold would be inherently slow. Instead a binary search algorithm has been developed which, knowing the earliest and last record timestamps, will check whether the target time lies above or below the current binary division and iterate until the `createTime` field of the target record is within three rows of the low and high row search limits. The `binary_search_time()` procedure is in the `binary-search.sql` file.
The `binary_search_time()` procedure takes one input parameter and returns two output parameters:
`IN p_retention_period time -- The retention period as a time type (e.g. '336:00:00' == 2 wks) Note that this is limited in SQL to '838:59:59', about 35 days`
`OUT p_first_row_id   -- The id value of the earliest row in the table (zeroth row).`
`OUT p_row_number INT -- The returned record number in the table which is closest to the target time. `
 			`This will be a reference to a variable provided by the calling scope.`


## Testing
There is a fairly comprehensive README.md file in C:\Instrument\Apps\EPICS\ISIS\IocLogServer\master\tests

For new systems with no pre-exiting database, the described test procedure can be invoked once the msg_log database has been built by running: C:\Instrument\Apps\EPICS\SystemSetup\confg_mysql.bat.

For systems with an existing msg_log database, there is a SQL script which simply creates the SQL event and procedures necessary for the automatic truncation, without affecting any existing database content:
cd C:\Instrument\Apps\EPICS\ISIS\IocLogServer\master
C:\Instrument\Apps\MySQL\bin\mysql.exe -u root --password=<db root password> < log-truncation-schema.sql

Note that the checks that the script is running correctly is by examining a new database table debug_messages, which is emptied before each truncation process. Details of the process are recorded in the table as simple text, which includes information on the progress of the binary search procedure.