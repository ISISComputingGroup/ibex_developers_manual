The dataweb service allows some information about each instrument to be viewed in a webpage from both inside and outside the ISIS network. This service already exists for SECI instruments.

## The Overall Architecture

![Architecture](dataweb/images/dataweb_architecture.png)

The dataweb system consists of a number of parts running on each instrument:

---

### The Archive Engine

The archive engine shown in the [high level design](High-Level-Architectural-Design) produces internal webpages that provides live data on various PVs in HTML format:

* INST (located at http://localhost:4812/group?name=INST&format=json) gives data on the PVs associated with the DAE etc.
* BLOCKS (located at http://localhost:4813/group?name=BLOCKS&format=json) gives data on the current status of all block PVs
* DATAWEB (located at http://localhost:4813/group?name=DATAWEB&format=json) gives data on hidden blocks

### The WebServer

The webserver is run as part of the BlockServer and provides all of the data on the current configuration in JSON format. This is the exact same data that is served on the GET_CURR_CONFIG_DETAILS PV. The webserver is currently serving the data on localhost:8008. Note that the fortinet VPN uses 8008 for internal configuration and so you cannot access this address through the fortinet VPN.

---

### On the Dataweb Server

There are also parts of the system running on a central [webserver](Webserver), which provides external access.

### JSON Bourne

The program collates all the data from the other sources, on all the EPICS instruments, such as putting the blocks and their values into the relevant groups as given by the configuration. This information is served as JSON to localhost:60000. This runs as a service on the central server and lives in C:\JSON_Bourne.

### The Website

Currently a simple JS script takes the JSON created by JSON Bourne and provides a simple webpage for an external client to view. This can be accessed from http://dataweb.isis.rl.ac.uk/. The code for the website, both the html and javascript are located in the central server at `C:\inetpub\wwwroot\DataWeb\IbexDataweb`.

### Grafana and Journals Setup

Docs can be found on the shares at `shares\isis_experiment_controls\web_dashboard_history.docx`

## Deployment

To update the production version of the dashboard:
* Remote desktop into external webserver (for username and password see password page)
* Open a git bash terminal in C:\JSON_Bourne and switch to the [release branch](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Creating-a-release)
* Run the deploy batch script as admin
* Restart JSON_bourne (see [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Web-Dashboard#restart-the-dataweb))
* Go to (for example) http://dataweb.isis.rl.ac.uk/IbexDataweb/default.html?Instrument=zoom and confirm the webpage is live

## Development/Testing

Clone the repository at https://github.com/ISISComputingGroup/JSON_bourne

To test the blockserver webserver:
* Start your instrument
* Navigate to `localhost:8008` in a browser

To test JSON_Bourne:
* Run webserver.py
* Navigate in a browser to http://localhost:60000/?callback=parseObject&Instrument=[Instrument-Name]&.
  Where [Instrument-Name] is replaced by the desired instrument (i.e., ZOOM&) in all capitals.

To test the front end on a developer machine:
* Open default.html with the variable of ?Instrument=instrument-name e.g. go to `file:///C:/Instrument/Dev/JSON_bourne/front_end/default.html?Instrument=larmor` in a browser to view larmor's dashboard. Note that the path is dependant on where you have created the local JSON_bourne repository. This will use the JSON bourne instance running on NDAEXTWEB!

To test the front end and JSON bourne on a developer machine:
* Run `webserver.py`
* Edit display\_blocks.js to look at http://localhost rather than http://dataweb.isis.rl.ac.uk
* Open default.html as above

To be able to see your instrument as well:
* Add your instrument to the `local_inst_list` dictionary in the `webserver.py` e.g. `local_inst_list = {"LOCALHOST": ("localhost")}`
* Run your instrument
* Run JSON Bourne up as above

If you need to update the archive engine then you will need to:

1. Run create_icp_binaries.bat
1. `make clean uninstall install` in `..\EPICS\CSS\master`

## Troubleshooting

### General Investigation

First look at the log to ensure that there are no issues. The log is held in `C:\JSON_Bourne\log`. Issues may be in the front end, in which case error logs are in the web browser, visit the webpage in a browser and open up the web console.
If there are a number of `HTTP Error 503. The service is unavailable` errors, restarting the server completely may be required, but simply restarting the Dataweb should be the first thing to try.

### Restart the Dataweb

As admin open the "Task Scheduler" (there is a shortcut for this on the desktop) and end and run the "JSON Bourne" task (in task scheduler library). Make sure that ending the task has killed the Python webserver process.

### New Instrument with No Details

If the instrument archive has never been restarted then the dataweb will fail to show any information and claim that the server hasn't been started. To fix this simple restart the instrument archive.

### Page for Individual Instrument not Working

[See here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Other-Troubleshooting#instrument-page-not-working-on-web-dashboard)

## Future Development Ideas

* We need to improve the unit test coverage of this project. It would be worth looking into the [requests-mock](https://pypi.python.org/pypi/requests-mock) library as this would make it very easy to test server code which makes HTTP requests.

## Overview page

http://dataweb.isis.rl.ac.uk/IbexDataweb/Overview/ibexOverview.html