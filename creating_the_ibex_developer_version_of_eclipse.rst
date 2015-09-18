==============================================
Creating the IBEX Developer Version of Eclipse
==============================================

This describes how to make a new version of the IBEX developer's version of Eclipse. If adding new plugins starting from the old version should be sufficent, but if upgrading the Eclipse version re-creating these steps may be easier.

Note this version of Eclipse can be found at \\\\isis\\inst$\\Kits$\\??? .

Steps to take
-------------

#. Download the latest version of Eclipse for RCP and RAP developers from https://www.eclipse.org/downloads/, unzip somewhere appropriate and start Eclipse
#. Set the workspace to ../workspace (or anothe suitable relative path)
#. Modify eclipse/plugins/org.eclipse.platform_4.5.0.v20150603-2000/splash.bmp to make clear this is the IBEX version of Eclipse
#. From Help -> Eclipse Marketplace install EclEmma
#. From Help -> Install New Software add a repository with the name ObjectAid UML Explorer and URL http://www.objectaid.net/update, then install ObjectAid Class Diagram only (uncheck the other 3 options)
#. From Help -> Eclipse Marketplace install Eclipse Checkstyle Plug-in
#. Configure Checkstyle, Window -> Preferences -> Checkstyle, select New, Internal Configuration then import the IBEX Checkstyle file (found in the root of the git repository for the UI) NOTE - This is why we can't use EPF exports, the Checkstyle configurations get lost
#. From Window -> Preferences -> Java -> Editor -> Save Actions choose Perform the selection actions on save, then Format source code (Format edited lines), Organize imports, Additional actions
#. From the previous settings click through to the Formatter page, and configure preferred formatting settings. Changes from Java Conventions are Tab policy -> Spaces only, Tab size -> 4, Statements within 'case' body
#. In Window -> Preferences -> Java -> Compiler -> Errors/Warning -> Annotations -> Unhandled Token in '@SupressWarnings' set to ignore
#. From Window -> Preferences -> Java -> Code Style -> Code -> New Java files Edit the pattern to add the license header
#. Tidy up - check for paths tied to your own user account and either remove the offending line or delete the file
#. Zip up both the workspace and the eclipse folder, to get all plugins and settings
