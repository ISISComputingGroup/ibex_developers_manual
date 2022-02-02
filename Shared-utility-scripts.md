A place to share resources for speeding up our workflow

## make_ioc batch script

Run in an EPICS terminal.
Makes an IOCs support module and IOC module or an IOCs ISIS module.

Usages: 
For an IOC with a support and IOC module: 
- `make_ioc support_folder_name ioc_folder_name`
- `make_ioc mk3chopper MK3CHOPR`
For an IOC in the EPICS directory (will give a warning): 
- `make_ioc isis_folder_name no_ioc`
- `make_ioc Chopper_sim no_ioc`
For an IOC with only an IOC module: 
- `make_ioc no_support ioc_folder_name`
- `make_ioc no_support mk3chopper`

Found in ibex_utils/workflow_support_scripts.
To make it easy to use add the ibex_utils/workflow_support_scripts folder to your PATH.

## make_ioc_test batch script

Run in an EPICS terminal.
Relies on the make_ioc script above.
Makes an IOC and then ask the user if they want to run tests.

Usage: 
- The same as make_ioc script but with a third parameter pointing towards the test
- `make_test_ioc oercone OERCONE oercone`
- `make_test_ioc oercone OERCONE oercone.OerconeTests.test_WHEN_device_is_started_THEN_it_is_not_disabled`

Found in ibex_utils/workflow_support_scripts.
To make it easy to use add the ibex_utils/workflow_support_scripts folder to your PATH.

## GitHub Workflows
Useful [GitHub Workflows](https://docs.github.com/en/actions/learn-github-actions) and [Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) which can be added to project repositories

### Pylint
Place the below example in `.github\workflows\` in a file called `pylint.yml` to add a GitHub workflow [on push](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#on) to a repository.
The workflow will execute [pylint](https://pypi.org/project/pylint/) on all `.py` files within the repository.

The idea behind adding this workflow to a repository is to make developers want to work towards improving the quality of python used in a repository. In doing so the repository will move towards meeting [PEP8](https://www.python.org/dev/peps/pep-0008/) standards.

When implementing this workflow, I recommend adding or altering the PR template for the repository to include a requirement that pylint checks must either stay the same or increase in quality. This should help prevent the codebase moving further away from PEP8 standards. 

**Please Note** that you should modify the python version in the YAML file to reflect the version of python used in the repository.

### View Suppressed Messages
To view suppressed messages when running Pylint on a given file which has `pylint: disable=` statements, add the flag `--enable=suppressed-message` to the Pylint command. Alternatively, you can run locally using: `pylint --enable=suppressed-message`.

### Workflow
```YAML
name: Pylint

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.8
      uses: actions/setup-python@v1
      with:
        python-version: 3.8
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pylint
    - name: Analysing the code with pylint
      run: pylint --rcfile=.pylintrc $(find . -name "*.py" | xargs)
```