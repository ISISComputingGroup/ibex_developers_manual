> [Wiki](Home) > [The Backend System](The-Backend-System) > [Nicos](Nicos) > Installing Nicos on Windows

You can find a broad introduction to Nicos [here](http://cdn.frm2.tum.de/fileadmin/stuff/services/ITServices/nicos-master/dirhtml/).

The Nicos source was written primarily for Linux and so things can be a bit more difficult on Windows.

## Install Genie python
As we intend to integrate with IBEX, we are going to work with Genie Python. You can use any Python 2 (2.6 or higher) distribution instead, though some steps may vary between 32 and 64-bit versions.

Genie Python can be installed by following the instructions [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/First-time-installing-and-building-(Windows)).

For the remainder of this wiki, when we refer to Python, it is Genie Python and all commands launched using Python should use the Genie Python executable.

## Clone the Nicos repository

The `nicos-core.git` repository is a submodule of the EPICS repository under `EPICS\ISIS\ScriptServer\nicos-core`.
Make sure you have it in your system.

## Install C++ compiler for Python 2.7

Install the Microsoft Visual C++ compiler for Python 2.7, which can be downloaded [here](http://aka.ms/vcpython27).

## Install sip

sip allows Python to access C/C++ libraries as Python modules. Unfortunately, the site does not provide a "wheel" installation package for Python 2 so we'll need to compile from source.

### Set up environment variables

If you are already running an EPICS terminal, you should skip this step as the necessary environment variables are set as standard. If you're using a standard command prompt, you should continue with this section.

We're going to use Visual Studio 2010 to run the make file and install sip, so install it if you don't already have it. Any recent version of Visual Studio should suffice. 

You may need to update some of the following paths based on your Visual Studio version and install location.

To set your environment variables correctly, run

    "C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\vcvarsall.bat" amd64

The ```amd64``` option sets the environment to use 64-bit tools. This is important because Genie Python is distributed as a 64-bit version of Python. If you wish to use a 32-bit version of Python, remove this option and use the defaults. 

You should now be able to run ```nmake``` successfully from the command line.

### Installing **sip** from source

Download the Windows source zip for **sip** from [here](https://www.riverbankcomputing.com/software/sip/download) and extract it to a local directory. Navigate to that directory and run the following command (using the same Python as is used for Genie e.g. `c:\Instrument\Apps\Python3\python.exe`)

    ...\python.exe configure.py

This will generate the necessary make file. 

Next (from the same directory) run

    nmake

then

    nmake install

With any luck, sip is now installed in your version of Genie Python.

#### Trouble shooting

If you receive the error `NMAKE : fatal error U1065: invalid option '-'` the environment variable `MAKEFLAGS` has been set to something undesirable. Blank it with `set MAKEFLAGS=`

## Get other required Python libraries

From the location of nicos-core, run the following

```
    ...\Python\scripts\pip.exe install -r requirements.txt
```

*Last time this didn't work for me and I got the error `Fatal error in launcher: Unable to create process using '"'`. In this case running `...\Python\python.exe -m pip install -r requirements.txt` worked instead.*

This will grab all of the required Python libraries for Nicos. Then run:

    ...\Python\scripts\pip.exe install --extra-index-url https://forge.frm2.tum.de/simple  nicos-pyctl

The installation for the Nicoslivewidget will fail. That's expected. Isabella and I tried hard to get the live widget to work to no avail. It means the live view will be unavailable when you launch the Nicos gui. As we don't intend to use that part of Nicos in IBEX, we've chosen to proceed without further attempts to resolve this issue.

## Check Nicos is installed correctly

Navigate to

    ...\nicos-core\bin

and run

    ...\Python\python.exe nicos-demo

This will launch the Nicos demo, which is comprised of several services, including a server monitoring window and the main Nicos gui.

#### Troubleshooting

* If you see errors about version numbers, it is because Nicos is trying to use ```git``` in the shell. You can fix this either by adding git to your PATH variables, or by launching the Nicos demo from a git-enabled bash.

* On error: `Starting NICOS demo system, please wait: cacheFatal error while initializing: Setup cache does not exist (setup paths are C:\Instrument\nicos-core\custom\NDW1407\setups)` this is an environment variable set wrongly. Rerun this from a new (standard non-EPICS) command line terminal

