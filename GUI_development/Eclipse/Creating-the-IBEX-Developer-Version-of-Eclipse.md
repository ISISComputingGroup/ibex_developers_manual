> [Wiki](Home) > [The GUI](The-GUI) > [Eclipse](GUI-Eclipse) > Creating the IBEX developer version of Eclipse

The recommended IBEX developer version of Eclipse can be found at `\\isis\inst$\Kits$\CompGroup\ICP\Developer Tools`.

# Old instructions (no longer in use)

We are no longer using these instructions as several plugins are no longer relevant to the project (for example, RCPTT) or do not support modern versions of java/eclipse (e.g. checkstyle).

The instructions are left here in case they are useful for a future "IBEX developer eclipse" with bundled plugins.

```
## Download and install plugins

* Download the latest version of Eclipse for RCP and RAP developers from https://www.eclipse.org/downloads/, unzip somewhere appropriate and start Eclipse
* Set the workspace to ../workspace (or another suitable relative path)
* Modify eclipse/plugins/org.eclipse.platform_4.5.0.v20150603-2000/splash.bmp (replacing 4.5.0... with the current version number) to make clear this is the IBEX version of Eclipse
* From Help -> Eclipse Marketplace install RCP Testing Tool
* From Help -> Eclipse Marketplace install EclEmma
* From Help -> Install New Software add a repository with the name ObjectAid UML Explorer and URL http://www.objectaid.com/update, then install ObjectAid Class Diagram only (uncheck the other 3 options)
* From Help -> Eclipse Marketplace install Eclipse Checkstyle Plug-in
* Configure Checkstyle, Window -> Preferences -> Checkstyle, select New, Internal Configuration then import the IBEX Checkstyle file (found in the root of base\uk.ac.stfc.isis.ibex.client.tycho.parent) NOTE - This is why we can't use EPF exports, the Checkstyle configurations get lost
* Be sure to call the new Checkstyle configuration "IBEX Checks".
* Set the IBEX checkstyle to be the default
* From Help -> Eclipse Marketplace install Unnecessary Code Detector
* Configure Unnecessary Code Detector, Window -> Preferences -> UCDetector, change the 'Active mode' to 'Unused only [built-in]'
* From Help -> Eclipse Marketplace install JAutodoc
* Configure JAutodoc, Window -> Preferences -> Java -> JAutodoc. Change the visibility to be public and package then add the standard IBEX header (copied from a pre-existing code) 
* Run an update from Help -> Check for Updates

Save actions
------------

* From Window -> Preferences -> Java -> Editor -> Save Actions choose Perform the selection actions on save, then Format source code (Format edited lines), Organize imports, Additional actions
* In Window -> Preferences -> Java -> Compiler -> Errors/Warning -> Annotations -> Unhandled Token in ``@SupressWarnings`` set to ignore
* From Window -> Preferences -> Java -> Code Style -> Organize Imports set the 'Number of static imports' to 2

Formatting
----------

There are a number of changes to the formatting. The easiest way to get the correct code formatting is to start with the most recent previous developer's edition, choose Window -> Preferences -> Java -> Code Style -> Formatter. IBEX should be active, choose to Edit then Export.

To recreate the formatter from scratch these are the known steps. Start by going to 'New', start with 'Java Conventions' and save the formatting as 'IBEX'. Then edit this profile.

* Under 'Indentation' Tab policy -> Spaces only, Tab size -> 4
* Under 'Indentation' check Statements within 'case' body
* Under 'Comments' uncheck 'Format line comments on first column'
* Under 'Comments'' check 'Enable header comment formatting'
* Under 'Comments'' uncheck 'New line after @param tags'
* Under 'Line Wrapping' select 'enum declaration'. For 'Constants and ''implements' clause' set the line wrapping to 'Wrap all elements, every element on new line' and check the 'Force split' box
* Under 'Line Wrapping' select 'enum declaration'. For 'Constant arguments' set the line wrapping to 'Wrap where necessary' and leave 'Force split' unchecked

Code templates
--------------

In Window -> Preferences -> Java -> Code Style -> Code Templates

* Check 'Automatically add comments for new methods and types'
* Remove all ``@author`` tags
* Change 'Overriding methods' to the same comment as 'Methods'
* For 'New Java files' add the licence header
* 'Method body' comment becomes ``// ${body_statement}``
* 'Constructor body' comment becomes ``// ${body_statement}``
* 'Catch block body' comment becomes ``// ${exception_var}.printStackTrace();``

Finally
-------

* From Window -> Preferences -> Maven -> Errors/Warnings choose 'Ignore' for 'Plugin execution not covered by lifecycle configuration'
* From Window -> Preferences -> General -> Error Reporting set 'Send mode' to 'Never send reports'
* Tidy up - check for paths tied to your own user account and either remove the offending line or delete the file
* Zip up both the workspace and the eclipse folder, to get all plugins and settings

```