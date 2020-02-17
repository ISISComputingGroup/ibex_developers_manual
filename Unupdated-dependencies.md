This page lists some dependencies which we are not updating for various reasons:

# Python 2

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |
| `iPython` | 5.9.0 | 7.12.0 | Newer version requires python 3 |
| `GitPython` | 2.1.14 | 3.0.5 | Newer version requires python 3 |
| `matplotlib` | 2.2.5 | 3.1.3 | Newer version requires python 3 |
| `scipy` | 1.2.3 | 1.4.1 | Newer version requires python 3 |
| `numpy` | 1.16.6 | 1.18.1 | Newer version requires python 3 |

# Python 3

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |
| `protobuf` | 3.6.1 | 3.11.3 | Newer version conflicts with `mysql-connector-python 8.0.19` |

# GUI

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |
| CS-Studio | [Specific git commits](https://github.com/ISISComputingGroup/isis_css_top) | [master (4.6)](https://github.com/ControlSystemStudio/cs-studio/) | Although CS-Studio itself builds correctly under Java 11, diirt does not, which makes it impossible to build a consistent set of update sites for use by the GUI. Note that although the GUI builds using Java 11, **the CS-Studio update site is built using Java 8**. |
| Java (JDK) | 11.0.4 | 12 | JDK 12 is not an LTS version and will quickly become unsupported. At the time of writing (Sept 2019), 11.0.4 is the latest LTS version. |
| Sapphire GEF Editor Support | 2018-09 | N/A | No longer available in the latest repositories |
| PyDEV | 5.9.2 | 7.3.0 | Versions 6.0 onwards have a bug which causes the python console to disappear when we press reset layout in the GUI. |

# System

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |
| Java | 8 | 11 (LTS) or 12 | The "System" java is used to run CS-Studio components such as the archive engine and alarm server. These components will not run on Java 11 until we can build all of CSS on java 11 - see GUI section above.

# EPICS

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |
| `EPICS Base` | 3.15.5 | 7.x.x | See [#4416](https://github.com/ISISComputingGroup/IBEX/issues/4416) |
