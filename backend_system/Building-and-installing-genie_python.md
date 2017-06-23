> [Wiki](Home) > [The Backend System](The-Backend-System) > genie_python

See also the [getting started guide](First-time-installing-and-building-(Windows))

### Development workflow

0. If you haven't installed genie_python as part of Python on your system yet, read the [getting started guide](First-time-installing-and-building-(Windows))
1. If you don't have a development version of genie_python already, clone the repo e.g. navigate to `C:\Instrument\Dev` and run command `git clone https://github.com/ISISComputingGroup/genie_python.git`
2. Make the desired modifications to genie_python
3. Open `build_python.bat` and comment out line 252 about building the MSI
3. Run `build_python.bat` - this will install a new version to c:\Instrument\Apps\Python-Build
4. Call the new functionality by running c:\Instrument\Apps\Python-Build\genie_python.bat

### Building

Note: these are essentially the same steps as used by the Jenkins build server.

Clone the source from https://github.com/ISISComputingGroup/genie_python.git

The process for building the product is automated; it just requires the build_python.bat file in the package_builder folder to be run.

The batch file does the following:

* Copies locally the Python packages where we have strict requirements on versions (e.g. NumPy) or created ourselves from a remote location (\\\\isis\\inst$\\Kits$\\CompGroup\\ICP\\genie_python_dependencies)

* Creates a virtual environment for installing all the required packages

* Installs all the required 3rd party packages. Some of the packages are stored locally as executables, some are zip files and some are downloaded

* Copies genie_python from the local directory in the virtual environment

* Copies the Scripts and site-packages directories into the clean Python installation

* Zips the Python installation and bundles it with the install scripts etc. 

* if called with the "install" parameter, installs it to c:\Instrument\Apps\Python and also copies it to the shared drive

### Creating Python packages

Some of the packages we want to use do not come with an installer that is suitable for an automated build (e.g. PyQt) or are packages we have modified to meet our needs.
For these packages we have created our own installable units as zip files. To create one of these units for a package with an unsuitable installer follow these steps:

* Install the correct version of Python

* Install the package using the supplied installer

* In the Python directory, locate the package in Lib\\site-packages and zip it up with a name of the form name-x.x.x.zip where x.x.x is the version number of the package

* Copy the zip file to the shared drive (\\\\isis\\inst$\\Kits$\\CompGroup\\ICP\\genie_python_dependencies)

* Modify the build_python.bat file so it includes the new zip

For packages that we have modified it ourselves it is just necessary to create an appropriately named zip file and modify build_python.bat to unzip the file to \\Lib\\site-packages.

### Installing on the instruments

On the instrument connect to the shared drive (\\\\isis\inst$\Kits$\CompGroup\ICP\genie_python\\[latest version]) and run the genie_python_install.bat file.

Please check that Notepad++ is set to replace tabs with spaces - it saves a lot of bother later when writing scripts.

### The location of instrument specific scripts

By default when setting an instrument the `init_default.py` file is loaded. This file checks for the existence of a folder called `C:\Instrument\Settings\config\NDX%INSTNAME%\Python` and adds this to the system path if it does. If this path exists and contains a file called `init_%INSTNAME%.py`, it will load it too.

As this folder is added to the Python path any other files put in this directory can also be imported into genie_python. Note that this is *NOT* done automatically it is still necessary to type `from my_instrument_scripts import my_function`.

Scripts relating to the operation of the instrument should be kept in `C:\Instrument\Settings\config\NDX%INSTNAME%\Python` too. This means that they can then be versioned in git.User scripts should not be stored here.

### Quickly deploy minor changes to instruments

If changes have been made to the genie_python source (and tested!), it can be quicker just to copy the changed files onto the instrument directly rather than wait for the build server.

The genie_python source can be found in C:\Instrument\Apps\Python\Lib\site-packages\genie_python.
Restarting genie_python will pick up the changes.
