# Adding a plugin or feature

The steps for adding a plug-in (one small part of IBEX, such as the blocks view) or feature (a larger collection of
plug-ins, such as CSS) to IBEX are:

* Add the plug-in to `feature.base`:
    * Open `feature.xml` in `uk.ac.stfc.isis.ibex.feature.base`
    * Go to "Included Plug-ins" (or "Included Features") tab and click "Add..."
    * Find your new plug-in in the list and add it
* Add the plug-in to `ibex.product`
    * Open `ibex.product` in `uk.ac.stfc.isis.ibex.e4.client.product`
    * Go to "Configuration" tab and click "Add..." next the "Start Levels" section
    * Find your new plug-in in the list and add it
* Convert the plug-in to a Maven project.
    * Right-click on the plug-in and select Configure > Convert to Maven Project
    * Click "Finish". This should create a `pom.xml` inside the project.
* Add the new plug-in to the Parent POM
    * Select the `pom.xml` file in `uk.ac.stfc.isis.ibex.client.tycho.parent`
    * On the overview tab click "Add..." under the Modules section
    * Select the new plug-in from the list
    * Enable the "Update POM parent section in selected projects" option and click "OK"
    * Save it
* Edit the plug-in `pom.xml` file
    * Select the pom.xml file
    * Open the pom.xml tab
    * Change/add the packaging to `eclipse-plugin` (or `eclipse-test-plugin` if it's a unit test plugin)
    * Remove the build section
    * Remove the `groupID` and version entries outside of parent
    * Verify that the resulting plug-in POM looks like an existing `pom.xml` for a similar plugin
