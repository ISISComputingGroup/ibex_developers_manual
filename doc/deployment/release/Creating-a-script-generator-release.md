# Creating a script generator release

The IBEX Script Generator is released as a zip file on GitHub (https://github.com/ISISComputingGroup/ScriptGeneratorReleases/releases).

First, to create the release on the share follow the instructions for the script generator on https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Creating-a-release.

To create a release run through create_release.py script from the [ScriptGeneratorReleases](https://github.com/ISISComputingGroup/ScriptGeneratorReleases) repo. For this script, you will need a GitHub personal access token with push access to the repo. 

You should run it with `<python3> create_release.py -v <version_number> -t <api_token>`. Replacing `<version_number>` with the version number e.g. `7.2.0` (you should leave out any `v`, this will be prepended by the script) and <api_token> with your generated personal access token.

There is also an optional argument for the script `-d <drive>` where you can specify which drive you would like to mount the share to (you must add the colon) e.g. `U:`. This defaults to `Z:`.

## Testing
After the release has been created, the standalone script generator must be tested in a non-developer environment. This emulates a user computer, where there is no pre-existing installation of python, git or the JVM. The instructions to do this testing are here: https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Script-Generator-Testing-Environment