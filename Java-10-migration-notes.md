The following are some rough notes from a trial migration of IBEX to java 10.

# Java 9 module system

In Java versions >9, there is a new module system. Certain packages are now not visible by default. This can cause errors in various areas of the GUI.

### The `--add-modules` and `--add-opens` flags

These frequently come up on sites like stackoverflow and the eclipse forums as a solution to "class not found" problems. It's a trap, and we shouldn't use these flags, as they will no longer be valid in a later java version. Instead, the correct solution is to explicitly add dependencies (via `targetplatform`, `feature.xml` and `MANIFEST.MF`) ourselves and **not** rely on the modules that come in the JDK.

### javax.xml.bind (and classloader conflicts)

This is one of the modules which is unavailable by default. However, after adding it as an explicit dependency, you may see classloader conflicts. These will be characterised by a message like:

```
Cannot cast class jrt:/javax.xml.bind to bundleclass:/javax.xml.bind
```

What this message means is that you are correctly depending on javax.xml.bind in one place (where is says 'bundleclass:/', this is an explicit dependency) but not in another. Where it loads a class from core java you will see `jrt:/<classname>`. You need to go to the class that claims it was loaded from core java, and ensure it has a correct explicit dependency. It is also worth ensuring `javax.xml` and `javax.xml.bind` dependencies are as high up as possible in the `MANIFEST.MF` dependency list.

### javax.activation

This is another class which is no longer available by default - the solution is the same as above, list it as an explicit dependency. I have not seen classloader conflicts with this class, but that's not to say they couldn't possibly occur.

# ECJ configuration

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

# Eclipse

Both the Tycho eclipse version and the eclipse version in the target platform should be as recent as possible. Anything under eclipse 4.8 is unlikely to work.