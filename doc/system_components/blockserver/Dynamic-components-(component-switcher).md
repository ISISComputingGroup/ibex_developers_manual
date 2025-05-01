# Dynamic components (component switcher)

The ComponentSwitcher is a module within the blockserver which is responsible for dynamically editing configurations in response to a PV value update. It adds and removes components to all configurations to achieve this.

### Configuration

The config switcher configuration file is in 
```
C:\Instrument\Settings\config\...\configurations\ComponentSwitcher\component_switcher.json
```

and has a structure similar to the following:

```json
[
    {
        "pv": "PARS:USER:R0",
        "is_local": true,
        "value_to_component_map": {
            "0.0": "test1",
            "1.0": "test2"
        }
    }
]
```

Where:
- `pv` is the PV which should be monitored for changes
- `is_local` controls whether the local PV prefix should be prepended to the PV before the monitor is created
- `value_to_component_map` is a dict mapping the pv values as strings to *dynamic components* which should be added
  * These values must be strings as they are JSON dict keys. The monitor will cast all received values using `str()`

### Overview

When a monitor is received, the following actions take place:
- The value is cast to a string
- If the value has a non-zero STAT or SEVR, the update is logged but then ignored (we don't want to change configs based on an invalid value from hardware)
- If the value is not present as a key in `value_to_component_map`, the update is ignored and an error is logged
- For each configuration:
  * Remove all components which are present in both the configuration and the `value_to_component_map`, except the component which corresponds to the value just received
  * Add the component which corresponds to the value in `value_to_component_map`, if it was not already present
  * If the configuration changed, save it to disk
  * If this is the current configuration and it changed, reload the config to get the changes

### Dynamic components

**The ConfigSwitcher will only add and remove components which are marked with the `isDynamic` flag.** To mark a config as "dynamic", go into the edit component menu and tick the "dynamic" option. Note that this option applies to the components being added/removed, not the configuration they are added to (otherwise every configuration on MuSR would need to be marked as dynamic).

### Debugging

The ComponentSwitcher logs to the blockserver log with the prefix `ComponentSwitcher: `.