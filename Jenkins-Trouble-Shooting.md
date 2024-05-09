> [Wiki](Home) > [Trouble Shooting Pages](trouble-shooting-pages) > Jenkins Trouble Shooting

## Ibex-Gui build failure

### Lack of randomness?

Build stops with:
    
    Failed to execute goal org.eclipse.tycho:tycho-surefire-plugin:0.20.0:test (default-test) on project uk.ac.stfc.isis.ibex.targets.tests: An unexpected error occurred (return code 13). See log for details. -> [Help 1]

In log file 

    java.lang.InternalError: Unexpected CryptoAPI failure generating seed

This might be caused by not enough randomness in the system (not sure). It went away once I logged into the server (which appeared to be new) and re-ran the build.

### General

## No tests Run

Look in console log. We found the lines:

```
RCPTT Runner version: 2.0
An error has occurred. See the log file
C:\Jenkins\workspace\System_Tests\Results\runner-workspace\.metadata\.log.
```

In this log it couldn't read open a given jar file. This appeared to be a problem with the version of RCPPT. So ran manually on reno and fixed the problems.

## Build Agent is OffLine

Remote desktop to the machine in question and start the Jenkins slave service using services.msc. 

If the service fails to start have a look in `C:\Jenkins` at `jenkins-slave.wrapper.log` it shows what the command line is. Run the command line and see the error then fix it. If it is the path to java this is set in `jenkins-slave.xml`. If you have some time you might try and couple this to the system path so that we no longer need the path in here.

## Java is out of date

If the wrong java path is set then the slave will not start. Update the path to the correct version of java in `...\Jenkins\jenkins-slave.xml`.

## Linux build node (`sl7cloud`) is offline

If the node has rebooted and/or installed updates then it may have removed `jenkins` from its ssh authority. You need to edit `/etc/ssh/sshd_config` (e.g. `sudo vi /etc/ssh/sshd_config` and add `jenkins` to the end of the `AllowGroups` line. Then run `sudo service sshd restart` on `sl7cloud`. You can then go to the webpage for `sl7cloud` on Jenkins and ask it to `relaunch agent` on the node.  

To log onto the node you need to `ssh` to its real hostname - you can get this by clicking on the `sl7cloud` node in jenkins, going to `configure` and then you will see a `<something>.nubes.stfc.ac.uk` hostname to use. Log in with fed id, authentication is via certificate. You should be able to sudo from your account. 

Log into the web page `https://cloud.stfc.ac.uk/` for an overview of all our VMs and `https://openstack.stfc.ac.uk/` for a more detailed management interface

## Builds failing to check out

If a jenkins job (often epics-static-clean on NDWVEGAS) is failing to run and near the start you see something like
```
21:47:24   > git submodule foreach --recursive git reset --hard # timeout=10
21:51:27  ERROR: Error fetching remote repo 'origin'
21:51:27  hudson.plugins.git.GitException: Failed to fetch from https://github.com/ISISComputingGroup/EPICS.git
21:51:27  	at hudson.plugins.git.GitSCM.fetchFrom(GitSCM.java:909)
21:51:27  	at hudson.plugins.git.GitSCM.retrieveChanges(GitSCM.java:1131)
21:51:27  	at hudson.plugins.git.GitSCM.checkout(GitSCM.java:1167)
21:51:27  	at org.jenkinsci.plugins.workflow.steps.scm.SCMStep.checkout(SCMStep.java:125)
21:51:27  	at org.jenkinsci.plugins.workflow.steps.scm.SCMStep$StepExecutionImpl.run(SCMStep.java:93)
21:51:27  	at org.jenkinsci.plugins.workflow.steps.scm.SCMStep$StepExecutionImpl.run(SCMStep.java:80)
21:51:27  	at org.jenkinsci.plugins.workflow.steps.SynchronousNonBlockingStepExecution.lambda$start$0(SynchronousNonBlockingStepExecution.java:47)
21:51:27  	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511)
21:51:27  	at java.util.concurrent.FutureTask.run(FutureTask.java:266)
21:51:27  	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
21:51:27  	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
21:51:27  	at java.lang.Thread.run(Thread.java:748)
21:51:27  Caused by: hudson.plugins.git.GitException: Command "git submodule foreach --recursive git reset --hard" returned status code 128:
```
This is usually caused by an `index.lock` file not having been removed correctly during a previous git operation. This file should only exist when git is running, if there are no git processes executing on that repository then there should be no `index.lock` file present.
 
You can search the workspace for these files, but there is a now a program to do this for you (which also checks for running git processes). See `\\isis\shares\ISIS_Experiment_Controls\git_lock_clean` 

## [Office365connector] Matched status 'FAILURE' for webhook with name 'Office 365'.

This is not an error with the `Office365connector`, it is reporting that the connector is being run because it had been configured to match a 'FAILURE' state and the build had failed. You will likely see this message at the end of most failed builds, the real reason for the build failure will be earlier in the jenkins log file.  

## Builds not Building on 1926

Connect to the computer and start the Jenkins Slave, the Beckhoff tests mean this has to be done manually on this system