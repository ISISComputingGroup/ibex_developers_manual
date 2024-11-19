> [Wiki](Home) > [The Backend System](The-Backend-System) > [genie_python](Building-and-installing-genie_python)

---

> [!IMPORTANT]
>
> The previous `genie_python` repository, which handled both library and distribution, was split into two components in November 2024: 
> - [genie](https://github.com/ISISComputingGroup/genie), the library:
>   * An installable pip package, `genie_python`
>   * The `genie_python` module itself, i.e. the result of `from genie_python import genie` in python
> - [uktena](https://github.com/ISISComputingGroup/uktena), the distribution:
>   * A `python.exe` at a specific version
>   * Many pre-installed libraries including `numpy`, `scipy`, `genie_python`, `ibex_bluesky_core`, ...
>
> From the perspective of the uktena python distribution, `genie_python` is "just" another library which happens to be installed alongside many other libraries - there is no special handling of the `genie_python` library in uktena.

---

# Setting up uktena python distribution

- Check whether `C:\Instrument\Apps\Python3` already exists.
  * If it exists and `git remote get-url origin` returns `https://github.com/ISISComputingGroup/genie_python.git`:
    * Stop IBEX server
    * Remove the entire `C:\Instrument\Apps\Python3` directory
    * Proceed as if `C:\Instrument\Apps\Python3` did not exist
  * If it exists and `git remote get-url origin` returns `https://github.com/ISISComputingGroup/uktena.git`:
    * Perform a `git checkout master && git pull` in `C:\instrument\apps\python3`
  * If it does not exist, from a git-enabled command line, run `git clone https://github.com/ISISComputingGroup/uktena.git C:/Instrument/Apps/Python3` (or if using ssh authentication `git clone git@github.com:ISISComputingGroup/uktena.git`).
- Navigate to `C:\Instrument\Apps\Python3\package_builder`
- Be sure to have 7-Zip installed before processing with the next step.
- Run `dev_build_python.bat` (You can use the indirection into a file to look back into the console output " > some_file_name  2>&1")

> Note: You cannot run `dev_build_python.bat` from an EPICS terminal

## First time

The first time you set up python, assuming you've never installed it previously, you'll need to set up an ipython profile. 

1. From `C:\Instrument\Apps\Python3`, run `python.exe .\Scripts\ipython.exe profile create` (use the EPICSTerm if Command Prompt results in errors) 
1. Copy `ipython_config.py` from the `package_builder` directory to `C:\Users\[fedid]\.ipython\profile_default\.` If the .ipython folder does not exist, create one and inside it make a profile_default folder and paste the file there.


# Development workflow

The uktena python distributions uses released versions of all dependencies by default. However, you can install development versions of libraries into it easily using `pip` editable installs.

### Dev process
- Check out the library you want to develop into `c:\instrument\dev\some_library`
- Run `c:\instrument\apps\python3\python.exe -m pip install -e c:\instrument\dev\some_library[dev]`
- Your uktena python distribution now contains a development install of the relevant library, which can be automatically reloaded (i.e. there is no need to rebuild `uktena` or re-run the `pip install` step after making changes)

For example, to install `genie` in an editable configuration:
- `git clone https://github.com/IsisComputingGroup/genie c:\instrument\dev\genie` (if it doesn't already exist)
- `c:\instrument\apps\python3\python.exe -m pip install -e c:\instrument\dev\genie[dev]`

Or to install `ibex_bluesky_core` in an editable configuration:
- `git clone https://github.com/IsisComputingGroup/ibex_bluesky_core c:\instrument\dev\ibex_bluesky_core` (if it doesn't already exist)
- `c:\instrument\apps\python3\python.exe -m pip install -e c:\instrument\dev\ibex_bluesky_core[dev]`

Once you have made the changes you want in `c:\instrument\dev\<library>`, they should be committed and pushed from that repository as usual. `uktena` will pick up the changes by default next time the library is released to `PyPI`.

You can now make changes in `c:\instrument\dev\some_library`. 
- Python code changes will be picked up immediately by your development python, no need to re-install the dependency for python-only changes
- If your changes modify dependencies, you will need to re-run the `pip` command above to pick up the new dependencies

Once you are happy with your changes locally, commit and push them from `c:\instrument\dev\some_library` as usual.
- In order to pick up the changes in future built versions of uktena, the changes will need to be released to pypi.

> [!NOTE]
>
> Our python dependencies, along with many other external dependencies, all define a `[dev]` optional dependency group which contains dev-only dependencies (like linters, documentation build tools, debugging tools and so on). If you are editable-installing an external library, it may use a different convention - consult that library's documentation or `pyproject.toml` to see which dependency groups are available.

# Writing system tests

As well as writing unit tests for genie_python you can write system tests. These are located in the [genie_python_system_tests repository]( https://github.com/ISISComputingGroup/genie_python_system_tests). On your local machine run the run_tests.py; on the jenkins machine it will install the latest version of Ibex server and genie and run the tests.

To use a new config add it to the configs directory, it must start with `rcptt_` so it will be ignored by git in IBEX. In the setup of the test ensure that the config is loaded. 

To run a test in pycharm make sure you set the environment to be the same as your epics environment for the variable: `ICPCONFIGROOT`, `EPICS_CA_MAX_ARRAY_BYTES`, `EPICS_CA_ADDR_LIST` and `EPICS_CA_AUTO_ADDR_LIST`.

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
