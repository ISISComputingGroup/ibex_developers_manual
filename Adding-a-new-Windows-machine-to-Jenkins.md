These are instructions for adding a new Windows machine as a node to be used by Jenkins.

Follow all the steps outlined in InitialSetup until the project builds.
Delete the EPICS subdirectory that you created in InitialSetup. (Maintaining C:\Instrument\Apps)
Add the builders password to the BUILDERPW environment variable (System variable)
Adding to Jenkins
Go to ​http://epics-jenkins.isis.rl.ac.uk/computer/ and login to Jenkins.
Create a New Node with the Node Name as the computer name, select Dumb Slave.
Give a root directory of C:\Jenkins
Give a label of windows (assuming you are adding a windows machine)
Select the Launch slave agents via Java Web Start under the Launch methods
Save
Select the slave that has just been created and click the Lauch agent from browser on slave button
This should launch a Java window from which select File, Install as Windows Service
See more here: ​https://wiki.jenkins-ci.org/display/JENKINS/Step+by+step+guide+to+set+up+master+and+slave+machines