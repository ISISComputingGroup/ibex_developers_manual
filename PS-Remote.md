> [Wiki](Home) > [The Backend System](The-Backend-System) > [Useful tools](Useful-tools) > Powershell Remote

Remote Powershell can be used on the NDX machines to run arbitrary command line scripts remotely. This could be useful for example if you want to run something as the database admin without having to interrupt instruments running.

**WARNING: This is obviously very dangerous - you will have the power to run any commands and could affect the running instrument quite severely.**

### How to set your machine up

1. Start a PowerShell terminal as administrator (found under `Windows PowerShell` in the Start Menu)
2. Run `Enable-PSRemoting` you should see an output like:
```
WinRM has been updated to receive requests.
WinRM service type changed successfully.
WinRM service started.

WinRM has been updated for remote management.
WinRM firewall exception enabled.
```
3. Run `Set-Item -Path WSMan:\localhost\Client\TrustedHosts -Value * -Force`.  This will allow your machine to access others.

### Using Powershell Remote

Once the above setup has been done you can use PowerShell Remote as follows:
1. Start a PowerShell terminal (does not need to be admin).
2. Run `$cred=get-credential` and you will see a pop up box asking for you to input some credentials.
3. Input the credentials for an instrument admin account (remember to put in an instrument machine as the domain but this can be any instrument machine, the credentials will still work for remote access as long as the machine has the same administrator account).
4. Run `Invoke-Command -Credential $cred  instrument_machine { command }`, where _`command`_ is the PowerShell command or script you'd like to run on the remote _`instrument-machine`_ (standard DOS commands can be executed with `{ cmd /c` _`command`_ }).

### Accessing lots of instruments

There are some useful power shell scripts in the isis private share `...private_git_repositories\private_scripts.git` including one that helps remote to instrument machines and run the same command.
