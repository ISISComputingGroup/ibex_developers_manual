# MDT (Microsoft deployment toolkit)

This page assumes you already have access to a machine with MDT installed. If you don't have access to this type of machine, you can build a new one by following the instructions listed [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Building-a-windows-10-MDT-build-server)

MDT is a tool used by some other organisations - as such, there is some documentation about how to use the tool online. Rather than trying to describe the full capabilities of the tool, this page aims to document the ISIS-specific ways in which it is used.

### Overview of concepts

- **Deployment share** - this is a static location which must be read-accessible from the new machine to be built, and write-accessible from the MDT build server.
- **MDT Build server** - this is a machine with MDT installed on it, that has write access to the deployment share. This can be a virtual machine, even one built using MDT itself...
- **Deployment ISO** - this is a virtual disk (ISO image) which gets built by the MDT process. It contains a minimal (bootstrap) operating system, and points back to the deployment share to read instructions from it. It is the bootable media which starts off the creation of a new virtual machine.
  * Note that it is not a standard windows 10 iso (like you might get directly from microsoft), as it has to contain instructions to point to the ISIS MDT deployment share location.

The basic process of an MDT update and deployment is:
- Make changes to the MDT configuration on the MDT build server.
- Update the deployment share so that the share contains the latest instructions for building a system
- Copy the deployment ISO to the machine that you want to deploy to
- Boot the brand-new machine using this deployment ISO, this will boot into a minimal MDT deployment environment (note that at this stage windows is not deployed yet!)
- The installation process will start by asking a few basic questions (e.g. hostname of new computer, admin password)
- Once the basic questions are complete, the MDT process will proceed to install the operating system and any specified applications
- Once the above process is complete (which may take a while as it does a lot of installations), you should have a working installation of windows and all relevant applications. The MDT deployment process is now complete and you can remove the MDT deployment ISO and proceed to use/configure the machine as normal.

Once you are into the main MDT interface, a few of the options along the left side of the screen are typically interesting to us:

### Applications

The applications folder in MDT houses the definitions of various "applications" that can be installed. Fundamentally this works by calling normal windows installers under the hood, so any setup which can be performed unattended can be done by MDT.

By clicking on a folder name and then right-clicking on an application name and selecting "properties", you can see and modify the details of the application installation process. You can also add installers in these menus, which will be copied onto the MDT deployment share location.

This set of applications is not automatically installed however - this is just a list of applications that MDT knows how to install.

### Task sequences

The most interesting items here are under "ISIS Instrument Reference" -> "Re-clone system" -> "Build thick W10 image" as this is the full automated install. By right clicking this and selecting "properties" and then "task sequence", it will bring up a menu containing an ordered list of the installation tasks. These can include installing the applications defined above, and various other items such as applying OS updates, arbitrary sleeps etc.

### Update deployment share

When you are done making some changes, you should update the ISO image on the deployment share. This is done by right-clicking on the deployment share location in the left-hand pane of MDT and selecting "update deployment share". This will build and deploy a new ISO image containing the new deployment instructions.

## Building clones via MDT

```{toctree}
:glob:
:titlesonly:

mdt/*
```
