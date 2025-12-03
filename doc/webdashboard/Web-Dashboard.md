# Web Dashboard

The web dashboard allows some information about each instrument (currently DAE information and block values) to be viewed in a webpage from both inside and outside the ISIS network.

## Overall architecture

The [Web Dashboard](https://isiscomputinggroup.github.io/WebDashboard/) is very simple in architecture - it uses [PVWS](https://github.com/ornl-epics/pvws) to provide EPICS updates via a websocket, then displays these updates with [NextJS](https://nextjs.org/) as React components. 

This means the "backend" of the system is just PVWS. Any logic that needs to be done on PVs, for example `CS:INSTLIST` needs parsing as JSON, is done on the user's web browser. This allows us to deploy the web dashboard as purely static html; currently this is deployed to github pages on a push to `main` using [this](https://github.com/ISISComputingGroup/WebDashboard/blob/main/.github/workflows/nextjs.yml) github actions CI/CD workflow.

### Block history: Grafana and Journals Setup

Docs can be found on the shares at `shares\isis_experiment_controls\web_dashboard_history.docx`

### PVWS setup

See {ref}`pvws`

{#webdashboard_troubleshooting}
## Troubleshooting

### Web dashboard showing outdated or incorrect information

If you cannot subscribe directly to a PV by using the [PVWS homepage](https://ndaextweb4/pvws/) ie it gets no update with a value in it, this is likely due to a central gateway issue or an issue with the NDX.
