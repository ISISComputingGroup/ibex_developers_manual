### Proposed structure for VNC Cloud Groups:

![](https://user-images.githubusercontent.com/10550207/86485047-9e0dec00-bd4f-11ea-8802-285f56966a20.png)

### Proposed procedure for setting up VNC Cloud access:

**Owner / Admin (Single Experiment Controls group member)**

1. Enables "global" Two-Factor Authentication for _all_ users of the VNC Cloud system, in accordance with site security advice.
1. Creates "Machine Groups" in VNC portal all within the ISIS "Team", one per physical ISIS instrument e.g. "LMX" (See diagram above)
1. Creates "People Groups", one per instrument (e.g. "LMX Instrument Scientists" or perhaps "LMX Users" containing instrument scientists _and_ external users for simplicity)
1. Grants access to Machine Group to appropriate People Group
1. Invites Instrument Scientists (IS) to create a VNC account via VNC portal (invitation email)
1. Grants "Manager" privilege to IS
1. Adds IS to appropriate People Group(s) 

**Manager (IS or other ExptCtrl member)**

1. Creates VNC Cloud account using link in invitation email from Owner/Admin
1. Sends emails to external users via VNC Cloud portal inviting them to create a VNC account
1. Grants "User" privilege to new users
1. Adds users to appropriate People (instrument) Group(s) (and removes when experiment over)
1. (Optional if willing & able) Installs VNC Server on the relevant machine(s) (e.g. NDCxxx & NDLxxx) via conventional VPN and RDP. (Details in "Deployment" section of VNC Cloud portal).  More help in [VNC Article](https://help.realvnc.com/hc/en-us/articles/360002253198-Installing-and-Removing-VNC-Connect#windows-0-0)
1. Enables "Cloud Connectivity" in Server options. More help in [VNC Article](https://help.realvnc.com/hc/en-us/articles/360002249737-All-About-Cloud-Connections#enabling-cloud-connectivity-on-a-remote-computer-0-1)
1. Adds "local" computers (viewing, analysis, etc.) to Machine Group(s) (See diagram above)
1. Performs below steps to use VNC client

**User (External facility user):**

1. Creates VNC cloud account using link in invitation email from IS
1. Downloads, installs and runs VNC client.
1. Logs in and is presented with list of machines authorised to connect to
1. Connects to a machine, typically a general access cabin PC (NDCxxx) or analysis machine (NDLxxx)
_[at this point has same access as if physically present in instrument cabin]_
1. Connects to instrument control computer (NDXxxx) via RDP (if session not already established)

### Read/Write and Read-only

The _Read Only_ and _Read/Write_ access is to be controlled by changing the privileges on the viewing machine's standard instrument user account (ISUA).

This will be for the simplest case for when the viewing machine is running Windows and has (ISIS instrument) standard local user and admin accounts, although the principal still applies to a Linux analysis machine and other cabin machines.

**Procedure:**

1. Instrument scientist adds ISUA to access list in "Users and Permissions" section of VNC Server options
1. IS changes permissions in VNC server settings for ISUA to be either R or R/W to suit experiment
1. User runs local VNC client and logs in using their personal account
1. User sees list of available machines and connects to one using ISUA
1. Views (if R only and connection previously established by IS) **OR**
1. Connects (if R/W) to screen of instrument control computer via RDP if no active session, or "local" VNC client (as if in cabin in person)
1. Instrument scientist sets privileges of ISUA back to Read Only after experiment ends
1. (Optional) IS removes user from "Instrument People group" in VNC Cloud portal

See [VNC article](https://help.realvnc.com/hc/en-us/articles/360002253618-Managing-Users-and-Session-Permissions-for-VNC-Server) for more information.

**NB**

When connecting using an account which has _Read Only_ access, the Users will have **_no control_** over the remote computer whatsoever, not even being able to connect to the control machine.  This option is severely limited (by design) and so relies heavily on the IS to create and leave the RDP session to the control machine in a state which will provide sufficient information to their Users.  

The _Read / Write_ option on the other hand, offers **_full control_** of the remote computer and so the IS needs to consider carefully the implications of allowing Users to connect with this privilege level.

# Troubleshooting

If you can connect via cloud VNC but get a blank screen that you can do nothing with, this may be because no monitor is attached to the computer. The cloud VNC mechanism needs to have the vnc server program running in service mode (as a windows service), and this seems to need a screen of some sort. We run VNC server in user mode on the NDX and this is happy just having an active remote desktop session rather than a real screen, but user mode only allows point to point and not cloud connections.  

We have purchased some "screen dongles" that can be used instead of a real monitor, these attach to e.g. a display port adapter port on the PC.    
