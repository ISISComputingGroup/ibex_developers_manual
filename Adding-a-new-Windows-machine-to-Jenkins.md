These are instructions for adding a new Windows machine as a node to be used by Jenkins.

### Initial Preparation

* First set up the machine so it can be used to build the back-end system manually by following these [instructions](First-time-installing-and-building-(Windows))

* Delete the EPICS subdirectory that was created in the previous step (maintaining C:\Instrument\Apps)

* Add the builders password as a environment variable (system variable) called BUILDERPW

### Adding to Jenkins

* Go to ​http://epics-jenkins.isis.rl.ac.uk/computer/ and log in to Jenkins

* Create a New Node with the Node Name as the computer name, select 'Dumb Slave'

* Set a root directory of C:\Jenkins

* Set a label of 'windows'

* Select the Launch slave agents via Java Web Start under the Launch methods

* Save

* Select the slave that has just been created and click the 'Launch agent from browser on slave' button

* This should launch a Java window from which, select File, Install as Windows Service

See the Jenkins [website](​https://wiki.jenkins-ci.org/display/JENKINS/Step+by+step+guide+to+set+up+master+and+slave+machines) for more information.

<a name="jenkins_gui_tests"></a>
### Special Notes on Jenkins for GUI Tests

The GUI test currently run on NDWRENO. The test behaviour is different when Jenkins is running as a service, so instead it is run as a command from a batch file. The batch file is located on the desktop for the user builder. On first start up this shows running in a console Window, but this is unintentionally hidden the the system tests.

In case NDWRENO goes offline the command to run the slave is shown at [http://epics-jenkins.isis.rl.ac.uk/computer/ndwreno/](http://epics-jenkins.isis.rl.ac.uk/computer/ndwreno/).

