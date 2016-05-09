> [Wiki](Home) > [The Backend System](The-Backend-System) > genie_python

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

* Zips the Python installation and bundles it with the install scripts etc. and copies it to the shared drive

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

On the instrument connect to the shared drive (\\isis\inst$\Kits$\CompGroup\ICP\Client\genie_python) and run the genie_python_install.bat file.

### Quickly deploy minor changes to instruments

If changes have been made to the genie_python source (and tested!), it can be quicker just to copy the changed files onto the instrument directly rather than wait for the build server.

The genie_python source can be found in C:\Instrument\Apps\Python\Lib\site-packages\genie_python.
Restarting genie_python will pick up the changes.
