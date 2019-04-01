# Location:

http://ibex-forum.isis.stfc.ac.uk/

# SSH access

Is possible with the domain above, but you must have been added explicitly. Currently Tom W and Freddie have these permissions. You will also need root access to administer discourse.

# Administration

The first port of call should be the discourse documentation/Q&A site: https://meta.discourse.org/

### Starting/stopping discourse

The discourse files are located in the `/var/discourse/` folder. To start discourse, go to that folder and use the command `./launcher run app`. To stop, type `./launcher stop app`.

### SMTP

Discourse uses SMTP to deliver emails. The SMTP settings are in the file `/var/discourse/containers/app.yml`. After editing this file, use `./launcher rebuild app` to rebuild discourse (note, this may wipe user data? not sure about this. be careful.).

Troubleshooting can be done with `./discourse-doctor` which runs a few diagnostics and may help you understand the root cause of an SMTP issue.