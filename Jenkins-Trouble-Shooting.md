> [Wiki](Home) > [Trouble Shooting Pages](trouble-shooting-pages) > Jenkins Trouble Shooting

## Ibex-Gui build failure

### Lack of randomness?

Build stops with:
    
    Failed to execute goal org.eclipse.tycho:tycho-surefire-plugin:0.20.0:test (default-test) on project uk.ac.stfc.isis.ibex.targets.tests: An unexpected error occured (return code 13). See log for details. -> [Help 1]

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

Remote desktop to the machine in question and start the Jenkins service using services.msc.