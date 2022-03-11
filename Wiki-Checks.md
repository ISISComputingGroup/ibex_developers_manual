We have a Jenkins pipeline for tests that check if our wikis are grammatically correct, that they reference valid links, and so on. It checks the developer's Wiki, the IBEX User's manual and the IBEX Wiki. 

## Running the Wiki Checker locally

In order to run them locally, you need to change directory to `C:\Instrument\Dev\ibex_wiki_checker` and then execute `run_tests.bat`.

## Running the Wiki Checker locally for a single file

Executing `python -u run_tests.py --file <FILE>`, in the `ibex_wiki_checker` folder, and substituting `<FILE>` for the file name (including the path) will run the tests on a single file.

## Running the Wiki Checker locally for a folder
Executing `python -u run_tests.py --folder <FOLDER>`, in the `ibex_wiki_checker` folder, and substituting `<FOLDER>` for the folder path will run the tests on all files ending `.md` in the folder.

## Running the Wiki Checker for other wikis

In order to run the wiki check tests for another Github Wiki, you need to locally check out the `ibex_wiki_checker` repository and locally change the line https://github.com/ISISComputingGroup/ibex_wiki_checker/blob/5c4a77057d0e480373115db27f983ccb5827c3f0/wiki.py#L31 to point to the URL of the wiki you want.
 
**Note:** DO NOT COMMIT THE CHANGE!
