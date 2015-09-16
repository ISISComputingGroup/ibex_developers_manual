=====================
Common Eclipse Issues
=====================

Sometimes the error messages that Eclipse gives are a little opaque, so here are some possible solutions for some of the more common issues.

The type XXXXXXX cannot be resolved. It is indirectly referenced from required .class files
-------------------------------------------------------------------------------------------
Possible solutions:

* Delete the complaining plugin from the workspace and then re-import it.
* Remove JRE System Library from the complaining plug-in's Java Build Path then re-add it.

Product XXXXXXXXXXX.product could not be found
----------------------------------------------

Typically is followed by a lot of errors relating to bundle resolution, for example:

.. code::

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

From this example it seems to be related to uk.ac.stfc.isis.ibex.ui.statusbar as that appears multiple times.

Possible solution:

* Check the offending plug-in has been added to one of the feature projects as a plug-in

