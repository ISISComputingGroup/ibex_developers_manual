# Matplotlib

```{seealso}
- {external+ibex_user_manual:doc}`scripting/Matplotlib` on the user manual
- {external+matplotlib:doc}`index` (reference documentation)
```

We allow plotting in IBEX via {external+matplotlib:doc}`matplotlib <index>`. These plots will appear in the IBEX client.

As of [ticket 6719](https://github.com/ISISComputingGroup/IBEX/issues/6719), we are using a custom {external+matplotlib:doc}`matplotlib backend <users/explain/figure/backends>`. This backend comprises two main components:
- The websocket backend in `genie_python\matplotlib_backend\ibex_websocket_backend.py`, which is based on matplotlib's {external+matplotlib:py:obj}`WebAgg <matplotlib.backends.backend_webagg>` backend. This serves plots over a websocket connection.
- The front-end code in the `uk.ac.stfc.isis.ibex.ui.graphing` plugin in the GUI. This reads data from the websockets published by the backend. It is effectively a Java reimplementation of {external+matplotlib:py:obj}`WebAgg <matplotlib.backends.backend_webagg>`'s front-end code.

## Python (backend) component

Our custom backend is defined in `genie_python\matplotlib_backend\ibex_websocket_backend.py`. It uses/builds on {external+matplotlib:py:obj}`WebAggCore <matplotlib.backends.backend_webagg_core>` under the hood. 

Fundamentally, it is a relatively simple backend which publishes a websocket. This websocket can send or receive:
- Binary messages, send only. These are PNG-encoded frames which should be published by the frontend.
- String messages, send & receive. These are encoded using JSON. They can be used, for example:
  * To notify the front-end that a new frame is available
  * To allow the front-end to request a new frame
  * To allow the front-end to resize a plot
  * To allow the front-end to pan/zoom the plot, via mouse handlers. Note the front end simply sends mouse events to the backend, {external+matplotlib:py:obj}`WebAgg <matplotlib.backends.backend_webagg>` then interprets these and redraws an appropriate plot.

We have modified the backend to:
- Be non-blocking, so that scientists can update their plot and still continue running scripts in the background
- To notify the IBEX client on calling {external+matplotlib:py:obj}`matplotlib.pyplot.show`, so that IBEX can show the plot windows.


## GUI (java) component

{external+matplotlib:py:obj}`WebAgg <matplotlib.backends.backend_webagg>` is published by matplotlib as a browser-based backend. IBEX previously rendered plots in an embedded web browser view within an OPI, but this had significant reliability problems.

We have since moved to reimplementing the javascript based frontend code in java, as it is very simple. When matplotlib is updated, we should verify that plots still work and update the protocol in the GUI if the underlying protocol in {external+matplotlib:py:obj}`WebAgg <matplotlib.backends.backend_webagg>` has changed or been extended. However this should be relatively rare as WebAgg is designed to be embedded in other applications (per {external+matplotlib:doc}`gallery/user_interfaces/embedding_webagg_sgskip`).

The front-end receives binary messages from the backend, and displays the binary message content as a PNG in the user interface. The user interface also occasionally forces plots to be redrawn, so that any missed updates will not cause a plot to completely freeze/fail to update.

The user interface implements a buffered redraw mechanism to prevent very fast updates from the matplotlib backend from overwhelming the UI thread of the client. This is defined in `/uk.ac.stfc.isis.ibex.ui.graphing/src/uk/ac/stfc/isis/ibex/ui/graphing/websocketview/MatplotlibFigureViewModel.java` and currently limits the UI to drawing at 250ms intervals. **Forced** redraws happen at an interval of 2000ms, this helps us to "catch-up" if any updates have been missed and is required in order to get updates to some dynamic plots.