# Web Dashboard

```{important}
The previous web dashboard, which used to be available under `https://dataweb.isis.rl.ac.uk`, is being switched off as of October 2025.
```

## Frontend

The web dashboard's front-end is deployed [on github pages](https://isiscomputinggroup.github.io/WebDashboard/). Deployment is done automatically via continuous deployment when a new change is pushed to the main branch.

Documentation for the setup, including local developer setup instructions, are available [in the README of its repository](https://github.com/ISISComputingGroup/WebDashboard/blob/main/README.md).

{#pvws}
## Backend (`pvws`)

PVWS is a tool which lets you get EPICS PV information and expose it via a websocket. This is used as the backend for the web dashboard.

Information on how we run this can be found [in the README of the `pvws-config` repository](https://github.com/ISISComputingGroup/pvws-config/blob/main/README.md).

See also {doc}`webserver systems documentation </systems/Webserver>` for the computer on which `pvws` is hosted.

## Grafana and Journals Setup

Documentation can be found on the shares at `shares\isis_experiment_controls\web_dashboard_history.docx`
