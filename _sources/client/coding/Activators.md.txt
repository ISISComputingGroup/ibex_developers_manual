# Activators

An Activator is the entry-point for a Plug-in - it gets created by the Eclipse framework when the Plug-in is first used.

Activators are implemented using a singleton pattern; a simplified typical activator looks like:

```java
import org.osgi.framework.BundleActivator;
import org.osgi.framework.BundleContext;

public class Help implements BundleActivator {

    private static BundleContext context;
    private static Help instance;

    static BundleContext getContext() {
        return context;
    }
    
    public Help() {
        instance = this;
    }
    
    @Override
    public void start(BundleContext bundleContext) throws Exception {
        Help.context = bundleContext;
    }

    public static Help getInstance() {
        return instance;
    }
    
    @Override
    public void stop(BundleContext bundleContext) throws Exception {
        Help.context = null;
    }
}
```

Activators may create and hold references to static data - for example models - so that they can later be referenced by
other plugins that need access to those models (for example, views).

:::{note}
At first glance the above pattern may seem dangerous - in most cases a singleton would need to check whether an instance
already exists and create one if not in `getInstance`, and would also need to use locking for thread safety.

However, this pattern is safe for Activators, because the Eclipse framework guarantees that `start` will
be called exactly once for a singleton plugin, before any other code can use the plugin, and that `stop` will only be
called when no other plugin will be able to access it afterwards (for example, during platform shutdown).
:::
