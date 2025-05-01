# Auto-start IBEX on Computer Restart

## Windows Server 2012 R2

**This appears to work but doesn't because the user does not have interactive mode permissions. There is a ticket to sort this out**

To make the ibex server restart when the computer restarts, do the following:

1. Ensure that the user who will run IBEX server has "log on as batch job" rights
    1. Open "Local Security Policy" as an admin
    1. Find "Local Policies" -> "User Right Assignments" click
    1. Find "Log on as a batch Job"
    1. Open and add the user above if they are not in this list
1. Create a scheduled task to start on reboot
    1. Open "Task Scheduler" as an admin
    1. Create a basic task
    1. Call in "Start IBEX on restart"
    1. Trigger: Trigger on "When the computer starts"
    1. Action: Start a program
    1. Start a program: 
        1. Program script is `cmd`
        1. Add arguments is `/c "C:\Instrument\Apps\EPICS\start_ibex_server.bat 2>&1 > C:\Instrument\var\logs\startup.log`
        1. StartIn `C:\Instrument\Apps\EPICS`
    1. Finish: Click "Open the Properties dialog for this task when I click Finish"
    1. Enter credentials for user running ibex server
    1. General Tab: Make sure Run whether user is logged on or not
    1. Check other tabs
