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

In many ways it can be consider the equivalent of a Makefile as it defines how the project is built. Here is an example:

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
    * The groupId is usually the name of the overarching project and is the same style as a Java package ID, e.g. org.apache.maven
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
* 'mvn package' - create the jar and runs the tests
