The script generator developed as part of IBEX is held in the same repository as the IBEX client/GUI. The script generator requires both a perspective in the IBEX GUI and a standalone application.

To achieve this, the script generator can be built in both eclipse and using maven, with minimal packages required from the main GUI codebase. The build system for the standalone application mirrors that of the main IBEX gui, with an independent `tycho.parent`, see [below](#the-directory-structure)

To prevent duplication, the GUI perspective depends wholly on the standalone application.

[Gotchas and Troubleshooting](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Gotchas-and-Troubleshooting-for-The-IBEX-Script-Generator).

## The directory structure
| Purpose        | Location |
| -------------- |----------|
| Perspective for the IBEX GUI ONLY | `base/uk.ac.isis.ibex.scriptgenerator` |
| Standalone app build directories | `base/uk.ac.isis.scriptgenerator/*` |

## Eclipse build
To build and run the app through eclipse, the script generator product is found in `base\uk.ac.stfc.isis.scriptgenerator.client.product`. The instructions for setting up eclipse and loading the target platform (necessary for the script generator) are found in the instructions for the [main IBEX GUI setup](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Building-the-GUI)

### Adding the perspective into the client
Currently the script generator perspective is not shown or selectable in the main IBEX GUI. It can be readded by modifying this line in `base/uk.ac.stfc.isis.ibex.e4.client/plugin_customization.ini` from:

```
uk.ac.stfc.isis.ibex.preferences/perspectives_not_shown=uk.ac.stfc.isis.ibex.client.e4.product.perspective.scriptGenerator
```

to:
```
uk.ac.stfc.isis.ibex.preferences/perspectives_not_shown=
```
This change should not be committed to master until the script generator is ready to be deployed to users

## Maven build
To build the standalone app through maven run `build\build_script_generator.bat`

There is a Jenkins pipeline which will build the script generator with every new commit to the IBEX GUI master branch.


## Data structures in the GUI

Each 'action', or step in a script is represented in the GUI as a row. Each cell contains one parameter for an action, which the users change to define their experiment. A complete row of defined parameters should be enough information to run the action once (see [Script Generator High-Level Design](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Script-generator-high-level-design#the-action-class))

![](https://raw.githubusercontent.com/ISISComputingGroup/ibex_developers_manual/master/images/scriptgen.png)

The parameter values are stored as strings in the underlying action. These strings are passed to the python process for validation, and to insert them into the output script. When the value of an underlying cell is updated, the GUI is notified by firing a property change (`actions`).

To change the type of action represented in the table, the singleton drops the current table and replaces it with a new one constructed using the new action type.

## Importing user-supplied script definitions
The `ActionDefinitions` are supplied by instrument scientists in [this form](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Script-generator-high-level-design#the-actiondefinition-class). All the python modules containing an `ActionDefinition` in a subdirectory are imported and stored in a `ScriptDefinitionWrapper` class. Using an instrument scientist supplied `ActionDefinition`, a `ScriptDefinitionWrapper` class is created containing the `ActionDefinition` with helper methods like `getParameters` and `parametersValid` to expose the parameters used in the action and their validation. These `ScriptDefinitionWrapper` classes are collected by the `ScriptDefinitionsWrapper`, which is then passed through the py4j interface to the GUI code.

Once in the GUI, the script generator table is created by generating `ActionParameters` from the parameter names exposed through the ScriptDefinitions class.


![Script generator code structure](https://raw.githubusercontent.com/ISISComputingGroup/ibex_developers_manual/master/images/ScriptGenerator.png)

## Checking the validity and generating python scripts

Generator classes are used to check validity and generate scripts. They use the script definition's supplied `run` and `parameters_valid` methods to check validity and generate scripts. We do not want to block the execution of the UI thread, and as such, all parameter validity checking and script generation is done by running a Java CompletableFuture and then firing a property change and passing this up the chain to the UI. This allows updates to happen in the background without blocking the UI thread.

## Saving the Parameter values and loading back up
Parameters values from the Script Generator can be saved in a file. The file format chosen is JSON due to its flexibility and well-tested parser available for upgrading it using upgrade script in future. 
The format of the chosen JSON file is as follows:

```
{
"version": "",
	"script_generator_version": "",
	"date": "",
	"time": "",
	"configuration_path": "",
	"configuration_file_git_hash": "",
	"genie_python_version": "",
	"configuration_content": "",
	"actions": [{
		"action_name": "",
		"parameter": {
			"param1": "value",
			"param2": "value"
		}
	}, {
		"action_name": "",
		"parameter": {
			"param1": "value",
			"param2": "value"
		}
	}]
}

```
Note: 

- For each action in `Actions` in the JSON file, there is a table in the script generator. 
- The `version` in the file is the version of the JSON format itself. This will be an integer and not tied to any other version number.
- configuration_path: this is the path of the configuration file within the git repository. Allowing us to group then by instrument if this becomes useful.
- configuration_file_git_hash: this is the git hash at the time the config file is used

The generated JSON also contains the actual content of the config file that was used when saving parameters. This is to make sure that the configuration that was used to generate JSON file is the same configuration that is being used to load the data from the JSON file. We want the JSON in a seperate file so that:
* It's language independent
* The user is less likely to modify it
* It would probably easier to upgrade at a later date if the JSON format changes

The generated script file will contain the compressed JSON. The compressed JSON can be used as a back up if the JSON file is lost to retrieve original values. For the MVP reading the JSON from the script will not be done and we will only read the JSON file.

JSON formats etc. were decided in a meeting on 20/02/2020 attended by Bish, Dom, John, Tom, Alistair and James.




