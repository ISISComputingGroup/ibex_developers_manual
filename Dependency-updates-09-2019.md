*Dependency update time!*

GUI
- Note: at no stage should you uninstall java 8. It is still required for the IBEX server.
- Download a recent version of eclipse, either from https://www.eclipse.org/downloads/packages/ (select "Eclipse IDE for RCP and RAP Developers") or from `\\isis\inst$\Kits$\CompGroup\ICP\Developer Tools`. You probably want 2019-06 as this is the most recent stable version. _Earlier versions will fall over with obscure, hard-to-diagnose bugs!_
- Download the latest Java 11 hotspot JDK from https://adoptopenjdk.net/?variant=openjdk11&jvmVariant=hotspot and install it. I would recommend not adding it to path and not setting `JAVA_HOME`.
- Ensure you have a maven version >=3.6.0, but not 3.6.1 as this has a bug. Double check you really do have the correct version by spawning a new command prompt and running `mvn -v`
- Pull the latest version of the GUI using `git checkout master && git pull`
- In eclipse, import the project as usual (if you have an "old" import, you probably want to remove it and reimport)
- In eclipse, go to Window -> preferences -> java -> installed JREs and select the JDK directory you installed above
- Then in the same preferences dialog go to "compiler" and turn "compliance level" up to 11.
- Set target platform and run as usual (in theory)

MySQL
- Run `services.msc` as admin
- Stop mysql service
- Delete `C:\instrument\apps\mysql`
- Copy version from `\\isis\inst$\Kits$\CompGroup\ICP\MySQL` locally
- Unzip it and move it to the same location as the old one (the path to `mysql.exe` should be `C:\instrument\apps\mysql\bin\mysql.exe`)
- Copy `C:\instrument\apps\epics\systemsetup\my.ini` to `C:\instrument\apps\mysql`
- Restart MySQL service

ActiveMQ
- `cd c:\instrument\apps\epics\isis\activemq\master && git checkout master && git pull`

IOC log server
- `cd c:\instrument\apps\epics\isis\ioclogserver\master && git checkout master && git pull`
- `clean-log-server.bat && cd .. && build-log-server.bat`

genie_python
- `cd C:\instrument\apps\python`
- `git checkout master && git pull`
- `cd package_builder`
- `dev_build_python.bat`