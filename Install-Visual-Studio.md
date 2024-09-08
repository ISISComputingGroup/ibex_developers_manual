Most developers should install VS2022 - we have 2010 on a build server for building the old galil driver (until we remove it), if you need to install 2010 locally then install it before you install 2022

# Instructions for Visual Studio 2010 (not needed in most cases)

Install SDK 7.1 
-The SDK may fail if you have these installed: 
* Microsoft Visual C++ 2010 x86 Redistributable
* Microsoft Visual C++ 2010 x64 Redistributable

If these do exist on your computer you need to uninstall them before installing the SDK.

Install: 
* [Visual Studio 2010 SP1](https://my.visualstudio.com/Downloads?q=visual%20studio%202010&pgroup=)
* Visual C++ 2010 SP1 Compiler Update for the Windows SDK 7.1

Note: The free version of Visual Studio 2010, Visual Studio 2010 Express, isn't supported by the EPICS build process.

# Instructions for Visual Studio 2022
Download installer (Visual Studio **Community** 2022 exe) from installer page https://my.visualstudio.com using your stfc email address.
During install, select "Desktop development with C++" and check/enable these individual features if they are not already: 
- The most recent Windows 11 SDK
- C++ MFC support
- C++ ATL support

Also select ".NET desktop development" (needed for mk3chooepr and astrium chopper):
- make sure .NET 4.7.2 development is included as one of the options   

# Instructions for Visual Studio 2019 (old)
Download installer (Visual Studio **Community** 2019 exe) from installer page https://my.visualstudio.com using your stfc email address.
During install, select "Desktop development with C++" and check/enable these individual features: 
- The most recent Windows 10 SDK
- C++ MFC support
- C++ ATL support

Also select .NET development and "Universal windows CRT/universal platform development" from the features  

# Installing a new Version of Visual Studio
If you are on a newer version of Visual Studio then you will need to upgrade various files to take this into account. Below is a list of things we needed to do when upgrading to 2017 your list may be different.

See https://github.com/ISISComputingGroup/IBEX/issues/5173 for the changes that were necessary to add support for Visual Studio 2019.

## Setup the environment (Only if you are going for a later version)

The visual studio compiler environment variables are set up from `...\EPICS\base\master\startup\windows.bat` this calls into the visual studio variable set up. Add your version to this.

# Converting Tabs to Spaces

To convert tabs to spaces inside of Visual Studio go to

`Tools->Options->Text Editor->All Languages->Tabs`

Change Tab to use "Insert Spaces" instead of "Keep Tabs".

Note you can also specify this per language if you wish to have different behaviour in a specific language.