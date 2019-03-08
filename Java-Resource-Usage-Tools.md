> [Wiki](Home) > [Project tools](Project-tools) > Java resource tools

# Java Memory and CPU Profiling and Leak Detection

## JVisualVM

This is started from any java jdk in bin double click on jvisualvm.exe. You can then immediately look at the heap of your java application.

You can then take a heap dump (button top right) and this can show where all the memory or instance have gone. (This can be extremely slow)

You can also look at what functions are using what resources by using the sampler or the profiler and using CPU/memory sampling or profiling.

# Setup JVisualVM to monitor a remote client

- Look in the log file for the client that you want to remotely monitor

- When the client first starts it will print `JMX url:` followed by a url that looks a bit like `service:jmx:rmi://machine/stub/rO0ABXNyAC5qYXZheC5tYW5hZ2V...`

- Add a JMX connection in the java visual VM and copy in the whole url

- **WARNING: using this interface you can do harm to the client and thus running experiments! Therefore you should only look at the monitoring graphs and use the sampler. For anything else you must inform the user that it may cause issues** 

## Memory Analyzer

Installed in eclipse through the market place (search for this)

Then edit your run configuration and include `-agentlib:hprof=heap=dump,format=b` in your VM arguments. When the program exists it produces a heap profile which the memory analyser can load and then find possible memory leaks in.

## See also

https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Debugging-memory-leaks-in-the-IBEX-GUI
