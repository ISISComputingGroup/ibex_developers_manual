If you wish to clean up your area of all built/generated (i.e. not under version control) ready to do a complete rebuild, type:
```
git clean -fdx
git submodule foreach "git clean -fdx"
```

If you also wish to discard all uncommitted changes to any files in all directories, type:
```
git reset --hard
git submodule foreach --recursive "git reset --hard"
```

If appropriate, you can then do an update from the main git repository to get any recent changes:
```
git pull
git submodule sync
git submodule update
```

