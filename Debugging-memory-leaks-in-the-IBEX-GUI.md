# Debugging memory leaks in the IBEX GUI

## Symptoms

- Java memory leaks cause high CPU usage rather than the more intuitive high memory usage. The IBEX GUI is limited to a heap size of 500MB by default. When the heap gets close to it's maximum size, the garbage collector goes crazy trying to recover memory wherever it can, and therefore uses a lot of CPU.

- Because of the high CPU usage, the GUI will feel slow and sluggish.

- When there is no more memory available, java will crash with an `OutOfMemoryException`. Note that this exception might not occur on the GUI thread, and therefore various components running in separate threads might fail before the GUI crashes.

## Tools

- Java visual VM (`C:\Program Files\Java\jdk1.8.0_73\bin\jvisualvm.exe` for example)

- Eclipse debugger

- A way to reproduce the issue

## Setup

- In the java visual VM, on the left, you should see an `Eclipse (pid xxxx)` process. This is either your Eclipse IDE or IBEX. If you're unsure which is which, look under "Threads" for anything to do with ActiveMQ: This will be IBEX.

- Reproduce your issue, looking at the heap usage in the java visual vm. 

- A healthy GUI will show heap usage fluctuating quite a lot on a short-term basis, but with no long-term trend. 

- A GUI with a memory leak will also fluctuate in the short term, but will also have a long term trend upwards while the issue is being reproduced.

## Diagnosis

- Go under Sampler -> Memory and look at which objects are using up a lot of heap space. Note that this is only the object, **not** any of the objects that it owns!

```
public class MemoryLeak{
     RealMemoryLeak thisThingIsReallyBig = reallyBig; // Something enormous
}
```

will **not** make `MemoryLeak` show up as a large object!

- Under "monitor" you can create a Heap Dump. This is a file with information about all the objects that were loaded at the time. You might find this useful or not depending on your problem.

- Don't bother trying to "compute retained sizes": The IBEX program is too large and will cause the profiler itself to crash with an `OutOfMemoryException`.