It is possible to get additional actions to be carried out by DAE IOC when commands such as begin/end/pause/resume/abort are executed. These actions are typically used to do things like open/close an intermediate (fast) shutter. A `PRE` action is executed before the command and a `POST` after it has run. Whether the IOC waits for a PRE/POST to complete before the next action is controlled by whether `PP` or `CA` is passed as part of configuration, `CA` will wait for a completion callback and `PP` will just inititate processing. The PV specified will have the number 0 written to it for a PRE action and 1 for a POST action, usually you will specify the `.PROC` of a PV so just processing is initiated, but you can specify e.g. the `.VAL` and it will get 0 or 1 written to it as appropriate   

The PV links to access are set by macros, either in the configuration or in globals.txt. The have names like `PRE_BEGIN_1` and `POST_BEGIN_1`, to specif in globals you would add something like   
```
ISISDAE_01__PRE_BEGIN_1=TE:NDW2127:DAE:DUMMYPRE PP
```
Not the PP added at the end to request processing
