We have a Jenkins pipeline for tests that check if our wikis are grammatically correct, that they reference valid links, and so on. It checks the developer's Wiki, the IBEX User's manual and the IBEX Wiki. 

## Running the Wiki Checker locally

In order to run them locally, you need to change directory to `C:\Instrument\Dev\ibex_wiki_checker` and then execute `run_tests.bat`.

## Running the Wiki Checker for other wikis

In order to run the wiki check tests for another Github Wiki, you need to locally check out the `ibex_wiki_checker` repository and locally change the line https://github.com/ISISComputingGroup/ibex_wiki_checker/blob/5c4a77057d0e480373115db27f983ccb5827c3f0/wiki.py#L31 to point to the URL of the wiki you want.
 
**Note:** DO NOT COMMIT THE CHANGE!