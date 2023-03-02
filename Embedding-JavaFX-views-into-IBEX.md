# Embedding JavaFX views into IBEX

This is useful for e.g. embedding native views from phoebus such as displaybuilder, databrowser etc.

### EFXclipse / compatibility layer setup

In order to be able to embed JavaFX views, the efxclipse compatibility layer must be configured on the branch you're attempting to use. The easiest way to check this is to check for the presence of an `uk.ac.stfc.isis.ibex.javafx` package - if this package is not present, you will not be able to embed javafx views. Currently this package is only available on the phoebus proof-of-concept branch.

### Creating a JavaFX view

They key bit of code to do this is actually rather simple:

```java
    @Override
    public void createPartControl(final Composite parent) {
    	FXCanvas fxCanvas = new FXCanvas(parent, SWT.NONE);
    	fxCanvas.setScene(new Scene(new AlarmTreeView(new AlarmClient("127.0.0.1:12345", "kafka_topic", null))));
    }
```

Where `AlarmTreeView` is a JavaFX UI class. `Scene` is a class provided by JavaFX (you can get this by depending on `uk.ac.stfc.isis.ibex.javafx` in the plugin's `MANIFEST.MF`). `FXCanvas` is the efxclipse class that enables SWT <-> JavaFX interoperability - again it is exported from `uk.ac.stfc.isis.ibex.javafx` - in particular it comes from `javafx-swt.jar`.

### JavaFX library setup

Note: we cannot currently get JavaFX from maven - although the dependency looks like it's there, it doesn't work for us due to the absence of `javafx-swt.jar`.

- Download javafx SDK from https://gluonhq.com/products/javafx/
- Put the jars in `uk.ac.stfc.isis.ibex.javafx/lib`
- Reference the jars on the plugin classpath and runtime-export any `com.sun.javafx.*` and `org.openjfx.*` packages from the plugin.

