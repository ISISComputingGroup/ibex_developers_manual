# Data Production

Data is produced by various parts of the IBEX infrastructure. 

- *scientific data*: is captured in NEXUS files is well understood and the process for storing and archiving it is well documented.
- *autosave*: captured in autosave files 
- *configurations*: including instrument scripts (not user scripts)
- *gui*: workspace of the gui (Apps\Client\workspace)
- *logs*
    - *conserver*: console servers logs
    - *ioc*: ioc logs
    - *other*: all other directories in var\logs
- *sql database*:
    - *mysql-alarm*: alarm schema
    - *mysql-archive*: archive schema for archive engines
    - *mysql-exp_data*: experimental database schema
    - *mysql-iocdb*: IOC information schema
    - *mysql-journal*: Journal schema
    - *mysql-msg_log*: message log schema
    - *mysql-mysql*: mysql own schema
    - *mysql-performance_schema*: performance schema
    - *mysql-sys*: system schema
    - *mysql_files*: files in the root on mysql data

# Current Data Volumes

We monitored 6 instruments over 19 days in cycle, the results are in an [excel file](design_documents/DataVolumns_resolution.xlsx). We found that the daily variation is not huge and therefore we can look at the averages of data captured per day. Of the various types of data the largest was conserver logs, ioc logs, mysql-archive, msg-logs and mysql files.

IMAT was the biggest user collecting less than 400MB/day.

# Decisions

## Collecting Data Rates Again

The data collection experiment was flawed because we are logging extra data this cycle because of the data being logged on MDEL instead of ADEL and not yet including the reducing of ioc logging when a pv is in an error state. **Action** log data usage over the next cycle.

## Data storage

We went through each data type thinking about how long it needed to be stored for the answers. We categorised these as:

* *Storage on instrument*: data is not deleted from the instrument until after this period 
* *Easy access storage*: data the users can access without help.
* *Other storage*: form of storage which would not necessarily be easy to access without out help

* forever as a time period means store for 2 years and then revisit this decision when we know how big the data is and problems involved.

Data type | Storage on instrument | Easy access storage | Other storage | Justification
--------  | --------------------- | ------------------- | ------------- | -------------
Autosave  | 2 cycles              | 1 year              | not needed    | Useful but only in the short term to redo settings and possibly see long term drifts
config    | -                     |  -                  | -             | These do not increase in size rapidly so do not need clearing out
logs-ioc/ nicos and genie python | 1 cycle | 2 cycles | forever | these are a primary source of information and can be used to analysis problems in the data which is held for 10 years. So we should keep
logs-conserver | 1 cycle        | 0 | 0 | These hold marginally more info than the ioc logs but that extra info is not interesting and the ioc logs are easier to access
mysql-msg_log | 1 cycle | 0 | 0 | Sub set of the ioc logs
mysql-archive | 1 cycle | 2 cycles | forever | Experiments can be across multiple cycles so keep access for scientists for 2 cycles off the instrument. Afterwards store where it is hard to get to we only get asked for this information ~twice a year.
mysql (all others) | - | - | - | Data can be reconstructed and does not grow


*logs-other*, *gui* was not talked about I think they are useful only to us to look for trends and that we should keep them on the machine for 1 year and then delete.

## Future plans

Not talked about at the meeting but Chris said the data volumes don't seem huge to him even for 30 instruments. I suggest that we do the following in every shutdown:

1. For autosave and logs-other delete all files older than 1 year. These are not big files so can be kept on the instrument.
1. For logs-conserver and mysql-msglog delete the data
1. For logs-ioc, logs-nicos and logs-genie move all files to the off-data drive for long term saving
1. For my-sql archive
    1. Dump the schema to csv files with relevant table names.
    1. Create a central database server (one time job)
    1. Empty central database schema of data
    1. Import dumped tables to central database server (ids of all will need changing because of multiple sources)

We then need some on-going actions to ensure the critical machine can continue running:

1. Define a data size for each area of data for each instrument and an action to take when the area get too large. Run a process on the machine which will check on the size every hour. At 90% of size send an email. Suggested actions:

Data type |  What to do if size is to big
--------  | ------------------- 
Autosave  | delete oldest files 
config    | email if bigger than 1GB 
logs-ioc, nicos and genie python | delete oldest files
logs-conserver | delete oldest files
mysql-msg_log | Create a ticket to think about this.
mysql-archive | Create a ticket to think about this.
mysql (all others) | Create a ticket to think about this.

Final actions:

1. Investigate the GUI workspace and see if we need to do anything with this.
1. Investigate options for database critical size
1. Create a separate labview log for messages that current are written to the mysql-msglog and treat it like an IOC log.
1. Collect a new sample of data over the next cycle. (Collect weekly but for more instruments)
1. Agree above things to do on shutdown create tickets to implement and automate these
1. Agree critical things to do all the time and create tickets to implement these

# Previous work
This page was substantially rewritten in 2024. The 2018 version is available in the git history. In 2018 we monitored 6 instruments over 19 days in cycle, the results are in an [excel file](design_documents/DataVolumns_resolution.xlsx). We found that the daily variation is not huge and therefore we can look at the averages of data captured per day. Of the various types of data the largest was conserver logs, ioc logs, mysql-archive, msg-logs and mysql files. At that time, IMAT was the biggest user collecting less than 400MB/day.