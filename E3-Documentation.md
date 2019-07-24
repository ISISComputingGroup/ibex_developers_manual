> [Wiki](Home) > [The GUI](The-GUI) > [Information about Eclipse E3](E3-Documentation)

This page contains information about the IBEX GUI as it was under eclipse 3. This information should be kept in the relevant heading until such time that we have retired the Eclipse 3 GUI. Heading link back to current page so it can be compared to E4 if needed.

# [Getting Started](GUI-Getting-Started)

## Building the GUI

These are the steps needed to run the GUI via Eclipse:

1. Start Eclipse IDE and select the workspace and use "Browse" to create and select a new workspace folder (example name: ibex_workspace)
1. From the menu bar choose: File->Import->General->Existing Projects into Workspace. Choose "Select root directory" and browse to where the IBEX code was cloned to, Eclipse should automatically select everything so click "Finish" to add them to the project
1. Expand the target platform folder (labelled as ``uk.ac.stfc.isis.ibex.targetplatform``), double click on the target file and choose "Set as Target Platform". This may take some time as parts of CS-Studio and DAWN are downloaded. It may also be required to update the Locations in use should some packages appear to be missing.
1. To run the application from within Eclipse: open "ibex.product" from the ``uk.ac.stfc.isis.ibex.client.product`` folder, select "Launch an Eclipse application"

# [Coding](GUI-Coding)
* [Adding a perspective](Adding-a-Button-to-the-Perspective-Switcher)
# [Testing](GUI-Testing)
* [System/UI testing with RCPTT](System-Testing-with-RCPTT)
# [Eclipse](GUI-Eclipse)
* [Eclipse 3.X vs Java 8](Eclipse-3.X-vs-Java-8)

## Common Eclipse task: Add A New Perspective

The perspective switcher is the control at the left hand side of the screen on our Eclipse client and contains buttons such as "Beam Status", "DAE", Motor", etc. Clicking one of these buttons opens the specified perspective.

The following steps will allow you to add an existing UI plugin to the perspective switcher. You should have already developed a main view class for the plugin, e.g., a class that extends ``org.eclipse.ui.part.ViewPart``.

1. Add a new class to the plugin called ``FooPerspective`` or something similar, and have it extend ``org.csstudio.isis.ui.perspectives.BasePerspective``.
1. Override the 'ID' and 'name' methods from BasePerspective. ID should return a string ID for the class (e.g, the fully qualified class name), and 'name' should return the name to be displayed on the button.
1. Optionally, add an image file which will be the perspective switcher button's icon. Put this in an 'icons' folder in the plugin directory.
1. If you added an icon, Override the 'image' method from BasePerspective to return an ``Image``:
    ```java
    @Override
    public Image image() {
        return ResourceManager.getPluginImage("org.csstudio.isis.ui.foo", 
            "icons/foo.png");
    }
    ```
1. If you want the perspective to be invisible by default, unless selected in the preferences Override the isVisibleDefault method from BasePersoective to return false:
    ```java
    @Override
    public boolean isVisibleDefault() {
        return false; 
    }
    ```
1. In the plugin's, ``plugin.xml`` file, go to the extensions tab and add the following extensions:
    * ``org.eclipse.ui.views`` - add a new 'view' to this; point it at the ViewPart class.
    * ``org.eclipse.ui.perspectives`` - add a new 'perspective' to this; point it at the Perspective class.
    * ``org.eclipse.ui.perspectiveExtensions`` - add a new ``perspectiveExtension`` to this; set the ``targetId`` as that of the perspective extension above.
    * Add a new ``view`` to this ``perspectiveExtension``; set the relative to be ``org.csstudio.isis.ui.perspectives.PerspectiveSwitcher``.
    * ``org.csstudio.isis.ui.perspectives`` - add a new 'contribution to this; the class should be the plugin's ``Perspective`` class.
1. In the same ``plugin.xml`` file, go to the build tab and make sure "plugin.xml" is checked. If not, some aspects (e.g. the `preferenceInitializer`) may not work in the application once built.

Once you've added everything, the ``plugin.xml`` file should look like:
```xml
<plugin>
  <extension point="org.eclipse.ui.views">
    <view class="org.csstudio.isis.ui.log.FooView"
      id="org.csstudio.isis.ui.log.FooView"
      name="Foo"
      restorable="true">
    </view>
  </extension>

  <extension point="org.eclipse.ui.perspectives">
    <perspective class="org.csstudio.isis.ui.log.FooPerspective"
        id="org.csstudio.isis.ui.log.FooPerspective"
        name="Foo">
    </perspective>
  </extension>

  <extension point="org.eclipse.ui.perspectiveExtensions">
    <perspectiveExtension targetID="org.csstudio.isis.ui.log.FooPerspective">
      <view closeable="false"
          id="org.csstudio.isis.ui.foo.FooView"
          minimized="false"
          ratio="0.1f"
          relationship="right"
          relative="org.csstudio.isis.ui.perspectives.PerspectiveSwitcher"
          showTitle="false"
          visible="true">
      </view>
    </perspectiveExtension>
  </extension>

  <extension point="org.csstudio.isis.ui.perspectives">
    <contribution class="org.csstudio.isis.ui.foo.FooPerspective">
    </contribution>
  </extension>
</plugin>
```
If you have followed the above steps and correctly extended all the extension points, a button for your plugin will be automatically added to the perspective switcher.

# [Control System Studio (CS-Studio)](GUI-CSS)
# [GUI Chats](GUI-Chats)
# [Other](GUI-Other)
