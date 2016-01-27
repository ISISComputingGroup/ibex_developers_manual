==============================================
Creating the IBEX Developer Version of Eclipse
==============================================

This describes how to make a new version of the IBEX developer's version of Eclipse. If adding new plugins starting from the old version should be sufficent, but if upgrading the Eclipse version re-creating these steps may be easier.

Note this version of Eclipse can be found at \\isis\inst$\Kits$\CompGroup\ICP\Developer Tools .

Download and install plugins
----------------------------

#. Download the latest version of Eclipse for RCP and RAP developers from https://www.eclipse.org/downloads/, unzip somewhere appropriate and start Eclipse
#. Set the workspace to ../workspace (or anothe suitable relative path)
#. Modify eclipse/plugins/org.eclipse.platform_4.5.0.v20150603-2000/splash.bmp (replacing 4.5.0... with the current version number) to make clear this is the IBEX version of Eclipse
#. From Help -> Eclipse Marketplace install EclEmma
#. From Help -> Install New Software add a repository with the name ObjectAid UML Explorer and URL http://www.objectaid.net/update, then install ObjectAid Class Diagram only (uncheck the other 3 options)
#. From Help -> Eclipse Marketplace install Eclipse Checkstyle Plug-in
#. Configure Checkstyle, Window -> Preferences -> Checkstyle, select New, Internal Configuration then import the IBEX Checkstyle file (found in the root of the git repository for the UI) NOTE - This is why we can't use EPF exports, the Checkstyle configurations get lost
#. From Help -> Eclipse Marketplace install Unnecessary Code Detector
#. Configure Unnecessary Code Detector, Window -> Preferences -> UCDetector, change the 'Active mode' to 'Unused only [built-in]'
#. Run an update from Help -> Check for Updates

Save actions
------------

#. From Window -> Preferences -> Java -> Editor -> Save Actions choose Perform the selection actions on save, then Format source code (Format edited lines), Organize imports, Additional actions
#. In Window -> Preferences -> Java -> Compiler -> Errors/Warning -> Annotations -> Unhandled Token in ``@SupressWarnings`` set to ignore
#. From Window -> Preferences -> Java -> Organize Imports set the 'Number of static imports' to 2

Formatting
----------

From Window -> Preferences -> Java -> Code Style -> Formatter

Click 'New', start with 'Java Conventions' and save the formatting as 'IBEX'. Then edit this profile.

#. Under 'Indentation' Tab policy -> Spaces only, Tab size -> 4
#. Under 'Indentation' check Statements within 'case' body
#. Under 'Comments' uncheck 'Format line comments on first column'
#. Under 'Comments'' check 'Enable header comment formatting'
#. Under 'Line Wrapping' select 'enum declaration'. For 'Constants and ''implements' clause' set the line wrapping to 'Wrap all elements, every element on new line' and check the 'Force split' box
#. Under 'Line Wrapping' select 'enum declaration'. For 'Constant arguments' set the line wrapping to 'Wrap where necessary' and leave 'Force split' unchecked

Code templates
--------------

In Window -> Preferences -> Java -> Code Style -> Code Templates

#. Check 'Automatically add comments for new methods and types'
#. Remove all ``@author`` tags
#. Change 'Overriding methods' to the same comment as 'Methods'
#. For 'New Java files' add the licence header
#. 'Method body' comment becomes ``// ${body_statement}``
#. 'Constructor body' comment becomes ``// ${body_statement}``
#. 'Catch block body' comment becomes ``// ${exception_var}.printStackTrace();``

Finally
-------

#. From Window -> Preferences -> Maven -> Errors/Warnings choose 'Ignore' for 'Plugin execution not covered by lifecycle configuration'
#. From Window -> Preferences -> General -> Error Reporting set 'Action' to 'Never Send'
#. Tidy up - check for paths tied to your own user account and either remove the offending line or delete the file
#. Zip up both the workspace and the eclipse folder, to get all plugins and settings

