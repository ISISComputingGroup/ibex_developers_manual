# Journal Viewer data

The ISISICP writes run summaries to an XML journal file on the instrument, these files are in c:/data but are then copied to the archive and stored under Instrument/logs/journal. 

The windows archive is smb mounted onto a linux server (`sparrowhawk.nd.rl.ac.uk`, which we maintain) and served to the lab as https://data.isis.rl.ac.uk/journals/ where programs such as Mantid and "standalone journal viewer" can access it. This machine runs on the facilities hyper-v cluster, technology department look after it from a server patching point of view and if there are major operating system issues. Try rebooting the server via the hyper-v console manager, if that doesn't work (e.g. drops into a recovery console talking about disk errors) then contact "Technology IT Support" on outlook. It seems that emails to "Technology IT Support" are only accepted from certain accounts, ISIS experiment controls looking not to be one of them at the moment - i will chase this.    

It is planned to remove the linux link and replace it with a Windows 2019 server some time during 2020.

Journals can be accessed remotely (outside the lab) by users using https://shadow.nd.rl.ac.uk/journals/. More documentation on this is available at `\\isis\shares\isis_experiment_controls\web_dashboard_history.docx`