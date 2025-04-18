# CS-Studio Views in the GUI

## Source Code

We have our own fork of the CSS source code [here](https://github.com/ISISComputingGroup/cs-studio). This should be kept up to date with the original code [here](https://github.com/ControlSystemStudio) and only be used to branch from when modifying CSS for our own purposes. Modifying CSS should be done in discussion with the Core CS-Studio Developers and once any modifications have passed our review every effort should be made to merge them with the original.

CSS is built via jenkins. Clone [this repository](https://github.com/ISISComputingGroup/isis_css_top) recursively and build using `build.bat`.

## Archive Engine

The Archive Engine is part of CSS and is used to archive PV values. Note that most facilities use the [Archive Appliance](https://slacmshankar.github.io/epicsarchiver_docs/index.html) as the Archive Engine (specifically MySQL) was found to be slow at millions of PVs. As we don't have that many PVs we have continued to use the Archive Engine. For more details see [here](/system_components/CSS-Archive-Engine).

## Alarm Server

The Alarm Server is part of CSS and alerts the GUI to any PV alarm changes. There is also a CSS Alarm View that we use as part of our GUI.

* [Building the alarm server for MySQL](/system_components/alarms/Building-the-alarm-server-for-mysql)

* [Using the alarm server with MySQL](/system_components/alarms/Using-the-alarm-server-with-mysql)

## Operator Interfaces

OPIs are the main way that users interact with an IOC. They are GUIs created in CSS and imported into our GUI.

```{toctree}
:glob:
:titlesonly:

opis/*
```

## Other

```{toctree}
:glob:
:titlesonly:

css_other/*
```