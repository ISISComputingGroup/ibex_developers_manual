The ISISICP writes run summaries to an XML journal file on the instrument, these files are in c:/data but are then copied to the archive and stored under Instrument/logs/journal. 

The windows archive is smb mounted onto a linux server (sparrowhawk, which we maintain) and served to the lab as https://data.isis.rl.ac.uk/journals/ where programs such as Mantid and "standalone journal viewer" can access it.

It is planned to remove the linux link and replace it with a Windows 2019 server some time during 2020.

Journals can be accessed remotely by users using https://shadow.nd.rl.ac.uk/journals/. More documentation on this is available at `\\isis\shares\isis_experiment_controls\web_dashboard_history.docx`