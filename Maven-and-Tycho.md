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

    <groupId>com.maven_example.myApp</groupId>
    <artifactId>myApp</artifactId>
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