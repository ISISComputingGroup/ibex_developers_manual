This page lists some dependencies which we are not updating for various reasons:

# Python 2

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |
| `iPython` | 5.9.0 | 7.12.0 | Newer version requires python 3 |
| `GitPython` | 2.1.14 | 3.0.5 | Newer version requires python 3 |
| `matplotlib` | 2.2.5 | 3.1.3 | Newer version requires python 3 |
| `scipy` | 1.2.3 | 1.4.1 | Newer version requires python 3 |
| `numpy` | 1.16.6 | 1.18.1 | Newer version requires python 3 |
| `xmlrunner` | 2.5.2 | 3.0.1 | Newer version requires python 3 |

# Python 3

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |
| `protobuf` | 3.6.1 | 3.11.3 | Newer version conflicts with `mysql-connector-python 8.0.19` |
| `pcaspy` | Git commit `085f06af23cc862387b0a272828e2a9009eb0935` | 0.7.2 | The git version is newer and has not yet been published to pypi |
| `CaChannel` | Git commit `92b53f2c5e81cc0dab178bc5b92ea058b17a7f7d` | 3.1.2  | The git version is newer and has not yet been published to pypi |

# GUI

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |
| CS-Studio | [Specific git commits](https://github.com/ISISComputingGroup/isis_css_top) | [master (4.6)](https://github.com/ControlSystemStudio/cs-studio/) | Although CS-Studio itself builds correctly under Java 11, diirt does not, which makes it impossible to build a consistent set of update sites for use by the GUI. Note that although the GUI builds using Java 11, **the CS-Studio update site is built using Java 8**. |
| Java (JDK) | 11.0.6 | 13 | JDK 13 is not an LTS version and will quickly become unsupported. At the time of writing (Feb 2020), 11.0.6 is the latest LTS version. |
| Sapphire GEF Editor Support | 2018-09 | N/A | No longer available in the latest repositories |
| Opal| 1.0.0 | ? | Project has been deprecated and moved into eclipse Nebula visualization widgets. Update process appears to be non-trivial. |

# System

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |
| Java | 8 | 11 (LTS) or 12 | The "System" java is used to run CS-Studio components such as the archive engine and alarm server. These components will not run on Java 11 until we can build all of CSS on java 11 - see GUI section above.

# EPICS

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |
