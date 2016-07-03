If you wish to clean up your area of all compiled/generated files to do a complete rebuild, type:
```
git clean -fdx
git submodule foreach git clean -fdx
```

If you wish to discard all changes to any files in all directories, type:
```
git reset --hard
git submodule foreach --recursive git reset --hard
```

You can then do an update:
```
git pull
git submodule sync
git submodule update
```

