Below is a list of code that we know is duplicated in IBEX. This should be better consolidated.
* Reading the instrument list is done in JSON Bourne and in the Experiment Database Populator
* GUI: [Load config handler](https://github.com/ISISComputingGroup/ibex_gui/blob/master/base/uk.ac.stfc.isis.ibex.ui.configserver/src/uk/ac/stfc/isis/ibex/ui/configserver/commands/LoadConfigHandler.java) vs [load recent config handler](https://github.com/ISISComputingGroup/ibex_gui/blob/master/base/uk.ac.stfc.isis.ibex.ui.configserver/src/uk/ac/stfc/isis/ibex/ui/configserver/commands/RecentConfigsHandler.java)
* Logic to tell which DAE actions are allowed (duplicated in isisicp, gui, genie_python)
* Logic to get instrument name based on machine name. genie_python, GUI, others (?)