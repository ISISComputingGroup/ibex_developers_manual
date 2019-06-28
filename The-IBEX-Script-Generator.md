The script generator developed as part of IBEX is held in the same repository as the IBEX client/GUI. The script generator requires both a perspective in the IBEX GUI and a standalone application.

To achieve this, the script generator can be built in both eclipse and using maven, with minimal packages required from the main GUI codebase. The build system for the standalone application mirrors that of the main IBEX gui, with an independant `tycho.parent`, see [below](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/The_IBEX_Script_Generator#the-directory-structure)

To prevent duplication, the GUI perspective depends wholly on the standalone application.

## The directory structure
| Purpose        | Location |
| -------------- |----------|
| Perspective for the IBEX GUI ONLY | `base/uk.ac.isis.ibex.scriptgenerator` |
| Standalone app build directories | `base/uk.ac.isis.scriptgenerator/*` |

## To build
To build and run the app through eclipse, the script generator product is found in `base\uk.ac.stfc.isis.scriptgenerator.client.product`. The instructions for setting up eclipse and loading the target platform (necessary for the script generator) are found in the instructions for the [main IBEX GUI setup](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Building-the-GUI)


To build the standalone app through maven run `build\build_script_generator.bat`

There is a Jenkins pipeline which will build the script generator with every new commit to the IBEX GUI master branch.
