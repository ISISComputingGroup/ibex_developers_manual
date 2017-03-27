To help dedbug the PVObserver and lower levels you can build a version of the GUI which includes logging and the code for PV manager.

1) Checkout [csstudio repository](https://github.com/ISISComputingGroup/CSStudio_3_3)
2) Switch to the Logging_for_PV_connections branch
    - NB the JCA and caj code has been copied from the caj and jca project to org.csstudio.platform.libs.epics and the jar deleted in this project. If you need to update this code create a new copy.
3) Switch the gui branch to Logging_for_PV_connections 
4) Clean and build. 
5) Run with the following plugins from the workspace instead of the P2 repository:
    - org.csstudio.logging
    - org.csstudio.platform.libs.epics
    - org.csstudio.utilities.pvmanager
    - org.csstudio.utilities.pvmanager.epics
6) This will now print out debug statements all containing the text Ticket2162
7) The logs can be filtered using a python program below (this program is very rough, don't forget to change the date)
8) This can be combined with Wireshark to analysis traffic if needed

Example log output

```
*2017-03-27 10:37:33.476 [pool-2-thread-2] INFO  com.cosylab.epics.caj.impl.CATransport - Ticket2162: unknown - CATransport processRead start
*2017-03-27 10:37:33.476 [pool-2-thread-2] INFO  com.cosylab.epics.caj.impl.CATransport - Ticket2162: unknown - CATransport handle response
*2017-03-27 10:37:33.476 [pool-2-thread-2] INFO  com.cosylab.epics.caj.impl.CATransport - Ticket2162: unknown - CATransport handle response
*2017-03-27 10:37:33.476 [pool-2-thread-2] INFO  com.cosylab.epics.caj.impl.CATransport - Ticket2162: unknown - CATransport handle response
*2017-03-27 10:37:33.476 [pool-2-thread-2] INFO  com.cosylab.epics.caj.impl.CATransport - Ticket2162: unknown - CATransport handle response
*2017-03-27 10:37:33.476 [pool-2-thread-2] INFO  com.cosylab.epics.caj.impl.CATransport - Ticket2162: unknown - CATransport handle response
*2017-03-27 10:37:33.476 [pool-2-thread-2] INFO  com.cosylab.epics.caj.impl.CATransport - Ticket2162: unknown - CATransport handle response
*2017-03-27 10:37:33.476 [pool-2-thread-2] INFO  com.cosylab.epics.caj.impl.CATransport - Ticket2162: unknown - CATransport processRead end
*2017-03-27 10:37:33.473 [pool-3-thread-1] INFO  org.epics.pvmanager.PVDirector - Ticket2162: TE:NDW1407:EUROTHRM_01:A01:TEMP:SP - PVDirector connected or exception event true
*2017-03-27 10:37:33.475 [pool-2-thread-4] INFO  com.cosylab.epics.caj.impl.handlers.CreateChannelResponse - Ticket2162: TE:NDW1407:EUROTHRM_01:A01:TEMP:SP - CreateChannel connect complete
*2017-03-27 10:37:33.477 [pool-3-thread-1] INFO  org.epics.pvmanager.PVReaderImpl - Ticket2162: TE:NDW1407:EUROTHRM_01:A01:TEMP:SP - PVReaderImpl connection
*2017-03-27 10:37:33.477 [pool-2-thread-4] INFO  com.cosylab.epics.caj.impl.CATransport - Ticket2162: TE:NDW1407:EUROTHRM_01:A01:TEMP:SP - CAResponseHandler id (18 is connection, 23 response) 18
*2017-03-27 10:37:33.477 [pool-2-thread-4] INFO  com.cosylab.epics.caj.impl.CATransport - Ticket2162: TE:NDW1407:EUROTHRM_01:A01:TEMP - CAResponseHandler id (18 is connection, 23 response) 18
*2017-03-27 10:37:33.477 [pool-2-thread-4] INFO  com.cosylab.epics.caj.CAJChannel - Ticket2162: TE:NDW1407:EUROTHRM_01:A01:TEMP - CAJChannel connect complete changegov.aps.jca.Channel$ConnectionState[DISCONNECTED=1]
*2017-03-27 10:37:33.477 [pool-2-thread-4] INFO  com.cosylab.epics.caj.CAJChannel - Ticket2162: TE:NDW1407:EUROTHRM_01:A01:TEMP - CAJChannel connect changegov.aps.jca.Channel$ConnectionState[CONNECTED=2]
*2017-03-27 10:37:33.477 [pool-2-thread-4] INFO  org.epics.pvmanager.MultiplexedChannelHandler - Ticket2162: TE:NDW1407:EUROTHRM_01:A01:TEMP - MultiplexChannelHandler connect changeJCAConnection [connected: true writeConnected: false channel: CAJChannel = { name = TE:NDW1407:EUROTHRM_01:A01:TEMP, connectionState = CONNECTED }]
*2017-03-27 10:37:33.477 [pool-2-thread-4] INFO  org.epics.pvmanager.ConnectionCollector - Ticket2162: TE:NDW1407:EUROTHRM_01:A01:TEMP - ConnectionCollector connect changetrue
*2017-03-27 10:37:33.477 [pool-2-thread-4] INFO  org.epics.pvmanager.ConnectionCollector - Ticket2162: TE:NDW1407:EUROTHRM_01:A01:TEMP - ConnectionCollector connect changefalse
*2017-03-27 10:37:33.477 [pool-3-thread-1] INFO  org.epics.pvmanager.PVDirector - Ticket2162: TE:NDW1407:CS:SB:TEMP1:SP - PVDirector connected or exception event true
*2017-03-27 10:37:33.477 [pool-3-thread-1] INFO  org.epics.pvmanager.PVReaderImpl - Ticket2162: TE:NDW1407:CS:SB:TEMP1:SP - PVReaderImpl connection
*2017-03-27 10:37:33.477 [pool-2-thread-4] INFO  com.cosylab.epics.caj.impl.handlers.CreateChannelResponse - Ticket2162: TE:NDW1407:EUROTHRM_01:A01:TEMP - CreateChannel connect complete
*2017-03-27 10:37:33.478 [pool-2-thread-4] INFO  com.cosylab.epics.caj.impl.CATransport - Ticket2162: unknown - CATransport processRead end
```

and filtered
```
             unknown = 10:37:33.476000: CATransport processRead start
             unknown = 10:37:33.476000: CATransport handle response
             unknown = 10:37:33.476000: CATransport handle response
             unknown = 10:37:33.476000: CATransport handle response
             unknown = 10:37:33.476000: CATransport handle response
             unknown = 10:37:33.476000: CATransport handle response
             unknown = 10:37:33.476000: CATransport handle response
             unknown = 10:37:33.476000: CATransport processRead end
OTHRM_01:A01:TEMP:SP = 10:37:33.473000: PVDirector connected or exception event true
OTHRM_01:A01:TEMP:SP = 10:37:33.475000: CreateChannel connect complete
OTHRM_01:A01:TEMP:SP = 10:37:33.477000: PVReaderImpl connection
OTHRM_01:A01:TEMP:SP = 10:37:33.477000: CAResponseHandler id (18 is connection, 23 response) 18
EUROTHRM_01:A01:TEMP = 10:37:33.477000: CAResponseHandler id (18 is connection, 23 response) 18
EUROTHRM_01:A01:TEMP = 10:37:33.477000: CAJChannel connect complete changegov.aps.jca.Channel$ConnectionState[DISCONNECTED=1]
EUROTHRM_01:A01:TEMP = 10:37:33.477000: CAJChannel connect changegov.aps.jca.Channel$ConnectionState[CONNECTED=2]
EUROTHRM_01:A01:TEMP = 10:37:33.477000: MultiplexChannelHandler connect changeJCAConnection [connected: true writeConnected: false channel: CAJChannel = { name = TE:NDW1407:EUROTHRM_01:A01:TEMP, connectionState = CONNECTED }]
EUROTHRM_01:A01:TEMP = 10:37:33.477000: ConnectionCollector connect changetrue
EUROTHRM_01:A01:TEMP = 10:37:33.477000: ConnectionCollector connect changefalse
W1407:CS:SB:TEMP1:SP = 10:37:33.477000: PVDirector connected or exception event true
W1407:CS:SB:TEMP1:SP = 10:37:33.477000: PVReaderImpl connection
EUROTHRM_01:A01:TEMP = 10:37:33.477000: CreateChannel connect complete
             unknown = 10:37:33.478000: CATransport processRead end
```



# Python to analysis the logs:

```
import os
import re
from datetime import datetime


TICKET="Ticket2162:"
SEVERE="SEVERE:"
SEVERE_LINE_START = "{0} {1}".format(SEVERE, TICKET)

class LogLine():
    def __init__(self, time, pv, message):
        self.time = time
        self.message = message.strip()
        self.pv = pv.strip()
    def __repr__(self):
        dateTimeString = datetime.strftime(self.time, "%H:%M:%S")
        return "{time}: {message}".format(time=dateTimeString, message=self.message)


def parse_severe_line(previous_line, line):


    # Mar 22, 2017 12:04:24 PM org.epics.pvmanager.SourceDesiredRateDecoupler sendDesiredRateEvent
    pattern = r"(.* (?:AM|PM)).*"
    match = re.match(pattern, previous_line)
    dateString, = match.groups()
    dateTime = datetime.strptime(dateString, '%b %d, %Y %I:%M:%S %p')

    # SEVERE: Ticket2162: TE:NDW1407:CS:IOC:INSTETC_01:DEVIOS:TOD - PVDirector event connected true

    match = re.match(SEVERE_LINE_START + "(.*) - (.*)", line)
    if match is None:
        exit("ERROR: servere message not match {0}".format(line))

    pv, message = match.groups()

    return LogLine(dateTime, pv, message)


def parse_normal_line(line):
    # *2017-03-22 12:04:24.556 [PVMgr Worker 3] INFO  org.epics.pvmanager.PVReaderImpl - Ticket2162: TE:NDW1407:CS:BLOCKSERVER:PVS:ACTIVE - PVReaderImpl valueChange

    pattern = r"\*(.*) \[.* " + TICKET + r"(.*) - (.*)"
    match = re.match(pattern, line)
    time_string, pv, message = match.groups()

    dateTime = datetime.strptime(time_string, r"%Y-%m-%d %H:%M:%S.%f")

    return LogLine(dateTime, pv, message)


if __name__ == "__main__":
    WANTEDPV = ["TE:NDW1407:CS:SB:TEMP1", "unknown"]

    pvChanges = []
    previous_line = ""
    filepath = r"C:\tmp\change_pv_name.txt"
    month = "2017-03"
    day = "27"
    filedir = r"C:\Instrument\runtime-ibex.product\logs" + "\\" + month
    filepaths = [os.path.join(filedir, filepath) for filepath in os.listdir(filedir) if month + "-" + day in filepath]
    filepaths.append(r"C:\Instrument\runtime-ibex.product\logs\isis.log")

    for filepath in filepaths:
        print("Reading: {0}".format(filepath))
        for line in file(filepath):

            if TICKET in line:
                if line.startswith(SEVERE):
                    pvChange = parse_severe_line(previous_line, line)
                else:
                    pvChange = parse_normal_line(line)

                pvChanges.append(pvChange)
            previous_line = line

    print("PVS:")
    for pv_name in set([x.pv for x in pvChanges]):
        print("    {0}".format(pv_name))
    print("\n\n")

    print("Timeline for {0}".format(WANTEDPV))
    for pvChange in pvChanges:
        #if pvChange.pv in WANTEDPV:
            print("{0:>20} = {1}".format(pvChange.pv.strip()[-20:], pvChange))
```