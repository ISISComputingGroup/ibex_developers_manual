### Proposed structure for VNC Cloud Groups:



### Proposed procedure for setting up VNC Cloud access:

**Owner / Admin (Single Experiment Controls group member)**

1. Enables "global" Two-Factor Authentication for _all_ users of the VNC Cloud system, in accordance with site security advice.
1. Creates "Machine Groups" in VNC portal all within the ISIS "Team", one per physical ISIS instrument e.g. "LMX" (See diagram above)
1. Creates "People Groups", one per instrument (e.g. "LMX Instrument Scientists" or perhaps "LMX Users" containing ISs _and_ external users for simplicity)
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
1. Enables "Cloud Connectivity" in Server options
1. Adds "local" computers (viewing, analysis, etc.) to Machine Group(s) (See diagram above)
1. Performs below steps to use VNC client

**User (External facility user):**

1. Creates VNC cloud account using link in invitation email from IS
1. Downloads, installs and runs VNC client.
1. Logs in and is presented with list of machines authorised to connect to
1. Connects to a machine, typically a general access cabin PC (NDCxxx) or analysis machine (NDLxxx)
_[at this point has same access as if physically present in instrument cabin]_
1. Connects to instrument control computer (NDXxxx) via RDP (if session not already established)
