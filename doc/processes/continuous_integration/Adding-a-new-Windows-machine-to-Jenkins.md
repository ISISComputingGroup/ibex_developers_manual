# Adding a new Windows machine to Jenkins

These are instructions for adding a new Windows machine as a node to be used by Jenkins.

### Initial Preparation

* First set up the machine so it can be used to build the back-end system manually by following these [instructions](/overview/First-Time-Build)

* After you have registered the ISISICP go into `c:\Instrument\Apps\EPICS\ICP_Binaries\isisdae` and read `README_isisicp_reg.txt` in particular you will probably need to add the the account running jenkins to the windows group mentioned 

* Delete the EPICS subdirectory that was created in the previous step (maintaining C:\Instrument\Apps)

### Adding to Jenkins

* Go to ​https://epics-jenkins.isis.rl.ac.uk/computer/ and log in to Jenkins

* Create a `New Node` with the Node Name as the computer name, select 'Permanent Agent'

* Set a root directory of C:\Jenkins

* Set a label of 'windows'

* Select the `Launch agent by connecting it to the controller`

* Save

* Select the slave that has just been created and make a note of secret. For an initial test make a note of the curl and java commands from `Run from agent command line: (Windows)`

* in a command window in c:\jenkins run the curl and java commands. These can be put into a bat file for interactive running.

## setup as service

We use https://github.com/jenkinsci/windows-slave-installer-module and https://github.com/winsw/winsw the relevant files are in 
`\\isis\shares\ISIS_Experiment_Controls_Public\third_party_installers\latest_versions\builderserver` to copy to `c:\Jenkins`   

Copy `jenkins-agent.exe` and `jenkins-agent.xml` into same directory on the target machine e.g. `c:\jenkins`

Edit `jenkins-agent.xml` and change  https://epics-jenkins.isis.rl.ac.uk/computer/COMPUTER/jenkins-agent.jnlp and the SECRET field to the same as they are from the Jenkins' Node page, add `-workDir` argument of `c:\jenkins`
COMPUTER should be capitalised in same way as written on Jenkins.

Open an admin cmd window and run `jenkins-agent.exe install` and then `servies.msc`

Find the jenkins service in the Service Manager window on the machine, and change it to run as `isis\ibexbuilder` rather than local service account, you'll need to enter `ISISBuilder` password.

Then run start service from the Service Manager window.

### configure jenkins-agent.xml

We need a longer git checkout time than default of ten minutes. To adjust for submodule operations see  https://plugins.jenkins.io/git/#plugin-content-default-timeout  which basically means you need to add `-Dorg.jenkinsci.plugins.gitclient.Git.timeOut=60` to both the jenkins server and the client args. On the java command line put it before the `-jar` option as otherwise it gets passed as an argument to the jar file

<a name="jenkins_gui_tests"></a>
### Special Notes on Jenkins for GUI Tests

The GUI test currently run on NDWRENO. The test behaviour is different when Jenkins is running as a service, so instead it is run as a command from a batch file. The batch file is located on the desktop for the user builder. On first start up this shows running in a console Window, but this is unintentionally hidden the the system tests. (I am not sure that this is true anymore - John)

In case NDWRENO goes offline the command to run the slave is also shown at [http://epics-jenkins.isis.rl.ac.uk/computer/ndwreno/](http://epics-jenkins.isis.rl.ac.uk/computer/ndwreno/).

System tests need the RCPTT plugin this is downloaded from here (http://www.eclipse.org/rcptt/download/), currently on 2.1.0. Once downloaded extract them to C:\Jenkins\RCPTT_Runner (set in runner.cmd). The current version appears to need java 1.8 and because the instrument add the latest JDK you need to install JDK 1.8. The version of java that jenkins slave uses is set in `jenkins-clas.xml` in `c:\jenkins`.
