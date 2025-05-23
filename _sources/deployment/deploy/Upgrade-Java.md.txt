# Java

## Instrument

```{note}
If you are following this link from the first-time installation guide, then you do not need to worry about this section.
```

1. Before you start, ensure you understand [Java's licensing](/processes/dev_processes/Understanding-Java-Licensing).
1. If any previous java version is installed on the system, uninstall it. Note that previous java versions may be under "Oracle", "AdoptOpenJDK", or "Eclipse Temurin JDK".
1. Install an appropriate version of java:
   - For developer installs, use the latest java in `...\ISIS_Experiment_Controls_Public\third_party_installers\latest_versions\OpenJDK...`
   - For IBEX version v11 and before, use JDK 11 in `...\ISIS_Experiment_Controls_Public\third_party_installers\old_versions`
   - For IBEX version v12 onwards, use JDK 17 in `...\ISIS_Experiment_Controls_Public\third_party_installers\latest_versions\OpenJDK...`
   - Do not use a copy downloaded from the internet as it may not have been tested with IBEX
1. Run the installer and install all components. The install menu should look like this:

![open_jdk_install_prompt](open_jdk_install_prompt.PNG)
1. Make sure you run the instrument, either now or before you finish
   - Answer any firewall questions "yes, allow through the firewall".

{#developer_upgrade_java}
## Developer

1. To build CS-Studio, Phoebus or versions of the IBEX GUI which include Phoebus components from source, you will need JavaFX binaries. These can be patched onto the AdoptOpenJDK/Eclipse Temurin installation. Download the Windows SDK from `\\isis\inst$\Kits$\CompGroup\ICP\Java_utils\openjfx-19_windows-x64_bin-sdk\javafx-sdk-19` (originally from [gluon](https://gluonhq.com/products/javafx/)) and copy the `bin`, `lib`, and `legal` directories over the corresponding directories in your java installation. Note that the JavaFX version does not necessarily need to match your java installation, as long as the versions are compatible. For example we can use JavaFX 19 on a Java 11 installation. Please check that the license is still appropriate before you install.
1. If you will be debugging lots of java applications you may wish to install the java Visual VM. This used to be bundled with oracle java but is no longer present in OpenJDK. You can download a GPL-licensed version of the visual VM from https://visualvm.github.io/

The binaries listed above are also copied in `\\isis\inst$\Kits$\CompGroup\ICP\Java_utils`.
