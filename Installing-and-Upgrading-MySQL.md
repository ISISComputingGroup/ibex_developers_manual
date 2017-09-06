> [Wiki](Home) > [Deployment](Deployment) >[Installing and upgrading MySQL](Installing-and-Upgrading-MySQL)

# Install first time

- Download the latest mysql community installer (correct version) from [mysql site](https://dev.mysql.com/downloads/mysql/)
- Create the folder tree `C:\ProgramData\MySQL\MySQL Server 5.7` (this will cause the installer to ask you to enter a data directory)
- Run the community installer as admin and do the following:
    - Licence page: accept licence
    - Type and Networking: Standalone MySqlServer
    - Server type: select server only (Development is good if you want mysql workbench but will require more checks later)
    - Path Conflict: Set the data dir to `C:\Instrument\var\mysql` (If this page doesn't appear go back to creatig the folder tree)
    - Installation: click execute
    - Product Config: next
    - Type and Network: Server (dev is also acceptable), other defaults are fine
    - Account: Use the password from the passwords page
    - Windows Service: Accept defaults
    - Plugin and Extensions: defaults (no document database)
    - Apply Server Config: execute
- Now reopen installer
    - click the spanner icon and turn off update of catalogue

- **Install only not upgrade** run the `config_mysql.bat` batch file in `C:\Instrument\Apps\EPICS\SystemSetup\`.
- **Install only not upgrade** For running tests locally, make sure that you have run `create_test_account.bat` from `C:\Instrument\Apps\EPICS\SystemSetup\` as well.

# Upgrade 5.6.x to 5.6.X or 5.7.x to 5.7.X (where 5.X is the same version)

- run the mysql installer as admin
- update the installer if needed
- click upgrade
- upgrade the product

# Upgrade between 5.6 and 5.7

Experimental:

- `cd C:\Program Files\MySQL\MySQL Server 5.6\bin`
- mysql -u root -p --execute="SET GLOBAL innodb_fast_shutdown=0"
- mysqladmin -u root -p shut
down (stops down service)
- backup mysql data base data files

- open MySQL installer under administrator account
  - If prompted to upgrade installer click "No" (Ignore windows error about not running correctly)
  - remove 5.6.X MySQL server but *do not delete data*
- yes to remove MySQL installer
- yes reboot (if asked)
- copy the my_for_5.7.ini file from the set up directory (`...EPICS\SystemSetup`) to `C:\Instrument\Var\mysql\my.ini`
- Install the new version as for first time install. But when it gets to starting service while it is waiting (spinning character)
    - upgrade the database using `"C:\Program Files\MySQL\MySQL Server 5.7\bin\mysql_upgrade" -u root -p --force`
    - restart the windows service
    - the installation should now finish
