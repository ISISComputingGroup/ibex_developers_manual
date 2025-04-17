# Bluesky

For information about scanning using bluesky, including information about:
- The bluesky run engine, `RE`
- Bluesky ophyd-async devices (for example `BlockR`, `BlockRw`, `BlockRwRbv`, `ReflParameter`, or `SimpleDae`)
  * If you are looking at bluesky code which uses `async def` and `await`, and imports `ophyd_async`, you're probably looking at a device.
- Bluesky plans, (for example `scan`, `adaptive_scan`)
  * If you are looking at bluesky code with lots of `yield from` statements, you're probably looking at a plan.
- Bluesky callbacks (for example `LivePlot`, `LiveFit`, `ISISCallbacks`, file-writing)

**See [ibex_bluesky_core docs](https://isiscomputinggroup.github.io/ibex_bluesky_core).**

---

For troubleshooting, see [ibex_bluesky_core troubleshooting guide](https://isiscomputinggroup.github.io/ibex_bluesky_core/dev/troubleshooting.html#). 

Please add troubleshooting information to that guide (via a pull-request on `ibex_bluesky_core`) rather than this page.