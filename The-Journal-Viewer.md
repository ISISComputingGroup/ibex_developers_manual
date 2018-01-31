_(Work in progress)_

# Overview

Contains information on the IBEX journal viewer 

## Setup journal parser on dev machine

1. Disable the slack call in the journal viewer program (comment out the call to sendSlackMessage in C:\Instrument\Apps\EPICS\ISIS\JournalParser\master\JournalParserApp\src\JournalParserSup.cpp). This is because we don't have slack keys on developer machines.
1. Ensure you have the following in your PATH environment variable:
    - C:\Instrument\Apps\EPICS\support\pugixml\master\bin\windows-x64
    - C:\Instrument\Apps\EPICS\support\curl\master\bin\windows-x64
    - C:\Instrument\Apps\EPICS\support\MySQL\master\bin\windows-x64
1. Make the journal parser: cd C:\Instrument\Apps\EPICS\ISIS\JournalParser\master && make clean && make
1. Run upgrade script in upgrade pull request, this will create the relevant SQL schema and users if it doesn't exist
1. Journal parser can be run as `C:\Instrument\Apps\EPICS\ISIS\JournalParser\master\bin\windows-x64\JournalParser.exe <Instrument Name> <Run Number> cycle_00_0 "C:\data" NDW<Instrument Name>`
    - Change `<Instrument Name>` to the name of your instrument
    - Change `<Run Number>` to one that exists in `C:\Data\Journal\journal_00_0.xml` on your machine
    - Note that you need to prefix your instrument with "NDW" in the last argument as this will get stripped by the script