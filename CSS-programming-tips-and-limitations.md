> [Wiki](Home) > [The GUI](The-GUI) > [CS Studio](GUI-CSS) > Programming tips and limitations

These are a few things I have discovered while creating the table of motors and synoptic view.

# Opening a new Opi
CSS can display one or more windows, each of which can be divided into multiple views, each of
which can contain multiple tabs, so there is huge flexibility but CSS has its own ideas about
how to do things, which introduce some annoying limitations.

CSS allows you to open a new opi in many locations:
* In place of the current Opi
* In a new window
* As a new tab in the current view
* As a new tab in the top, bottom, left or right views of the current window

What it does not allow you to do is to replace the contents of another view.
Therefore you cannot have a window with navigation controls in the top view 
that change the opi shown
in the main view. They can only create new tabs in the main view

Alternatively the opi can be shown in a linking container

## Linking Containers

The contents of the linking container can be changed dynamically by setting the 'opi_file' property.

The macros seen by the contents of the container can be set by:

```
from org.csstudio.opibuilder.scriptUtil import DataUtil
...
macros = DataUtil.createMacrosInput(True)
macros.put('NAME', 'VALUE')
container.setPropertyValue('macros', macros)
```

but the new macros only take effect when a new opi is loaded. If the new opi has the same name as the previous one, nothing is loaded and the new macros do not take effect. To force a reload, set 'opi_file' to the empty string then back to its old value.

When an opi is displayed in a linking container, scripts on the opi display widget do not get run because the display widget is not loaded. The contents of the display widget instead become children of the linking container. If you want a script to run in these circumstances it has to hang off one of the child widgets.

# The CSS object model as viewed from Python
This is largely undocumented. The help in CSS/BOY says little and Google can find little.
The only way I was able to find out how to manipulate the actions on a button was to view the java source on ][GitHub](https://github.com/ControlSystemStudio/cs-studio/tree/master/applications/plugins). The Python objects simply expose the public Java methods.

# Changing actions
The list of actions on a button is:

```
actionList = myButton.getPropertyValue('actions').getActionsList()
```

This is a Java list which can be subscripted and has methods like add() and clear().

If you have an existing action, new write PV actions can be created:

```
action = sourceList[0].__class__()
action.setPropertyValue('pv_name', 'loc://myPV')
action.setPropertyValue('value', valueToSet)
action.setPropertyValue('description', 'What appears in the menu')
actionList.add(action)
```

For some reason new open opi action created in this way do not work, but existing open opi actions can be altered and added to a different button:

```
action.setPropertyValue('replace', 1)
action.setPropertyValue('description', 'What appears in the menu')
action.setPropertyValue('path', 'my.opi')
actionList.add(action)
```

In the synoptic view I have a hidden button with actions than can be reused.

# Running a script on page load
There is no way to specify that a script run when an opi is loaded. Instead scripts can only be triggered from PV changes. It is however possible to use a local PV to get the effect. Each page needs to have a script triggered from loc://where, which contains the following:

```
where = display.getPropertyValue('name')
if PVUtil.getString(pvs[0])!=where:
	pvs[0].setValue(where)
```

So long as each opi has a different name, every time a new opi is loaded, the value will be different and so the script will run. 

NB The if test is required. The script must only change the name if it needs changing, otherwise the script runs endlessly, potentially bringing down CSS.

# Creating new widgets

Given an existing widget of the correct type, new widgets can be created and added to a container. 

The following will create a new widget of the same type as Label0 and set some of its properties:

```
label = group.getWidget('Label0')
source = label.getModel()
model = source.__class__()
model.setName('NewLabel')
model.setX(6)
model.setY(142)
model.setWidth(163)
group.addChild(model)
```

The model has set and get methods for the widget properties, or `group.getWidget('NewLabel')` can be used to obtain the widget so its properties can be set using `setPropertyValue()`.

The widget can be removed using `group.removeChildByName('NewLabel')`

Note that for dynamically create widgets that do not normally have click actions (e.g. the grouping containers that I use to fake transparent buttons), it seems to be impossible to hook an action to a left click but it is possible to add them to the right click menu.

# Utilities

Seven utility classes are provided, but there seems to be no way to get to some of them in the online help other than to know their names and search for them:

* ConsoleUtil has methods for writing debug messages to the console.
* DataUtil has the createMacrosInput method.
* FileUtil has methods for reading and writing files and displaying an open file dialog. There is also a saveFileDialog method that has been omitted from the online help.
* GUIUtil has a yes/no dialog and methods for going to full screen or compact mode
* PVUtil
* !ScriptUtil
* !WidgetUtil