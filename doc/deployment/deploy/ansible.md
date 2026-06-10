# Ansible

We are moving towards using [Ansible](https://github.com/ISISComputingGroup/IBEX_utils) for both initial configuration of machines as well as deployment. 

The main repository for this is [here](https://github.com/ISISComputingGroup/ansible-playbooks) which contains our configuration, inventories, playbooks, roles and tasks. 

[Ansible playbooks](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_intro.html) used for remotely automating tasks on NDX machines and other machines we look after. 

These run on your own computer (the control node) and orchestrate steps on remote machines. 

Playbooks should be idempotent, ie. they can be run multiple times and will always result in the same output - this is marked in Ansible as `OK`/`Changed` if a task is skipped or changed respectively. For example, checking that a dependency is a certain version and skipping a set of tasks to update it (which may remove the previous version) and so on. This means that the "deploy" playbook can be run absolutely everywhere, and machines that are already up to date will get most tasks skipped completely. Most Ansible modules are built to be idempotent by default. 

We are working towards these playbooks being the declarative steps to provision an instrument machine so it can easily be (re)created. As a developer you should keep this in mind - Ansible playbooks _can_ be used for one-shot rollouts of a specific set of tasks, but we should make them repeatable. This repo should not become a 'dumping ground' of playbooks we've written to roll out a certain change - they should be applied to the [blueprints of an instrument machine](https://github.com/ISISComputingGroup/ansible-playbooks/blob/main/windows/instrument_deploy.yaml) so we can use them again. 

## Setup 
Preliminary steps to run these: 
1. If you haven't already, set up a keeper account with access to our group's passwords.
1. Make sure your ssh public keys (which should be stored [here](https://github.com/ISISComputingGroup/keys)) are deployed to instruments - see below for the playbook that does this
1. Set up the WSL if you're using a Windows control node - [Ansible does not support running on a windows control node natively](https://docs.ansible.com/projects/ansible/latest/installation_guide/intro_installation.html#control-node-requirements). You will need your [SSH keys registered in the WSL](https://devblogs.microsoft.com/commandline/sharing-ssh-keys-between-windows-and-wsl-2/). If you are running Linux you can install ansible natively.
1. Install Ansible, including plugins we require, by:
  1. `sudo snap install astral-uv --classic`
  1. `uv venv` & `source .venv/bin/activate`
  1. `uv pip install -r requirements.txt`
1. Install the galaxy collections and roles by running `ansible-galaxy install -r requirements.yml`
1. Add the DNS search suffix (`isis.cclrc.ac.uk`) to `/etc/resolv.conf` (to edit the file, use e.g. `nano /etc/resolv.conf`) by adding the following line: 

```
...
search isis.cclrc.ac.uk
...
```

To test if this works, run an [adhoc command](#Ad-hoc-commands) and use the module `ping` (for linux machines) or `win_ping` (for windows machines ie. NDXes) to test for aliveness. 

PRs will be linted by CI. To run this locally run `ansible-lint` - this is included in `requirements.txt`. Configuration is set by `.ansible-lint`.

## Hosts.yaml
This is the main [inventory file](https://docs.ansible.com/projects/ansible/latest/inventory_guide/intro_inventory.html) which lists hosts in groups such as by target station and/or by deploy group. It is contained in the inventory directory.

to limit running a playbook to just TS1 instruments, for example, you can use `ansible-playbook playbook.yaml --limit ts1`. This works because `ts1` is a host group in the inventory file. 


## Windows-only playbooks (`windows/`)

### Notes

These playbooks will prompt for a host group to run on, equivalent to (and taking precedence over) `--limit` as a command line argument. 

As an example, to run the playbook on all NDXes other than `NDXENGINX`, enter `ndxes,!NDXENGINX` - this syntax is documented [here](https://docs.ansible.com/projects/ansible/latest/inventory_guide/intro_patterns.html#common-patterns) 

### `truncate_databases.yaml`

This performs a backup and truncation of the local databases on instruments. It will prompt for hosts so to run use:

`ansible-playbook windows/truncate_databases.yaml`

{#instrumentdeployyaml}
### `instrument_deploy.yaml`

This is the main playbook for deploying software to NDXes. Currently this stops the server if it is running and installs the JDK using the `jdk` role. 

To use this you need to run `ansible-playbook windows/instrument_deploy.yaml` - it should prompt for hosts. 

{#ansibleupdatingjdk}
#### Updating JDK version

To update the JDK version, you will need to set the vars in `roles\defaults\main.yaml`. 
These are: 

- `jdk_major_ver` - the major version (excluding .min.patch) of the JDK. 
- `jdk_full_ver` - the full version string of the JDK.
- `jdk_url` - the URL to download the JDK from. 
- `jdk_checksum` - the checksum for the downloaded JDK.
- (optionally) `jdk_force_update` - whether to overwrite the current version if it already exists


### `deploy_ssh_keys.yaml`

This is the windows equivalent of the Linux workflow for deploying [the group's ssh keys](https://github.com/ISISComputingGroup/keys) and turning off password auth in favour of pubkey auth. 

To run this on all NDXes run `ansible-playbook windows/deploy_ssh_keys.yaml`. To limit to certain hosts/host groups use `--limit` ie. 
`--limit NDXHRPD_SETUP` to just run on `NDXHRPD_SETUP` or `--limit muons` to only run on muon NDXes. 

### `nsclient.yaml`

Install nsclient++ monitor program. Needs to be run with 

`ansible-playbook --ask-vault-password windows/nsclient.yaml`

There is a host group `nsclient` that is used to hold encrypted passwords and can also be used
for deploying


### `instrument_deploy.yaml`

This is for deploying software to NDXes. Currently this stops the server if it is running and installs the JDK using the `jdk` role. 

To use this you need to run `ansible-playbook windows/instrument_deploy.yaml` - it should prompt for hosts. 

### `deploy_wincred.yaml`

This is for deploying a new set of credentials to NDXes. The credentials should be updated in keeper first; this playbook reads the credentials from keeper.

To use this you need to run `ansible-playbook windows/deploy_wincred.yaml --ask-vault-pass` - it should prompt for ansible vault password (found in keeper - search for "ansible") and hosts to target. 


## Linux-only playbooks (`linux/`)

### Initial SSH set up 

This involves: 
1) copying over the keys in [this repo](https://github.com/ISISComputingGroup/keys)
2) disabling openssh password-authentication (ie. you can only use pub/priv keys!)

It can be run multiple times if for example you wanted to update the deployed keys if someone new joins the team or someone gets a new computer with a different public key. 

#### Deploying ssh keys (`playbook_deploy_ssh_keys.yaml`)

This can be run on multiple hosts by using `ansible-playbook playbook_deploy_ssh_keys.yaml` if you already have ssh key-based auth set up (ie. if you wanted to _update_ the list of keys because someone's public key changed), but if this is a new machine you should use `--ask-pass` (to ask for the ssh password) along with `--limit` to limit the single host (as your ssh passwords may/should be different between machines)

For example, to run this on `madara`: 

`ansible-playbook playbook_deploy_ssh_keys.yaml --ask-pass --limit madara`
which will prompt for madara's ssh password. 

This step also prompts for a personal access token to access the `keys` repo, which is in Keeper. 

#### Turning off `sshd` password authentication (`playbook_turn_off_ssh_passwd_auth.yaml`)

This is fairly obvious but to do this you need to have done the above step otherwise you'll lock yourself out. 

to run on all hosts, use: 

`ansible-playbook playbook_turn_off_ssh_passwd_auth.yaml`

This will prompt for the vault password, which is in keeper (`ds-config ansible vault`)

### General system updates

`playbook_system_updates.yaml` exists to update the system packages. 

### Kafka cluster provisioning

`deploy_kafka.yaml` and `deploy_redpanda_console.yaml` exist to provision a kafka cluster, currently on the test machines in R55. 

## Notes

### Setting up a windows hyper-v virtual machine for testing 

To test playbooks on a local virtual machine running in Hyper-V, you need to set the following up: 

1) A virtual machine itself. You can use the [evaluation `.iso` images for this](https://www.microsoft.com/en-gb/evalcenter/)
2) If using the `Default switch` on the VM, you need to forward the WSL network so it can reach the VM. To do this run `Get-NetIPInterface | where {$_.InterfaceAlias -eq 'vEthernet (WSL (Hyper-V firewall))' -or $_.InterfaceAlias -eq 'vEthernet (Default Switch)'} | Set-NetIPInterface -Forwarding Enabled -Verbose` from an _elevated_ powershell window. Note that by default most server windows images do not respond to ping requests. You can enable this by enabling the inbound rule `File and Printer Sharing (Echo Request - ICMPv4-In)` in the firewall settings.
3) [OpenSSH set up](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse) on the VM


### Ad-hoc commands 
To run an [adhoc command](https://docs.ansible.com/projects/ansible/latest/command_guide/intro_adhoc.html) to ie. `win_ping` to `TS2` machines to check they're reachable, you can run: 

`ansible ts2 -m win_ping`

This can also be used to perform one-line shell/bash commands remotely. 

#### Chaining commands

There is an issue with passing environment variables on windows specifically between chained commands. 
If you wanted to run `config_env.bat` to define `MYPVPREFIX` then call `caput` after, you need to use a batch script and copy it across instead. 

This can be done with a playbook similar to the following: 

<details>
<summary>Show playbook</summary>

```yaml
---
- name: set some PVs
  hosts: ndxes
  tasks:
    - name: create temp dir
      ansible.windows.win_tempfile:
        state: directory
      register: tmpdir
    - name: copy bat over
      ansible.windows.win_copy:
        src: mybat.bat
        dest: "{{tmpdir.path}}"
    - name: call bat
      ansible.windows.win_command: "{{tmpdir.path}}\\mybat.bat"
      register: output
    - name: print output
      debug:
        var: output

```

which copies over a batch script `mybat.bat` to a temporary dir, calls it, then Ansible cleans up the temp dir containing the batch script. 

Example batch script, which resets the power check with a for loop: 

```bat
call \instrument\apps\epics\config_env.bat
@echo on
FOR /L %%v IN (1, 1, 9) DO (
    echo running caput %MYPVPREFIX%MOT:DMC0%%v:PWRDET:RESET:SP 1
caput %MYPVPREFIX%MOT:DMC0%%v:PWRDET:RESET:SP 1
)

exit /B 0
```

</details>
