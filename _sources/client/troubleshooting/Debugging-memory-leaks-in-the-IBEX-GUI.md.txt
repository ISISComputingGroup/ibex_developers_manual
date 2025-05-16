# Debugging memory leaks in the IBEX GUI

This page is currently heavily based on https://github.com/ISISComputingGroup/IBEX/issues/2017. Please update this as we gain more experience!

## Symptoms

- Java memory leaks cause high CPU usage rather than the more intuitive high memory usage. The IBEX GUI is limited to a heap size of 1024MB by default. When the heap gets close to it's maximum size, the garbage collector goes crazy trying to recover memory wherever it can, and therefore uses a lot of CPU.

- Because of the high CPU usage, the GUI will feel slow and sluggish.

- When there is no more memory available, java will crash with an `OutOfMemoryException`. Note that this exception might not occur on the GUI thread, and therefore various components running in separate threads might fail before the GUI crashes.

## Tools

- Java visual VM (download the GPL-licensed binary from https://visualvm.github.io/download.html ) 
    - If you experience problems trying to run the standalone client where a pop up warning windows notifies you of a JRE problem, try first checking if you have the correct version of Java in your system environment variables and that no older/newer versions exist in addition to the correct version (removing if necessary). Secondly, try the following command next to the VisualVM executable you are having issues with: `visualvm.exe --jdkhome c:\Progra~1\Eclips~1\jdk-11.0.14.9-hotspot` changing the version of jdk where applicable to the version you have.
- Eclipse debugger
- A way to reproduce the issue

## Setup

- In the java visual VM, on the left, you should see an `Eclipse (pid xxxx)` process. This is either your Eclipse IDE or IBEX. If you're unsure which is which, look under "Threads" for anything to do with ActiveMQ: This will be IBEX.

- Reproduce your issue, looking at the heap usage in the java visual vm. 

- A healthy GUI will show heap usage fluctuating quite a lot on a short-term basis, but with no long-term trend. 

- A GUI with a memory leak will also fluctuate in the short term, but will also have a long term trend upwards while the issue is being reproduced.

## Setup to monitor a remote client

- Look in the log file for the client that you want to remotely monitor

- When the client first starts it will print `JMX url:` followed by a url that looks a bit like `service:jmx:rmi://machine/stub/rO0ABXNyAC5qYXZheC5tYW5hZ2V...`

- Add a JMX connection in the java visual VM and copy in the whole url

- **WARNING: using this interface you can do harm to the client and thus running experiments! Therefore you should only look at the monitoring graphs and use the sampler. For anything else you must inform the user that it may cause issues** 

## Diagnosis 1

- Under `Sampler -> Memory` and look at which objects are using up a lot of heap space. Note that this is only the object, **not** any of the objects that it owns!

```java
public class MemoryLeak{
     RealMemoryLeak thisThingIsReallyBig = reallyBig; // Something enormous
}
```

will **not** make `MemoryLeak` show up as a large object!

You may also find it useful to look at the instance count of suspicious classes. If some action in the GUI causes the instance count of a class to go up but not down again when closed, this is almost certainly a memory leak (but not necessarily a large memory leak - so it's possible that it's not the leak you're looking for).

## Diagnosis 2

Once you have a few candidate objects from above which you think are suspicious, use the eclipse debugger to inspect them at runtime. If you find that they're very big / contain a lot of items, then your problem has been located. If not, then rinse and repeat Diagnosis 1.

## Diagnosis 3

If you have objects which you think should be being garbage collected, but are not, then you can find out why they are being kept around using the Visual VM.
- Reproduce the issue (so that the GUI contains some objects which should have been released)
- Connect VisualVM
- Force a garbage collection by clicking the "GC now" button
- Under the "memory sampler" view, create a heap dump
- In the heap dump, search for the class that you're interested in
- Click the "GC root" button. This may take a few seconds, but will show you the reference chain which is keeping the object in memory
- You will now need to figure out where you need to "break" this chain, so that the object can be reclaimed. You may need to iterate this process several times if the object is referred to by multiple garbage collection roots. Eventually, once all reference chains from GC roots have been broken, the object should be eligible for GC.

## Fixing

Once you've diagnosed *where* the memory leak is, you need to fix it. This may not be obvious at first! There's not really any generic help that can be given here.

## Notes

- The java garbage collector is responsible for cleaning up dereferenced objects. If your objects aren't being freed when you click the `Perform GC` button in java visual VM, then you still have references to them somewhere.
  * The java garbage collector uses reachability analysis, not reference counting, to test whether an object can be GC'd. The garbage collection "roots" are listed [here](https://www.ibm.com/support/knowledgecenter/en/SS3KLZ/com.ibm.java.diagnostics.memory.analyzer.doc/gcroots.html), but usually in IBEX these will be either statically reachable objects (e.g. singletons) or the current stack frame for each running thread.
- Some things need to be closed before/on garbage collection, for example sockets. Java's `finalize()` method is called once an object is eligible for GC, but before it is actually GC'd. Beware of using finalizers to perform "cleanup" - in some cases (e.g. closing observables), not running the cleanup will mean the object will still be reachable and so the finalizer will never be run!

## Observables

One common problem that we have repeatedly run into in IBEX is the use of observables. If an observer can be created multiple times, it is **very important** that it gets removed when no longer required. Otherwise, the observable will still have a reference back to the observer, which will prevent both the observer and anything which the observer references from being garbage collected. In other words, this will lead to a memory leak. The only case where is is acceptable for an observable to never be removed is if it is only created a small constant number of times and is necessary for the full lifetime of the client (for example, the instrument list).

We have considered in the past making the reference from an observable to it's observers a `WeakReference`, however this does not work in many cases as the observable is often the only reference to the observer, meaning that the observer will be garbage collected and not work.

