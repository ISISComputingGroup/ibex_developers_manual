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

In May 2024 we went through each of these data types, and reviewed decisions made in 2018 ([see below](Data-Generation-and-Storage-on-Instrument-PCs-(NDX's)#previous-work)). In each case we identified how long we needed to keep them on the instrument, whether (and if so, how long) we needed to keep the data having moved it off the instrument, and what changes could be made to better automate that movement. 

Data type | Retention on instrument PC | Retention after migration | Automation | Notes
--------  | -------------------------- | ------------------------- | ---------- | -----
Autosave  | Indefinitely               | N/A                       | N/A        | Trivially Small and useful
Config    | [Tracked with git](Settings-and-Configurations) | N/A  | N/A        | Small
logs: all, other than those listed below (inc. IOC, Genie-python, ICP, DAE ...) | 10 days | 10 years | [#8360](https://github.com/ISISComputingGroup/IBEX/issues/8360) | Currently moved by a script being run manually between cycles. Agreed that the usefulness of these logs declines sharply with time and the potential volume is such as to justify the 10 day retention period
logs: conserver | 10 days              | Delete after 10 days      | [#8363](https://github.com/ISISComputingGroup/IBEX/issues/8363) | These contain no additional information over other logs, but are useful for debugging in some specific contexts, as such no need to retain beyond the period they would be useful for that debugging.  
MySQL: msg_log | TBC (?30 days?)       | ?10 years?                | [#8364](https://github.com/ISISComputingGroup/IBEX/issues/8364) | Searchable DB of things in the IOC log. Retention time requires discussion with existing users of the IBEX IOC log. 
MySQL: archive | 1 cycle               | ?10 years?                | #836n | Source for IBEX graphs. Agreed keeping for one cycle would be appropriate retention. If we then find manual truncation is still required in cycle, then we should adapt the truncation script to leave n days of data behind. 
MySQL: all others not listed above | Indefinitely | N/A            | N/A        | Small

# Previous work
This page was substantially rewritten in 2024, including a change in name. [The 2018 version](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Data-Generation-and-Storage/89680073e9034ff5381470be73eacfc2daf24a40) is available in the git history. In 2018 we monitored 6 instruments over 19 days in cycle, the results are in an [excel file](design_documents/DataVolumns_resolution.xlsx). We found that the daily variation is not huge and therefore we can look at the averages of data captured per day. Of the various types of data the largest was conserver logs, ioc logs, mysql-archive, msg-logs and mysql files. At that time, IMAT was the biggest user collecting less than 400MB/day.