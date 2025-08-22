# Journals

```{toctree}
:glob:
:titlesonly:
:maxdepth: 1
:hidden:

journal_viewer/*
```

Contains information on the IBEX journal viewer. This feature is intended to provide users with easy access to the journal data via a view integrated into the IBEX client, that shows a table with data from journal files for the current instrument and cycle. This solution is implemented completely independently of pre-existing journal viewers and consists of:
- A MySQL database containing run information
- A journal parser that populates the database with data read from XML journal files in the machine's `C:\Data\` directory
- An external webpage served by a linux server see [here](journal_viewer/Journal-Viewer-Data) 
- An IBEX perspective searching, reading and displaying data from the database.

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

## Repopulate Journals following truncation
To add journal entries back on an instrument following a truncation (e.g. if there is the following nagios error: `EPICS MYSQL Journal Entries`),  run `[group public share]\JournalParser\add_journal_entries.bat` on the instrument. 
