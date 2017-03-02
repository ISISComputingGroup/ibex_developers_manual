> [Wiki](Home) > [Deployment](Deployment) > [Creating a release](Creating a release) > Understanding Java Licensing

# Understanding Java Licensing

In December 2016, Oracle announced that they would be taking steps to ensure customers using commercial features of Java paid the appropriate license fee (see http://www.theregister.co.uk/2016/12/16/oracle_targets_java_users_non_compliance/).  This announcement has caused some confusion.  The purpose of this page is to clarify Java Licensing for IBEX developers.

For a complete understanding of Java Licensing terms & conditions consult Oracle's [Java SE and Java Embedded Products](http://www.oracle.com/technetwork/java/javase/terms/products/index.html) page.

## Java SE Product Editions

Java SE comes in three different product editions. Each product edition provides a different set of functional capabilities, and is intended for different kinds of applications and development scenarios.  The three product editions are:

1. Java SE
1. Oracle Java SE Advanced & Oracle Java SE Advanced Desktop
1. Oracle Java SE Suite

It is important to understand that Oracle does _**not**_ provide installation programs that correspond directly to these 3 product editions. Depending on which of the products you have licensed, you will need to download one or more installer packages.  Regardless of which product edition you intend to use, you must agree to the terms of the relevant product license.

### Java SE Product Edition

The Java SE Product Edition includes the following components:

* Java Runtime Environment (JRE), (Server and regular packages)
* Java Development Kit (JDK), including the JavaFX Software Development Kit (SDK),
* JavaFX Runtime,
* JRockit JDK

The JRE provides a Java Virtual Machine (JVM), the standard class libraries and other components to run applications written in the Java programming language.  The JDK is a superset of the JRE, and contains everything in the JRE, plus tools such as compilers and debuggers for development.

JavaFX is a software platform for creating and delivering desktop applications, as well as rich internet applications (RIAs) that can run across a wide variety of devices. JavaFX is intended to replace Swing as the standard GUI library for Java SE, but both will be included for the foreseeable future.  At the present time (March 2017), IBEX does not use JavaFX.

JRockit is an alternative JVM for Oracle middleware applications.  The JRockit JDK is a development toolkit for creating applications which use the JRockit JVM.  At the present time (March 2017), IBEX does not use JRockit.<br>
**Note:** JRockit JDK is free to use.  However, applications developed using the JRockit JDK may attract a run-time license fee.  Therefore, we should not use JRockit in IBEX.

With the exception of those features designated as Commercial Features (see below), Java SE can be used for free internally to run applications and may be redistributed in accordance with the [Oracle Binary Code License Agreement for the JAVA SE Platform Products](http://www.oracle.com/technetwork/java/javase/documentation/otn-bcl-02april2013-1966219.pdf) (the “Java BCLA”) - this version of the JAVA BCLA dates from 02-April-2013.

### Oracle Java SE Advanced & Oracle Java SE Advanced Desktop Product Edition

Java SE Advanced and Java SE Advanced Desktop product editions are both supersets of Java SE.  They include  additional features for so-called "mission critical enterprise client and server deployments of Java", as well as Java-based applications and solutions from independent software vendors (ISVs).

The Java SE Advanced and Java SE Advanced Desktop product editions both include Commercial Features.  We should not use these product editions in IBEX.

### Oracle Java SE Suite Product Edition

Java SE Suite is a superset of Oracle Java SE Advanced.  In addition to Java SE Advanced, it includes features for soft real-time applications, based on the JRockit Real Time JVM.

The Java SE Suite product editions includes Commercial Features.  We should not use it in IBEX.

### Installation Packages for Java SE Product Editions
Oracle does not provide installation programs that correspond directly to various Java SE product editions described above. Depending on the products licensed, one or more of the following individual packages must be downloaded:

* JRE (Server or regular packages)
* JDK
* Java Advanced Management Console
* Microsoft Windows Installer (MSI) Enterprise JRE Installer
* JavaFX Runtime
* JRockit JDK
* JRockit Mission Control

For the purpose of developing IBEX, the only installer packages we need be concerned about are the first two, the JRE and the JDK.  We do not use features provided by the other installer packages, so there is no need to download them.

## Commercial Features of Java SE Product Editions

All of the Java SE product edition included one or more commercial features.  The table below lists each of the commercial features and the product editions that contain those commercial features.

Commercial Feature | Product Editions containing the Commercial Feature 
------------------ | -------------------------------------------------- 
JRE Usage Tracking | JRE (version 7+, 8+)
Java Flight Recorder | JDK (versions 7u40+, 8+)
Java Mission Control | JDK (versions 7u40+, 8+) Java Mission Control
Java Advanced Management Console | (versions JDK 8u20+), Java Advanced Management Console
MSI Enterprise JRE Installer | JDK (versions 8u20+), MSI Enterprise JRE Installer
JRockit Flight Recorder | JRockit JDK 
JRockit Mission Control Console observability | JRockit JDK, JRockit Real Time, JRockit Mission Control
JRockit Mission Control Memory Leak Detector observability | JRockit JDK, JRockit Real Time, JRockit Mission Control 
JRockit Real Time, Deterministic GC | JRockit JDK, JRockit Real Time, JRockit Mission Control 

### Using Commercial Features of Java SE

According to the [Java command line options](http://docs.oracle.com/javase/7/docs/technotes/tools/windows/java.html) page:  <br> 
``-XX:+UnlockCommercialFeatures``: Use this flag to actively unlock the use of commercial features. Commercial features are the products Oracle Java SE Advanced or Oracle Java SE Suite, as defined at the Java SE Products web page.  If this flag is not specified, then the default is to run the Java Virtual Machine without the commercial features being available. After they are enabled, it is not possible to disable their use at runtime.

Oracle documentation makes it very clear that you cannot run commercial features of Java without specifying 
the ``-XX:+UnlockCommercialFeatures`` option on the command line.  

The key word in the above quote is "actively".  You have to actively choose to use the commercial features of Java.  Obviously, if you do choose to use commercial features of Java, then you need to ensure that you pay the appropriate license fee.

### IBEX Policy Regarding Commercial Features of Java SE 

In developing IBEX, our policy is **TO NOT USE COMMERCIAL FEATURES** of Java SE.  Therefore, we should never use the ``-XX:+UnlockCommercialFeatures`` command line option.

## Reference Material
* [Java Licensing](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Forms/AllItems.aspx?RootFolder=%2Fisis%2Fcomputing%2FICPdiscussions%2FJava%20Licensing&FolderCTID=0x01200027AD8F05966A2748B3B04C98BB5B442B&View={F2C33C51-70E6-4343-B937-2C59A2568306}) folder on ICP Discussions site.
* [Oracle Binary Code License Agreement for the JAVA SE Platform Products (02-April-2013)](http://www.oracle.com/technetwork/java/javase/documentation/otn-bcl-02april2013-1966219.pdf)