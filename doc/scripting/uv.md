# `uv` and python environments

`uv` is a Python package and project manager. See [`uv`'s docs](https://docs.astral.sh/uv/) for more information.

We are currently considering whether we could use it to split up our python processes and use it for python version management on instrument machines. 

## `uv` files

- `c:\Instrument\apps\uv\` is the main installation folder for `uv` itself. 
- `c:\Instrument\apps\uv\snakes` is the location of individually-versioned python interpreter executables. These are "bare" interpreters, that do not contain any dependencies such as `genie_python`.
- `c:\Instrument\var\tmp\uvcache` is the location of `uv`'s pip download cache. This can safely be deleted and will be recreated as-needed.

{#installing_uv}
## Installing `uv`
We have a script which is used in various places to install `uv`. This will install `uv` into `c:\Instrument\apps\uv\` and can be run on instruments, build machines and developer machines. 

To install `uv` run `\\isis\shares\ISIS_Experiment_Controls_Public\ibex_utils\installation_and_upgrade\install_or_update_uv.bat`

For developer machines currently this can be used for things that aren't in `\Instrument\Apps\EPICS\` such as projects you have in `Instrument\dev\` or for manually running the items below. 

## Usage of `uv` in IBEX

### IBEX install scripts

`uv` is used for a few things here. 

Firstly, installing the python executable itself onto an instrument machine.

Secondly, setting up a temporary virtual environment, which gets deleted at the end of the script, for using the deploy scripts themselves.

### Build jobs e.g. ConfigChecker

`uv` is used for creating a virtual environment for jenkins-run python checks. 

It can be used on Github actions CI, but isn't currently. 

### Instrument processes

In the future we may consider using `uv` to create and build virtual environments for each respective python process that runs on the NDX. This requires some decisions and subsequent work: 
- `uv.lock` files - should we keep them in source, or at least on the build server, then build virtual environments on the NDXes with those specific versions?
- python wheels need to be available for everything we use - the NDXes do not have compilers ie. Visual Studio installed.

