# Java

## Instrument

The deploy scripts will check the locally installed Java version and upgrade it as needed.

{#developer_upgrade_java}
## Developer

1. To build CS-Studio, Phoebus or versions of the IBEX GUI which include Phoebus components from source, you will need JavaFX binaries. These can be patched onto the AdoptOpenJDK/Eclipse Temurin installation. Download the Windows SDK from `\\isis\inst$\Kits$\CompGroup\ICP\Java_utils\openjfx-19_windows-x64_bin-sdk\javafx-sdk-19` (originally from [gluon](https://gluonhq.com/products/javafx/)) and copy the `bin`, `lib`, and `legal` directories over the corresponding directories in your java installation. Note that the JavaFX version does not necessarily need to match your java installation, as long as the versions are compatible. For example we can use JavaFX 19 on a Java 11 installation. Please check that the license is still appropriate before you install.
1. If you will be debugging lots of java applications you may wish to install the java Visual VM. This used to be bundled with oracle java but is no longer present in OpenJDK. You can download a GPL-licensed version of the visual VM from https://visualvm.github.io/

The binaries listed above are also copied in `\\isis\inst$\Kits$\CompGroup\ICP\Java_utils`.
