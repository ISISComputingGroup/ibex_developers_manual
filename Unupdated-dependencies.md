This page lists some dependencies which we are not updating for various reasons:

# Python 3

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |
| `CaChannel` | 3.1.3 | 3.1.3 | Currently installed using `pip install github link`. `pip install CaChannel` copies dll onto itself. |
| Python3 | 3.11.6 | 3.12.0 | [pathtools does not build with Python 3.12](https://github.com/gorakhargosh/pathtools/issues/13) as of 11/23 check. |

# GUI

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |
| Opal| 1.0.0 | ? | Project has been deprecated and moved into eclipse Nebula visualization widgets. Update process appears to be non-trivial. |

# EPICS

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |
