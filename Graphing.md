The user has a requirement to graph data within the IBEX interface.

### Use case scanning

The experiment runs through a series of positions, after it reaches before it moves it changes period, then moves the motors then collects data. The user wants to plot the integral of a spectra against position. After each point is plotted the whole graph needs to be fitted to a Gaussian and this fit shown in the graph (possibly with the maximum).

This is needed just for the current run. 

## Implementation Plan

Initial create one set of pvs which capture a graph (it would be worth investigating whether this can be one Epics 4 pv):

- Title PV
- x axis name PV
- y axis name PV
- chart enabled PV
- 4 series:
    - series enabled PV
    - name of series PV
    - x values waveform PV
    - y values waveform PV

In the GUI display the above graph on an OPI at the point the chart becomes enabled.

Extend gennie_python with the following commands:

- `create_graph(title)`
- `close_graph()`
- `set_titles(title, xaxis, yaxis)`
- `append_point(series_num=0, x_value, y_value)`
- `empty_series(series_num=0)`
- `extend_points(series_num=0, x_valuex, y_values)`)

**Think about making this like a python list**

TODO: Reasons why

TODO: Extension to mat plot lib


 
