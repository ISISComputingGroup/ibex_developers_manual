# MySQL

## Installation

Follow the steps set out in [upgrade mysql to version 8.0](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Upgrading-to-MySQL-8), skipping the step to uninstall MySQL 5.7 if this is a first time install as opposed to an upgrade.

## Troubleshooting

### The installer is complaining that it needs a new version of the .NET framework

This may just be an issue with the installer rather than with MySQL itself. There is a workaround that lets you avoid having to install a new .NET framework:
1. Use an installer for an older version of MySQL
1. Once complete, run the MySQL Community Installer from the start menu
1. Click on the "Catalog..." button. Follow the prompts to download the latest MySQL product catalog.
1. Once that is done, click on the "Upgrade" button on the MySQL installer home page. Here you can manually select the version you would like to install.

```
