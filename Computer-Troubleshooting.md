Issue related to the computer that IBEX is running on


## Screen Resolution needs to be Set

The resolution is setable on a remote desktopm, even to a resolution bigger than the current screen. To do this there is a menu item on the remote desktop window for “smart sizing” which does just this. 

![smart screen](troubleshooting\rdp_smart_screen.png)

It doesn’t seem to persist on server 2012 unless you edit it into the .rdp file (and it also requires that you don’t select full screen or it takes a lower resolution).  I’ve edited the RDP file appropriately on the NDHSMUONFE desktop so that this works at 1920x1200.  The key bits are at the top here – but you we can fiddle the resolution down a bit if a different aspect ratio works better.

'''
screen mode id:i:1
use multimon:i:0
desktopwidth:i:1920
desktopheight:i:1200
smartsizing:i:1
...
'''


