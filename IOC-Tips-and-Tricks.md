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

**N.B.**: IF you need to parameterise your macro names, you will need to use a template and not a `dbLoadRecordsList` or `dbLoadRecordsLoop`.