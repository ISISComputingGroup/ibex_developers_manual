# Remote IOCs

Some IOCs run on remote systems (e.g. Tritons after [ticket 3125](https://github.com/ISISComputingGroup/IBEX/issues/3125)). This page describes the *instrument* archiver functionality for these IOCs.

There are essentially 3 places where data could be logged:

# On the remote PC

We are not doing this as there are concerns about how we would monitor resource use for a PC which is not on the network. It could be done in future by running a normal MySQL / archiver setup on the remote PC.

# Centrally

This is, at least initially, where all data from all remote IOCs will be being archived.

The central archiver is running as a service on `control-svcs` (passwords on the usual sharepoint page). The archiver is in `/home/epics/EPICS/CSS/master/ArchiveEngine/` and the settings are in `archive_config_central.xml`.

The archiver is running as a service, after modifying the archive configuration file it needs to be restarted using `systemctl restart epics_archiver.service`

# Onto the instrument archive

This is not being done initially as it is hard. What would need to be done to make this happen is:
- Some service running on the instrument PCs that the remote IOC can push archived PVs to.
- This service would need to merge the archived PVs from all connected remote IOCs
- The service would probably need to translate the remote PVs (`ME:...`) to their local aliases (`IN:...`).
- The instrument archive would then need to be reloaded with these changed settings