# Automated log rotation

IBEX logs are rotated by a script called `logrotate.py` in `C:\instrument\apps\epics\utils\logrotate.py`. This script is called nightly by a windows scheduled task. 

Currently, for all files not modified within the last 10 days, it:
- Deletes them if they are console logs
- Moves them to `stage-deleted` otherwise


The scheduled task is added/recreated as an install step in `ibex_utils` under `server_tasks`.

A nagios check will use the same script, but in dry-run mode and with a cutoff of 14 days, to notify us if the log rotation stops working.