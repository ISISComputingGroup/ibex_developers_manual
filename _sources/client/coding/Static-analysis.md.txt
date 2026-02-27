# Static analysis

We are currently making use of 2 static analysis tools in the IBEX GUI: 
[Checkstyle](https://checkstyle.sourceforge.io/) and [CodeQL](https://codeql.github.com/).

## Checkstyle

Checkstyle is designed to enforce a set of highly configurable coding standards. It is run as part of the Maven build
process, and will fail the GUI build if violations are detected. Eclipse can also be
[configured to highlight Checkstyle violations](../eclipse/Checkstyle-setup).

Checkstyle supports a very large number of rules including ones relating to naming conventions, annotations, javadoc
comments, poor coding practices, etc. Checkstyle configuration is done by 
[an XML file called 'checkstyle.xml'](https://github.com/ISISComputingGroup/ibex_gui/blob/master/base/uk.ac.stfc.isis.ibex.client.tycho.parent/checkstyle.xml)
in the IBEX GUI repository.

In cases where Checkstyle has flagged code as non-compliant, but is being overzealous, a `@SuppressWarnings` annotation
can be used to tell Checkstyle to ignore certain warnings for specific classes or methods. For example:

```java
    @SuppressWarnings("checkstyle:magicnumber")
    public void getSecondsInHours(int hours) {
        return hours * 60 * 60;    // Magic numbers!
    }
```

Or for multiple warnings:

```java
    @SuppressWarnings({"checkstyle:magicnumber", "checkstyle:localvariablename"})
    public void getSecondsInHours(int hours) {
        int seconds_per_hour = 60 * 60;    // Magic numbers and a variable name that does not conform to the recommended style!
        return hours * seconds_per_hour;
    }
```

## CodeQL

CodeQL is a security-focused linting tool. It aims to find coding patterns which are known to be insecure, though it
also has a smaller number of stylistic lint rules.

CodeQL is set to run on Github pull requests. It will automatically comment on pull requests with any findings. If not
relevant, these findings can be dismissed via the Github interface. CodeQL is currently not set up to run locally.
