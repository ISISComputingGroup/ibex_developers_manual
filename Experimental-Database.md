> [Wiki](Home) > [The Backend System](The-Backend-System) > [System components](System-components) > [Experimental Database](Experimental-Database)

The experimental database keeps track of:

1. experiments (`experiment` table)
1. experiment team members (`experimentteams` table)
1. users in the team  (`user`)
1. roles in the team  (`role`)

The data is populated centrally from the [Experiment Database Populator](https://github.com/ISISComputingGroup/ExperimentDatabasePopulator) (alternatively named RB number populator) which is run on control-svcs.

## Architecture

The experiment database populator is a Python 3 program that is designed to run centrally and periodically update instrument databases. It does the following: 
* Monitors 'CS:INSTLIST' for instruments that are scheduled
* Gathers 200 days worth of data from the web services hosted by business apps (Using the credentials stored in a git repository on the local share).
* Reformats the data slightly to match the structure of the instrument databases
* Pushes to the instrument database (Using the credentials stored in a git repository on the local share).
* Optionally repeats every hour

## Testing

* The populator has unit tests that are run in [jenkins](http://epics-jenkins.isis.rl.ac.uk/job/Experiment_Database_Populator/). 
* The `DEBUG` flag can be set in the main file to push instrument data to your local experiment database.
* A system test is included that will check the data gathered from the website is the same as that on the instruments. This is mainly useful for comparison to the old system.

## Deployment

The populator is installed on the linux server control-svcs. This can be accessed using the credentials in the usual place. The program is installed under `/home/epics/RB_num_populator` and is being run as a `cron` job every hour. Logs for the program are written into `/home/epics/RB_number_populator/logs`.