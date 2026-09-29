# Log file locations

Various log file locations:

log file | location | what it shows
------   | -------  | -------------
genie_python | `..\Instrument\Var\logs\genie_python\genie-YYYY-MM-DD.log` | Every command that genie python executes (log is written before command is executed)
ISIS DAE IOC Log | `..\Instrument\Var\logs\ioc\ISISDAE_01-YYYMMDD.log` | Shows what ISIS DAE IOC, this is controlling the isisicp
ISIS ICP Log | `c\Data\Export only\logs\icp\log\icp-YYYY-MM-DD-Ddd.log` |  Shows what the isis icp data collection program is doing
ISIS ICP Putlog (Put log) | `C:\data\[instrument name][run number]_ICPputlog.txt` | Shows caputs to PV's including their new and old values