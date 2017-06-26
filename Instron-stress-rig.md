# Setup

The Instron stress rig is a National Instruments GPIB device. It requires some special setup to get going:

- The Ethernet GPIB box requires a driver for the LabVIEW driver. This can be installed from \olympic\Babylon5\Public\GHowells\NI GPIB
- Run the installer as an administrator, accept the defaults. It will unzip, then install. It takes a while to install.
- You then need to set up the ENET box, Gareth or Freddie can show you how to set this up
- LabVIEW vi located at : C:\LabVIEW Modules\Instruments\ENGINX\Stress Rig\Stress Rig - System Functions.llb\Stress Rig - 100 kN Stress Rig.vi
- On running the vi, you will get some dialogs – just ok through them. The indicators should then be updating.
- If you can't get the labview to talk at all, the stress rig might need to be power cycled. @GDH-ISIS and @FreddieAkeroyd know how to do this.