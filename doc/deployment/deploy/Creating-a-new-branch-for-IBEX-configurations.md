# Creating a new branch for IBEX configurations

This creates the repository to save all the IBEX configurations for a new instrument.

1. Navigate to `C:\Instrument\Settings\NDXxxxx` in a git bash terminal on an IBEX developer's machine (i.e. not an instrument)
1. Note the current branch you are on, usually this is will be the name of the machine you are working on, e.g. `NDXxxxx`
1. Review and commit any changes you have on your current branch
1. Run `git checkout master` and `git pull` to get the latest copy of the base configuration
1. Remove any uncommitted changes you have on your branch
    * NOTE: This may delete some uncommitted changes that you may wish to keep. Ensure these are all committed before running  `git clean -fdx`
1. Create and checkout a new branch for the instrument using `git checkout -b NDXyyyy` where `yyyy` is the name of the instrument in capital letters
1. Run the [config upgrader](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Config-Upgrader) to get this into an up to date state
1. Run `git push` to push your changes to the main git repository
1. `git checkout NDXxxxx` will get you back to your local configuration