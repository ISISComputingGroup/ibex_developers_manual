> [Wiki](Home) > [The GUI](The-GUI) > [Coding](GUI-Coding) > Adding a plugin or feature to Maven

There are essentially two steps: adding a POM file to the plug-in/feature and editing the parent POM to include the new file. A plug-in is one small part of IBEx, such as the blocks view, and a feature is a large collection of plug-ins, such as CSS.

## Create the plugin

* Right click in eclipse in the list of plugins

* Create a new plugin, naming it suitably

* Right click the new plugin, select 'Convert to Maven Project'

* Edit the 'tycho.parent' pom.xml file to include the new plugin.