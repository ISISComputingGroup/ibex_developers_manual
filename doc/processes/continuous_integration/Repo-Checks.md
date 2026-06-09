# Repository Checking

Given the complex relationships between the various repositories used in our distribution and how easy it is to make mistakes there are various checks undertaken against our repositories ensuring clean source code which can be automated via Jenkins.

The default is to check out the `master` branch of the top level of EPICS and does the following:
- Run the unit tests for this code
- Resets the upstream git checkout tags prior to submodule version check (`reset_checkout_tags`)
- Checks that the submodule revisions have all been pushed (`submodule_revisions_check`)
- Checks that there is a newline at the end of files which should have one (`do_newline_endfile_check`)
- Check the format of the IOC names are correct (`do_ioc_naming_check`)
- Look for double carriage returns in any Make files (`do_makefile_separator_check`)
- Check for any temporary build directories (`temporary_build_directories_check`)
- Check for any `__pycache__` directories (`pycache_directories_check`)
- Check for any `pyc`/`pyo` files (`pyc_pyo_file_check`)
- Check for any Db files in the `gitignores` (`do_gitignore_check`)
- Check for any archived repos (`do_archived_repo_check`)
- Check for any missing/unremoved directories (`missing_dir_check`)
- Check that repos have the correct permissions for the groups used at ISIS, this is considered an unstable test

If you don't want to run all the tests there are a few arguments that can be passed to the script, to use these in Jenkins, just add them after the call in the `Execute Shell`, you can `--skip_unit_test=Yes`, and similarly you can `--skip_unstable_checks=Yes` to skip any unstable tests. Note that any text after the `=` will skip these items at this time. For the rest of them you can opt to include a subset instead using `--do_these_tests` and provide a comma separated list after an `=` of the test names as given inside the parentheses above.

## Checking against other branches
If checking against a different branch at the top EPICS level as part of the CI via Jenkins, check out the appropriate branch and run it at that level is likely to be the safest option.
If you want to check on a submodule on a specific branch then you can use the `--repo_branch` argument to provide a list in this kind of manner, "relative path from the check_scripts directory to the repo in question"+name_of_branch_to_checkout (e.g. `--repo_branch=".."+Ticket123456` would check out a branch called `Ticket123456` at the top level, whilst `--repo_branch="../support/device/master"+Ticket987654,"../ioc/master"+Ticket987654` would check out a branch called `Ticket987654` for the device specified in support and for the main IOC repo)

## Checking for changes on only certain submodules
If you only want to be informed of errors on certain submodules of EPICS the the argument `--submodules_of_interest` should be set to a comma separated list of submodules of interest, e.g. `--submodules_of_interest=ioc,device` would only provide an error if there were unpushed errors in IOC or the device repo.

# Running these tests by hand
If you are using a windows system you will need to do the following in a Git Bash window:
1. If you don't have a python executable in your path you can add one temporarily in the following fashion `export PATH="/path/to/pyhton/folder:$PATH"`, and you will need to install the `requests` module via `pip` if it isn't already available.
2. You will need a GitHub Token with suitable permissions, this is already handled for Jenkins, and the same token can be reused if other jobs need to be created that use this script.
3. To run with the default settings simply execute the following: `GITHUB_TOKEN=[the_token_information] python3 do_all_checks.py`
4. To run them with various settings as above, just add the arguments to the end, for example `GITHUB_TOKEN=[the_token_information] python3 do_all_checks.py --submodules_of_interest=ioc,device --repo_branch="../support/device/master"+Ticket987654,"../ioc/master"+Ticket987654 --skip_unit_test=Yes --skip_unstable_checks=Yes --do_these_tests=submodule_revisions_check,do_ioc_naming_check` would report on the submodule revisions check of IOC and device, and make sure that the naming is correct, for the `Ticket987654` branch only.

