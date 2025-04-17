If you wish to clean up your area of all built/generated (i.e. not under version control) files ready to do a complete rebuild, type:
```
git clean -fdx
git submodule foreach "git clean -fdx"
```

The above is very similar to doing a "make clean uninstall" but much faster. **WARNING**: if you have created a new file and not yet added it to version control, it will get deleted too, so you may want to use "git status" first to check.
 
If you also wish to discard all _staged_ uncommitted changes to any files in all directories, type:
```
git reset --hard
git submodule foreach --recursive "git reset --hard"
```

If you want to discard all _unstaged_ changes, type:
```
git checkout -- .
```
to get rid of all unstaged changes, or:
```
git checkout -- path/to/file
```
to discard changes to a specific file. Note that this will have no effect on changes staged for commit.  

The above combination of clean and reset are equivalent to a new checkout, but much quicker. In fact this is what Jenkins does for clean builds.

If appropriate, you can then do an update from the main git repository to get any recent changes:
```
git pull
git submodule init
git submodule sync
git submodule update --merge
```

