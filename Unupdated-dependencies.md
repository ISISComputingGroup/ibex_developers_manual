This page lists some dependencies which we are not updating for various reasons:

# Python

Note: update to python 3 is being handled as a separate chunk of work

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |
| `Python 2` | 2.7.15 | 2.7.16 | Change only affects Mac OSX - no reason to update |
| `iPython` | 5.8.0 | 7.8.0 | Newer version requires python 3 |
| `GitPython` | 2.1.14 | 3.0.1 | Newer version requires python 3 |
| `matplotlib` | 2.2.4 | 3.1.1 | Newer version requires python 3 |
| `scipy` | 1.2.2 | 1.3.1 | Newer version requires python 3 |
| `numpy` | 1.16.5 | 1.17.2 | Newer version requires python 3 |

# GUI

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |
| CS-Studio | [Specific git commits](https://github.com/ISISComputingGroup/isis_css_top) | [master (4.6)](https://github.com/ControlSystemStudio/cs-studio/) | Although CS-Studio itself builds correctly under Java 11, diirt does not, which makes it impossible to build a consistent set of update sites for use by the GUI. Note that although the GUI builds using Java 11, **the CS-Studio update site is built using Java 8**. |
| Java (JDK) | 11.0.4 | 12 | JDK 12 is not an LTS version and will quickly become unsupported. At the time of writing (Sept 2019), 11.0.4 is the latest LTS version. |
| Eclipse framework | 2019-06 (4.12) | 2019-09 (4.13) | 4.13 was released mid-way through the dependency updates; it's not clear that it would benefit us greatly at this stage, and given that it is so new it may be unstable for a short time. The main changes in 4.13 relate to support for Java 13, which we are not using. |
| PyDEV | 5.9.2 | 7.3.0 | Versions 6.0 onwards have a bug which causes the python console to disappear when we press reset layout in the GUI. |

# System

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |
| Java | 8 | 11 (LTS) or 12 | The "System" java is used to run CS-Studio components such as the archive engine and alarm server. These components will not run on Java 11 until we can build all of CSS on java 11 - see GUI section above.

# EPICS

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |
| `EPICS Base` | 3.15.5 | 7.x.x | See [#4416](https://github.com/ISISComputingGroup/IBEX/issues/4416) |
