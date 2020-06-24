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

## Linux build node (s7cloud) is offline

If the node has rebooted and/or installed an `sshd` update, it may have removed jenkins from its ssh authority. You need to edit `/etc/ssh/sshd_config` and add `jenkins` to the `AllowGroups` line. Then run `service sshd restart` on s7cloud. You can then ask the Jenkins server to relaunch the node.  
