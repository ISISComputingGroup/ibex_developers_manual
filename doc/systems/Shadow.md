# Shadow

Shadow is a Linux machine which hosts various services. Credentials are in Keeper. 

## Apache

Apache is running as the main http server, it proxies requests running to other services ie. Jenkins on shadow.

Configuration is located at `/etc/httpd/conf.d/`.

## Jenkins

Shadow hosts the [Jenkins instance.](https://epics-jenkins.isis.rl.ac.uk/) and is the built-in node.   

This runs as a `systemd` service called `jenkins`, its configuration is stored in `/isis2/jenkins/instances/epics/`.

## Site-mirrored Wikis

These are currently being built by Github actions, Shadow executes periodic cron jobs (run `sudo su - isisupdate` then `crontab -e` to see these) which pull the `gh-pages` branches of the Github wikis.

The cron jobs run `/isis/scripts/update_x` where `x` is the name of the wiki.

