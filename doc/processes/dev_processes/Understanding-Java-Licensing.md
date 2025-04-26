# Understanding Java Licensing

## OpenJDK

The OpenJDK is what we use on the IBEX project. The OpenJDK is available under the GNU General Public License (GPL). The license is included in the JDK directory, for reference if required.

## Oracle JDK

```{danger}
We should **not** need an Oracle JDK for IBEX - we should be using OpenJDK instead. 

Please ensure you thoroughly understand Oracle's licensing model before installing or using an Oracle JDK (if you must use it).

This information is left here for completeness only.
```

> In December 2016, Oracle announced that they would be taking steps to ensure customers using commercial features of Java paid the appropriate license fee (see [The Register](http://www.theregister.co.uk/2016/12/16/oracle_targets_java_users_non_compliance/) article).  This announcement has caused some confusion.  The purpose of this page is to clarify Java Licensing for IBEX developers.
> This page merely summarises the key points we, the IBEX development team, need to understand about Java licensing.  For a complete understanding of Java Licensing terms & conditions consult Oracle's [Java SE and Java Embedded Products](http://www.oracle.com/technetwork/java/javase/terms/products/index.html) page.
> ## Java SE Product Editions
> Java SE comes in three different product editions. Each product edition provides a different set of functional capabilities, and is intended for different kinds of applications and development scenarios.  The three product editions are:
> 1. Java SE
> 1. Oracle Java SE Advanced & Oracle Java SE Advanced Desktop
> 1. Oracle Java SE Suite
> All three product editions contain a mix of free-to-use & free-to-distribute features _**and**_ [Commercial Features](#java_licensing_features).  If you only use free-to-use and free-to-distribute features, you do not incur a license fee.  And, of course, if you use Commercial Features, you do incur a license fee.
> It is also important to understand that Oracle does _**not**_ provide installation programs that correspond directly to these 3 product editions. Depending on which of the products you have licensed, you will need to download one or more installer packages.  Regardless of which product edition you intend to use, you must agree to the terms of the relevant product license.
> Taking these two points into consideration, understanding which features of the various Java SE product editions we use is essential to determining whether ISIS is liable to pay a license fee for its use of Java in IBEX.
> ### Java SE Product Edition
> The Java SE Product Edition includes the following components:
> * Java Runtime Environment (JRE), (Server and regular packages)
> * Java Development Kit (JDK), including the JavaFX Software Development Kit (SDK),
> * JavaFX Runtime,
> * JRockit JDK
> The JRE provides a Java Virtual Machine (JVM), the standard class libraries and other components to run applications written in the Java programming language.  The JDK is a superset of the JRE, and contains everything in the JRE, plus tools such as compilers and debuggers for development.
> JavaFX is a software platform for creating and delivering desktop applications, as well as rich internet applications (RIAs) that can run across a wide variety of devices. JavaFX is intended to replace Swing as the standard GUI library for Java SE, but both are likely to be included for the foreseeable future.  At the present time (March 2017), IBEX does not use JavaFX.
> JRockit is an alternative JVM for Oracle middleware applications.  The JRockit JDK is a development toolkit for creating applications which use the JRockit JVM.  At the present time (March 2017), IBEX does not use JRockit.<br>
> **Note:** JRockit JDK is free to use.  However, applications developed using the JRockit JDK may attract a run-time license fee.  Therefore, we should not use JRockit in IBEX.
> With the exception of those features designated as [Commercial Features](#java_licensing_features), Java SE can be used for free internally to run applications and may be redistributed in accordance with the [Oracle Binary Code License Agreement for the JAVA SE Platform Products](http://www.oracle.com/technetwork/java/javase/documentation/otn-bcl-02april2013-1966219.pdf) (the “Java BCLA”) - this version of the JAVA BCLA dates from 02-April-2013.
> ### Oracle Java SE Advanced & Oracle Java SE Advanced Desktop Product Edition
> Java SE Advanced and Java SE Advanced Desktop product editions are both supersets of Java SE.  They include  additional features for so-called "mission critical enterprise client and server deployments of Java", as well as Java-based applications and solutions from independent software vendors (ISVs).
> The Java SE Advanced and Java SE Advanced Desktop product editions both include Commercial Features.  IBEX does not need to use any of the additional features (commercial or otherwise) provided by Java SE Advanced and Java SE Advanced Desktop.  Therefore, we should not use them.
> ### Oracle Java SE Suite Product Edition
> Java SE Suite is a superset of Oracle Java SE Advanced.  In addition to Java SE Advanced, it includes features for soft real-time applications, based on the JRockit Real Time JVM.
> The Java SE Suite product editions includes Commercial Features.  IBEX does not need to use any of the additional features (commercial or otherwise) provided by Java SE Suite.  Therefore, we should not use it.
> ### Installation Packages for Java SE Product Editions
> Oracle does not provide installation programs that correspond directly to various Java SE product editions described above. Depending on the products licensed, one or more of the following individual packages must be downloaded:
> * JRE (Server or regular packages)
> * JDK
> * Java Advanced Management Console
> * Microsoft Windows Installer (MSI) Enterprise JRE Installer
> * JavaFX Runtime
> * JRockit JDK
> * JRockit Mission Control
> For the purpose of developing IBEX, the only installer packages we need be concerned about are the first two, the JRE and the JDK.  We do not use features provided by the other installer packages, so there is no need to download them.
>
> {#java_licensing_features}
> ## Commercial Features of Java SE Product Editions
> All of the Java SE product edition included one or more commercial features.  The table below lists each of the commercial features and the product editions that contain those commercial features.
> Commercial Feature | Product Editions containing the Commercial Feature 
> ------------------ | -------------------------------------------------- 
> JRE Usage Tracking | JRE (version 7+, 8+)
> Java Flight Recorder | JDK (versions 7u40+, 8+)
> Java Mission Control | JDK (versions 7u40+, 8+) Java Mission Control
> Java Advanced Management Console | JDK (versions 8u20+), Java Advanced Management Console
> MSI Enterprise JRE Installer | JDK (versions 8u20+), MSI Enterprise JRE Installer
> JRockit Flight Recorder | JRockit JDK 
> JRockit Mission Control Console observability | JRockit JDK, JRockit Real Time, JRockit Mission Control
> JRockit Mission Control Memory Leak Detector observability | JRockit JDK, JRockit Real Time, JRockit Mission Control 
> JRockit Real Time, Deterministic GC | JRockit JDK, JRockit Real Time, JRockit Mission Control 
> **Note:** Full details of [Java Commercial Features](http://www.oracle.com/technetwork/java/javase/terms/products/index.html)
> ### Using Commercial Features of Java SE
> According to the [Java command line options](http://docs.oracle.com/javase/7/docs/technotes/tools/windows/java.html) page:  <br> 
> ``-XX:+UnlockCommercialFeatures``: _Use this flag to actively unlock the use of commercial features. Commercial features are the products Oracle Java SE Advanced or Oracle Java SE Suite, as defined at the Java SE Products web page.  If this flag is not specified, then the default is to run the Java Virtual Machine without the commercial features being available. After they are enabled, it is not possible to disable their use at runtime._
> Oracle documentation makes it very clear that we cannot run commercial features of Java without specifying 
> the ``-XX:+UnlockCommercialFeatures`` option on the command line.  
> The key word in the above quote is "actively".  We have to actively choose to use the commercial features of Java.  Obviously, if we do choose to use commercial features of Java, then ISIS becomes liable to pay a license fee.  Therefore, choosing to use commercial features of Java, implies that we seek prior approval to purchase the appropriate Java SE license.
> ### IBEX Policy Regarding Commercial Features of Java SE 
> At the present time, IBEX does not need to use any of the commercial features of Java SE.  Therefore, in developing IBEX, our policy is **TO NOT USE COMMERCIAL FEATURES** of Java SE.  We should never use the ``-XX:+UnlockCommercialFeatures`` command line option.  Nor should we use the MSI Enterprise JRE Installer.
> ### IBEX Build Scripts & Commercial Features of Java SE
> At the time of writing (2nd March 2017), the IBEX build scripts conform to the above policy.  The scripts used to invoke Java in order to run the IBEX client are generated by the IBEX build server.  The ``-XX:+UnlockCommercialFeatures`` command line option is **not** included in the configuration of the build script.  See:
> 1. [build.bat](https://github.com/ISISComputingGroup/ibex_gui/blob/master/build/build.bat) and
> 1. [pom.xml](https://github.com/ISISComputingGroup/ibex_gui/blob/master/base/uk.ac.stfc.isis.ibex.client.tycho.parent/pom.xml)
> We also use ActiveMQ on the IBEX server.  [ActiveMQ](http://activemq.apache.org/) is a Java application (from the [Apache Software Foundation](http://www.apache.org/)).  ActiveMQ is invoked via one of two batch files:
> 1. [`activemq.bat`](https://github.com/ISISComputingGroup/EPICS-ActiveMQ/blob/master/bin/activemq.bat)
> 1. [`activemq-admin.bat`](https://github.com/ISISComputingGroup/EPICS-ActiveMQ/blob/master/bin/activemq-admin.bat)
> The ``-XX:+UnlockCommercialFeatures`` command line option is **not** a feature of either batch file. Given that the Apache SF is dedicated to the provision of open-source software, it seems highly unlikely that they will ever use 
> the ``-XX:+UnlockCommercialFeatures`` command line option.
> ## Reference Material
> * [Java Licensing](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Forms/AllItems.aspx?RootFolder=%2Fisis%2Fcomputing%2FICPdiscussions%2FJava%20Licensing&FolderCTID=0x01200027AD8F05966A2748B3B04C98BB5B442B&View={F2C33C51-70E6-4343-B937-2C59A2568306}) folder on ICP Discussions site.
> * [Oracle Binary Code License Agreement for the JAVA SE Platform Products (02-April-2013)](http://www.oracle.com/technetwork/java/javase/documentation/otn-bcl-02april2013-1966219.pdf)
> * [Ticket: #1915](https://github.com/ISISComputingGroup/IBEX/issues/1915)