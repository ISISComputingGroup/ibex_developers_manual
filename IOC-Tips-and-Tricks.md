## DBLoadRecordsLoop and DBLoadRecordLoop

You can load Db records in a loop using `dbLoadRecordsLoop`.

```
# Example usage of dbLoadRecordsLoop() and iocshCmdLoop() etc.
# Define a loop or list variable, then references to \$(VAR) will be replaced by loop/list values.
# You can use \$(VAR) in any of the values of the parameters, including the db file name.
# The loop/list variable "I" is passed to the DB file along with any other specified macros.
# We now loop "I" over a range of 1 to 3.
dbLoadRecordsLoop("db/utilitiesTest.db", "P=$(MYPVPREFIX),Q=A\$(I)", "I", 1, 3)
```

You can also iterate over a list using `dbLoadRecordsList`.

```
# Here S is our list variable with values x, Y and Z.
dbLoadRecordsList("db/utilitiesTest.db", "P=$(MYPVPREFIX),Q=A\$(S)", "S", "X;Y;Z", ";")

# As the loop/list variable is always passed though, we can instead iterate over Q.
dbLoadRecordsList("db/utilitiesTest.db", "P=$(MYPVPREFIX)", "Q", "BX;BY;BZ", ";")
```

You can execute IOC commands in loops as well.

```
# We can execute iocs commands in a similar way.
iocshCmdLoop("dbgrep $(MYPVPREFIX)A\$(I)*", "", "I", 1, 3)
iocshCmdList("dbgrep $(MYPVPREFIX)A\$(S)*", "", "S", "X;Y;Z", ";")

# We can also load files. The macro Q and I will be defined as temporary environment.
# variables for use in the script and then reset back to their pre-script values.
iocshCmdLoop("< st\$(I).cmd", "Q=Hello\$(I)", "I", 1, 2)
```

More details can be found at http://epics.isis.stfc.ac.uk/doxygen/main/support/utilities/dbLoadRecordsFuncs_8cpp.html#a32071967b99f42356b1e04b06746cc73.

**N.B.** If you need to parameterise your macro names, you will need to use a template and not a `dbLoadRecordsList` or `dbLoadRecordsLoop`.

## Toggle multiple PV's from a single set-point

Sometimes you might want to have a single record set point that processes multiple records. An example of this would be for a device that requires different commands to be sent for Start and Stop. Rather than having to process two distinctly different records for each command you can use this template to toggle these from a single record:

```
record(bi, "$(P)TOG:RECORD:SP") {
	field(DESC, "Toggle record set point")
	
	field(ZNAM, "Record1")
	field(ONAM, "Record2")
	info(INTEREST, "HIGH")
}

# Add 1 to the value of the toggle set point to map the fanout 
# forward link index.
record(calcout, "$(P)_TOG:CALC:RECORD") {
	field(INPA, "$(P)TOG:RECORD:SP CP")
	
	field(CALC, "A+1")
	
	field(OUT, "$(P)_TOG:RECORD.SELN PP")
}

record(fanout, "$(P)_TOG:RECORD") {
	field(SELM, "Specified")
	
	field(LNK1, "$(P)_RECORD1:SP PP")
	field(LNK2, "$(P)_RECORD2:SP PP")
}

record(bo, "$(P)_RECORD1:SP") {
	field(DESC, "Process record1")
	field(DTYP, "stream")
	field(SCAN, "Passive")
	
	field(OUT, "@device.proto set_record1() $(PORT)")
}

record(bo, "$(P)_RECORD2:SP") {
	field(DESC, "Process record2")
	field(DTYP, "stream")
	field(SCAN, "Passive")
	
	field(OUT, "@device.proto set_record2() $(PORT)")
}
```

This takes the set points binary value, shifts it by +1 in a calc record which allows for it to be mapped with the forward link outputs of the fanout record, these forward links are then processed. This can be easily extended with additional forward links or sequence records.

## Processing of calc records

There are two major ways in which your calc records can be processed:

1)The first way is to either use a forward link or have the name of your calc record in the OUT field of another PV, followed by the PP flag. In this way, the calc record will not be processed when the IOC starts. This way is better for when the other PV is a setpoint, since you want the calc record to process only when the setpoint is explicitly set, not also when the IOC starts and when the setpoint is initialized.

2)The other way is to have the PV that should trigger the processing of the calc record in the an INP field of the calc record, followed by the CP MS flags. The CP flag enables monitoring of that PV, and then the MS flag means any alarm of that PV will propagate to the calc record. The calc record will be processed every time the other PV is processed, including when the IOC starts. This way is better for when the other PV is a readback, because you want the calc to be processed each time the readback changes.

## Creating many IOC aliases

If you would like to create a set of PV aliases in an IOC from the `st.cmd` then that is possible using `dbAliasRecordsPrefix` (to simply swap a prefix) or `dbAliasRecordsRE` (to use a more complicated regular expression)

To create aliases for all records with e.g. the `ME:` (movable equipment) prefix that instead have the local pv prefix 
```
dbAliasRecordsPrefix("ME:", "$(MYPVPREFIX)")
```
The equivalent using a regular expression would be
```
dbAliasRecordsRE("ME:(.*)", "$(MYPVPREFIX)\1")
```
but much more complex rewrites are possible

## For general information on commands see:
* http://epics.isis.rl.ac.uk/doxygen/main/support/utilities/index.html
* https://epics.anl.gov/base/R3-14/12-docs/AppDevGuide/node19.html