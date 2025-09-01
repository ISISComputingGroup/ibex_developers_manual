# SSH key-based auth

Instruments run an SSH server, which can be used to execute commands remotely.

It is possible to access this SSH server using key-based authentication. Keys are associated with
an individual, but are used to grant access to the instrument accounts. This means that keys
for individuals no longer on the team can be easily revoked.

## Key-pair generation

:::{note}
If you already have a suitable SSH key, which is encrypted using a passphrase, you may
skip this step.
:::

Generate a key-pair using a strong algorithm, for example `ed25519`:
```
ssh-keygen -t ed25519
```
**You must encrypt this key with a strong password when prompted.**
Don't use an empty passphrase for these keys. This is not a shared
password, it is a password for your personal key-pair; store it in your password
manager. This will generate two files: `~\.ssh\id_ed25519` and `~\.ssh\id_ed25519.pub`. The file
ending in `.pub` is a public key, the one without the `.pub` extension is a private key. It
would be sensible to store copies of these two files in your password manager too.

:::{warning}
For the avoidance of doubt, the **public** key (`*.pub`) can be freely shared with everyone (for
example, by being copied onto instruments). Do not share your **private** key. The private key
is additionally encrypted using your selected password.
:::

{#keeper_ssh}
## Keeper

To avoid having to copy and paste your passphrase every time, you can use [Keeper](https://ukri.sharepoint.com/sites/thesource/SitePages/Keeper-Password-Manager.aspx) to store your passwords and SSH keys.

If you want to use Keeper (you'll need the desktop client for this, _not_ the browser plugin) for storing your SSH keys, and not have local plain text copies on your machine, you can do so. 

This is done by following [this guide](https://docs.keeper.io/en/keeperpam/privileged-access-manager/ssh-agent#activating-the-ssh-agent) with your public key, private key and passphrase filled in. 

You may need to [turn the `OpenSSH` agent off](https://docs.keeper.io/en/keeperpam/privileged-access-manager/ssh-agent#windows-note-on-ssh-agent-conflicts) if it's on your machine - see if `ssh-agent` is running in your services in task manager. 

It would also be a good idea to change the vault timeout to something relatively short to minimise scope of access for when the SSH keys are available. 

### SSH works and prompts to use passphrase, but git doesn't show the prompt
 If `ssh git@github.com` works fine, your SSH key has been added to Github and `ssh` is using it.  

You may need to set the `GIT_SSH` environment variable to wherever your ssh executable is, as git might try and use its own ssh executable which doesn't seem to work with Keeper. `where ssh` will tell you where this is. 

{#manual_ssh_agent}
## Manually Setting up SSH agent

```{note}
Ignore this section if you followed {ref}`the section on setting up keeper as your ssh agent<keeper_ssh>`.
```

In a powershell window, run the following commands:
```powershell
Get-Service ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent
```

## Deploying the public key

- Add your public key to the [keys repository](https://github.com/ISISComputingGroup/keys).
- Ask a developer whose key is *already* deployed to run the [`deploy_keys.py` script](https://github.com/ISISComputingGroup/keys/blob/main/deploy_keys.py), which will
update the `authorized_keys` files on each instrument.

If the permissions on `administrators_authorized_keys` are wrong, that file won't work. The
permissions can be fixed by running:

```
icacls.exe "c:\ProgramData\ssh\administrators_authorized_keys" /inheritance:r /grant "Administrators:F" /grant "SYSTEM:F"
```

## One-off usage

To connect via SSH to an instrument, use:

```
ssh spudulike@NDXINST
```

(If you aren't [using Keeper](#keeper_ssh)) This will prompt you on each connection for the passphrase to unlock your SSH key, this is the
password you set earlier for your personal SSH key. You will not be prompted for an
account password; your key is sufficient to grant you access.

## Bulk usage

:::{caution}
If you intend to run a command across many instruments, it is worth getting that command
reviewed by another developer and running it together. This is **especially** true if you intend to
run a command as a privileged user.
:::

Typing the password to unlock your SSH key for each instrument would be tedious.
To avoid this, we can either [use Keeper](#keeper_ssh), or **temporarily** add the key to the SSH agent:

```
ssh-add
```
This will prompt for the passphrase to unlock your SSH key. You can check that your key is now in
the SSH agent by running:

```
ssh-add -l
```

Once the key has been added to the agent, you can SSH to an instrument without any further prompts:

```
ssh spudulike@NDXINST
```

Commands can be executed like:

```
ssh spudulike@NDXINST "dir /?"
```

Since we no longer have any authentication prompts (having added our key to the SSH-agent),
this command is suitable for automating in a loop over instruments - for example from python
or a `.bat` script.

Once you have finished with the administration task which needed SSH across multiple instruments, you
should remove your key from the agent (and then verify that it has been removed):

```
ssh-add -D
ssh-add -l
```

:::{important}
Do not leave these keys permanently added to the SSH agent - having *immediate* SSH access to *every*
instrument is an unnecessary risk most of the time (for example if your developer machine was compromised).
Add the keys to the SSH agent only when needed, and remove them from the agent again when your administration
task is complete. The usual sudo lecture applies:
> We trust you have received the usual lecture from the local System
> Administrator. It usually boils down to these three things:
> 1) Respect the privacy of others.
> 2) Think before you type.
> 3) With great power comes great responsibility.
:::
