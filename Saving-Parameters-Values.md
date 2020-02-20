Parameters values from the Script Generator can be saved in a file. The file format chosen is JSON due to its flexibility and well-tested parser available for upgrading it using upgrade script in future. 
The format of the chosen JSON file is as follows:

```
{
	"version": "",
	"ScriptGeneratorVersion": "",
	"Date": "",
	"Time": "",
	"ConfigurationFileName": "",
	"ConfigurationFileGitHash": "",
	"GeniePythonVersion": "",
	"ConfigurationContent": "",
	"Actions": [{
		"actionName": "",
		"parameter": {
			"param1": "value",
			"param2": "value"
		}
	}, {
		"actionName": "",
		"parameter": {
			"param1": "value",
			"param2": "value"
		}
	}]
}

```
Note: For each action in `Actions` in the JSON file, there is a table in the script generator.

The Script Generator also contains the actual content of the config file that was used when saving parameters. This is to make sure that the configuration that was used to generate JSON file is the same configuration that is being used to load the data from the JSON file.

The python file will contain the hash of JSON file from the time when the JSON file was generated. This hash will be present as a string data type in python, accessible through a getter method.

 




