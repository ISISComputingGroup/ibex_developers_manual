> [Wiki](Home) > [Project tools](Project-tools) > [Archive Event Log](Archive-Event-Log)

There is a tool for generating event data from the archive database, i.e. when pvs changed. This tool is run with:

    cd ...\EPICS\ISIS\inst_servers\master\scripts
    %PYTHON3% log_event_generator.py

Options are:

```
usage: log_event_generator.py [-h] --end_time END_TIME --start_time START_TIME [--host HOST] [--filename FILENAME]
                              [--default_field DEFAULT_FIELD]
                              pv_names [pv_names ...]

Create a log of events from the archive. E.g. python log_event_generator.py --start_time 2018-01-10T09:00:00
--end_time 2018-01-11T8:10:00 --host ndximat --filename.csv IN:IMAT:MOT:MTR0101.RBV IN:IMAT:MOT:MTR0102.RBV

positional arguments:
  pv_names              Each pv appearing in the data

optional arguments:
  -h, --help            show this help message and exit
  --end_time END_TIME, -e END_TIME
                        End time
  --start_time START_TIME, -s START_TIME
                        Start time for sample iso date, 2018-12-20T16:01:02
  --host HOST           Host to get data from defaults to localhost
  --filename FILENAME, -f FILENAME
                        Filename to use for the log file.
  --default_field DEFAULT_FIELD
                        If the pv has no field add this field to it.
```


Output is something like:

```
Initial values
IN:POLREF:MOT:MTR0801.RBV, -66.743
IN:POLREF:MOT:MTR0802.RBV, -129.31900000000002
IN:POLREF:MOT:MTR0803.RBV, -27.444
IN:POLREF:MOT:MTR0804.RBV, 0.0
Changes for time period
2020-12-17T09:28:17.569875, IN:POLREF:MOT:MTR0803.RBV, -27.443
2020-12-17T09:28:17.811507, IN:POLREF:MOT:MTR0803.RBV, -27.444
2020-12-17T09:28:19.915512, IN:POLREF:MOT:MTR0803.RBV, -27.445
2020-12-17T09:31:57.748000, IN:POLREF:MOT:MTR0804.RBV, Disconnected
2020-12-17T09:32:07.335438, IN:POLREF:MOT:MTR0804.RBV, 0.0
2020-12-17T09:32:07.343902, IN:POLREF:MOT:MTR0801.RBV, -66.743
2020-12-17T09:32:07.344014, IN:POLREF:MOT:MTR0802.RBV, -129.31900000000002
```
