> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Logging from the archive](Logging-from-the-archive)

An IOC can be made to log values to a file based on the value of a PV. Consider whether you IOC needs to do this. 

To add logging to an IOC you need to add info fields to your records. The logging is based on a logging PV; when the logging pv switches off (1 to 0) then the period for which it was on will be written into a file in `c:\logs`. To define what is in the log file add an info field of the form:

       info(<info field name>, <value>)

The value will always have `this_pv` substituted with the pv name of the record the info field is in. 

For the changes to logging to take effect you must have built and run the IOC and then restarted the archiver access process. If you have changed or added the archive log rate then the instrument archiver (ARINST) must have been restarted since the IOC was run.

### Archive setting

For a PV to appear either in a header line or a column, or for it to trigger a log the pv must be archived. The rate of archive must be at least as small as the maximum scan period; otherwise values might be missed. To add it to the archive use the usual notion (see [finishing touches](IOC-Finishing-Touches#2-archive-pvs) ).

Example: PV changing a maximum of once every 0.1s use `info(archive, "VAL 0.1")`

### Formatted PV Value

Many fields accept a formatted pv value this is written as follows:

    `{pvname[!converter][|format]}`

This is similar to the python format and using the same syntax except the variable name is replaced with the pvname and the colon is replaced with a pipe. The converter and format are both options. The converter will allow you to perform a conversion this is either `s` from string representation, `r` from representation (__rep__). The format are as the python formatter (see [python docs](https://docs.python.org/2/library/string.html#format-string-syntax)). Examples:

-  `{this_pv}` - is the pv of the current record
-  `{IN:LARMOR:SIMPLE:VALUE1|10.6f}` - the pv `IN:LARMOR:SIMPLE:VALUE1` is formatted as a float with 10 character and 6dp
-  `{this_pv!s|10s}` - the current pv converted using the string representation and then given a width of 10

### `LOG_trigger`

The trigger pv indicates which pv turns logging on (pv value 1) and off (pv value 0). When the PV goes from 0 to 1 it triggers log creation. Only one of these should be defined, if you define two then last one into the database wins.

The value of the field is either:
*  `""` (empty string) - use the pv this is annotating as the trigger pv
* `"<pvname>"` - use the pv name as the trigger 

Example: 

```
record(bi, "$(P)LOGGING")
{
    field(DESC, "Set logging")
    field(ZNAM, "Off")
    field(ONAM, "On")
    field(PINI, "YES")
    field(VAL "0")
    info(archive, "VAL 1")
    info(LOG_trigger, "")
}
```

### `LOG_headerX`

If you want header lines in your log then use this field. Header lines are ordered alphanumerically by the X; X values 1-9 probably make most sense.

The value of the field is the header you want in the file. An empty value will produce a blank line. If you include a PV value it will be the value that PV had when the logging starts. To add a PV use the standard PV format. 

Example: `info(LOG_header1, "Temperature {this_pv|10.6f}")` First header line is "Temperature XXX" where XXX is the pv that the field is in format as float with 10 width and 6dp

### `LOG_column_headerX`

The main part of the log are columns with data. Each column can have its own header and this is specified with the LOG_column_headerX annotation. If there is no header then the default is the template, if the template is blank it is the pv name. The value is the text that will be used for the column header. There should not be more than one X for each column if there are then one will win.

Example: `info(LOG_column_header1, "Temperature (K)")` produces a header of  "Temperature (K)" for column `

NB See archive setting

### `LOG_column_template`

The main part of the log are columns with data. Each column can have its own template and this is specified with the LOG_column_templateX annotation. If there is no template (just a header) or it is blank then the default is the pv name in which the header record or template record occur. The value is the template that will be used for the column data. The format for the template is a formatted PV value. There should not be more than one X for each column if there are then one will win.

Example: `info(LOG_column_template1, "{this_pv|10.6f}")` produces a column of floats for the current records pv.

NB See archive setting

### `LOG_period_seconds`

The period of the log is set using the LOG_period_seconds info field. It sets the time period between limes in the table in seconds. It should be noted that if the PV is not changing more often than the value then the value will not change more often. This is an alternative to `LOG_period_pv`.

Example: `info(LOG_period_seconds, "0.5")` produces a time series in half second intervals.

### `LOG_period_pv`

The period of the log can be set based on the value of a PV when the logging is started. This allows the IOC to control the period of the log. The value is the PV that is being used to set the logging period if it is blank the current record is used. It should be noted that if the PV is not changing more often than the value then the value will not change more often. This is an alternative to `LOG_period_seconds`.

Examples: 
    - `info(LOG_period_seconds, "TE:INST:SIMPLE:PERIOD")` produces a time series with an interval set by the pv 
TE:INST:SIMPLE:PERIOD.
    - `info(LOG_period_seconds, "")` produces a time series with an interval set by the pv record containing this

