# Maven and Tycho

The IBEX GUI is built using Tycho which is an extension of Maven designed for building Eclipse RCP products.

This document provides a brief overview of both Maven and Tycho.

## Maven ##
### What is it? ###
The official description:

_Apache Maven is a software project management and comprehension tool. Based on the concept of a project object model (POM), Maven can manage a project's build, reporting and documentation from a central piece of information._

In simple terms:

_Maven is a build automation tool used primarily for Java projects._

### What is a POM file? ###
An XML file that describes the software project being built, its dependencies on other external modules and components, the build order, directories, and required plug-ins.

In many ways it can be consider the equivalent of a C-style Makefile as it defines how the project is built. Here is an example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">

    <modelVersion>4.0.0</modelVersion>
    <groupId>com.maven_example.test</groupId>
    <artifactId>test</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <dependencies>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.8.2</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <build>
        <plugins>
            <plugin>
                <groupId>org.sonatype.install4j</groupId>
                <artifactId>install4j-maven-plugin</artifactId>
                <executions>
                    <execution>
                        <id>compile-installers</id>
                        <phase>package</phase>
                        <goals>
                            <goal>compile</goal>
                        </goals>
                        <configuration>
                            <projectFile>${project.basedir}/src/main/installer/myproject.install4j</projectFile>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>

</project>
``` 

Let's explain the various parts shown:
* Near the top we have the following information:
    * The `groupId` is usually the name of the overarching project and is the same style as a Java package ID, e.g. org.apache.maven
    * The name that the project is often known by, e.g. maven
    * The version number. SNAPSHOT is automatically replaced by a date-time indicating the build time
    * Packaging defines what is built, in this case a standard jar file
* The dependencies section defines any external dependencies required for the project, in this case only junit is required
* The properties section is used to define other properties relevant to the build
* The build section defines specific information for the build such as the plugins to use. In this example, we use install4j to create an executable file

See https://maven.apache.org/pom.html for more information on the various sections.

### A Maven project ###

Maven is very picky about how a project is laid out, it requires the various directories to be named and positioned correctly.
Luckily, most IDEs will take care of this for us.

The layout is as follows:
```
|- The top-level of the project
    |- src
        |- main
            |- java
                |- The packages directories for the source e.g. com.myexample
            |- resources
        |- test
            |- java
                |- The packages directories for the tests
    - pom.xml 
```


The POM described above is sufficient for us to build a project from the command line using Maven. The commonly used commands used are:

* `mvn compile` - this creates the JVM bytecode
* `mvn test` - this runs any unit tests
* `mvn package` - create the jar and runs the tests
* `mvn clean` - removes any previous build artifacts

### Multiple modules ###

If we have a project made up of a number of different packages (or modules) with dependencies then Maven can handle that.
For example, let's say we have two separate packages: com.example.library; and, com.example.application where application depends on library. The POM for application would need to indicate this dependency like so:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.maven_example</groupId>
    <artifactId>myApp</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <dependencies>
        <dependency>
            <groupId>com.example.library</groupId>
            <artifactId>library</artifactId>
            <version>1.0-SNAPSHOT</version>
            <scope>compile</scope>
        </dependency>
        <dependency>
            <groupId>com.google.code.gson</groupId>
            <artifactId>gson</artifactId>
            <version>2.6.2</version>
            <scope>compile</scope>
        </dependency>
    </dependencies>
</project>
```
It also has a dependency on GSON for the hell of it. The dependencies have a scope, this determines how they are treated. The most common options are:

* `compile` - dependencies are available in all classpaths (default)
* `test` - only needed for testing
* `provided` - provided at run-time, e.g. from the JDK
* `runtime` - not needed for compilation
* `system` - have to provide the containing JAR explicitly

There are other options and more detailed explanations on the [Maven website] (https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html) 

Now application has no idea where to find library, so we create a new POM file in a higher directory which will be our parent POM. The parent provides the information for both modules to work together. The POM looks something like:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example.parent</groupId>
    <artifactId>parent</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>
 
  <modules>
    <module>com.example.application</module>
    <module>com.example.library</module>
  </modules>
</project>
```
The modules tags specify the location of the modules to build. And the modules' POMs need to have a reference to the parent, like so:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">

    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>library</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <parent>
        <groupId>com.example.parent</groupId>
        <artifactId>parent</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
</project>
``` 
Running the build using the parent POM (i.e. from the same directory) will build both modules and link them appropriately.

### Profiles ###
Using profiles it is possible to configure the build for different circumstances. For example, say I want to install the final product in a certain directory sometimes then I can add a profile for this, like so:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">

    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>library</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <parent>
        <groupId>com.example.parent</groupId>
        <artifactId>parent</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <profiles>
    <profile>
        <id>release</id>
        <build>
            <directory>c:\\release\</directory>
        </build>
    </profile>
   </profiles>
</project>
``` 
Running the build with the profile specified will result in the final product being installed into the specified directory. To run a profile, specify the profile using -P like so:
```mvn package -Prelease```

Profiles can be used for a number of things, such as specifying the JDK version number or the OS to build for.

For more information see the [Maven website] (http://maven.apache.org/guides/introduction/introduction-to-profiles.html)

## Tycho ##
### What is it? ###
Tycho is a set of Maven plugins and extensions for building Eclipse-based applications with Maven. Tycho allows Maven to support building bundles, fragments, features, P2 repositories, RCP applications etc.

Tycho is used to build the IBEX GUI application that is deployed on the instruments.

### The parent POM ###
Maven allows a parent POM to be defined which contains references to the other POM files for the other projects that make up an application. This is used in the IBEX GUI because it allows the centralisation of the settings for building the application.

The IBEX POM contains a lot of information, so here is a stripped down version to show the key points.

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<groupId>CSS_ISIS</groupId>
	<artifactId>uk.ac.stfc.isis.ibex.client.tycho.parent</artifactId>
	<version>1.0.0-SNAPSHOT</version>
	<packaging>pom</packaging>

	<properties>
		<tycho.version>0.20.0</tycho.version>
		<tycho-repo.url>https://oss.sonatype.org/content/groups/public/</tycho-repo.url>
		<kepler-repo.url>http://download.eclipse.org/releases/kepler</kepler-repo.url>
		<kepler-updates-repo.url>http://download.eclipse.org/eclipse/updates/3.8</kepler-updates-repo.url>
		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
	</properties>

	<repositories>
		<repository>
			<id>kepler-updates</id>
			<layout>p2</layout>
			<url>${kepler-updates-repo.url}</url>
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

                <!-- Other plugins omitted such as unit testing and checkstyle -->
		</plugins>
	</build>

	<modules>
		<module>../uk.ac.stfc.isis.ibex.client.product</module>
		<module>../uk.ac.stfc.isis.ibex.feature.base</module>
		
                <!-- Other plugins that make up IBEX would be listed here -->

		<module>../uk.ac.stfc.isis.ibex.ui.mainmenu.tests</module>
	</modules>
</project>

```
Let's explain the various parts shown:
* At the top we have the standard Maven boiler plate as discussed above
* The properties section is used to define properties relevant to the build, in this case, the URLs for the various repositories we are using
* The repositories section defined the version of Eclipse we are building against.
* The build section defines the plugins that will be used to build the application. Most of the ones we used have been removed for clarity. The Tycho plugin entry tells Maven to download Tycho and use that to define the build
* The modules section lists the locations of the POM files for the various projects that make up the application (remember that this is the parent POM)

### A child POM ###
A typical child POM is shown below

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <artifactId>uk.ac.stfc.isis.ibex.banner</artifactId>
  <packaging>eclipse-plugin</packaging>
  <parent>
  	<groupId>CSS_ISIS</groupId>
  	<artifactId>uk.ac.stfc.isis.ibex.client.tycho.parent</artifactId>
  	<version>1.0.0-SNAPSHOT</version>
  	<relativePath>../uk.ac.stfc.isis.ibex.client.tycho.parent</relativePath>
  </parent>
  <version>1.0.0-SNAPSHOT</version>
</project>
```

Basically it is very simple - it points at the parent POM to get most of its information.

The packaging type is defined a eclipse-plugin. This is a packaging type defined by Tycho, Maven itself has no idea what this means. Other Tycho types used in IBEX are eclipse-feature for features,eclipse-test-plugin for fragment projects that define unit tests and eclipse-repository for configuring builds.

### Creating an application ###

In IBEX we define a separate project called `uk.ac.stfc.isis.ibex.client.product` which defines how the product is built. It has a POM file of packaging type eclipse-repository.

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
    <version>1.0.0-SNAPSHOT</version>
  <artifactId>uk.ac.stfc.isis.ibex</artifactId>
  <packaging>eclipse-repository</packaging>
  <parent>
  	<groupId>CSS_ISIS</groupId>
  	<artifactId>uk.ac.stfc.isis.ibex.client.tycho.parent</artifactId>
  	  <version>1.0.0-SNAPSHOT</version>
  	<relativePath>../uk.ac.stfc.isis.ibex.client.tycho.parent</relativePath>
  </parent>
  
  <build>
    <plugins>
      <plugin>
        <groupId>org.eclipse.tycho</groupId>
        <artifactId>tycho-p2-director-plugin</artifactId>
        <version>${tycho.version}</version>
        <executions>
          <execution>
            <!-- install the product using the p2 director -->
            <id>materialize-products</id>
            <goals>
              <goal>materialize-products</goal>
            </goals>
          </execution>
          <execution>
            <!-- create zip file with the installed product -->
            <id>archive-products</id>
            <goals>
              <goal>archive-products</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
</project>
```

The key area is the materialize-products section, this tells Tycho to actually create the product. Without this the build runs and checks everything is okay, but does not produce an executable.

## How to add a new plugin to the Maven build ##

https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Adding-a-Plugin-or-Feature-to-Maven-Build
