> [Wiki](Home) > [The GUI](The-GUI) > [Coding](GUI-Coding) > Adding a plugin or feature to Maven

There are essentially two steps to adding a plug-in (one small part of IBEX, such as the blocks view) or feature (a larger collection of plug-ins, such as CSS) to the maven build: Adding a POM file to the plugin/feature, and editing the parent POM (in `uk.ac.stfc.isis.ibex.client.tycho.parent`) to include the new file.

# Step by step:

* Convert the plug-in to a Maven project.
    * Right-click on the plug-in and select Configure > Convert to Maven Project
    * Click "Finish". This should create a `pom.xml` inside the project.
    
* Add the new plug-in to the Parent POM
    * Select the `pom.xml` file in `uk.ac.stfc.isis.ibex.client.tycho.parent`
    * On the overview tab click "Add..." under the Modules section
    * Select the new plug-in from the list
    * Enable the "Update POM parent section in selected projects" option and click "OK"
    * Save it
    
* Edit the plug-in pom.xml file
    * Select the pom.xml file
    * Open the pom.xml tab
    * Change/add the packaging to `eclipse-plugin` (or `eclipse-test-plugin` if it's a unit test plugin)
    * Remove the build section
    * Remove the groupID and version entries outside of parent
    * Save it

## Example POM

An example of what the plug-in POM should look like:

```
    <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
      <modelVersion>4.0.0</modelVersion>
      <artifactId>tychodemo.bundle.tests</artifactId>
      <packaging>eclipse-plugin</packaging>
      <parent>
            <groupId>tychodemo</groupId>
            <artifactId>parent</artifactId>
            <version>1.0.0-SNAPSHOT</version>
            <relativePath>../tychodemo.parent</relativePath>
      </parent>
    </project>
```
