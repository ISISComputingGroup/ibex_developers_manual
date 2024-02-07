# LabVIEW errors

This page documents common LabVIEW errors and how to resolve them

## Large LabVIEW log files in `Users\<username>\AppData\Local\Temp`

Symptom: the above files of the form `*_cur.txt` and `*_log.txt` are very large and getting spammed with messages of the form 

```
VirtualInstrument::GetNumOfBreaks: negative mNumBreakpoints (4294967295); vi=[LinkIdentity "Vector-control-v16isis.vi" [ Main Application Instance]
```

To the best of our knowledge this is an incompatibility between different versions of LabVIEW. If you open "Breakpoint manager" in the LabVIEW GUI this will stop the errors with the message 

```
BkptManager::InitLVDialog: FixNumBreakpointsCount because GetNumOfBreaks was -1(now 0) on [VI "Vector-control-v16isis.vi" (0x06de49c0)]
```

However, this is not a permanent fix and the errors will return if LabVIEW is restarted. More permanent fix is to make a no-op change to the VI (e.g. slightly move a label), and press save, this forces LabVIEW to re-save the VI, and this stops the errors from returning on next LabVIEW start.

Note that the `_cur.txt` log is the log from the currently-running instance of labview, while `_log.txt` is from the last instance to run. So to fully make the large logs disappear LabVIEW needs to be restarted twice. Alternatively you can manually delete the logs.

This is probably caused by the 3dmagnet https://github.com/ISISComputingGroup/EPICS-Magnet3D/blob/master/magnet3DApp/protocol/lv_controls.xml