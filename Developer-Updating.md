Updating your local IBEX

Firstly you may want to check what branches all your submodules are on:

    git submodule foreach "git branch" | egrep "^Entering|^\*"

If you don't see either "master" or "detached HEAD" then you need to decide if you really want to be on that branch, or just forgot to swap back after reviewing a ticket.

From a git shell do:

    git pull
    git submodule init

You can now do either

    git submodule update --merge

or just

    git submodule update

The main difference is that --merge will leave you on any local branch you have switched to and attempt to merge in changes, whereas leaving it off will switch you from a branch to a new detached HEAD just put you on a 
See [[Things-to-know-as-a-developer]] for speeding up a build