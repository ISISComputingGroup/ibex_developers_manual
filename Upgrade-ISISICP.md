> [Wiki](Home) > [Deployment](Deployment) > [Deployment on an Instrument Control PC](Deployment-on-an-Instrument-Control-PC) > [Upgrade ISISICP](Upgrade-ISISICP)

1. Check isisicp is not running
1. Copy to `c:\data\old\isisdae_backup_YYY_MM_DD`
    - `c:\LabVIEW Modules\dae`
    - `c:\data\recovery.run`
1. Open a command window
1. Run:
   ```
      cd c:\LabVIEW Modules\dae
      update_inst.cmd
   ```
1. Check there are no access denied messages except for `ss.ini`
1. Run again from the same directory (you need to do `cd ..`)
1. Should be quicker this time
1. Open a command terminal as administrator
1. Run
   ```
   cd "c:\labview modules\dae"
   register_programs.cmd
   ```


      