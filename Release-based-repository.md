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
# Associating an instrument with releasae

In instrument computer NDXEMMA-A is running release 12.0.1 for example then open git bash in c:\instrument\apps\epics and run
```
git remote add origin http://control-svcs.isis.cclrc.ac.uk/gitroot/releases/12.0.1/EPICS.git
git checkout -b NDXEMMA-A
git push -u origin NDXEMMA-A
```
