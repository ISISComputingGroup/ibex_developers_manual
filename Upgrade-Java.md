> [Wiki](Home) > [Deployment](Deployment) > Upgrade java

## When Java needs to be updated on the instrument:

1. Before you start, ensure you understand [Java's licensing](Understanding-Java-Licensing).
1. Determine which new version of Java should be installed.
1. If oracle java is on the system uninstall it
1. Copy the latest version of the openJDK installer from the public share at
 `...\ISIS_Experimental_Controls_Public\third_party_installers\latest_versions\OpenJDK...`
   - Do not use a copy downloaded from the internet as it may not have been tested with IBEX
1. Run the installer and install all components. The install menu should look like this:
![](https://raw.githubusercontent.com/ISISComputingGroup/ibex_developers_manual/master/images/openjdk_install_prompt.PNG)
1. Make sure you run the instrument, either now or before you finish
   - Answer any firewall questions "yes, allow through the firewall".

## Additional optional steps for developer installations (not required on instruments):

1. To build CS-Studio from source, you will need JavaFX binaries. These can be patched onto the AdoptOpenJDK installation. Download the latest binaries from https://github.com/SkyLandTW/OpenJFX-binary-windows/releases and follow the instructions on that page to patch your JDK. Please check that the license is still appropriate before you install.
1. If you will be debugging lots of java applications you may wish to install the java Visual VM. This used to be bundled with oracle java, but is no longer present in OpenJDK. You can download a GPL-licensed version of the visual VM from https://visualvm.github.io/

The binaries listed above are also copied in `\\isis\inst$\Kits$\CompGroup\ICP\Java_utils`.
