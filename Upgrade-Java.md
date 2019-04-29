> [Wiki](Home) > [Deployment](Deployment) > Upgrade java

When Java needs to be updated on the instrument:

1. Before you start, ensure you understand [Java's licensing](Understanding-Java-Licensing).
1. Determine which new version of Java should be installed.
1. If oracle java is on the system uninstall it
1. Copy the latest version of the openJDK installer from the public share at
 `...\ISIS_Experimental_Controls_Public\third_party_installers\latest_versions\OpenJDK...`
   - Do not use a copy downloaded from the internet as it may not have been tested with IBEX
1. Run the installer and install all components. The install menu should look like this:
![](https://raw.githubusercontent.com/ISISComputingGroup/ibex_developers_manual/master/images/openjdk_install_prompt.PNG)
1. Make sure you run the instrument, either now or before you finish, so that any firewall question can be resolved as yes allow through the firewall.
