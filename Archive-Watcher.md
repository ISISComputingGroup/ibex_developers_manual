This program monitors the `data$` share on the NDX instrument specified and copies across new files to the local computer it is running on, it is installed as a windows service.
 
Run setup.exe from `\\isis\shares\ISIS_Experiment_Controls_Public\archive_watcher` it will install to `c:\Program Files (x86)\STFC ISIS Facility\ISIS Archive Watcher` and register as a service. If you get issues with setup.exe, just run msi on its own. After install create an admin window and run the `postinstall` bat script in the install directory. You then need to follow `README_POSTINSTALL.rtf` in this directory, you will create an `archive_watcher.properties` with relevant content. For musr this was
```
watcher.instrument = musr
watcher.fileprefix = musr
watcher.localdir = c:/data
watcher.copylogs = true
watcher.digits = 8
watcher.muonautosave = true
## if you want files pulled to this machine to be pushed elsewhere too, define watcher.pushto
watcher.pushto = file:////ndavms/musrdata
## if you want to override the default \\ndxinstrument\data$ file source define  watcher.sharename 
# watcher.sharename = 
```
`watcher.pushto` is not needed in most cases,  `watcher.muonautosave` set to false unless on a muon instrument. watcher.digits is 5 or 8, it is the number of digits in your raw file run number. `copylogs` is whether to copy the *.log/*.txt files as well as the raw data file.  





