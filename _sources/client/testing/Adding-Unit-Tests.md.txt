# Adding tests

:::{seealso}
- [Introduction to unit testing](An-Introduction-to-Unit-Testing)
:::

The steps required to add unit tests for a plugin are:

* Create a new Fragment Project
    * File > New > Project... > Plug-in Development > Fragment Project
    * Set the project name to `<the full name of the plug-in to test\>.tests`
    * Change the location to the repository rather than the workspace: `ibex_gui\base\<project_name>` (don't 
forget the project name!)
    * Click "Next"
    * Make sure the Execution Environment points at the correct version of Java
    * Click the "Browse" button next to "Plug-in ID" 
    * Select the plug-in to test and click "OK"
    * Finish
    
* In the newly created plug-in, add a new Package with the same name or structure as the plug-in.
    * Select the plug-in
    * File > New > Package
    * Enter the name and click "Finish"
    
* In the new Package create a class for adding test
    * Select the Package
    * File > New > Class
    * The class name **must** end with `Test` to be picked up by the automated build
    
* Add tests to the class
    * Add `org.junit` and `org.mockito` (if required) to the 'Required Plug-ins', under the Dependencies tab for the
manifest (`MANIFEST.MF`)

* Add the test plug-in to the Maven build by [following these steps](../coding/Adding-a-Plugin-or-Feature-to-Maven-Build)
    
* Running the Maven build should now also run the tests

