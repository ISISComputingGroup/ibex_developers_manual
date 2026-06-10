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
key and the (encrypted with passphrase) private key to your WSL instance.

See instructions [on this page.](https://devblogs.microsoft.com/commandline/sharing-ssh-keys-between-windows-and-wsl-2)

This will start an agent automatically on login if one is not already started, and add your SSH key to it, prompting for the passphrase the first time you use it for the first time since the WSL has started.
