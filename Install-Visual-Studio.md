Install a version of visual studio. 2010 is used by most developers unless you are on windows 10 in which case install 2017.

# Install Visual Studio 2010
Install Visual Studio 2010

Install SDK 7.1 
-The SDK may fail if you have these installed: 
* Microsoft Visual C++ 2010 x86 Redistributable
* Microsoft Visual C++ 2010 x64 Redistributable

If these do exist on your computer you need to uninstall them before installing the SDK.

Install: 
* [Visual Studio 2010 SP1](https://my.visualstudio.com/Downloads?q=visual%20studio%202010&pgroup=)
* Visual C++ 2010 SP1 Compiler Update for the Windows SDK 7.1

Note: The free version of Visual Studio 2010, Visual Studio 2010 Express, isn't supported by the EPICS build process.

# Install Visual Studio 2013
Windows SDK 7 has compatibility issues with newer versions of Windows. In this case, Visual Studio 2013 may be used instead.

During the installation of VS2013, under "Optional Features" make sure to include Microsoft Foundation Classes for C++.

Additionally, download and install the [Multibyte MFC Library](https://www.microsoft.com/en-us/download/details.aspx?id=40770).

# Install Visual Studio 2017

Download installer (Visual Studio **Community** 2017 exe) from installer page https://my.visualstudio.com using your stfc email address.
During install, choose Desktop development with C++ and from the right checkboxes: 
* The most recent Windows 10 SDK, Windows 8.1 SDK, and MFC and ATL support
* Windows Universal CRT SDK
If these boxes aren't visible on the right it is most likely because you are trying to install professional rather than community.
# Installing a new Version of Visual Studio

If you are on a new version of visual studio (2019?) then you will need to upgrade various files to take this into account. Below is a list of things we needed to do when upgrading to 2017 your list may be different.

## Setup the environment

The visual studio compiler environment variables are set up from `...\EPICS\base\master\startup\win32.bat` this calls into the visual studio variable set up. Add your version to this.

## Converting Tabs to Spaces

To convert tabs to spaces inside of Visual Studio go to

`Tools->Options->Text Editor->All Languages->Tabs`

Change Tab to use "Insert Spaces" instead of "Keep Tabs".

Note you can also specify this per language if you wish to have different behaviour in a specific language.