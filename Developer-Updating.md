Updating your local IBEX

If you just want a clean start then you can use a pre-built build server checkout [[Developer-Server-Build]] as a new starting point

If you want to up date your existing checkout, read on...

Firstly you may want to check what branches all your submodules are on:

    git submodule foreach "git branch" | egrep "^Entering|^\*"

If you don't see either "master" or "detached HEAD" then you need to decide if you really want to be on that branch, or just forgot to swap back after reviewing a ticket.

From a git shell do:

    git pull
    git submodule update --init --recursive

You can now do either

    git submodule update --merge

or just

    git submodule update

The main difference is that --merge will leave you on any local branch you have switched to/working on and attempt to merge in new changes, whereas leaving off --merge will switch you from your branch to a new detached HEAD on master. 

Now build IBEX in the usual way. See [[Things-to-know-as-a-developer]] for speeding up a build.

### Troubleshooting

If you get errors, the most likely causes are:
1. A file was renamed, but EPICS has not updated its Makefile dependency rules and is still looking for the old one
2. A directory was renamed/deleted, but the original directory is still on your computer because it was not empty

For 1. a "make clean uninstall" in the directory concerned should be enough
For 2. You need to go to the directory and do a "git status" and remove any "untracked files" that shouldn't be there. The "git clean" command can be used for this, "git clean -fd" will remove all untracked files and directories. "git clean -fdx" will additionally remove files ignored by .gitignore (such as compiler build output)

In many cases problems will be isolated to a particular module and you do not need to build everything again. If you are about to go home and want to set off a complete rebuild then you can do the following (assuming you have no untracked files you are working on and have forgotten to add to git)

    git clean -fdx
    git submodule foreach "git clean -fdx"

this simulates a clean checkout (its actually what Jenkins does too) 
   