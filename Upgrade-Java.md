> [Wiki](Home) > [Deployment](Deployment) > Upgrade java

## When Java needs to be updated on the instrument:

(Please note if you are following this link from here https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/First-time-installing-and-building-(Windows) then you do not need to worry about this section. )
1. Before you start, ensure you understand [Java's licensing](Understanding-Java-Licensing).
1. Determine which new version of Java should be installed.
1. If oracle java, or any previous java version, is on the system uninstall it
1. **If on IBEX V11 or previous, Copy Java 11 from** `...\ISIS_Experiment_Controls_Public\third_party_installers\old_versions` otherwise copy the latest version of the openJDK installer from the public share at
 `...\ISIS_Experiment_Controls_Public\third_party_installers\latest_versions\OpenJDK...`
   - Do not use a copy downloaded from the internet as it may not have been tested with IBEX
1. Run the installer and install all components. The install menu should look like this:

![open_jdk_install_prompt](https://user-images.githubusercontent.com/55101160/96607156-fa414f80-12ef-11eb-8b07-60d709bf643c.PNG)
1. Make sure you run the instrument, either now or before you finish
   - Answer any firewall questions "yes, allow through the firewall".

## Additional optional steps for developer installations (not required on instruments):

1. To build CS-Studio from source, you will need JavaFX binaries. These can be patched onto the AdoptOpenJDK installation. Download the latest **long term support** binaries from https://openjfx.io/ and unzip openjfx-11.XXX.zip and copy over the bin, legal and lib directory to your java (C:\Program Files\AdoptOpenJDK\jdk-11.0.8.10-hotspot). Please check that the license is still appropriate before you install.

1. If you will be debugging lots of java applications you may wish to install the java Visual VM. This used to be bundled with oracle java but is no longer present in OpenJDK. You can download a GPL-licensed version of the visual VM from https://visualvm.github.io/

The binaries listed above are also copied in \\isis\inst$\Kits$\CompGroup\ICP\Java_utils.

