Clone the source from https://github.com/ISISComputingGroup/genie_python.git

The process for building the product is automated; it just requires the build_python.bat file in the package_builder folder to be run.

The batch file does the following:

* Copies locally the Python packages where we have strict requirements on versions (e.g. NumPy) or created ourselves from a remote location (\\\\isis\\inst$\\Kits$\\CompGroup\\ICP\\genie_python_dependencies)

* Creates a virtual environment for installing all the required packages

* Installs all the required 3rd party packages. Some of the packages are stored locally as executables, some are zip files and some are downloaded

* Copies genie_python from the local directory in the virtual environment

* Copies the Scripts and site-packages directories into the clean Python installation

* Zips the Python installation and bundles it with the install scripts etc. and copies it to the shared kits$ drive
