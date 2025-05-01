# Updating your local IBEX EPICS directory

## using a pre-built distribution

If you just want a clean start then you can use a pre-built build server checkout [[Developer-Server-Build]] as a new starting point. This is by far the easiest - it is the equivalent of deleting your current EPICS directory, doing a clean checkout and then building, just a bit quicker as it has already been built/compiled for you on the build server. If you have no important local changes (i.e. everything is pushed to github) then you will lose nothing and can just swap back to these branches after the new install.

## updating in-place

Here we will update all modules from git to the latest version and then rebuild. This however does not always proceed smoothly, mainly due to issues with the directory tree that is being updated. Some things that can cause problems are:
- a local directory has changed files and git will not want to overwrite these
- upstream has renamed a directory, git likes to do a delete and re-create, but it cannot do the delete if the directory is not empty (i.e. has some build products like .obj files in it or a subdirectory)

So you need to make sure that your directory tree is in a good state. You can probably do this iteratively after each failure as you update, or you can do it all first. 
- make sure all work is pushed. You don't usually need to reset branches back to master/main, but may be a good point to do this if work is finished 
- particularly after a dependency update where the likelihood of directory name changes is greatest, remove all build products: either `make clean uninstall` or `git submodule foreach --recursive "git clean -fdx"` from top directory. The git command is probably faster, but removes all files not under version control so you need to be sure you haven't forgotten to `git add` and push something to a remote branch.   

To check what branches all your submodules are on:

`git submodule foreach --recursive "git branch" | egrep "^Entering|^\*"`

If you don't see either "master" or "detached HEAD" then you need to decide if you really want to be on that branch, or just forgot to swap back after reviewing a ticket. If you are leaving a module on a non main/master branch, it may be worth merging the latest upstream main/master into this branch. 

To update, from a git shell at top do:

    git pull
    git submodule init
    git submodule update --init --recursive

You can use

    git submodule update --init --recursive --merge

if you wish to leave items on their branch and merge in upstream, if you leave off `--merge` you will get switched to a detached HEAD at the upstream version.    

If you want to remove local changes as they are causing issues, you can use `git reset --hard` in a module or `git submodule foreach --recursive "git reset --hard"` to do all from the top level.

For info, Jenkins does the following to update a git tree on a clean build:
```
git reset --hard
git clean -fdx 
git submodule foreach --recursive "git reset --hard"
git submodule foreach --recursive "git clean -fdx"
git fetch
git checkout master
git submodule init
git submodule sync
git submodule update --init --recursive
git reset --hard
git clean -fdx
git submodule foreach --recursive "git reset --hard"
git submodule foreach --recursive "git clean -fdx"
```

Now build IBEX in the usual way. See [[Things-to-know-as-a-developer]] for speeding up a build.

### Troubleshooting

typing `git status` should not show unexpected changes being flagged.

If you get errors, the most likely causes are:
1. A file was renamed, but EPICS has not updated its Makefile dependency rules and is still looking for the old one
2. A directory was renamed/deleted, but the original directory is still on your computer because it was not empty

For 1. a "make clean uninstall" in the directory concerned should be enough
For 2. You need to go to the directory and do a "git status" and remove any "untracked files" that shouldn't be there. The "git clean" command can be used for this, "git clean -fd" will remove all untracked files and directories. "git clean -fdx" will additionally remove files ignored by `.gitignore` (such as compiler build output). Some of our submodules now contain submodules of their own, if a `git status` keeps showing something as modified you may need to `git submodule update` in this module to update that directory properly.  

In many cases problems will be isolated to a particular module and you do not need to build everything again. If you are about to go home and want to set off a complete rebuild then you can do the following (assuming you have no untracked files you are working on and have forgotten to add to git)
```
    git clean -fdx
    git submodule foreach --recursive "git clean -fdx"
```
this simulates a clean checkout (its actually what Jenkins does too) 
   