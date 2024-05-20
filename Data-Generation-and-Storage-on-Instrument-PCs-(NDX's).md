****__WORK IN PROGRESS (20/05/2024 - will finish tomorrow, GR)__****

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

# Decisions

## Data storage

In May 2024 we went through each of these data types, and reviewed decisions made in 2018 ([see bellow](Data-Generation-and-Storage-on-Instrument-PCs-(NDX's)#previous-work)). In each case we identified how long we needed to keep them on the instrument, whether (and if so, how long) we needed to keep the data having moved it off the instrument, and what changes could be made to better automate that movement. 

Data type | Storage on instrument | Easy access storage | Other storage | Justification
--------  | --------------------- | ------------------- | ------------- | -------------
Autosave  | 2 cycles              | 1 year              | not needed    | Useful but only in the short term to redo settings and possibly see long term drifts
config    | -                     |  -                  | -             | These do not increase in size rapidly so do not need clearing out
logs-ioc/ nicos and genie python | 1 cycle | 2 cycles | forever | these are a primary source of information and can be used to analysis problems in the data which is held for 10 years. So we should keep
logs-conserver | 1 cycle        | 0 | 0 | These hold marginally more info than the ioc logs but that extra info is not interesting and the ioc logs are easier to access
mysql-msg_log | 1 cycle | 0 | 0 | Sub set of the ioc logs
mysql-archive | 1 cycle | 2 cycles | forever | Experiments can be across multiple cycles so keep access for scientists for 2 cycles off the instrument. Afterwards store where it is hard to get to we only get asked for this information ~twice a year.
mysql (all others) | - | - | - | Data can be reconstructed and does not grow

# Previous work
This page was substantially rewritten in 2024, including a change in name. [The 2018 version](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Data-Generation-and-Storage/89680073e9034ff5381470be73eacfc2daf24a40) is available in the git history. In 2018 we monitored 6 instruments over 19 days in cycle, the results are in an [excel file](design_documents/DataVolumns_resolution.xlsx). We found that the daily variation is not huge and therefore we can look at the averages of data captured per day. Of the various types of data the largest was conserver logs, ioc logs, mysql-archive, msg-logs and mysql files. At that time, IMAT was the biggest user collecting less than 400MB/day.