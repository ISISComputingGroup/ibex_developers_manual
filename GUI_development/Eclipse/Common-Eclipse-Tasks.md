> [Wiki](Home) > [The GUI](The-GUI) > [Eclipse](GUI-Eclipse) > Common Eclipse tasks

## Add A New Plugin

1. In Eclipse IDE, File Menu > New > Plugin Project.
1. Give the Project a name, e.g. ``uk.ac.stfc.isis.ibex.foo``. If it is a UI plugin, it should have a "ui" in the top part of the name e.g. ``uk.ac.stfc.isis.ibex.ui.foo`` 
1. For location, select the base source code folder, e.g., ``C:\Instrument\Dev\Client\base\uk.ac.stfc.isis.ibex.foo``, rather than the default option (which will probably be the workspace).
1. Click next.
1. Make sure 'Generate an activator, a Java...' is checked.
1. If this is to be a UI plugin, check 'This plug-in will make contributions to the UI'. This will cause the Activator to extend ``AbstractUIPlugin`` rather than ``BundleActivator``. Plugins that contribute to the UI in any way such as by adding a preference page or menu item, need to be UI plugins
1. Click finish.
1. In the plugin ``uk.ac.stfc.isis.ibex.feature.base``, open ``feature.xml`` and go to the 'Plug-ins' tab. Add your new plugin to the plug-ins list.

1. Add a ``pom.xml file`` to the plugin so that it can be built with maven. This should be the same as the pom file in every other project; the only thing you'll need to change is the plugin's name (the ``artifactId``). The contents should be as below. Other sections of the pom follow will be inherited from ``org.csstudio.isis.tycho.parent`` and so don't need to be explicitly included:
    ```xml
    <project xmlns="http://maven.apache.org/POM/4.0.0" 
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
        xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
          http://maven.apache.org/xsd/maven-4.0.0.xsd">
      <modelVersion>4.0.0</modelVersion>
      <artifactId>uk.ac.stfc.isis.ibex.foo</artifactId>
      <packaging>eclipse-plugin</packaging>
      <parent>
        <groupId>CSS_ISIS</groupId>
        <version>1.0.0-SNAPSHOT</version>
        <artifactId>uk.ac.stfc.isis.ibex.client.tycho.parent</artifactId>
        <relativePath>../uk.ac.stfc.isis.ibex.client.tycho.parent</relativePath>
      </parent>
      <version>1.0.0-SNAPSHOT</version>
    </project>
    ```
1. In the plugin ``uk.ac.stfc.isis.ibex.client.tycho.parent``, add your new plugin to the list of modules (you may have to do this manually in the XML view).


## Easy Plugin Access

One option to enable easy access to your plug-in object is to use the singleton pattern. Declare a static variable in your plug-in class for the singleton. Store the first (and only) instance of the plug-in class in the singleton when it is created. Then access the singleton when needed through a static ``getDefault()`` method. Your Activator class should look something like this:
```java
public class Activator extends AbstractUIPlugin 
{
    public static final String PLUGIN_ID = "org.csstudio.isis.ui.logger";

    private static Activator plugin;

    public Activator() {
    }

    public static Activator getDefault() {
        return plugin;
    }

    public void start(BundleContext context) throws Exception {
        super.start(context);
        plugin = this;
    }

    public void stop(BundleContext context) throws Exception {
        plugin = null;
        super.stop(context);
    }
}
```

## Force Plugin To Start At Eclipse Startup

Normally plugins are loaded lazily, i.e., the first time they are actually needed. It can be useful to force a plugin to start when the program launches.

In your plugin:

1. Make a class called, e.g., ``org.csstudio.isis.foo.FooStartup`` that extends the Eclipse interface, ``IStartup``. Override the public method ``earlyStartup()``, with blank implementation.
1. Open ``META-INF`` > ``MANIFEST.MF`` > ``Extensions`` tab. Make sure "Show only extension points from required plug-ins" is unchecked.
1. Click ``Add`` and type: ``org.eclipse.ui.startup``.
1. In the Extension element details, select the startup, ``FooStartup``, class you created earlier.


## Running A Background Job

In Eclipse, Jobs are units of runnable work that can be scheduled to be run with the job manager. Once a job has completed, it can be scheduled to run again (jobs are reusable). You might want to use a job to prevent UI freeze, i.e., if clicking a button performs a long operation or calculation, you still want the UI to respond while performing the operation. You might also use a job if a task needs to run continuously in the background for the lifetime of the program (as is the case for the JMS handler thread that receives messages from the IOC log server).

A job can be prepared as follows:
```java
Job fooJob = new Job("My Foo Job") 
{
    @Override
    protected IStatus run(IProgressMonitor monitor) 
    {
        fooCalculator.performLongTask();
        return Status.OK_STATUS;
    }
};
```
The string passed to the constructor will be the name of the thread that you will see if you are debugging the application.

The job can be started with:
```java
fooJob.schedule();
```
More details can be found in the [Vogella tutorial](http://www.vogella.com/tutorials/EclipseJobs/article.html).


## Updating The UI (Without Data Binding)

Where possible, you should use the Eclipse data binding framework to update UI elements (see [Vogella databinding tutorial](http://www.vogella.com/tutorials/EclipseDataBinding/article.html); however in some cases this is not convenient or possible.

The display of UI elements is not handled in the main execution thread but in a separate UI thread. Consequently, if you attempt to alter the display of any UI element from the main thread, you will get an Invalid Thread Access exception. We can overcome this limitation by calling the ``Display.asyncExec()``, which passes a runnable command to the UI thread and asks for it to be run at the next available opportunity.

As an example, if you had a UI class, FooDisplay, which had a method, ``setLabelText()``, you might implement it as follows:
```java
public class FooDisplay extends Canvas
{
    private Label fooLabel;

    private void setLabelText(final String text)
    {
        Display.getDefault().asyncExec(new Runnable() 
        {
            @Override
            public void run() {
                fooLabel.setText(text);
            }
        });
    }
}
```

## Add A New Perspective

Instructions on adding a new perspective can be found [here](Adding-a-Button-to-the-Perspective-Switcher).

Add A Preference Page
---------------------

Many plugins may have options that you want the user of the client to be able to configure. The simplest way to achieve this is to have the plugin contribute a preference page to the client's preference window.

1. Make sure your plugin contributes to the UI, i.e., that its activator class extends ``AbstractUIPlugin``, not ``BundleActivator``, and that it has a static ``getDefault()`` method.
1. In your plugin, add a new preference package, called e.g., ``org.csstudio.isis.foo.preferences``.
    
1. Create a new class called e.g., ``FooPreferenceConstants``, which will store tags and default values for each preference in your plugin. In the below example, we specify tags and defaults for a String preference called name and a integer preference called count. The tags are used internally by eclipse to refer to the preference and will not be displayed to the user:
    ```java
    public class FooPreferenceConstants 
    {
        public static final String TAG_NAME = "fooName";
        public static final String TAG_COUNT = "fooCount";

        public static final String DEFAULT_NAME = "This is my foo name!";
        public static final int DEFAULT_COUNT = 5;
    }
    ```    
1. Create a new class called e.g., ``FooPreferenceInitializer``, that extends ``AbstractPreferenceInitializer``, which will set the default values of each preference:
    ```java
    public class FooPreferenceInitializer 
        extends AbstractPreferenceInitializer {

        public void initializeDefaultPreferences() {
            IPreferenceStore store 
                = Activator.getDefault().getPreferenceStore();

            store.setDefault(FooPreferenceConstants.TAG_NAME, 
                FooPreferenceConstants.DEFAULT_NAME);
            store.setDefault(FooPreferenceConstants.TAG_COUNT, 
                FooPreferenceConstants.DEFAULT_COUNT);
        }
    }
    ```      
1. Add a new preference page class called, e.g., ``FooPreferencePage``, and have it extend the Eclipse class ``FieldEditorPreferencePage`` and implement the interface ``IWorkbenchPreferencePage``.
1. Add a constructor and implementations of the functions ``creatFieldEditors()`` and ``init()``:
    ```java
    public class FooPreferencePage extends FieldEditorPreferencePage 
        implements IWorkbenchPreferencePage 
    {
        public FooPreferencePage() {
            super(GRID);
            setPreferenceStore(Activator.getDefault().getPreferenceStore());
            setDescription("Settings for Foo.");
        }

        @Override
        public void createFieldEditors() {
            addField(new StringFieldEditor(FooPreferenceConstants.TAG_NAME, 
                "Foo Name", getFieldEditorParent()));
            addField(new StringFieldEditor(FooPreferenceConstants.TAG_COUNT, 
                "Foo Count", getFieldEditorParent()));
        }

        @Override
        public void init(IWorkbench workbench) {
        }
    }
    ```
1. Open the plugins ``plugin.xml`` and navigate to the Extensions tab.

  * Add the extension ``org.eclipse.core.runtime.preferences``.
  * To this, add a new ``Initializer`` and set its class as ``FooPreferenceInitializer``.
  * Add the extension ``org.eclipse.ui.preferencePages``.
  * To this, add a new ``Page`` and set its class to ``FooPreferencePage``. You can also set the ``name``, which will displayed in the UI.

The ``plugin.xml`` should look like the following:
```xml  
<?xml version="1.0" encoding="UTF-8"?>
<?eclipse version="3.4"?>
<plugin>
   <extension point="org.eclipse.core.runtime.preferences">
      <initializer 
        class="org.csstudio.isis.foo.preferences.FooPreferenceInitializer">
      </initializer>
   </extension>
   <extension point="org.eclipse.ui.preferencePages">
      <page
        class="org.csstudio.isis.foo.preferences.FooPreferencePage"
        id="org.csstudio.isis.foo.preferences.FooPreferencePage"
        name="Foo Preferences">
      </page>
   </extension>
</plugin>
```
When you start the client, the Foo preference page should now appear in the Eclipse Preferences window. Changes made by the user will be persisted to file automatically by the Eclipse framework and will be reloaded next time the user starts the client.

For more details see the [Vogella preferences tutorial](http://www.vogella.com/tutorials/EclipsePreferences/article.html).


## Add A Menu

Sometimes it may be necessary to add a new menu item to the menu bar in the Eclipse client so you can open some sort of dialog window or perform some other action. If you want the menu item to open a dialog, make sure you already have a ``Dialog`` class prepared in your plugin.

1. Create a class that extends ``org.eclipse.core.commands.IHandler``; call it something like ``FooHandler``. Add the unimplemented methods.
1. Make ``isEnabled()`` and ``isHandled()`` return ``true``.
1. Make ``execute()`` instantiate and open your dialog (or perform whatever other action you have in mind):
    ```java
    public class FooHandler implements IHandler 
    {
        @Override
        public void addHandlerListener(IHandlerListener handlerListener) {
        }

        @Override
        public void dispose() {
        }

        @Override
        public Object execute(ExecutionEvent event) throws ExecutionException {
            Shell shell = PlatformUI.getWorkbench().getActiveWorkbenchWindow().getShell();
            FooDialog dialog = new FooDialog(shell);
            dialog.open();
            return null;
        }

        @Override
        public boolean isEnabled() {
            return true;
        }

        @Override
        public boolean isHandled() {
            return true;
        }

        @Override
        public void removeHandlerListener(IHandlerListener handlerListener) {
        }
    }
    ```    
1. Open the plugins ``plugin.xml`` and navigate to the Extensions tab.

  * Add the extension ``org.eclipse.ui.commands``.
  * To this, add a new ``command``. Set the ``id``, give it a ``name``, and set the ``defaultHandler`` to the ``FooHandler`` class that you made earlier.
  * Add the extension ``org.eclipse.ui.menus``.
  * To this, add a new ``menuContribution``; set the ``locationURI`` to ``menu:org.eclipse.ui.main.menu``.
  * To this, add a new ``menu``. Give it an ``id`` and ``label`` (this will be displayed on the menu bar).
  * To the ``menu``, add a new ``command``. Set the ``commandId`` to be the ``id of the ``command`` you created earlier and give it a label that will be displayed in the menu on the UI;
  
The ``plugin.xml`` should now resemble:
```xml  
<?xml version="1.0" encoding="UTF-8"?>
<?eclipse version="3.4"?>
<plugin>
   <extension point="org.eclipse.ui.menus">
      <menuContribution
            allPopups="false"
            locationURI="menu:org.eclipse.ui.main.menu">
         <menu label="Foo Menu">
            <command
                  commandId="org.csstudio.isis.foo.command"
                  label="Foo Menu Item"
                  style="push">
            </command>
         </menu>
      </menuContribution>
   </extension>
   <extension point="org.eclipse.ui.commands">
      <command
            defaultHandler="org.csstudio.isis.foo.FooHandler"
            id="org.csstudio.isis.foo.command"
            name="Do Foo">
      </command>
   </extension>
</plugin>
```
The menu should now be visible in the client UI. For more details see the [Vogella menus tutorial](http://www.vogella.com/tutorials/EclipseCommands/article.html).

## Add A Third Party Library To A Plugin

To do