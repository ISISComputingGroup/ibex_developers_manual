# Adding tests

For more detailed information see [an_introduction_to_unit_testing.rst](An-Introduction-to-Unit-Testing).

It is relatively simple to add unit tests for a plug-in in such a way that maven can run them as part of the build.

Here are the steps required in Eclipse:

* Create a new Fragment Project
    * File > New > Project... > Plug-in Development > Fragment Project
    * Set the project name to \<the full name of the plug-in to test\>.tests
    * Change the location to the repository rather than the workspace: xxx\ibex_gui\base\\\<project_name> (don't forget the project name!!)
    * Click "Next"
    * Make sure the Execution Environment points at the correct version of Java (currently JavaSE-11)
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

* Add the test plug-in to the Maven build by [following these steps](../coding/Adding-a-Plugin-or-Feature-to-Maven-Build)
    
* Running the Maven build should now also run the tests

