# Creating a patch/hotfix branch

If there has been an EPICS dependency update, then taking DLLs/EXE from the latest build server or your desktop for an instrument will not work as there will be library mismatches. If you need to build a new exe/dll for an existing release, this is the procedure to setup a jenkins job for this 

If EPICS has a git tag v14.0.0 then

if first time you need to create branch
```
git checkout -b Release_14.0.0_hotfix v14.0.0
git push -u origin Release_14.0.0_hotfix
git submodule update --recursive
```
subsequently just change to it - either locally or if somebody else has already created it and pushed it
```
git checkout Release_14.0.0_hotfix
git submodule update --recursive
```
If you just want to use master of a new module, you can just `git add` that. In more complicated setups you may need to create a `Release_14.0.0_hotfix` branch in the submodule based on its original 14.0.0, cherry pick across relevant changes, and then `git add` the submodule at the top
