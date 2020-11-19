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
| `stomp.py`  | 2.24.0 | 6.1.0 | Newer version requires python 3 |

# Python 3

| Dependency | Our version | Available version | Reason |
| `CaChannel` | 3.1.3 | 3.1.3 | Currently installed using `pip github link`  |
| `matplotlib` | 3.2.2 | 3.3.3 | 3.3 onwards do not work on IE and hence do not work within GUI (plot renders blank)  |

# GUI

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |
| Java (JDK) | 11.0.8 | 13 | JDK 13 is not an LTS version and will quickly become unsupported. At the time of writing (Oct 2020), 11.0.8 is the latest LTS version. |
| Sapphire GEF Editor Support | 2018-09 | N/A | No longer available in the latest repositories |
| Opal| 1.0.0 | ? | Project has been deprecated and moved into eclipse Nebula visualization widgets. Update process appears to be non-trivial. |

# EPICS

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |
