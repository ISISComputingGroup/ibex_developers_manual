# Common Eclipse issues

Sometimes the error messages that Eclipse gives are a little opaque, so here are some possible solutions for some of the more common issues.

## Plugin execution not covered by lifecycle configuration

Go to window -> preferences -> Maven -> Errors/Warnings. 
Change "Plugin execution not covered by lifecycle configuration" to ignore in the drop down.

## The type XXXXXXX cannot be resolved. It is indirectly referenced from required .class files

### Errors appear for single plugin
Possible solutions (in order of desperation):

* Check the error message: you may need to add a dependency to the plugin that contains XXXXXXX. For example: if the error message is ```The type org.eclipse.ui.plugin.AbstractUIPlugin cannot be resolved. It is indirectly referenced from required .class files``` then the org.eclipse.ui plugin requires adding.bundle to the required bundle in the manifest file of your plugin.
* Delete the complaining plugin from the workspace and then re-import it.
* Remove JRE System Library from the complaining plug-in's Java Build Path then re-add it.
* This can also occur in similar cases to the **Invalid class hierarchy**.

### Errors appear across entire project

Suggests that eclipse has got itself into a funny state. Try `Project > Clean` first, if that does not get rid of the problems, try:
1. Reset the targetplatform: Open file in `uk.ac.stfc.isis.ibex.targetplatform`, reload dependencies if they are in error, then click `Reload Target Platform` top right
2. Synchronize the runnable product: open `ibex.product` in `uk.ac.stfc.isis.ibex.e4.client.product`, click `Synchronize this configuration with the product's defining plug-in.`
3. Confirm the problems have disappeared. (you may need to repeat step 1 & 2 a couple of times)
4. Launch application from `ibex.product` (little green arrow on the top right) and confirm the client starts

## Invalid class hierarchy

* Make sure that you don't have any circular dependencies. That is package A imports package B imports package A.
* If you have several layers of derived dependencies, particularly containing CSStudio or eclipse classes, make sure the correct bundles have been imported. Dependencies are not necessarily re-exported from the intermediate layers by default. There are two solutions:
    * Add the base bundle to the list of dependencies of your new class via the manifest file
    * Go through the classes you derive from. In their bundles go to the dependencies menu and click on the plugin you're deriving from. Click properties and check the box that says "Reexport this dependency". Once the intermediate layers all reexport their dependencies then it should become available to your class.


## Product XXXXXXXXXXX.product could not be found

Typically is followed by a lot of errors relating to bundle resolution, for example:

```
    !MESSAGE Product uk.ac.stfc.isis.ibex.product.product could not be found.

    !ENTRY org.eclipse.osgi 2 0 2015-09-16 15:25:45.343
    !MESSAGE One or more bundles are not resolved because the following root constraints are not resolved:
    !SUBENTRY 1 org.eclipse.osgi 2 0 2015-09-16 15:25:45.343
    !MESSAGE Bundle reference:file:/C:/CodeWorkspaces/GitHub/ibex_gui/base/uk.ac.stfc.isis.ibex.ui.perspectives/ was not resolved.
    !SUBENTRY 2 uk.ac.stfc.isis.ibex.ui.perspectives 2 0 2015-09-16 15:25:45.343
    !MESSAGE Missing required bundle uk.ac.stfc.isis.ibex.ui.statusbar_1.0.0.
    !SUBENTRY 1 org.eclipse.osgi 2 0 2015-09-16 15:25:45.343
    !MESSAGE Bundle reference:file:/C:/CodeWorkspaces/GitHub/ibex_gui/base/uk.ac.stfc.isis.ibex.product/ was not resolved.
    !SUBENTRY 2 uk.ac.stfc.isis.ibex.product 2 0 2015-09-16 15:25:45.343
    !MESSAGE Missing required bundle uk.ac.stfc.isis.ibex.ui.statusbar_0.0.0.
    !SUBENTRY 1 org.eclipse.osgi 2 0 2015-09-16 15:25:45.343
    !MESSAGE Bundle reference:file:/C:/CodeWorkspaces/GitHub/ibex_gui/base/.metadata/.plugins/org.eclipse.pde.core/.bundle_pool/plugins/uk.ac.gda.common_1.2.0.v20140919-1144.jar was not resolved.
    !SUBENTRY 2 uk.ac.gda.common 2 0 2015-09-16 15:25:45.344
    !MESSAGE Missing native code match lib/linux-x86/libgda_common.so; processor=x86; osname=linux, lib/linux-x86_64/libgda_common.so; processor=x86_64; osname=linux.

    !ENTRY org.eclipse.osgi 2 0 2015-09-16 15:25:45.389
    !MESSAGE The following is a complete list of bundles which are not resolved, see the prior log entry for the root cause if it exists:
    !SUBENTRY 1 org.eclipse.osgi 2 0 2015-09-16 15:25:45.389
    !MESSAGE Bundle uk.ac.stfc.isis.ibex.ui.weblinks_1.0.0.qualifier [460] was not resolved.
    !SUBENTRY 2 uk.ac.stfc.isis.ibex.ui.weblinks 2 0 2015-09-16 15:25:45.393
    !MESSAGE Missing required bundle uk.ac.stfc.isis.ibex.ui.perspectives_1.0.0.
    !SUBENTRY 1 org.eclipse.osgi 2 0 2015-09-16 15:25:45.393
    ...
    <Lots of similar messages removed>
    ...
    !MESSAGE Bundle uk.ac.stfc.isis.ibex.ui.perspectives_1.0.0.qualifier [465] was not resolved.
    !SUBENTRY 2 uk.ac.stfc.isis.ibex.ui.perspectives 2 0 2015-09-16 15:25:45.393
    !MESSAGE Missing required bundle uk.ac.stfc.isis.ibex.ui.statusbar_1.0.0.
```

From this example it seems to be related to uk.ac.stfc.isis.ibex.ui.statusbar as that appears multiple times.

Possible solution:

* Check the offending plug-in has been added to one of the feature projects as a plug-in

## New plugin is not available (and possibly crashing existing plugins)

This might be difficult to find as an error, and it may not exist for other developers - even on the same branch!
Adding the plugin directly to your configuration solves this.

## Plugins compile fine but dependencies cause errors at runtime

If you can run the application fine but are seeing a `java.lang.NoClassDefFoundError` at runtime, try re-setting the target platform, synchronizing `client.product` (under "testing" in the product overview), and doing a clean.

## Menu items are missing

This is usually because a dependency is missing. See "I really cannot work out why the GUI won't start!" below.

## No application ID

Starting the GUI via Eclipse just doesn't seem to work and I cannot see why!

One useful thing to try is to use the run configuration to check all the correct plug-ins are included:

* Right-click on ibex.product in uk.ac.stfc.isis.ibex.client.product and select Run As->Run Configurations...
* Select ibex.product under Eclipse Application
* From the tabs select "Plug-ins" and click the "Validate Plug-ins" button
* If it displays errors because plug-ins are missing:

    * Close the dialogs and add the missing plug-ins to the feature.xml file in uk.ac.stfc.isis.ibex.feature.base or one of the other features
    * Repeat this whole process again from the beginning
    
* If there are no errors then click the "Run" button to see if it works

Sometimes eclipse will tell you that you have errors in various projects when you open it. The following operations (may) help.
- Refresh, clean and build all projects. Select all projects, press F5 to refresh, then go to `Project -> Clean` to clean all projects.
- Go to `Run -> Run Configurations -> Plugins` and press "Add required plugins". You can now validate/apply your choice.
- In `uk.ac.stfc.isis.ibex.targetplatform`, open `uk.ac.stfc.isis.ibex.targetplatform.target` and click "set as target platform". 
- If all else fails, delete all the projects from eclipse's workspace and reimport them.

## The GUI starts but looks strange and some items (e.g. menu bar, perspective buttons) are missing

This can happen if the wrong ".product" file is run and not all plugins are defined in the application.

* Make sure you *only* run ibex.product in uk.ac.stfc.isis.ibex.**client**.product *not* any other ".product" file in the workspace e.g. uk.ac.stfc.isis.ibex.product

## I can't see changes in a new branch

Sometimes when you check out a new branch in the ibex GUI repository, you won't see any changes in the GUI. You can fix this by following the steps below:

1. In Eclipse, remove all the projects from the workspace and close Eclipse.
1. Then, while checked out to the branch you want to see the changes on, perform a `git clean -fdx && git reset HEAD --hard` to reset the git repository. This will remove any changes you have made to the branch.
1. Restart Eclipse and repeat the steps to get the GUI working from [Building the GUI](../compiling/Building-the-GUI).

## Build fails with `[ERROR] Failed to resolve target definition ... targetplatform.target: Could not find "org.eclipse.e4.tools.spies.feature.feature.group..." in the repositories of the current location`

This probably means that our pinned target has gone out of date and needs updating. Open the Eclipse IDE and click on `org.eclipse.tools/latest` and click `update` this should fail and show `Unable to locate installable unit ...`. To fix this remove the plugin and then add it from the `software site `, work with `org.eclipse.e4.core.tools.update - http://download.eclipse.org/e4/snapshots/org.eclipse.e4.tools/latest` then you add `Eclipse E4 - All Spies`.

## Validation error in target platform `jython` manifests

Make sure that `-Djdk.util.zip.disableZip64ExtraFieldValidation=true` is included in `eclipse.ini` (located right next
to the `eclipse.exe` executable).

## `java.lang.UnsupportedClassVersionError`

If you see a `java.lang.UnsupportedClassVersionError` error at runtime, then:
- Select Window -> Preferences -> Java -> Compiler
- Set compliance level to 21.

## Adding a dictionary to Eclipse's spelling checker

- In Eclipse open `Window > Preferences > General > Editors > Text Editors > Spelling`
- Change the "User defined dictionary" to `<ISIS Experiment Controls Shares>/Eclipse settings/code_dictionary.txt`

