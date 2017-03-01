> [Wiki](Home) > [Project tools](Project-tools) > Java memory leak tools

# Java Memory Profiling and Leak Detection

## JVisualVM

This is started from any java jdk in bin double click on jvisualvm.exe. You can then immediately look at the heap of your java application.

You can then take a heap dump (button top right) and this can show where all the memory or instance have gone.

## Memory Analyzer

Installed in eclipse through the market place (search for this)

Then edit your run configuration and include `-agentlib:hprof=heap=dump,format=b` in your VM arguments. When the program exists it produces a heap profile which the memory analyser can load and then find possible memory leaks in.

## See also

https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Debugging-memory-leaks-in-the-IBEX-GUI
