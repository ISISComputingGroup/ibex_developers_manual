# Automated Install

There is a script to automatically install MySQL 8. You can find it in `<public share>\ibex_utils\installation_and_upgrade\upgrade_mysql.bat`.
Ask another member of the team if you do not know where to find the share.

# Manual install (legacy instructions)

MySQL version 8 is somewhat different to MySQL 5.7. I will aim to document the transition process here

### 1. Uninstall old versions of MySQL. Go to the MySQL installer and uninstall the "MySQL server 5.7" product.

If the installer asks whether you want to remove old data directories, click "yes". Note that this will totally nuke any data that you have stored in your database!

There is no need to uninstall MySQL Workbench or the MySQL installer, so don't tick the "Yes, uninstall the MySQL Installer" tick box.

### 2. Download MySQL 8.0 (zip, not installer)

Go to [the MySQL download page](https://dev.mysql.com/downloads/mysql/) and download the latest stable version of mysql 8.0 as a zip file.

Alternatively, there is a version in the kits area under `<kits area on share>\CompGroup\ICP\MySQL`. Pick the version with the largest major/minor/patch versions if there are multiple versions available.

### 3. Unzip the inner folder of MySQL 8 to `C:\Instrument\Apps\mysql`

You should end up with a path to MySQL that looks like `C:\Instrument\Apps\mysql\bin\mysql.exe`

### 4. Install MySQL8 as a service

Save the following as a batch file somewhere on your computer and then run it **as administrator**. It is advised to launch this from within a command prompt (also ran as administrator) so you can debug potential errors as it runs. When prompted for passwords, enter the MySQL root password. The MySQL root password is stored on the ISIS sharepoint, which you will need access to. 

```
sc stop MYSQL80 > nul
sc delete MYSQL80 > nul

ping -n 5 127.0.0.1 >nul

pushd C:\Instrument\Apps\mysql\bin

rmdir /s /q C:\Instrument\var\mysql-old
move C:\Instrument\var\mysql C:\instrument\var\mysql-old

mkdir C:\Instrument\var\mysql
mkdir C:\Instrument\var\mysql\data

copy /y "C:\instrument\apps\epics\systemsetup\my.ini" "C:\instrument\apps\mysql\my.ini"

ping -n 5 127.0.0.1 >nul

mysqld.exe --datadir="C:/Instrument/var/mysql/data" --initialize-insecure --console --log-error-verbosity=3

if %errorlevel% neq 0 exit /B %errorlevel%

mysqld.exe --install MYSQL80 --datadir="C:/Instrument/var/mysql/data"

if %errorlevel% neq 0 exit /B %errorlevel%

ping -n 2 127.0.0.1 >nul

sc start MYSQL80
sc config MYSQL80 start= auto

ping -n 2 127.0.0.1 >nul

set /p pass="Enter MYSQL root password: "

mysql.exe -u root -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '%pass%';FLUSH privileges;"

if %errorlevel% neq 0 exit /B %errorlevel%

pushd C:\instrument\apps\epics\systemsetup\

config_mysql.bat

exit /B 0
```

The MySQL service will fail to setup if you are trying to install MySQL version 8 using a MySQL version 5 my.ini file. This will occur if the EPICS TOP repository is not up to date (see step 4.). To fix this, navigate to `C:\Instrument\Apps\EPICS\` and run `git pull`.

### 5. Check that the MySQL service has installed and is started (and set to automatically start)

Go to services.msc and verify that there is an entry for `MYSQL80` which is running and set to auto-start. Its command line should be `C:\Instrument\Apps\mysql\bin\mysqld.exe --datadir=C:/Instrument/var/mysql/data MYSQL80`