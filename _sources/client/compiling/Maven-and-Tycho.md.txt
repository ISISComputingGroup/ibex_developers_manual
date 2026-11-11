# Maven and Tycho

The IBEX GUI is built using Tycho, which is a Maven plugin used for building Eclipse RCP products.

This document provides a brief overview of both Maven and Tycho.

:::{seealso}
[Code chats](/processes/meetings/Code-Chats-and-Lightning-Talks) have been given on this topic (
[slides](https://stfc365.sharepoint.com/:p:/r/sites/ISISExperimentControls/ICP%20Discussions/GUI_Chat_Slides/IBEX%20GUI%20build%20system.pptx?d=w74aa3046025f4622bcdeadbdeca9395c&csf=1&web=1&e=aQEGJZ),
[recording](https://stfc365.sharepoint.com/sites/ISISExperimentControls/_layouts/15/stream.aspx?id=%2Fsites%2FISISExperimentControls%2FICP%20Discussions%2FGUI%5FChat%5FSlides%2FIBEX%20GUI%20build%20System%20Code%20chat%2Emp4&amp;referrer=StreamWebApp%2EWeb&amp;referrerScenario=AddressBarCopied%2Eview&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E0f53ae8b%2D3184%2D43c1%2D955e%2D039109fcd0e1)
).
:::

## Maven

The official description:

> _Apache Maven is a software project management and comprehension tool. Based on the concept of a project object model
> (POM), Maven can manage a project's build, reporting and documentation from a central piece of information._

In simple terms, Maven is a build automation tool used primarily for Java projects.

See the [getting started guide in the Maven documentation](https://maven.apache.org/guides/getting-started/index.html)
for more information about what Maven is.

### POM files

POM files are XML files, called `pom.xml`, that describes the software project being built, its dependencies on other
external modules and components, the build order, directories, and required plug-ins. In many ways, it can be considered
the equivalent of a C-style Makefile as it defines how the project is built.

See [the Maven documentation](https://maven.apache.org/pom.html) for detailed information on the various sections of a
`pom.xml` in a pure Maven project.

### Building a Maven project

Maven uses multiple build phases - for example, `compile`, `test`, `package`. If you are really unsure, a good
default is to run `mvn clean verify` to build a project; this will clean the project (deleting any old build files),
and then run compilation, unit tests, packaging, and verification (e.g. checkstyle) phases.

For more information, see the Maven
[build lifecycle documentation](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html).

## Tycho

Tycho is a set of Maven plugins and extensions for building Eclipse-based applications with Maven. Tycho allows Maven
to support building bundles, fragments, features, P2 repositories, RCP applications etc.

Tycho is used to build the IBEX GUI application.

### Parent POM

Maven allows a parent POM to be defined which contains references to the other POM files for the other projects that
make up an application. This is used in the IBEX GUI because it allows the centralisation of the settings for
building the application.

The [IBEX GUI parent `pom.xml`](https://github.com/ISISComputingGroup/ibex_gui/blob/master/base/uk.ac.stfc.isis.ibex.client.tycho.parent/pom.xml)
contains a lot of information, so here is a stripped down version to show the key points:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>CSS_ISIS</groupId>
    <artifactId>uk.ac.stfc.isis.ibex.client.tycho.parent</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <properties>
        <tycho.version>4.0.9</tycho.version>
        <tycho-repo.url>https://oss.sonatype.org/content/groups/public/</tycho-repo.url>
        <photon-repo.url>http://download.eclipse.org/releases/2024-09</photon-repo.url>
        <photon-updates-repo.url>http://download.eclipse.org/eclipse/updates/4.33</photon-updates-repo.url>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <repositories>
        <repository>
            <id>photon-updates</id>
            <layout>p2</layout>
            <url>${photon-updates-repo.url}</url>
        </repository>
    </repositories>

    <build>
        <plugins>
            <plugin>
                <groupId>org.eclipse.tycho</groupId>
                <artifactId>tycho-maven-plugin</artifactId>
                <version>${tycho.version}</version>
                <extensions>true</extensions>
            </plugin>
            <!-- Other maven plugins omitted such as unit testing and checkstyle -->
        </plugins>
    </build>

    <modules>
        <module>../uk.ac.stfc.isis.ibex.client.product</module>
        <module>../uk.ac.stfc.isis.ibex.feature.base</module>
        <!-- Other modules that make up IBEX would be listed here -->
        <module>../uk.ac.stfc.isis.ibex.ui.mainmenu.tests</module>
    </modules>
</project>
```

Let's explain the various parts shown:
* At the top we have the standard Maven metadata: `groupId`, `artifactId`, `version`.
* The properties section is used to define URLs for the Tycho plugin and the Eclipse RCP framework. The versions here
are updated periodically during [dependency updates](/processes/dev_processes/Dependency-Updates)
* The repositories section tells Maven to look for a repository for the Eclipse RCP framework version specified above
* The build section defines the Maven plugins necessary to build the application. The Tycho plugin entry tells Maven to
download Tycho and use it as part of the build process
* The modules section lists the locations of the POM files for the various modules that make up the application. When a
new module is added to IBEX, it will need to be added to this list.

### Child POM

A typical child POM look like
[this](https://github.com/ISISComputingGroup/ibex_gui/blob/master/base/uk.ac.stfc.isis.ibex.dashboard/pom.xml).
It is very simple - it points at the parent POM to get most of its information. These is one of these `pom.xml` files
for each module that makes up the IBEX client.

The packaging type is defined as `eclipse-plugin`; this is a packaging type defined by Tycho. Other Tycho types used in
IBEX are `eclipse-feature` for features, `eclipse-test-plugin` for fragment projects that define unit tests and
`eclipse-repository` for configuring builds.

### Application POM

In IBEX we define a separate project called `uk.ac.stfc.isis.ibex.e4.client.product` which defines how the product is 
built. It has a 
[POM file](https://github.com/ISISComputingGroup/ibex_gui/blob/master/base/uk.ac.stfc.isis.ibex.e4.client.product/pom.xml)
of packaging type `eclipse-repository`.

The key area is the `materialize-products` section, this tells Tycho to actually create the product. Without this Maven
will compile & unit test the code, but will not produce an executable.
