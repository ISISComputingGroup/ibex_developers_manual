# Setting up WSL (Windows Subsystem for Linux)

As a developer you will often need to run applications on Linux rather than Windows. You can do this on your
developer machine using WSL (Windows subsystem for Linux).

## Installation

Follow the [official guide](https://learn.microsoft.com/en-us/windows/wsl/install) to install WSL. An `Ubuntu`
distribution is recommended so that Ubuntu-specific commands documented on the wiki can be used, though if
you are more comfortable with another distribution you are free to use it.

## Mounting WSL filesystem from windows

The WSL filesystem can be accessed using `\\wsl$\` on your native Windows machine.

## SSH

After you have {external+sysadmin:doc}`generated an SSH key <services/SSH-keys>`, you may copy both the public
key and the (encrypted with passphrase) private key to `~/.ssh/` in your WSL instance.

### Disabling host-key checking for Ansible

To avoid Ansible asking for host-key verification for each machine it connects to, you can disable the SSH host-key check prompt.

You can use either:
```bash
export ANSIBLE_HOST_KEY_CHECKING=False
``` 
in `~/.bashrc` to disable host-key checking only in Ansible, or

```
Host *
   StrictHostKeyChecking no
```
in `~/.ssh/config` to disable it everywhere.

### Adding SSH key to SSH agent automatically on WSL startup

Add the following lines to `~/.bashrc`:

```bash
env=~/.ssh/agent.env

agent_load_env () { test -f "$env" && . "$env" >| /dev/null ; }

agent_start () {
    (umask 077; ssh-agent >| "$env")
    . "$env" >| /dev/null ; }

agent_load_env

# agent_run_state: 0=agent running w/ key; 1=agent w/o key; 2=agent not running
agent_run_state=$(ssh-add -l >| /dev/null 2>&1; echo $?)

if [ ! "$SSH_AUTH_SOCK" ] || [ $agent_run_state = 2 ]; then
    agent_start
    ssh-add
elif [ "$SSH_AUTH_SOCK" ] && [ $agent_run_state = 1 ]; then
    ssh-add
fi

unset env
```

This will start an agent automatically on login if one is not already started, and add your SSH key to it.
