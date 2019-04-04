> [Wiki](Home) > [Project tools](Project-tools) > [Archive Event Log](Archive-Event-Log)

There is a tool for generating event data from the archive database, i.e. when pvs changed. This tool is run with:

    cd ...\EPICS\ISIS\inst_servers\master\scripts
    python log_event_generator.py

Options are:

```
usage: log_event_generator.py [-h] --point_count POINT_COUNT --start_time
                              START_TIME --delta_time DELTA_TIME [--host HOST]
                              [--filename FILENAME]
                              [--default_field DEFAULT_FIELD]
                              pv_values [pv_values ...]

Create a log of events from the archive. E.g. python log_event_generator.py
--start_time 2018-01-10T09:00:00 --point_count 1000 --delta_time 1 --host
ndximat --filename.csv IN:IMAT:MOT:MTR0101.RBV IN:IMAT:MOT:MTR0102.RBV

positional arguments:
  pv_values             Each pv appearing in the data

optional arguments:
  -h, --help            show this help message and exit
  --point_count POINT_COUNT, -c POINT_COUNT
                        Number of sample points
  --start_time START_TIME, -s START_TIME
                        Start time for sample iso date, 2018-12-20T16:01:02
  --delta_time DELTA_TIME, -d DELTA_TIME
                        The time between points in seconds
  --host HOST           Host to get data from defaults to localhost
  --filename FILENAME, -f FILENAME
                        Filename to use for the log file.
  --default_field DEFAULT_FIELD
                        If the pv has no field add this field to it.
```
