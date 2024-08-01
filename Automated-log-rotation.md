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

**Binary Search**:
```
    IN p_retention_period time -- The retention period as a time type (e.g. '336:00:00' == 2 wks) Note that this is limited in SQL to '838:59:59', about 35 days
    OUT p_first_row_id   -- The id value of the earliest row in the table (zeroth row).
    OUT p_row_number INT -- The returned record number in the table which is closest to the target time.
 			    This will be a reference to a variable provided by the calling scope.
```
The procedure `truncate_message_table()` calls the binary search procedure and uses the returned first row ID and target row ID to determine the rows to be deleted. Potentially the number of rows to be deleted could be very large, in some cases millions, so it is important that the database server is not locked for significant periods. Instead, rows are deleted in blocks of, say 1000 rows at a time, with a sleep period in between. This makes the deletion process cooperative and prevents data loss and timeouts from other database clients.
The `truncate_message_table()` procedure takes one input parameter and returns two output parameters, in the same way as the binary search procedure:

**Truncation procedure**:
```
    IN p_retention_period time -- The retention period as a time type (e.g. '336:00:00' == 2 wks) Note that this is limited in SQL to '838:59:59', about 35 days
    OUT p_first_row_id   -- The id value of the earliest row in the table (zeroth row).
    OUT p_row_number INT -- The returned record number in the table which is closest to the target time.
 			    This will be a reference to a variable provided by the calling scope.
```

The `log_truncation_event()` is triggered periodically, typically once per day at 01:00 and calls the `truncate_message_table()`, supplying the retention period in days. Within the `CREATE EVENT` block, there are two STARTS lines, one of which is commented out and can be instated for testing with a short interval. 

Files specific to automatic truncation are:

| File | Description |
| -----| ----------- |
| binary_search.sql | Defines the binary_search_time() procedure |
| truncate_message_table.sql | Defines the truncate_message_table() procedure |
| truncate_event.sql | Defines the log_truncation_event() event |
| create_event_logger.sql | Defines the EventsLog table for auto truncation process logging |
| debug_log.sql | Defines the debug_log procedure appending info to the process log |
| test\test_truncate_proc.sql | A SQL script to quickly test the truncate_message_table() procedure |
| test\test_fill_message.sql | A SQL script to populate the message table with records assigned a `createDate` field value at one hour intervals over the given period (period_days)  |

## Testing
There is a fairly comprehensive README.md file in C:\Instrument\Apps\EPICS\ISIS\IocLogServer\master\tests

For new systems with no pre-exiting database, the described test procedure can be invoked once the msg_log database has been built by running: `C:\Instrument\Apps\EPICS\SystemSetup\config_mysql.bat`.

For systems with an existing msg_log database, there is a SQL script which simply creates the SQL event and procedures necessary for the automatic truncation, without affecting any existing database content:
cd C:\Instrument\Apps\EPICS\ISIS\IocLogServer\master
C:\Instrument\Apps\MySQL\bin\mysql.exe -u root --password=<db root password> < log-truncation-schema.sql

**Dummy data**:

There is a script : SQL file tests\test_fill_message.sql which will insert dummy log records into the message table. Message records will be assigned a `createDate` field value at one hour intervals over the given period (period_days). These parameters are configurable within the script.

`C:\Instrument\Apps\MySQL\bin\mysql.exe -u root --password=<db root password> < tests\test_fill_message.sql`

**Run the test**:

After filling the message table, it is then possible to test the truncation procedure via:
`C:\Instrument\Apps\MySQL\bin\mysql.exe -u root --password=<db root password> < tests\test_truncate_proc.sql`
Metrics are output to the screen. It can also be helpful to manually examine the message table to view the remaining data and check the time span.

Note that the checks that the script is running correctly is by examining a new database table debug_messages, which is emptied before each truncation process. Details of the process are recorded in the table as simple text, which includes information on the progress of the binary search procedure.

If you want to update a procedure, simply edit the SQL file in the `C:\Instrument\Apps\EPICS\ISIS\IocLogServer\master` directory or `tests\` subdirectory, then use the mysql executable to do the change to the database accordingly, e.g.:

`C:\Instrument\Apps\MySQL\bin\mysql.exe -u root --password=<db root password> < truncate_event.sql`

