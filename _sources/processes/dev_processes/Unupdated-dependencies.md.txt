# Unupdated dependencies

This page lists some dependencies which we are not updating for various reasons:

## Python

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |
| `CaChannel` | 3.1.3 | 3.1.3 | Currently installed using `pip install github link`. `pip install CaChannel` copies dll onto itself. |

## GUI

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |
| Opal | 1.0.0 | ? | Project has been deprecated and moved into eclipse Nebula visualization widgets. Update process appears to be non-trivial. |
| `com.sun.istack.commons-runtime` | `3.x` | `4.x` | Causes `javax`/`jakarta` conflicts with `javax.activation`. |
| `activemq` | `5.x` | `6.x` | v6 uses `jakarta` packages, CSS needs `javax` packages. Need to update CSS to resolve. |

## EPICS

| Dependency | Our version | Available version | Reason |
| --- | --- | --- | --- |
