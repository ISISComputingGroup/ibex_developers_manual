# Introduction

Starting from the July 2017 cycle, we are migrating IBEX from running on the Eclipse 3 platform to running on the Eclipse 4 platform. Initial investigation by Dominic Oram indicates that this is going to require significant time investment from the team.

# Selected platform

The goal of the project is to run IBEX on an Eclipse 4.x platform. Notably the current stable release of CSS is 4.4.3, which runs on Eclipse Mars (4.5), hence we have used this as our target platform as well as our development environment

# Getting started

## Setting up your E4 workspace

This is largely the same as [setting up your E3 workspace](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Building-the-GUI). It's best to create a separate workspace for your E3 & E4 development.

The e4 work is based on the the "master" branch that you will need to swap to. It is worth doing a "git clean -fdx" afterwards, but make sure there is no uncommitted work as you will lose it.

Launching the E4 application is very similar to the launching the E3 application as detailed in the getting started guide.

- Create a new workspace
- Import all of the plugins from `C:\Instrument\Dev\ibex_gui\base`
- Set the target platform. If it's covered in red, select each source followed by "Update" and "Reload". Once that's done, click "Set target platform"
- Clean project
- Open `ibex.product` in e4.client.product
- Click `Synchronize` in the `Testing` section
- Go to the `...e4.client.product` plugin.
- Click `Launch Eclipse application` or equivalent for debug
- you may need to launch a couple of time initially, the first launch failing due to checkstyle
- once you have run eclipse, you can set the run configuration as below
- Change your run configuration to clear the workspace on launch. Unless you do this in E4 applications, changes to the code are not always propagated to the build
    - Open the run configurations dialog
    - With "ibex.product" selected under "Eclipse Application" in the left-hand nav bar, go to the "Main" tab
    - Make sure the "Clear" box is ticked with the radio button set to "workspace"
    - Under the "Configuration" tab, select "Clear the configuration area before launching". _Note that this will lead to certain properties not persisting between IBEX instances as they should, e.g. remembering the last selected instrument._
    - Click "Apply" then close the dialog
- you can remove some of the errors shown by going to: window -> preferences -> maven -> error/warnings and setting "plugin ... lifecycle configuration" to "ignore" 

If you are still experiencing errors, you may still need to set up your new workspace for IBEX development. See [this page](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Creating-the-IBEX-Developer-Version-of-Eclipse) for instructions.

# Migrating an existing E3 perspective

See [Migrating or adding a button to the E4 perspective switcher](Migrating-or-adding-a-button-to-the-E4-perspective-switcher).

# The compatibility layer and preliminary migration

Eclipse 4 supports running Eclipse 3.x applications using the "compatibility" layer. In Eclipse 4.5, this is built into the tooling and so doesn't require any code changes to activate. The required plugins just need to be activated as part of the run configuration. Eclipse does an OK job at handling this automatically but has a tendency to either pull in too much if optional dependencies are included, or too little if they are not.

As part of the branch `Ticket2376_E4_Compatibility`, the code will build on the Eclipse 4 platform. However, I have not had much luck successfully launching IBEX in it's current form:

- Including all plugins in a workspace along with required plugins (and optional) results in an application that will not launch
- Including `*.ui.dashboard` and everything it needs (40 other IBEX plugins) results in an application that does make it to launch eventually (it struggles) but all of the plugins fail to initialise and there are many visual issues. Notably in this format, the current **views do not have fixed size**.

Owing to this investigation, and discussions with John and Kevin, I have chosen to create a brand new application based on the Eclipse 4 application model using the existing code as a base.

# E4 application prototype, July 2017 sprint

As part of the first stage of the application migration, I have created a branch `Ticket2376_E4_prototype_migrated`. To run it, set up a new E4 workspace as per [these instructions](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Eclipse-4-migration-notes#setting-up-your-e4-workspace).

Many of the application's views have been mocked using screenshots of the current system. These are 'cartoonified' to make them look less realistic to avoid confusion. The views that have been converted so far are the dashboard and the beam status view.

There are a few technical aspects that are worth noting that will affect future migration steps.

## The dashboard is coupled to the script generator

I discovered this while importing the minimal plugins for the dashboard. There is an architectural error in having it rely on the script generator. The dependency comes from `...ibex.ui.widgets`. This dependency should ideally be resolved.

## Don't forget `features.xml`.

At the moment, the plugins required for the build are defined in the `feature` plugins. We don't have to change these very often on master because we don't often add new plugins. However, we will do it very frequently on this branch. So that the run configuration is valid, when you add a new plugin, make sure to add it and any dependencies to the `feautre.xml` file. You shouldn't ever need to edit the included plugins via the `Run configurations` menu.

## Don't use `jre6.fragment`, it's a trap!

There's a CSStudio plugin called `jre6.fragment`. Despite appearances, it is an RAP, not and RCP plugin. If you include it, many of the views won't load properly. In some cases, I've had to add new imports into the target platform to get around this limitation. If you ask the "Run configurations" menu to add required plugins though, it will add it and your application will no longer run properly. You have been warned!

## To-dos

I've gotten into the habit of using `TODOs` in Eclipse to identify bits of work that I haven't yet gotten around to or rely on later stages of migration. They can be listed by opening up the Eclipse "Tasks" window.

# Useful people to talk to

Nick Battam at Diamond has been very helpful. He has also recommended we speak to Will Rogers, as he's done a lot of Eclipse 4 work in CSStudio.

# E4 application groundwork and early steps, August 2017 sprint

## Using an Eclipse 3.x CSS view in IBEX

The Application model in `uk.ac.stfc.isis.ibex.e4.client` defines the structure of the application. In a pure E4 application, when parts are created we use annotations and dependency injection to define when and how the views are constructed. That's different from Eclipse 3.x which used parts derived from `ViewPart` that call `createPartControl` instead of using the annotation `@PartConstruct`. Further, even if we do manage to build the view with some clever function calls, the RCP model is unavailable to us and we get lots of exceptions (e.g. `getSite()` returns `null`).

To use a CSS view, or something derived from it, in Eclipse 4, create a shared part element in the application model.
- For the ID of the part, give it the ID of the view you want to use (e.g. `uk.ac.stfc.isis.ibex.ui.alarm.AlarmView` - **make sure this ID corresponds to the class of the view!** You can check this by selecting the appropriate view in the target plug-in's `plugin.xml` in the `Extensions` tab under `org.eclipse.views`)
- For the `Class URI` use `bundleclass://org.eclipse.ui.workbench/org.eclipse.ui.internal.e4.compatibility.CompatibilityView`. When you use that shared element in your perspective, it will build and run as if it were in Eclipse 3.x.

## Hiding unwanted UI elements

The way Eclipse RCP works, if you include certain plugins (often denoted with the suffix `ui`) in your application, it will add certain elements to the UI, whether you want it to or not! Sometimes you can't avoid adding these plugins because they're required for something else you want to use. To get rid of them, hide them from the application model:

1. Make sure model spy is active. The feature `uk.ac.stfc.isis.ibex.feature.spies` should be included in `uk.ac.stfc.isis.ibex.feature.base`.
1. Open `ibex.product` in `uk.ac.stfc.isis.ibex.e4.client.product` and click `Synchronize` to make sure all relevant plugins have been activated in the run configuration
1. Launch the application
1. Press `Ctrl+Shift+F9` to access the application spies
1. Find the model spy and navigate to the element you want to hide
1. Add the element to `Application.e4xmi` in `uk.ac.stfc.isis.ibex.e4.client` and untick the `To Be Rendered` and `Visible` checkboxes


## Menu Items

To create a menu item:

1. Create a command in `Commands` in application
1. Create a menu item in the application model "windows and dialogue" > "Main menu" and use the command you have just created
1. Add the command to a command category if applicable (I am not sure why but it might be useful later)
1. Add a handler in which handles the command just created which is the same one used before the migration: 
    1. Change the handler to not inherit from AbstractHandler
    1. Replace `@override` on the execute method with a `@Execute` you will probably also want the shell injected to display stuff e.g.
        ```
        @Execute
        public void execute(Shell shell)
        ```
    1. Add an method and label @CanExecute this should return true if the command can be executed
1. Remove the menu item from the extension to avoid the errors like `[main] ERROR org.eclipse.ui.workbench - uk.ac.stfc.isis.ibex.ui.mainmenu.managermode.ManagerModeHandler cannot be cast to org.eclipse.core.commands.IHandler` 

# E4 migration continuation, November 2017 Sprint

## Adding a CSS editor to a view

When adding a CSS editor to a view (such as a DataBrowser), it will search the current application model for a part with id `org.eclipse.ui.editorss` to attach it to. You can create a placeholder in the desired place pointing at a shared element in which you want to display the databrowser. [This guide for re-using editor parts](https://openchrom.wordpress.com/2016/05/19/editor-3-x4-x-org-eclipse-ui-editorss/) contains instructions and screenshots for all the necessary steps.

