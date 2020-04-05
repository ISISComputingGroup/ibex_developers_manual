> [Wiki](Home) > [Deployment](Deployment) > - [How to deploy IBEX to training machine](IBEX-Deployment-on-Training-machine)

Training machines have there own deployment script. It is similar but not the same as the usual instrument upgrade/deployment. It removes all previous traces of IBEX on the system and then installs it as if it was a clean machine. It also installs some training material and a training config.

Steps:

1. Make sure that the install script has been pulled it is in `...isis experiment controls public share\ibex_utils`
1. Open a command line inside the `installation_and_upgrade` folder
1. Run `training_update.bat`
1. Follow the steps until the end

On register step
Copy contents of C:\Instrument\Apps\EPICS\ICP_Binaries\isisdae\x64\visa to C:\Instrument\Apps\EPICS\ICP_Binaries\isisdae\x64\Release


