> [Wiki](Home) > [Deployment](Deployment) >[Installing and upgrading MySQL](Installing-and-Upgrading-MySQL)

# Install (mysql version 8.0)

Follow the steps set out in [upgrade mysql to version 8.0](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Upgrading-to-MySQL-8), skipping the step to uninstall MySQL 5.7 if this is a first time install as opposed to an upgrade.


# Install (mysql version 5.7)

**These instructions should only be used if you really intend to install 5.7**. Since [ticket 3506](https://github.com/ISISComputingGroup/IBEX/issues/3506), we are using MySQL 8.0 by default, and so we should no longer need these instructions: 

```
- Download version 5.7.X of the mysql community installer from [mysql site](https://dev.mysql.com/downloads/mysql/5.7.html#downloads)
    - Scroll down to recommended download in GA Release, click Go To Download Page
    - Scroll down to GA Release again and choose one of the two downloads (both are 32bit installers), the smaller one will download as it installs, the larger one downloads everything before starting.
    - Scroll past Login and Sign Up, and just click "No thanks, just start my download" which will finally download the installer.
- Create the folder tree `C:\ProgramData\MySQL\MySQL Server 5.7` (this will cause the installer to ask you to enter a data directory)
- Run the community installer as admin and do the following:
    - Licence page: accept licence
    - Choosing a Setup Type: Server only (use Developer Default for developer machine, the MySQL Workbench is useful)
    - Path Conflict: Set the data dir to `C:\Instrument\var\mysql` (If this page doesn't appear go back to creating the folder tree)
    - Check requirements: click execute (don't worry if there are Python dependencies we will install Python later for something else anyway, just ignore it)
    - Installation: click execute
    - Product Config: next
    - Type and Network: select server machine (Development is also fine I think this is overwritten when using the standard mysql.ini), other defaults are fine
    - Accounts and roles: Use the password from the passwords page
    - Windows Service: Accept defaults
    - Plugin and Extensions: defaults (no document database)
    - Apply Server Config: execute
- Now reopen installer
    - click the spanner icon and turn off update of catalogue
- Record the [installed software](https://github.com/ISISComputingGroup/IBEX/wiki/installed-software)

- Copy `my.ini` from `EPICS\SystemSetup` to `c:\instrument\var\mysql\my.ini` and restart the MySQL service to pick up the new settings

- **Install only not upgrade** run the `config_mysql.bat` batch file in `C:\Instrument\Apps\EPICS\SystemSetup\`.
- **Install only not upgrade** For running tests locally, make sure that you have run `create_test_account.bat` from `C:\Instrument\Apps\EPICS\SystemSetup\` as well.

# Upgrade 5.6.x to 5.6.X or 5.7.x to 5.7.X (where 5.X is the same version)

- run the mysql installer community as admin (find in the start menu)
- update the installer if needed
- click upgrade
- upgrade the product
- Record the [installed software](https://github.com/ISISComputingGroup/IBEX/wiki/installed-software)

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

# Troubleshooting

### The installer is complaining that it needs a new version of the .NET framework

This may just be an issue with the installer rather than with MySQL itself. There is a workaround that lets you avoid having to install a new .NET framework:
1. Use an installer for an older version of MySQL
1. Once complete, run the MySQL Community Installer from the start menu
1. Click on the "Catalog..." button. Follow the prompts to download the latest MySQL product catalog.
1. Once that is done, click on the "Upgrade" button on the MySQL installer home page. Here you can manually select the version you would like to install.

```
