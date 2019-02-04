> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Jaws and Slits](Jaws-and-slits) > [General Jaws](Jaws)

The general jaws are a set of jaws that can be placed onto 4 motors which represent North, South, East and West. They will allow a centre and gap to be set in both horizontal and vertical directions. It is a requirement that if an underlying motor position is set then the gap and centre should adjust to be in sync.

The jaws are a db record which can be added to most motors. They are added through the configuration area based on the motor.

## Example

For a galil they might be in a file in the instrument settings called `<inst name>\configurations\galil\jaws.cmd`:

```
# Define a set of jaws from first 4 motors on first controller (if present)
$(IFIOC_GALIL_01) dbLoadRecords("$(JAWS)/db/jaws.db","P=$(MYPVPREFIX)MOT:,JAWS=JAWS1:,mXN=MTR0101,mXS=MTR0102,mXW=MTR0103,mXE=MTR0104")
$(IFIOC_GALIL_01) dbLoadRecords("$(JAWS)/db/jaws.db","P=$(MYPVPREFIX)MOT:,JAWS=JAWS2:,mXN=MTR0105,mXS=MTR0106,mXW=MTR0107,mXE=MTR0108")

# Define a set of jaws from first 4 motors on second controller (if present)
$(IFIOC_GALIL_02) dbLoadRecords("$(JAWS)/db/jaws.db","P=$(MYPVPREFIX)MOT:,JAWS=JAWS3:,mXN=MTR0201,mXS=MTR0202,mXW=MTR0203,mXE=MTR0204")
$(IFIOC_GALIL_02) dbLoadRecords("$(JAWS)/db/jaws.db","P=$(MYPVPREFIX)MOT:,JAWS=JAWS4:,mXN=MTR0205,mXS=MTR0206,mXW=MTR0207,mXE=MTR0208")
```
