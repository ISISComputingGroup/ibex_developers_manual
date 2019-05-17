# Location:

http://ibex-forum.isis.stfc.ac.uk/

# SSH access

Is possible with the domain above, but you must have been added explicitly. Currently the following have access:
* Tom W 
* Freddie 
* Dom 

You will also need root access to administer discourse.

# Administration

The first port of call should be the discourse documentation/Q&A site: https://meta.discourse.org/ and the install instructions at https://github.com/discourse/discourse/blob/master/docs/INSTALL-cloud.md

### Starting/stopping discourse

The discourse files are located in the `/var/discourse/` folder. To start discourse, go to that folder and use the command `sudo ./launcher start app`. To stop, type `sudo ./launcher stop app`.

### SMTP

Discourse uses SMTP to deliver emails. The SMTP settings are in the file `/var/discourse/containers/app.yml`. After editing this file, use `./launcher rebuild app` to rebuild discourse (this won't wipe the database, but will cause ~15 minutes of downtime).

Troubleshooting can be done with `./discourse-doctor` which runs a few diagnostics and may help you understand the root cause of an SMTP issue.

### HTTPS

Discourse can use a HTTPS certificate from [let's encrypt](https://letsencrypt.org/). However, this doesn't work as our forum is not available externally, so we have used our own certificates instead, installed as per the documentation at https://meta.discourse.org/t/advanced-setup-only-allowing-ssl-https-for-your-discourse-docker-setup/13847

### Server logs

SSH into the server and use `./launcher logs app` to view logs, or `./launcher enter app` to "enter" the docker container, at which point you can debug the internals of discourse.