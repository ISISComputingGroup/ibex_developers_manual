> [Wiki](Home) > [The Backend System](The-Backend-System) > [genie_python](Building-and-installing-genie_python)

---

# Setting up uktena python distribution

- Check whether `C:\Instrument\Apps\Python3` already exists.
  * If it exists and `git remote get-url origin` returns `https://github.com/ISISComputingGroup/genie_python.git`:
    * Stop IBEX server
    * Remove the entire `Python3` directory
    * Proceed as if `Python3` `C:\Instrument\Apps\Python3` did not exist
  * If it exists and `git remote get-url origin` returns `https://github.com/ISISComputingGroup/uktena.git`:
    * Perform a `git pull` in `c:\instrument\apps\python3`
  * If it does not exist, from a git-enabled command line, run `git clone https://github.com/ISISComputingGroup/uktena.git C:/Instrument/Apps/Python3` (or if using ssh authentication `git clone git@github.com:ISISComputingGroup/uktena.git`).
- Navigate to `C:\Instrument\Apps\Python3\package_builder`
- Be sure to have 7-Zip installed before processing with the next step.
- Run `dev_build_python.bat` (You can use the indirection into a file to look back into the console output " > some_file_name  2>&1")

> Note: You cannot run `dev_build_python.bat` from an EPICS terminal

## First time

The first time you set up `genie_python`, assuming you've never installed it previously, you'll need to set up an ipython profile. 

1. From `C:\Instrument\Apps\Python3`, run `python.exe .\Scripts\ipython.exe profile create` (use the EPICSTerm if Command Prompt results in errors) 
1. Copy `ipython_config.py` from the `package_builder` directory to `C:\Users\[fedid]\.ipython\profile_default\.` If the .ipython folder does not exist, create one and inside it make a profile_default folder and paste the file there.


# Development workflow

1. Make sure you have a development version of `genie_python` set up as described above.
1. Create a branch for your changes as per the [standard development workflow](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Git-workflow).
1. Apply changes to the `genie_python` source at `C:\Instrument\Apps\Python3\Lib\site-packages\genie_python`, remembering to commit any changes to your branch.
1. If you need any extra libraries, or change `genie_python` dependencies, add them to `requirements.txt` and rerun `dev_build_python.bat` to make them available in your distribution. Note if you need extra libraries for a project other than `genie_python` see [here](Python-dependencies#how-python-dependencies-should-be-handled-in-the-future).
1. You can run the `genie_python` unit tests at any time with `C:\Instrument\Apps\Python3\python.exe C:\Instrument\Apps\Python3\Lib\site-packages\genie_python\run_tests.py`. Alternatively, from an EPICS terminal with the current working directory as `C:\Instrument\Apps\Python3\Lib\site-packages\genie_python` you can simply run `python run_tests.py`.

# Building notes

The batch file `common_build_python.bat` used by the developer and Jenkins build script does the following:

* Copies locally the Python packages where we have strict requirements on versions (e.g. NumPy) or created ourselves from a remote location (\\\\isis\\inst$\\Kits$\\CompGroup\\ICP\\genie_python_dependencies)

* Creates a virtual environment for installing all the required packages

* Installs all the required 3rd party packages. Some of the packages are stored locally as executables, some are zip files and some are downloaded

* Copies startup scripts from the `package_builder` directory into the installation

Jenkins only:

* Copies genie_python from the local directory in the virtual environment

* Copies site-packages directories into the clean Python installation

* Zips the Python installation and bundles it with the install scripts etc. 

* Copies the installation to the shared drive

# Developing

As well as writing units test for genie_python you can write system tests. These are located in the [genie_python_system_tests repository]( https://github.com/ISISComputingGroup/genie_python_system_tests). On your local machine run the run_tests.py; on the jenkins machine it will install the latest version of Ibex server and genie and run the tests.

To use a new config add it to the configs directory, it must start with `rcptt_` so it will be ignored by git in IBEX. In the setup of the test ensure that the config is loaded. 

To run a test in pycharm make sure you set the environment to be the same as your epics environment for the variable: `ICPCONFIGROOT`, `EPICS_CA_MAX_ARRAY_BYTES`, `EPICS_CA_ADDR_LIST` and `EPICS_CA_AUTO_ADDR_LIST`.

## Creating Python packages

Some of the packages we want to use do not come with an installer that is suitable for an automated build (e.g. PyQt) or are packages we have modified to meet our needs.
For these packages we have created our own installable units as zip files. To create one of these units for a package with an unsuitable installer follow these steps:

* Install the correct version of Python

* Install the package using the supplied installer

* In the Python directory, locate the package in Lib\\site-packages and zip it up with a name of the form name-x.x.x.zip where x.x.x is the version number of the package

* Copy the zip file to the shared drive (\\\\isis\\inst$\\Kits$\\CompGroup\\ICP\\genie_python_dependencies)

* Modify the build_python.bat file so it includes the new zip

For packages that we have modified it ourselves it is just necessary to create an appropriately named zip file and modify build_python.bat to unzip the file to \\Lib\\site-packages.

# Installing on the instruments

On the instrument connect to the shared drive (\\\\isis\inst$\Kits$\CompGroup\ICP\genie_python\\[latest version]) and run the genie_python_install.bat file.

Please check that Notepad++ is set to replace tabs with spaces - it saves a lot of bother later when writing scripts.

On some computer you may have to [set the core type that the `open blas` library uses](genie_python-Troubleshooting#genie_python-rashes-on-start-underlying-python-works-but-fails-on-import-numpy).

## The location of instrument specific scripts

By default when setting an instrument the `init_default.py` file is loaded. This file checks for the existence of a folder called `C:\Instrument\Settings\config\NDX%INSTNAME%\Python` and adds this to the system path if it does. If this path exists and contains a file called `init_%INSTNAME%.py`, it will load it too.

As this folder is added to the Python path any other files put in this directory can also be imported into genie_python. Note that this is *NOT* done automatically it is still necessary to type `from my_instrument_scripts import my_function`.

Scripts relating to the operation of the instrument should be kept in `C:\Instrument\Settings\config\NDX%INSTNAME%\Python` too. This means that they can then be versioned in git.User scripts should not be stored here.

## Quickly deploy minor changes to instruments

If changes have been made to the genie_python source (and tested!), it can be quicker just to copy the changed files onto the instrument directly rather than wait for the build server.

The genie_python source can be found in C:\Instrument\Apps\Python\Lib\site-packages\genie_python.
Restarting genie_python will pick up the changes.

# Importing from arbitrary locations

You can import modules from anywhere on your machine into genie_python. This is done for example for the shared scans library, which lives in `\Instrument\Scripts` by default. 

To do this, you must first append the location to the system path. The command for this is `sys.path.insert( <path> )`. You can now import modules in `<path>` normally.


# Troubleshooting

See the [genie_python troubleshooting guide](genie_python-Troubleshooting).
