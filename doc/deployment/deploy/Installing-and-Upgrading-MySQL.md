# MySQL

## Installation

There is a script to automatically install MySQL 8. You can find it in `\\isis\shares\ISIS_Experiment_Controls_Public\ibex_utils\installation_and_upgrade\upgrade_mysql.bat`

## Troubleshooting

### The installer is complaining that it needs a new version of the .NET framework

This may just be an issue with the installer rather than with MySQL itself. There is a workaround that lets you avoid having to install a new .NET framework:
1. Use an installer for an older version of MySQL
1. Once complete, run the MySQL Community Installer from the start menu
1. Click on the "Catalog..." button. Follow the prompts to download the latest MySQL product catalog.
1. Once that is done, click on the "Upgrade" button on the MySQL installer home page. Here you can manually select the version you would like to install.

```
