> [Wiki](Home) > [Project tools](Project-tools) > [Working with git and github](Working-with-git-and-github) > Git and SSH key authentication

By default our workflows expect token based authentication and https connections to GitHub. If you are stuck in your ways and wish to use SSH authentication, the following will work. It assumes you have already [generated an SSH key, placed it in .ssh, and added it to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh). 

# Git configuration
You could make your developer set up work by simply replacing all of the remotes for your git repositories with addresses in the ssh connection format. However, our processes often overwrite these and there are a large number of sub-modules which would also need changing. Luckily git has a configuration option that will globally rewrite these addresses for you. Simply add the following to your global git configuration:

```
[url "ssh://git@github.com/"]
    insteadOf = https://github.com/
    pushInsteadOf = https://github.com/`
```

_(Remember if you use multiple instances of git for some reason, ensure that you add it to all the ones you wish to use for IBEX development!)_

If you grow tired of entering your passphrase every time you run a git command - follow the configuration instructions bellow. 

# Scripts that contain git commands
The above will work fine until you encounter a script which runs a git command (possibly only those using the python git library), this will not prompt you for your ssh key passphrase and so will fail with an authentication error. To overcome this, you need to already have an ssh agent running and have added your key. To do this you can do the following

## Initial configuration
You need to configure your environment to launch an ssh agent and add your key. It will do this every time you open a new window - prompting you to enter your passphrase. To do this add the following to ~/.bash_profile (or if you don't have one, create one with this in):

```
eval `ssh-agent`
ssh-add
```

## Every time you wish to run a script

### To run a script in Git Bash
Having followed the configuration steps above, simply open git bash (enter your passphrase) and run your script

### To run a script in Windows Command Prompt
Having followed the configuration steps above, open git bash (enter your passphrase) and run `start cmd`. Run your script in the window that opens, it will use the ssh agent that started when you started Git Bash.

### To run a script in an EPICS terminal
Having followed the configuration steps above, open git bash (enter your passphrase) and run `start /c/Instrument/Apps/EPICS/config_env
`. Run your script in the window that opens, it will use the ssh agent that started when you started Git Bash.