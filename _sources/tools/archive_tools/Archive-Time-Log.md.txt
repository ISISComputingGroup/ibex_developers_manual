# Archive Time Log

There is a tool for generating a log of data from the archive database at given points in time. This tool is run with:

    cd ...\EPICS\ISIS\inst_servers\master\scripts
    python log_file_generator.py

```
usage: log_file_generator.py [-h] --point_count POINT_COUNT --start_time
                             START_TIME --delta_time DELTA_TIME [--host HOST]
                             [--filename_template FILENAME_TEMPLATE]
                             header_and_pvs [header_and_pvs ...]

Create a log file from the archive. E.g. python
log_file_generator.py --start_time 2018-01-10T09:00:00
--point_count 1000 --delta_time 1 --host ndximat --filename_template
log{start_time}.csv MOT0101 IN:IMAT:MOT:MTR0101.RBV MOT0102
IN:IMAT:MOT:MTR0102.RBV

positional arguments:
  header_and_pvs        A header followed by the name for each pv appearing in
                        the data

optional arguments:
  -h, --help            show this help message and exit
  --point_count POINT_COUNT, -c POINT_COUNT
                        Number of sample points
  --start_time START_TIME, -s START_TIME
                        Start time for sample iso date, 2018-12-20T16:01:02
  --delta_time DELTA_TIME, -d DELTA_TIME
                        The time between points in seconds
  --host HOST           Host to get data from defaults to localhost
  --filename_template FILENAME_TEMPLATE, -f FILENAME_TEMPLATE
                        Filename template to use for the log file.
  --default_field       The field to add to a pv if it has no field. The default 
                        is `val` so all PVs will be found in an instrument archive. 
                        This means that to access the blocks or the central control 
                        archives you need to set this to `""` .
```
