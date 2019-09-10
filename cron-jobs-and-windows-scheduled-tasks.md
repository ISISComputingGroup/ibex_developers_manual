In Windows, it is possible to set up a task that is scheduled to run at certain intervals or given certain conditions.

## Task Scheduler

To do this in Windows 10 we use the Task Scheduler app provided by the OS. You can find this by searching in the Windows taskbar for Task Scheduler or going to control panel -> System and Security -> Administrative Tools -> Schedule tasks.

Previously scheduled tasks can be found by clicking on the Task Scheduler Library in the left panel and then viewing them in the middle top panel.

To create a task click the Create Task button in the Actions panel on the right. Here give it a relevant name and description for the job. 

In the triggers tab, we can set when the task is run by clicking new and customising the trigger in the popped up window. 

To define the action we can create a batch script carrying out the task we wish to do (see batch scripts below). This batch script is then linked to the task when in the create task phase in the actions tab by clicking New and linking the program/script.

You can customize other parts of the task in the conditions and settings tabs.

## Batch scripts

Used to script processes and tasks that can be run automatically.

In a batch script, we can execute commands one after the other as we would in the cmd with the syntax "start <our command>".

Batch scripts also come with commands they can run such as "timeout 10" which makes the script wait for 10 seconds.

## DETMON run control

A cron job is used on [DETMON](https://github.com/ISISComputingGroup/IBEX/wiki/DETMON-Instrument-Details) to start and stop runs at midnight in order to create a new nexus log file for each day. This was done as part of ticket [4182](https://github.com/ISISComputingGroup/IBEX/issues/4182)