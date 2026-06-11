# Bluesky

For information about scanning using bluesky, including information about:
- The bluesky run engine, {external+ibex_bluesky_core:py:obj}`RE <ibex_bluesky_core.run_engine.get_run_engine>`
- Bluesky ophyd-async devices (for example {external+ibex_bluesky_core:py:obj}`BlockR <ibex_bluesky_core.devices.block.BlockR>`, {external+ibex_bluesky_core:py:obj}`BlockRw <ibex_bluesky_core.devices.block.BlockRw>`, {external+ibex_bluesky_core:py:obj}`BlockRwRbv <ibex_bluesky_core.devices.block.BlockRwRbv>`, {external+ibex_bluesky_core:py:obj}`ReflParameter <ibex_bluesky_core.devices.reflectometry.ReflParameter>`, or {external+ibex_bluesky_core:py:obj}`SimpleDae <ibex_bluesky_core.devices.simpledae.SimpleDae>`)
  * If you are looking at bluesky code which uses `async def` and `await`, and imports `ophyd_async`, you're probably looking at a device.
- Bluesky plans, (for example `scan`, `adaptive_scan`)
  * If you are looking at bluesky code with lots of `yield from` statements, you're probably looking at a plan.
- Bluesky callbacks (for example {external+ibex_bluesky_core:doc}`LivePlot <callbacks/plotting>`, {external+ibex_bluesky_core:doc}`LiveFit <callbacks/fitting/fitting>`, {external+ibex_bluesky_core:doc}`ISISCallbacks <callbacks/isiscallbacks>`, {external+ibex_bluesky_core:doc}`file-writing <callbacks/file_writing>`)

**See {external+ibex_bluesky_core:doc}`index`.**

---

For troubleshooting, see {external+ibex_bluesky_core:doc}`ibex_bluesky_core troubleshooting guide <dev/troubleshooting>`.

Please add troubleshooting information to that guide via a pull-request onto the [ibex_bluesky_core repository](https://github.com/ISISComputingGroup/ibex_bluesky_core/), rather than this page.