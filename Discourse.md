# Location:

http://ibex-forum.isis.stfc.ac.uk/

# SSH access

Is possible with the domain above, but you must have been added explicitly. Currently Tom W and Freddie have these permissions. You will also need root access to administer discourse.

# Administration

The first port of call should be the discourse documentation/Q&A site: https://meta.discourse.org/ and the install instructions at https://github.com/discourse/discourse/blob/master/docs/INSTALL-cloud.md

### Starting/stopping discourse

The discourse files are located in the `/var/discourse/` folder. To start discourse, go to that folder and use the command `./launcher run app`. To stop, type `./launcher stop app`.

### SMTP

Discourse uses SMTP to deliver emails. The SMTP settings are in the file `/var/discourse/containers/app.yml`. After editing this file, use `./launcher rebuild app` to rebuild discourse (this won't wipe the database, but will cause ~15 minutes of downtime).

Troubleshooting can be done with `./discourse-doctor` which runs a few diagnostics and may help you understand the root cause of an SMTP issue.

### HTTPS

Discourse can use a HTTPS certificate from [let's encrypt](https://letsencrypt.org/). Edit the `/containers/app.yml` uncommenting the lines relevant to SSL near the top of the file.

Note: this currently doesn't work as Let's encrypt doesn't like the DNS response from our servers.