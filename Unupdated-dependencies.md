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
| CS-Studio | [Specific commit](https://github.com/ISISComputingGroup/isis_css_top) | [master (4.6 testing)](https://github.com/ControlSystemStudio/cs-studio/) | Although CS-Studio itself builds correctly under Java 11, diirt does not, which makes it impossible to build a consistent set of update sites for use by the GUI. Note that although the GUI builds using Java 11, **the CS-Studio update site is built using Java 8**. |
| Java (JDK) | 11.0.4 | 12 | JDK 12 is not an LTS version and will quickly become unsupported. At the time of writing (Sept 2019), 11.0.4 is the latest LTS version. |

# System

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |

# EPICS

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |
| `EPICS Base` | 3.15.5 | 7.x.x | See [#4416](https://github.com/ISISComputingGroup/IBEX/issues/4416) |
