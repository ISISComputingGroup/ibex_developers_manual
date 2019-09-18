The following are some rough notes from a trial migration of IBEX to java 10.

### Java 9 module system

In Java versions >9, there is a new module system. Certain packages are now not visible by default. This can cause errors in various areas of the GUI. Generally the solution is to supply an explicit dependency (via the target platform and appropriate `MANIFEST.MF` files) for the appropriate API.

### The `--add-modules` and `--add-opens` flags

These frequently come up on sites like stackoverflow and the eclipse forums as a solution to "class not found" problems. It's a trap, and we shouldn't use these flags, as they will no longer be valid in a later java version. Instead, the correct solution is to explicitly add dependencies (via `targetplatform`, `feature.xml` and `MANIFEST.MF`) ourselves and **not** rely on the modules that come in the JDK.

### `javax.xml.bind` (and classloader conflicts)

This is one of the modules which is unavailable by default. However, after adding it as an explicit dependency, you may see classloader conflicts. These will be characterised by a message like:

```
Cannot cast class jrt:/javax.xml.bind to bundleclass:/javax.xml.bind
```

What this message means is that you are correctly depending on javax.xml.bind in one place (where is says 'bundleclass:/', this is an explicit dependency) but not in another. Where it loads a class from core java you will see `jrt:/<classname>`. You need to go to the class that claims it was loaded from core java, and ensure it has a correct explicit dependency. It is also worth ensuring `javax.xml` and `javax.xml.bind` dependencies are as high up as possible in the `MANIFEST.MF` dependency list.

### `javax.activation`

This is another class which is no longer available by default - the solution is the same as above, list it as an explicit dependency. I have not seen classloader conflicts with this class, but that's not to say they couldn't possibly occur.

### `org.apache.batik`

This is not part of the new module system, but newer versions of eclipse that are required to run java 10 bundle a dependency on org.apache.batik at version `1.10`. CS-Studio has a dependency on version `1.7`, and by default the build will choose the bigger version number, which causes IBEX to be unable to launch as it can't find the version CS-Studio wants at runtime. The solution is to pin the version of these plugins in the `feature.xml` to 1.7. This problem may go away if we update CS-Studio versions.

### `org.w3c.dom`

This is a package for XML DOM manipulation. Unfortunately it can be loaded from both the java standard library and an explicit dependency - for things to work properly we want the JDK version to be loaded in preference to the external one. To resolve this, ensure that the JDK is above "maven dependencies" in any dependency lists (in particular, on the project build path).

### `org.omg.CORBA`

This package is an indirect dependency of CS-Studio (although it has been removed from their very latest version). This package is **not** available from the JDK, even with command-line JDK options. However, JARs implementing this API are available from the JACORB project. This project does not offer a P2 site so we have built our own. The build configuration is [here](https://github.com/ISISComputingGroup/jacorb) and it gets deployed to [here](http://shadow.nd.rl.ac.uk/ICP_P2/jacorb/).

### ECJ

There was a bug in older versions of the `tycho-compiler-plugin` which prevented dependencies from overriding modules even if those modules were not visible. This bug has since been fixed. To tell the build to use a newer version of the compiler, add the following to the `pom.xml` in `client.tycho.parent` (you may need to bump version numbers - check maven central for the latest versions):

```
<plugin>
 <groupId>org.eclipse.tycho</groupId>
 <artifactId>tycho-compiler-plugin</artifactId>
 <version>${tycho.version}</version>
 <configuration>
  <compilerArgument>-err:-forbidden</compilerArgument>
 </configuration>
 <dependencies>
  <dependency>
   <groupId>org.eclipse.jdt</groupId>
   <artifactId>org.eclipse.jdt.core</artifactId>
   <version>3.15.0</version>
  </dependency>
  <dependency>
   <groupId>org.eclipse.jdt</groupId>
   <artifactId>org.eclipse.jdt.compiler.apt</artifactId>
   <version>1.3.200</version>
  </dependency>
  <dependency>
   <groupId>org.eclipse.jdt</groupId>
   <artifactId>org.eclipse.jdt.compiler.tool</artifactId>
   <version>1.2.300</version>
  </dependency>
 </dependencies>
</plugin>
```

### Eclipse

Both the Tycho eclipse version and the eclipse version in the target platform should be as recent as possible. Anything under eclipse 4.8 is unlikely to work. For java 11, anything older than eclipse 2019-06 is unlikely to work.

### Maven

To get better (more verbose) error output out of maven, edit `build.bat` and add the switches `-e -X` in the call to maven. You may find it beneficial to redirect this to file, as your console buffer is unlikely to be big enough to hold all of the build output with these flags.

### Parent POM: Tycho versions

There are a variety of tycho bugs that prevent compilations from succeeding on java 11, most of these have been resolved in Tycho 1.4.0, which is the version we should be using.

### Parent POM: eclipse versions

As well as the Tycho bugs described above, various parts of the eclipse build process will not work unless the parent POM (i.e. `uk.ac.stfc.isis.client.tycho.parent\pom.xml` and `uk.ac.stfc.isis.scriptgenerator.tycho.parent\pom.xml`) must have eclipse versions >= 4.10 defined, for example:

```
<photon-repo.url>http://download.eclipse.org/releases/photon</photon-repo.url>
<photon-updates-repo.url>http://download.eclipse.org/eclipse/updates/4.10</photon-updates-repo.url>
```

Lower versions, for example 4.8, will appear to work but give hard-to-debug dependency conflicts in the maven build. These conflicts will change depending on exactly how the build is set up. This seems to be because earlier eclipse versions break out of resolving a dependency cycle too early, which can lead to some dependencies looking like they can't be resolved even though they are in all of the appropriate POMs/Manifests. An example error is given below:

```
[ERROR] Cannot resolve project dependencies:
[ERROR]   Software being installed: scriptgenerator.product 1.0.0.qualifier
[ERROR]   Only one of the following can be installed at once: [org.eclipse.equinox.launcher 1.5.200.v20180922-1751, org.eclipse.equinox.launcher 1.5.0.v20180512-1130]
[ERROR]   Cannot satisfy dependency: org.eclipse.equinox.executable.feature.group 3.8.0.v20180518-2029 depends on: org.eclipse.equinox.p2.iu; org.eclipse.equinox.launcher [1.5.0.v20180512-1130,1.5.0.v20180512-1130]
[ERROR]   Cannot satisfy dependency: scriptgenerator.product 1.0.0.qualifier depends on: org.eclipse.equinox.p2.iu; org.eclipse.equinox.executable.feature.group 0.0.0
[ERROR]   Cannot satisfy dependency: scriptgenerator.product 1.0.0.qualifier depends on: org.eclipse.equinox.p2.iu; uk.ac.stfc.isis.scriptgenerator.feature.base.feature.group [1.0.0,1.0.1)
[ERROR]   Cannot satisfy dependency: uk.ac.stfc.isis.scriptgenerator.feature.base.feature.group 1.0.0.SNAPSHOT depends on: org.eclipse.equinox.p2.iu; org.eclipse.equinox.launcher [1.5.200.v20180922-1751,1.5.200.v20180922-1751]
```