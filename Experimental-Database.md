> [Wiki](Home) > [The Backend System](The-Backend-System) > [System components](System-components) > [Experimental Database](Experimental-Database)

The experimental database keeps track of:

1. experiments (`experiment` table)
1. experiment team members (`experimentteams` table)
1. users in the team  (`user`)
1. roles in the team  (`role`)

The data is populated centrally from the [Experiment Database Populator](https://github.com/ISISComputingGroup/ExperimentDatabasePopulator) (alternatively named RB number populator) which is run on control-svcs. The RB numbers were populated by a different service on SECI, which can be found at https://github.com/ISISNeutronMuon/RBNumberFinder.

## Architecture

The experiment database populator is a Python program that is designed to run centrally and periodically update instrument databases. It does the following: 
* Monitors 'CS:INSTLIST' for instruments that are scheduled
* Gathers 200 days worth of data from the web services hosted by business apps (Using the credentials stored in a git repository on the local share).
* Reformats the data slightly to match the structure of the instrument databases
* Pushes to the instrument database (Using the credentials stored in a git repository on the local share).
* Optionally repeats every hour

## Installation

```
git clone https://github.com/ISISComputingGroup/ExperimentDatabasePopulator
cd ExperimentDatabasePopulator
python -m venv .venv
.venv\Scripts\activate
python -m pip install -e .[dev]
```

## Testing

* You will need to add access permission for the populator to write to your local database, to do this run `EPICS/SystemSetup/create_test_account.bat`
* You can write some dummy test data into your local database by using the `--test_data` argument. You must specify the username and password for writing to the database using the `--db_user` and `--db_pass` flags. The username/password can be found in `EPICS/SystemSetup/test_account.sql`.

## Deployment

Please follow the below instructions as part of deploying:

* Make sure you are firstly a super user to epics using the following command: `sudo su - epics`
* Pull most recent changes from master in `home/epics/RB_num_populator`
* From `home/epics/RB_num_populator`, check that a python virtual environment exists called _"exp_db_populator_venv"_.
* Activate virtual environment if present and check `/home/epics/RB_num_populator/requirements.txt` file matches dependencies in venv and then deactivate the virtual environment.
* If there is no virtual environment called _"exp_db_populator_venv"_ or dependencies are not inline with `/home/epics/RB_num_populator/requirements.txt`, run `/home/epics/RB_num_populator/create_rb_number_populator_python_venv.sh` and check the virtual environment has been created.
* Check that the cron job is running correctly using the following command: `crontab -l`. The output should look similar to: ```20 * * * * sh /home/epics/RB_num_populator/rb_number_populator.sh > /tmp/rb_num_pop.out 2>&1```
* Finally, check cron job is executing correctly by looking at recent logs since deploying under `/home/epics/RB_number_populator/logs` and for any errors indicating the cron job is not executing correctly under `/tmp/rb_num_pop.out`.
