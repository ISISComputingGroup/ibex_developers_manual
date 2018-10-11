The user has a requirement to graph data within the IBEX interface.

### Use case 1: Scanning

The experiment runs through a series of positions, after it reaches before it moves it changes period, then moves the motors then collects data. The user wants to plot the integral of a spectra against position. After each point is plotted the whole graph needs to be fitted to a Gaussian and this fit shown in the graph (possibly with the maximum).

This is needed just for the current run. 

### Use case 2: Field v Current

In muon experiments, scientists like to monitor the strength of the magnetic field as a function of the current. Here is a screenshot of a VI ![Field v Amps](https://user-images.githubusercontent.com/34268759/42496162-19d9a072-841d-11e8-9497-c4d23799bb57.png) 

showing 3 graphs which plot field against current.

### Use case 3: Counts v Current

In muon experiments, scientists like to monitor the muon count rates as a function of the current. Here is a screenshot of a graph ![Count Rates v Current](https://user-images.githubusercontent.com/34268759/42496176-23dcf1b4-841d-11e8-8797-3f89788ae3c2.jpg)

which plots muon count rates for each of the 3 muon instruments (HIFI, MUSR, EMU) against current.

## Implementation Plan

Initial create one set of pvs which capture a graph (it would be worth investigating whether this can be one Epics 4 pv) but with the view that there will be multiple of these:

- Title PV
- x axis name PV
- y axis name PV
- chart enabled PV
- Data series (configurable number):
    - series enabled PV
    - name of series PV
    - x values waveform PV (configurable max size)
    - y values waveform PV (configurable max size)

NB configurable here means like the number of user pvs. The PVs might live in the same place as the user pvs.

In the GUI display the above graph on an OPI at the point the chart becomes enabled.

Extend genie_python with the following commands:

- `graphs[graph_index]`: gets the `graph` object at index

Properties and methods on the graph object:

- `xlabel(label)`: set the x axis label
- `ylabel(label)`: set the y axis label
- `title(tile)`: set the graph title
- `show()`: set enabled true
- `hide()`: set enabled to False
- `plot(x_values, y_values, series=0)`: set the PVs to the given values
- `append_point(x_value, y_value, series_index=0)`: append a point to an existing series
- `clear_series(series_index=0)`: remove all points from a series
- `show_series(series_index=0)`: show series
- `hide_series(series_index=0)`: hide series
- `series_name(name, series_index=0)`: set the name of a series

## Decision

This issue has two parts the plotting of the data and the creation of that data.

### Plotting of the data

The plotting could be done client side or server side, just the image is sent to the client. The choice is client side plotting because it allows individual users to pan and zoom data. We also need to choose between exposing it in an OPI, using some other java component, using Mat plot lib.

*Suspended because of further requirements*

The data used to create the plots could be created server side or client 

1. Storing


TODO: Extension to mat plot lib


 
