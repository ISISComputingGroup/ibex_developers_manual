> [Wiki](Home) > [genie_python](genie_python) > [Python Dependencies](Python-dependencies)

> [!NOTE]
>
> Much of the information on this page is now obsolete.
>
> The split of library and distribution was done in [ticket 8381](https://github.com/ISISComputingGroup/IBEX/issues/8381)
>
> `genie_python` can now be installed via `pip`.

This page as much as possible distinguishes between the standard Python version installed on instruments/developer machines and the `genie_python` module that is actually used to communicate with IBEX. These have historically been conflated by both users and developers, leading to the problems outlined in below.

### How Python Dependencies were Historically Handled

Historically when a new Python module was required by any part of the IBEX system it was added as a requirement to the singular standard python installation. As the project has grown this has lead to a number of problems:

* It is unclear where and how our dependencies are used particularly the split between dependencies of the server, client and of a scientist using `genie_python` alongside other tools
* Increased risk that dependency updates will break something
* Additional overhead in what we are giving to users as their Python client
* Conflict of requirements between projects

### How Python Dependencies should be Handled in the Future

To move away from this it was decided by Freddie, Dom, Tom and John in a meeting on 19/05/2020 that we should aim instead for a system where every Python project within the IBEX system had it's own requirements listed in a `requirements.txt` and ran in a separate clean `virtualenv`. This is obviously a large change to the system so it was proposed that rather than do this in one go:

* Every time a new requirement is added to the system going forward the project that needed it be adapted to conform to the new model
* Every time a new Python project is started it uses the model described above

Currently, because of the conflation between the `genie_python` module and the installed Python, there is no easy mechanism to install `genie_python` into a clean `virtualenv` and so it is impossible to move to the proposed model. To fix this we should make `genie_python` able to be installed via `pip` (see [here](https://github.com/ISISComputingGroup/IBEX/issues/3571)). In the meantime a virtual environment should be created with all of the installed modules of the parent Python, this can be done using `virtualenv my_env --system-site-packages`. You should assume that all you are inheriting is the `genie_python` module and still list requirements even if you know they will come with the Parent python. In this way we should be able to remove dependencies in the installed python version without affecting your module.