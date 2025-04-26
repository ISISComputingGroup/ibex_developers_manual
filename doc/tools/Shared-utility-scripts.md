# Shared Utility Scripts (`ibex_utils`)

A place to share resources for speeding up our workflow - most of these live in https://github.com/ISISComputingGroup/ibex_utils

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

{#ioc_copier_script}
## IOC Copier
Run in an Epics terminal. This should be run from within the IOC's base folder, ie. `\instrument\apps\epics\ioc\master\TEKDMM40X0` if trying to duplicate the `TEKDMM40X0` IOC. 

Makes duplicates of an IOC correctly numbered for use when large numbers of an IOC are needed.
This should only be used on IOC 2 or greater, as these IOCs link to some files in the first rather than duplicating them.
Usage:
- Copy to IOC folder.
- Takes 4 parameters, the name of the ioc, the number ioc to copy, the first copy to create, and the last copy to make.
- e.g. `%python3% ioc_copier.py DFKPS 11 12 35`
- This would copy the Danfysik using ioc-11 as the base, and create copies 12 through 35
Found in ibex_utils/ioc_copier.

## GitHub Workflows
Useful [GitHub Workflows](https://docs.github.com/en/actions/learn-github-actions) and [Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) which can be added to project repositories

### Update Submodules Automatically
A template repository which can be used when creating a submodule where you would like the parent repository to be updated automatically on push to the main / master branch of the child repository.
* https://github.com/ISISComputingGroup/Update_Submodule_Workflow_Action

The repository was created in response to a discussion held in the retrospective [Retrospective notes 2022.09.07](/processes/retrospective-notes/Retrospective-Notes-2022.09.07) to remove the need for a check to scan repositories to ensure submodules have correctly been updated.

The repository can be used as a starting point for integration into Jenkins CI/CD.

#### Workflow
```YAML
name: Send submodule updates to parent repo
on:
  push:
    branches:
      - main #NOTE: If adding this action to a new repo you may need to change the child repo branch name
env:
  PARENT_REPO_NAME: <GITHUB_ORGANISATION_ACCOUNT>/<PARENT_REPOSITORY> #NOTE: You may need to change the parent repo
  PARENT_REPO_BRANCH: main #NOTE: You may need to change the parent repo branch name
jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout ${{ github.event.repository.name }}
        uses: actions/checkout@v2
        with:
          token: ${{ secrets.PRIVATE_TOKEN_GITHUB }}
      - name: Checkout ${{ env.PARENT_REPO_NAME }}
        uses: actions/checkout@v2
        with:
          repository: ${{ env.PARENT_REPO_NAME }}
          submodules: 'true'
          ref: ${{ env.PARENT_REPO_BRANCH }}
          token: ${{ secrets.PRIVATE_TOKEN_GITHUB }}
          fetch-depth: 0
      - name: Get submodule updates
        run: |
          cd ${{ github.event.repository.name }}
          git fetch --all
          git switch ${{ github.ref_name }}
      - name: Commit and push the changes to ${{ env.PARENT_REPO_NAME }}
        run: |
          git config user.email "actions@github.com"
          git config user.name "GitHub Actions - update submodules"
          git add --all
          git commit -m "Auto-update: ${{ github.event.repository.name }}" -m "This is an automatic update completed by GitHub Actions, using submodule_update.yml. It was triggered by a push to the ${{ github.ref_name }} branch of the ${{ github.event.repository.name }} submodule repo." || echo "No changes to commit"
          git push
```

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