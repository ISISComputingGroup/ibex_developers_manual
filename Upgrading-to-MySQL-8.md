MySQL version 8 is somewhat different to MySQL 5.7. I will aim to document the transition process here

### 1. Uninstall old versions of MySQL. Go to the MySQL installer and uninstall the "MySQL server 5.7" product.

If the installer asks whether you want to remove old data directories, click "yes". Note that this will totally nuke any data that you have stored in your database!

There is no need to uninstall the MySQL installer, so don't tick the "Yes, uninstall the MySQL Installer" tick box.

### 2. Download MySQL 8.0 (zip, not installer)

Go to [the MySQL download page](https://dev.mysql.com/downloads/mysql/) and download the latest stable version of mysql 8.0 as a zip file.

Alternatively, version `8.0.15` is in the kits area under `..\CompGroup\ICP\MySQL`.

### 3. Unzip MySQL 8 to `C:\Instrument\Apps\mysql`

You should end up with a path to MySQL that looks like `C:\Instrument\Apps\mysql\bin\mysql.exe`

### 4. Ensure relevant submodules are up to date and rebuilt if necessary

Various dependencies have changed to be compatible with MySQL 8. As a minimum, you will need updated versions of:
- `EPICS top`
- `EPICS-PVDump` (needs rebuilding as well)
- `EPICS-IocLogServer`
- `EPICS-CSS`
- `GUI` (needs rebuilding as well)

You will need either the branch for `Ticket3506` or master at a point after `Ticket3506` is merged.

### 5. Ensure that your version of CSS (and its archive/alarm tools) is up to date.

- From `C:\instrument\apps\epics` run `create_icp_binaries.bat`
- From `C:\instrument\apps\epics\css\master` remove `css-win.x86_64`
- From `C:\instrument\apps\epics\css\master` run `setup_css.bat`

### 6. Install MySQL8 as a service

Save the following as a batch file somewhere on your computer and then run it **as administrator**. When prompted for passwords, enter the MySQL root password.

```
sc stop MYSQL80 > nul
sc delete MYSQL80 > nul

ping -n 5 127.0.0.1 >nul

pushd C:\Instrument\Apps\mysql\bin

rmdir /s /q C:\Instrument\var\mysql-old
move C:\Instrument\var\mysql C:\instrument\var\mysql-old

mkdir C:\Instrument\var\mysql
mkdir C:\Instrument\var\mysql\data

mkdir "C:\ProgramData\MySQL"
mkdir "C:\ProgramData\MySQL\MySQL Server 8.0"
copy /y "C:\instrument\apps\epics\systemsetup\my.ini" "C:\instrument\apps\mysql\my.ini"

ping -n 5 127.0.0.1 >nul

mysqld.exe --datadir="C:/Instrument/var/mysql/data" --initialize-insecure --console --log-error-verbosity=3

if %errorlevel% neq 0 exit /B %errorlevel%

mysqld.exe --install MYSQL80 --datadir="C:/Instrument/var/mysql/data"

if %errorlevel% neq 0 exit /B %errorlevel%

ping -n 2 127.0.0.1 >nul

sc start MYSQL80
sc config MYSQL80 start=auto

ping -n 2 127.0.0.1 >nul

set /p pass="Enter MYSQL root password: "

mysql.exe -u root -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '%pass%';FLUSH privileges;"

if %errorlevel% neq 0 exit /B %errorlevel%

pushd C:\instrument\apps\epics\systemsetup\

config_mysql.bat

exit /B 0
```

### 7. Check that the MySQL service has installed and is started (and set to automatically start)

Go to services.msc and verify that there is an entry for `MYSQL80` which is running and set to auto-start. Its command line should be `C:\Instrument\Apps\mysql\bin\mysqld.exe --datadir=C:/Instrument/var/mysql/data MYSQL80`

### 8. Run `make iocstartups` from top level EPICS

From `C:\instrument\apps\epics\`, run `config_env.bat && make iocstartups`

Note: a few errors of the form "No such file or directory" are acceptable, this will be fixed as of https://github.com/ISISComputingGroup/IBEX/issues/4080

### 9. Start IBEX server

As verification that the install is correct, check the following:
- Log messages can be searched for from the GUI
- Alarms appear in the alarms view
- The instrument and block archiver webpages are accessible and contain correct values
- The list of IOCs is populated, and running IOCs come up as running in the list
- Do a run, verify that block values appear in `C:\data\xxx00000.log`