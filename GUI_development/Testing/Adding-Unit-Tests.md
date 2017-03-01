> [Wiki](Home) > [The GUI](The-GUI) > [Testing](GUI-Testing) > Adding tests

For more detailed information see an_introduction_to_unit_testing.rst

It is relatively simple to add unit tests for a plug-in in such a way that maven can run them as part of the build.

Here are the steps required in Eclipse:

* Create a new Fragment Project
    * File > New > Project... > Plug-in Development > Fragment Project
    * Set the project name to \<the full name of the plug-in to test\>.tests
    * Change the location to the repository rather than the workspace: xxx\ibex_gui\base\\\<project_name> (don't forget the project name!!)
    * Click "Next"
    * Make sure the Execution Environment points at the correct version of Java (currently JavaSE-1.8)
    * Click the "Browse" button next to "Plug-in ID" 
    * Select the plug-in to test and click "OK"
    * Finish
    
* In the newly created plug-in, add a new Package with the same name as the plug-in or something equally sensible.
    * Select the plug-in
    * File > New > Package
    * Enter the name and click "Finish"
    
* In the new Package create a class for adding test
    * Select the Package
    * File > New > Class
    * The class name **must** end in Test to be picked up by the automated build
    
* Add tests to the class
    * Add org.junit and org.mockito (if required) to the 'Required Plug-ins', under the Dependencies tab for the manifest

* Convert the new plug-in to a Maven project
    * Right-click on the plug-in and select Configure > Convert to Maven Project
    * Click "Finish"
    
* Add the new plug-in to the Parent POM
    * Select the pom.xml file in uk.ac.stfc.isis.ibex.client.tycho.parent
    * On the overview tab click "Add..." under the Modules section
    * Select the new plug-in from the list
    * Enable the "Update POM parent section in selected projects" option and click "OK"
    * Save it
    
* Edit the plug-in pom.xml file
    * Select the pom.xml file
    * Open the pom.xml tab
    * Change the packaging to eclipse-test-plugin
    * Remove the build section
    * Remove the groupID and version entries outside of parent
    * Save it
    
* Running the Maven build should now also run the tests

## Example POM

An example test plug-in POM:

```
    <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
      <modelVersion>4.0.0</modelVersion>
      <artifactId>tychodemo.bundle.tests</artifactId>
      <packaging>eclipse-test-plugin</packaging>
      <parent>
            <groupId>tychodemo</groupId>
            <artifactId>parent</artifactId>
            <version>1.0.0-SNAPSHOT</version>
            <relativePath>../tychodemo.parent</relativePath>
      </parent>
    </project>
```

