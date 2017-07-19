If you wish to clean up your area of all built/generated (i.e. not under version control) files ready to do a complete rebuild, type:
```
git clean -fdx
git submodule foreach "git clean -fdx"
```

The above is very similar to doing a "make clean uninstall" but much faster. Note that if you have created a new file and not yet added it to version control, it will go too, so you may want to use "git status" first to check.
 
If you also wish to discard all uncommitted changes to any files in all directories, type:
```
git reset --hard
git submodule foreach --recursive "git reset --hard"
```

The above combination of clean and reset are equivalent to a new checkout, but much quicker. In fat this is what Jenkins does for clean builds.

If appropriate, you can then do an update from the main git repository to get any recent changes:
```
git pull
git submodule init
git submodule sync
git submodule update
```

