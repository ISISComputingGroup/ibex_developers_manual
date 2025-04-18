# Test Machines

Test machines are currently virtual machines running on ... to access them:

1. Run Hyper-V Manager using your admin account (you may have to install it)
1. Connect to the server ndhspare70 (use right click, I think I used my admin credentials and Chris had to enable access for me)

## To reset them

1. Click on the server (left)
1. Click the Virtual machine you want to reset (middle)
1. Right click on the Clean for Clone check point and click `apply ...`
1. Click Apply yes I do
1. Right click and delete checkpoint sub tree (above clean for clone) - this removes history
1. Bring up the machine console (double click on the machine name)
1. Click power on (green button left on toolbar)
1. Wait for boot
1. Task Sequence: Build Basic W7
1. Computer Details: Set machine name and next
1. Move Data and Settings: Do not move
1. User Data: Do not restore
1. Administration Password: Leave as is
1. Ready: Begin
1. Leave to boot
