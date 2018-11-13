> [Wiki](Home) > [Deployment](Deployment) > [Migrate an Instrument Control PC](Migrate-an-Instrument-Control-PC) > Creating a new branch for IBEX configurations

1. Navigate to `C:\Instrument\Settings\NDXxxxx` in a git bash terminal on an IBEX developer's machine (i.e. not an instrument)
1. Note the current branch you are on, usually this is will be the name of the machine you are working on, e.g. `NDXxxxx`
1. Review and commit any changes you have on your current branch
1. Run `git checkout master` and `git pull` to get the latest copy of the base configuration
1. Remove any uncommitted changes you have on your branch
    * NOTE: This may delete some uncommitted changes that you may wish to keep. Ensure these are all committed before running  `git clean -fdx`
1. Create and checkout a new branch for the instrument using `git checkout -b NDXyyyy` where `yyyy` is the name of the instrument in capital letters
1. Add any files that are needed in the new configuration
1. Commit the changes you have made
1. Review the state of the configuration to ensure that everything looks as you expect
1. Run `git push` to push your changes to the main git repository
1. `git checkout NDXxxxx` will get you back to your local configuration