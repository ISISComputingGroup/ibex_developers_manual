# Introduction

Starting from the July 2017 cycle, we are migrating IBEX from running on the Eclipse 3 platform to running on the Eclipse 4 platform. Initial investigation by Dominic Oram indicates that this is going to require significant time investment from the team.

# Selected platform

The goal of the project is to run IBEX on an Eclipse 4.x platform. Notably the current stable release of CSS is 4.4.3, which runs on Eclipse Mars (4.5), hence we have used this as our target platform as well as our development environment

# The compatibility layer and preliminary migration

Eclipse 4 supports running Eclipse 3.x applications using the "compatibility" layer. In Eclipse 4.5, this is built into the tooling and so doesn't require any code changes to activate. The required plugins just need to be activated as part of the run configuration. Eclipse does an OK job at handling this automatically but has a tendency to either pull in too much if optional dependencies are included, or too little if they are not.

As part of the branch `Ticket2376_E4_Compatibility`, the code will build on the Eclipse 4 platform. However, I have not had much luck successfully launching IBEX in it's current form:

- Including all plugins in a workspace along with required plugins (and optional) results in an application that will not launch
- Including `*.ui.dashboard` and everything it needs (40 other IBEX plugins) results in an application that does make it to launch eventually (it struggles) but all of the plugins fail to initialise and there are many visual issues. Notably in this format, the current **views do not have fixed size**.

Owing to this investigation, and discussions with John and Kevin, I have chosen to create a brand new application based on the Eclipse 4 application model using the existing code as a base.

# E4 application prototype, July 2017 sprint

As part of the first stage of the application migration, I have created a branch `Ticket2376_E4_prototype_migrated`. To run it, follow the usual steps (more or less)

- Import all of the IBEX plugins in base into your workspace
- Set the target platform
- Open 'uk.ac.stfc.isis.ibex.e4.client.product', 'ibex.product'
- Click "Launch an Eclipse application"

Many of the application's views have been mocked using screenshots of the current system. These are 'cartoonified' to make them look less realistic to avoid confusion. The views that have been converted so far are the dashboard and the beam status view.

There are a few technical aspects that are worth noting that will affect future migration steps.

## The dashboard is coupled to the script generator

I discovered this while importing the minimal plugins for the dashboard. There is an architectural error in having it rely on the script generator. The dependency comes from `...ibex.ui.widgets`. This dependency should ideally be resolved.

## Don't forget `features.xml`.

At the moment, the plugins required for the build are defined in the `feature` plugins. We don't have to change these very often on master because we don't often add new plugins. However, we will do it very frequently on this branch. So that the run configuration is valid, when you add a new plugin, make sure to add it and any dependencies to the `feautre.xml` file. You shouldn't ever need to edit the included plugins via the `Run configurations` menu.

## Don't use `jre6.fragment`, it's a trap!

There's a CSStudio plugin called `jre6.fragment`. Despite appearances, it is an RAP, not and RCP plugin. If you include it, many of the views won't load properly. In some cases, I've had to add new imports into the target platform to get around this limitation. If you ask the "Run configurations" menu to add required plugins though, it will add it and your application will no longer run properly. You have been warned!

## TODOs

I've gotten into the habit of using `TODOs` in Eclipse to identify bits of work that I haven't yet gotten around to or rely on later stages of migration. They can be listed by opening up the Eclipse "Tasks" window. The current `TODOs` are:

- `BeamStatusView.java`: The PVs haven't been connected to the beam status view because the archiver doesn't connect properly yet
- 'BeamStatusView.java`: Using the `showToolbar(false)` command doesn't actually hide the toolbar in the beam status view. I've tried working around this but ran out of time. We should sort it out eventually but I've left it for the time being. We may want to change that entire part eventually to just be two databrowsers in different tabs rather than embedding the graph in a separate view. That relies on a later bit of work though.
- Perspective switching: I've written a basic perspective switcher `uk.ac.stfc.isis.ibex.e4.ui.perspectiveswitcher`. It does what we need it to for now but later on we should switch to using snippets rather than shared elements to build our perspectives. The reason is that shared elements retain changes to their size between perspectives which sounds nice but can lead to very weird behaviour. I think it's best avoided. Similarly, snippets will be necessary to do things like restoring default views of a perspective. In all, we shouldn't have to hard code our perspectives, so it would be better managed via an extension point.
# Useful people to talk to

Nick Battam at Diamond has been very helpful. He has also recommended we speak to Will Rogers, as he's done a lot of Eclipse 4 work in CSStudio.

# E4 application groundwork and early steps, August 2017 sprint

## Using an Eclipse 3.x CSS view in IBEX

The Application model in `uk.ac.stfc.isis.ibex.e4.client` defines the structure of the application. In a pure E4 application, when parts are created we use annotations and dependency injection to define when and how the views are constructed. That's different from Eclipse 3.x which used parts derived from `ViewPart` that call `createPartControl` instead of using the annotation `@PartConstruct`. Further, even if we do manage to build the view with some clever function calls, the RCP model is unavailable to us and we get lots of exceptions (e.g. `getSite()` returns `null`).

To use a CSS view, or something derived from it, in Eclipse 4, create a shared part element in the application model. Give it the ID of the view you want to use (e.g. `uk.ac.stfc.isis.ibex.ui.alarm.AlarmView`) and in `Class URI` use `bundleclass://org.eclipse.ui.workbench/org.eclipse.ui.internal.e4.compatibility.CompatibilityView`. When you use that shared element in your perspective, it will build and run as if it were in Eclipse 3.x.

## Hiding unwanted UI elements

The way Eclipse RCP works, if you include certain plugins (often denoted with the suffix `ui`) in your application, it will add certain elements to the UI, whether you want it to or not! Sometimes you can't avoid adding these plugins because they're required for something else you want to use. To get rid of them, hide them from the application model:

1. Make sure model spy is active. The feature `uk.ac.stfc.isis.ibex.feature.spies` should be included in `uk.ac.stfc.isis.ibex.feature.base`.
1. Open `ibex.product` in `uk.ac.stfc.isis.ibex.e4.client.product` and click `Synchronize` to make sure all relevant plugins have been activated in the run configuration
1. Launch the application
1. Press `Ctrl+Shift+F9` to access the application spies
1. Find the model spy and navigate to the element you want to hide
1. Add the element to `Application.e4xmi` in `uk.ac.stfc.isis.ibex.e4.client` and untick the `To Be Rendered` and `Visible` checkboxes

## Migrating an E3 perspective in a couple of easy steps

1. Open the Application.e4xmi from `uk.ac.stfc.isis.ibex.e4.client`
1. Go to `Snippets`
1. Click `Add` to add a new perspective
1. Set the perspective up using an existing migrated perspective as a template
    1. Set a sensible ID
    1. Give it a label
    1. Set the icon
    1. Add controls. This should be a hierarchy of part sash containers. You can see how it should be set up from the existing perspectives. Don't forget to set the container data where appropriate; it sets the relative size of sibling components.
1. Add the perspective-specific parts
    1. In the alarms perspective, you'll see one part in the final part sash container called alarms. Do the same thing in your new perspective, but give it an appropriate name
    1. Change the ID of your new part to the ID of the view class you want the perspective to open
1. Add the dependency of the view you've added to the `plugin.xml` in the `...e4.client` plugin
1. Add the new dependency to `...feature.base`
1. Open IBEX
1. Check the new perspective scales appropriately and change the layout accordingly if needed