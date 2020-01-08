> [Wiki](Home) > [Deployment](Deployment) > [Quick Deploy](Quick-Deploy)

Use the deployment script for a quick deploy. It is found in [Ibex Utils](https://github.com/ISISComputingGroup/ibex_utils) and usually copied to the public share.

1. Stop IBEX server
1. Move/remove contents of apps directory (except for mysql)
1. Run the script in `installation_and_upgrade/instrument_install_latest_build_only.bat`.
1. On demo (and any instrument which has labview modules but needs icp binaries) you must then run:

   ```
    ...\EPICS\create_icp_binaries.bat
   ```
