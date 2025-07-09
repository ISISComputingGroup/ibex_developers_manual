# `uv` and python environments

`uv` is a Python package and project manager. See [`uv`'s docs](https://docs.astral.sh/uv/) for more information.

We are currently considering whether we could use it to split up our python processes and use it for python version management on instrument machines. 

## `uv` files

- `c:\Instrument\apps\uv\` is the main installation folder for uv itself. 
- `c:\Instrument\apps\uv\snakes` is the location of individually-versioned python interpreter executables. These are "bare" interpreters, that do not contain any dependencies such as `genie_python`.
- `c:\Instrument\var\tmp\uvcache` is the location of `uv`'s pip download cache. This can safely be deleted and will be recreated as-needed.

## Details of `uv` setup

### IBEX install scripts

`uv` is used for a few things here. 

Firstly, installing the python executable itself onto an instrument machine.

Secondly, setting up a temporary virtual environment, which gets deleted at the end of the script, for using the deploy scripts themselves.

### Build jobs e.g. ConfigChecker

`uv` is used for creating a virtual environment for jenkins-run python checks. 

It can be used on Github actions CI, but isn't currently. 

### Instrument processes

In the future we may consider using `uv` to create and build virtual environments for each respective python process that runs on the NDX. This requires some decisions and subsequent work: 
- `uv.lock` files - should we keep them in source, or at least on the build server, then build venvs on the NDXes with those specific versions?
- python wheels need to be available for everything we use - the NDXes do not have compilers ie. Visual Studio installed.