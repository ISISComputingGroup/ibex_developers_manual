> [Wiki](Home) > [Project tools](Project-tools) > Java resource tools

# Java Memory and CPU Profiling and Leak Detection

## JVisualVM

This is started from any java jdk in bin double click on jvisualvm.exe. You can then immediately look at the heap of your java application.

You can then take a heap dump (button top right) and this can show where all the memory or instance have gone. (This can be extremely slow)

You can also look at what functions are using what resources by using the sampler or the profiler and using CPU/memory sampling or profiling.

The JVisualVM can also be connected to a client running on an instrument machine through JMX on port 3333.

## Memory Analyzer

Installed in eclipse through the market place (search for this)

Then edit your run configuration and include `-agentlib:hprof=heap=dump,format=b` in your VM arguments. When the program exists it produces a heap profile which the memory analyser can load and then find possible memory leaks in.

## See also

https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Debugging-memory-leaks-in-the-IBEX-GUI
