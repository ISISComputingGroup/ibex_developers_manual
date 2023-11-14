# Creating repository

If a release repo of the correct version is not shown on https://control-svcs.isis.cclrc.ac.uk/git/ then it can be added as follows

e.g. for 12.0.1
```
robocopy "<kits$>\CompGroup\ICP\Releases\12.0.1\EPICS\.git" "\\control-svcs.nd.rl.ac.uk\git$\releases\12.0.1\EPICS.git" /mir /nfl /ndl
```
then edit EPICS.git\config and  change    `bare=false`   to   `bare=true`

Also Add an extra section at end of the config file
```
[http]
        receivepack = true
```
