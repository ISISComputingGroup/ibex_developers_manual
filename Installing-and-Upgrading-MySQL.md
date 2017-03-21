*Install first time*

- Copy the installer from `\\isis\inst$\Kits$\External\BuildServer(ndwvegas)\mysql-installer-community-X.X.X.0.msi` to your local machine.
- Create a command windows as an admin
- cd to where you copied it to
- Run in that window; with passwords replaced by standard password and versions by current version.
    `msiexec.exe /qb- /l*vx MySQL.log REBOOT=ReallySuppress UILevel=67 ALLUSERS=2 CONSOLEARGS="install server;5.7.17;x64:*:type=config;openfirewall=true;generallog=true;binlog=true;datadir=""C:\Instrument\var\mysql"";serverid=1;enable_tcpip=true;port=3306;rootpasswd=<password>:type=user;username=root;password=<password>;role=DBManagerY" /I mysql-installer-community-5.7.17.0.msi`
- Ensure that you have `C:\Instrument\Var\mysql\my.ini` from the set up directory (`...EPICS\SystemSetup`).
- If this doesn't work, i.e. the installer is installed but mysql is not (it does not appear in program files) then instead (I have not yet done this so this may need some evaluation). This happened on IRISTest but not Demo:
    - run the "mysql installer" in admin mode
    - install the correct version of mysql
    - configure mysql accepting defaults
    - stop the service
    - move the data files from `c:\program data\mysql...data` to `C:\Instrument\Var\mysql\data`
    - Create a new service: `"C:\Program Files\MySQL\MySQL Server 5.6\bin\mysqld" --install MySQL56 --defaults-file="C:\Instrument\Var\mysql\my.ini"
    - Set the user running the service: LogOn tab -> This account to NETWORK SERVICE no password (this removes the notes and when you click start adds them back in)
    - Start the service

- **Install only not upgrade** run the `config_mysql.bat` batch file in `C:\Instrument\Apps\EPICS\SystemSetup\`.
- **Install only not upgrade** For running tests locally, make sure that you have run `create_test_account.bat` from `C:\Instrument\Apps\EPICS\SystemSetup\` as well.

*Upgrade 5.6.x to 5.6.X*

- run the mysql installer as admin
- update the installer if needed
- click upgrade
- upgrade the product

*Upgrade between 5.6 and 5.7*
- mysql -u root -p --execute="SET GLOBAL innodb_fast_shutdown=0"
- mysqladmin -u root -p shutdown (stops down service)

- open MySQL installer under administrator account
  - If prompted to upgrade installer click "Yes" (Ignore windows error about not running correctly)
  - remove 5.6.X MySQL server but *do not delete data*
- yes to remove MySQL installer
- yes reboot (if asked)
- copy the mysql.ini file from the set up directory (`...EPICS\SystemSetup`) to `C:\Instrument\Var\mysql\my.ini`
- Install the new version as for first time install. But when it gets to starting service while it is waiting (spinning character)
    - upgrade the database using `"C:\Program Files\MySQL\MySQL Server 5.7\bin\mysql_upgrade" -u root -p --force`
    - restart the windows service
    - the installation should now finish

The above process seems flakey I am leaving the below until we can find a process which works:
```
   - Install the MySQL Installer from the msi. This should be done with admin privileges. **NB: You are installing the installer, not MySQL itself**
- *upgrade* Check the installer version it should be 1.x if it isn't
    - start wmic as an admin
    - run `product where name="MySQL Installer for Windows - Community" call uninstall` if this does not match the name find its name using `product get name`
    - press Y to uninstall
    - then start from scratch

- Run the MySQL installer, again with admin privileges (from run menu type mysql installer)
- *upgrade* Click remove and select the currently installed `MySql Server`, execute and yes.
- *upgrade* On `Remove data folder ...` click No
- *upgrade* Next and reboot as advised
- Click "Add" to add a new product
- Select the version of MySQL server 64-bit shown in the current [dev notes](https://github.com/ISISComputingGroup/IBEX/wiki/ReleaseNotes_Dev) and execute.
    - If the version is older than the one you want to install
        - click *Catalog* to update it
        - Execute
        - Do not upgrade the installer
        - Next and Finish
    - If the version is newer then you need to remove the current GA filter in the filter box
- Do not configure you instance (I think) exit.
- Configure mysql (from an admin windows)
    - upgrade you schema with `"C:\Program Files\MySQL\MySQL Server 5.7\bin\mysql_upgrade" -u root -p --force`
    - Setup a service `"C:\Program Files\MySQL\MySQL Server 5.6\bin\mysqld" --install MySQL57 --defaults-file="C:\Instrument\Var\mysql\my.ini"`
    - run as admin `services.msc` and set the user to `NETWORK SERVICES` (set the password to blank to do this)
    - Restart the service
This is where I am, but it needs thinking about I am not sure I want to do this on a machine.

- Click through the pages and set the following:
   - For "Choosing a Configuration Type," select "Server Machine"
   - Use the password from the password page

On the next page, set the Data Directory to `C:\Instrument\Var\mysql`

After it installs you will get to the "Type and Networking" page, for the "Config Type" choose "Server Machine".

Leave TCP/IP access enabled.

On the "Accounts and Roles" page make sure you use the agreed password for root. 
If you don't know what that password is you should be able to find it on the passwords page.

Under "Windows Service" make sure "Start the MySQL Server at System Startup" is **checked**

```
