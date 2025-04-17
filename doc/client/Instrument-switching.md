# Instrument switching

Instrument switching in the GUI uses an extension point. This means that the switch can take place in a central place but then each plugin which is interested can sign up to the switching event. This keeps a separation between the plugins and the instrument switching module; i.e. a plugin can be removed without changing the instrument switching code.

The instrument switching in E4 is performed through the E3 compatibility layer, as E4 has no native support for extension points. The equivalent behaviour in E4 is provided through services, which might be a necessary transition as services and extensions points are not cross-compatible.

This extension point is setup in `uk.ac.stfc.isis.ibex.instrument/META-INF/MANIFEST.MF` (see the extension Points tab). This sets up the name of the extension point and the schema. The schema is in `/uk.ac.stfc.isis.ibex.instrument/schema/uk.ac.stfc.isis.ibex.instrument.info.exsd` (click Schema on previous page). This defines the methods that should be fulfilled by the plugin that want to sign up to this extension. In this case there are three methods:

   `preSetInstrument` - this will be called before the instrument is switched. This is useful for closing resources using the old instrument.
   `setInstrument` - this will be called to set the instrument and should actually perform the change.
   `postSetInstrument` - this will be called after the instrument is set. It can be used, for example, to perform final clean up of resources or reopening of perspectives.

The instrument handler is responsible for calling this method on each registered plugin. It does this in the method `uk.ac.stfc.isis.ibex.instrument.Instrument.setInstrumentForAllPlugins` in the private method `updateExtendingPlugins`. Notice that it call all preSetInstruments methods before setInstrument.

To sign up to this event the plugin must create a class which implements the interface `uk.ac.stfc.isis.ibex.instrument.InstrumentInfoReceiver`. This will be instantiated when the instrument is switched to. This class is registered in the plugin's extensions (this is similar to the perspectives see [adding a perspective](Adding-a-Button-to-the-Perspective-Switcher#adding-the-perspective-and-view-to-the-gui) ).
