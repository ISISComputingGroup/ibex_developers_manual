# Debugging memory leaks in the IBEX GUI

This page is currently heavily based on https://github.com/ISISComputingGroup/IBEX/issues/2017. Please update this as we gain more experience!

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

## Diagnosis 1

- Go under Sampler -> Memory and look at which objects are using up a lot of heap space. Note that this is only the object, **not** any of the objects that it owns!

```
public class MemoryLeak{
     RealMemoryLeak thisThingIsReallyBig = reallyBig; // Something enormous
}
```

will **not** make `MemoryLeak` show up as a large object!

- Under "monitor" you can create a Heap Dump. This is a file with information about all the objects that were loaded at the time. You might find this useful or not depending on your problem.

- Don't bother trying to "compute retained sizes": The IBEX program is too large and will cause the profiler itself to crash with an `OutOfMemoryException`.

## Diagnosis 2

- Once you have a few candidate objects from above which you think are suspicious, use the eclipse debugger to inspect them at runtime. If you find that they're very big / contain a lot of items, then your problem has been located. If not, then rinse and repeat Diagnosis 1.

## Fixing

Once you've diagnosed *where* the memory leak is, you need to fix it. This may not be obvious at first! There's not really any generic help that can be given here.

## Notes

- The java garbage collector is responsible for cleaning up dereferenced objects. If your objects aren't being freed when you click the `Perform GC` button in java visual VM, then you still have references to them somewhere.

- Some things need to be closed before/on garbage collection, for example sockets. Java's `finalize()` method is called just before the object is GC'd, and can be used to close anything that needs closing.

- The JVisualVM can also be connected to a client running on an instrument machine through JMX, the port used for JMX is dynamic and can be found by looking through the client logs.

- Good luck :)