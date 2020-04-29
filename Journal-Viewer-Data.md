The ISISICP writes run summaries to an XML journal file on the instrument, these files are in c:/data but are then copied to the archive and stored under Instrument/logs/journal. 

The archive is smb mounted onto a linux server (sparrowhawk) and served to the lab as https://data.isis.rl.ac.uk/journals/ where programs such as Mantid and "standalone journal viewer" can access it.

It is planned to remove the linux link and replace it with a Windows 2019 server some time during 2020.
 