Records can be added to the db files by running:

`python C:\Instrument\Apps\EPICS\ISIS\DbChecker\master\add_sim_records.py <db file> -o <new_file>`

this will produce sim_<file> which includes sim records for various values as well as a disable record for the comms on all values. To not add the disable record specify the `-nd` flag and to specify an external PV to turn on/off record sim use the `-s` flag.