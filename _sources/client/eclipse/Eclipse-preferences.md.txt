# Eclipse preferences

There are two sorts of settings. 

`System.getProperty("x")` will read a setting supplied on the command line as `-Dx=value`. To set in Eclipse go to "Run/Run Configurations..." and add to the "VM arguments" on the Arguments tab

The second sort are Eclipse preferences. On the plugin's extensions tab under "org.eclipse.core.runtime.products/???? (product)" there should be a preferenceCustomization proper whose value is the name of the preferences file. In that file set a property like:

```
org.csstudio.isis.product/prefix = NDW1298:sjb99183:
```

To access it from org.csstudio.isis.product:

```
prefix = DefaultScope.INSTANCE.getNode(Activator.PLUGIN_ID).get("prefix", "no found");
```
