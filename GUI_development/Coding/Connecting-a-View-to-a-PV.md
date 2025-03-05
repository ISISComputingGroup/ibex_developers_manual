> [Wiki](Home) > [The GUI](The-GUI) > [Coding](GUI-Coding) > Connecting a view to a PV

See [An Introduction to Databinding](An-Introduction-to-Databinding) for a explanation of databinding.

The basic arrangement for the mechanism for connecting a View to a PV is shown below:

![Basic principle](GUI_development/images/connecting_a_view_to_a_pv/basic_principle.png)

## Adding an Observable

The Observable is responsible for the connection to the PV and monitoring it for changes.

For this example we are going to connect and read the title PV on the DAE IOC. There is already a way of getting the title in the IBEX GUI, but for demonstration purposes we are going to ignore that!

First we need to create a new Plug-in in Eclipse:

* Select File->New->Plug-in Project

* Enter org.csstudio.isis.title for the project name

* Un-check 'Use default location' and browse to where the GUI code is located and append the project name to the path. For example, on my system the location would be C:\\Instrument\\Dev\\client\\ISIS\\base\\org.csstudio.isis.title
 
* Click 'Next'

* On the next screen, check the 'Generate an activator ...' check-box and un-check the others.

* Set 'Would you like to create a 3.x rich client application?' to 'No'

* Click 'Finish'

Now the Plug-in is created we can create an Observable:

* Open the MANIFEST.MF file in META-INF and under the 'Dependencies' tab add org.csstudio.isis.instrument to the list of required plug-ins

* Don't forget to save the changes

* Create a new Class called TitleVariable, this will be the class that holds the connection to the PV

* First we will need to create an observable factory to get our observable, in this case the PV should be updated when the instrument switches so add the following as a field.
```java
private final ObservableFactory obsFactory = new ObservableFactory(OnInstrumentSwitch.SWITCH);
```

* Next we get the specific variable for the PV the observable for the PV:
```java
package org.csstudio.isis.title;

import uk.ac.stfc.isis.ibex.epics.observing.ForwardingObservable;
import uk.ac.stfc.isis.ibex.epics.switching.ObservableFactory;
import uk.ac.stfc.isis.ibex.epics.switching.OnInstrumentSwitch;
import org.csstudio.isis.instrument.Channels;
import org.csstudio.isis.instrument.channels.CharWaveformChannel;
import uk.ac.stfc.isis.ibex.instrument.InstrumentUtils;

public class TitleVariable {
    
    private final ObservableFactory obsFactory = new ObservableFactory(OnInstrumentSwitch.SWITCH);
    public final ForwardingObservable<String> titleRBV = 
            obsFactory.getSwitchableObservable(new CharWaveformChannel(), InstrumentUtils.addPrefix("DAE:TITLE"));

    public TitleVariable() {
    }

} 
```
Explanation on Channels, InitialiseOnSubscribeObservable and reader.

## Adding a Model interface

Next we create a Model interface:

* Create a new Interface called TitleModel

* Implementing the interface will require getTitle and setTitle methods, so the code needs to look like:
```java
package org.csstudio.isis.title;

public interface TitleModel {
    String getTitle();
    void setTitle(String value);
}
```

## Adding an ObservableModel

Next we create an ObservableModel which allows us to bind controls on the View to the PV Observable:

* Create a new Class called ObservableTitleModel

* ObservableTitleModel needs to inherit from ModelObject from org.csstudio.isis.model, so change the code to look like:
```java
package org.csstudio.isis.title;

public class ObservableTitleModel extends ModelObject {

}
```    
* To fix the errors we need to add org.csstudio.isis.model to the required plug-ins list in the MANIFEST.INF. We can either add it manually or hover over the error and select "Add 'org.csstudio.isis.model' to required bundles"

* The next error can be fixed via the drop-down by selecting "Import 'ModelObject' (org.csstudio.isis.model)"

* The class also needs to implement TitleModel, so change the code to implement TitleModel:
```java
public class ObservableTitleModel extends ModelObject implements TitleModel {
```
* There should now be an error because the methods of TitleModel are not implemented. Hover over the error and select 'Add unimplemented methods'. The code should look like this:
```java
package org.csstudio.isis.title;

import org.csstudio.isis.epics.observing.BaseObserver;
import org.csstudio.isis.model.ModelObject;

public class ObservableTitleModel extends ModelObject implements TitleModel {

    private String title;
    
    @Override
    public String getTitle() {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public void setTitle(String value) {
        // TODO Auto-generated method stub
        
    }

}
```    
* The correctly cased getter and setter are requirements for the object to be bindable from a View (http://en.wikipedia.org/wiki/JavaBeans). We now need to add our own code to the methods:
```java
package org.csstudio.isis.title;

import org.csstudio.isis.model.ModelObject;


public class ObservableTitleModel extends ModelObject{
    private String title;
    
    public String getTitle() {
        return title;
    }
    
    public void setTitle(String value) {
        firePropertyChange("title", this.title, this.title = value);
    }
}
```
The firePropertyChange method raises an event when the title changes.
    
* Next we create a BaseObserver inside the class, like so:
```java
package org.csstudio.isis.title;

import org.csstudio.isis.epics.observing.BaseObserver;
import org.csstudio.isis.model.ModelObject;

public class ObservableTitleModel extends ModelObject implements TitleModel {

    private String title;
    
    private final BaseObserver<String> titleObserver = new BaseObserver<String>(){

        @Override
        public void onValue(String value) {
            setTitle(value);
        }

        @Override
        public void onError(Exception e) {
            
        }

        @Override
        public void onConnectionChanged(boolean isConnected) {
            
        }
    };
    
    @Override
    public String getTitle() {
        return title;
    }
    
    @Override
    public void setTitle(String value) {
        firePropertyChange("title", this.title, this.title = value);
    }
}
```
* The BaseObserver is responsible for observing changes in the TitleVariable, but for that we need to wire the objects up. Add a private variable for TitleVariable, like so:
```java
...
public class ObservableTitleModel extends ModelObject implements TitleModel {

    private String title;
    private final TitleVariable titleVar;
    
    private final BaseObserver<String> titleObserver = new BaseObserver<String>(){
...
```
* Now we add a constructor for that allows the wiring up of the BaseObserver and the TitleVariable:
```java
public ObservableTitleModel(TitleVariable titleVar) {
    this.titleVar = titleVar;
    titleVar.titleRBV.subscribe(titleObserver);
}
```
* The final class looks like this:
```java
package org.csstudio.isis.title;

import org.csstudio.isis.epics.observing.BaseObserver;
import org.csstudio.isis.model.ModelObject;

public class ObservableTitleModel extends ModelObject implements TitleModel {

    private String title;
    private final TitleVariable titleVar;
    
    private final BaseObserver<String> titleObserver = new BaseObserver<String>() {

        @Override
        public void onValue(String value) {
            setTitle(value);
        }

        @Override
        public void onError(Exception e) {
            
        }

        @Override
        public void onConnectionChanged(boolean isConnected) {
            
        }
    };
    
    @Override
    public String getTitle() {
        return title;
    }
    
    @Override
    public void setTitle(String value) {
        firePropertyChange("title", this.title, this.title = value);
    }
    
    public ObservableTitleModel(TitleVariable titleVar) {
        this.titleVar = titleVar;
        titleVar.titleRBV.subscribe(titleObserver);
    }
}
```
## The Activator

The Activator is the entry-point for the Plug-in - it gets created when the Plug-in is first used.
This is where we wire up the ObservableTitleModel and the TitleVariable:

* First we want to rename Activator because it is not a very descriptive name, let's refactor it to be called Title (okay that is not much better...)

* We want to make the Activator a singleton, so we need it to contain a static instance of itself, a constructor and a getInstance method:
```java
package org.csstudio.isis.title;

import org.osgi.framework.BundleActivator;
import org.osgi.framework.BundleContext;

public class Title implements BundleActivator {

    private static BundleContext context;
    private static Title instance;

    public Title() {
        instance = this;		
    }
    
    public static Title getInstance() {
        return instance;
    }

    static BundleContext getContext() {
        return context;
    }

    /*
     * (non-Javadoc)
     * @see org.osgi.framework.BundleActivator#start(org.osgi.framework.BundleContext)
     */
    public void start(BundleContext bundleContext) throws Exception {
        Title.context = bundleContext;
    }

    /*
     * (non-Javadoc)
     * @see org.osgi.framework.BundleActivator#stop(org.osgi.framework.BundleContext)
     */
    public void stop(BundleContext bundleContext) throws Exception {
        Title.context = null;
    }
}
```  
* Now we need it to wire up our classes from earlier, so we add the wiring up to the constructor:
```java
...
private static BundleContext context;
private static Title instance;

private TitleVariable titleVar;
private ObservableTitleModel model;

public Title() {
    instance = this;		
    titleVar = new TitleVariable(Instrument.getInstance().channels());
    model = new ObservableTitleModel(titleVar);
}
...
```
* Finally we add a method to retrieve the model so we can bind against it. The final code look like this:
```java
package org.csstudio.isis.title;

import org.csstudio.isis.instrument.Instrument;
import org.osgi.framework.BundleActivator;
import org.osgi.framework.BundleContext;

public class Title implements BundleActivator {

    private static BundleContext context;
    private static Title instance;
    
    private TitleVariable titleVar;
    private ObservableTitleModel model;
    
    public Title() {
        instance = this;		
        titleVar = new TitleVariable(Instrument.getInstance().channels());
        model = new ObservableTitleModel(titleVar);
    }
    
    public static Title getInstance() {
        return instance;
    }
    
    public ObservableTitleModel model() {
        return model;
    }

    static BundleContext getContext() {
        return context;
    }

    /*
     * (non-Javadoc)
     * @see org.osgi.framework.BundleActivator#start(org.osgi.framework.BundleContext)
     */
    public void start(BundleContext bundleContext) throws Exception {
        Title.context = bundleContext;
    }

    /*
     * (non-Javadoc)
     * @see org.osgi.framework.BundleActivator#stop(org.osgi.framework.BundleContext)
     */
    public void stop(BundleContext bundleContext) throws Exception {
        Title.context = null;
    }
}
```
## A little tidying up

By convention we should put any class etc. we don't want exposed outside outside of the Plug-in in a package ending in internal. In this example the package would be called org.csstudio.isis.title.internal.

## Binding the View to the Model

The simplest way to do this is to add a method for creating the binding to the View:
```java
private DataBindingContext bindingContext;

private void doBinding(Label lblTitle){
    bindingContext = new DataBindingContext();
    bindingContext.bindValue(WidgetProperties.text().observe(lblTitle), BeanProperties.value("title").observe(Title.getInstance().model()));
}
```
* Then the method can be called from the `createPartControl` method of the View

## Writing to a PV

For this example we will start by adding a writeable PV for writing to the title to the TitleVariable class, so it now looks like this:
```java
package org.csstudio.isis.title;

import uk.ac.stfc.isis.ibex.epics.observing.ForwardingObservable;
import org.csstudio.isis.epics.writing.Writable;
import org.csstudio.isis.instrument.Channels;
import org.csstudio.isis.instrument.channels.CharWaveformChannel;
import uk.ac.stfc.isis.ibex.instrument.InstrumentUtils;

public class TitleVariable {
    
    private final ObservableFactory obsFactory = new ObservableFactory(OnInstrumentSwitch.SWITCH);
    public final ForwardingObservable<String> titleRBV = 
            obsFactory.getSwitchableObservable(new CharWaveformChannel(), InstrumentUtils.addPrefix("DAE:TITLE"));

    private final WritableFactory writeFactory = new WritableFactory(OnInstrumentSwitch.SWITCH);
    public final Writable<String> titleSP = 
            writeFactory.getSwitchableWritable(new CharWaveformChannel(), InstrumentUtils.addPrefix("DAE:TITLE:SP"));

    public TitleVariable() {
    }
}
```
Note that the type of the new PV is Writable and uses writable and not reader.

Next we open the TitleModel interface and add two new methods for working with the set-point, it now looks like this:
```java
package org.csstudio.isis.title;


public interface TitleModel {
    String getTitle();
    void setTitle(String value);
    String getTitleSP();
    void setTitleSP(String value);
}
```
This interface is implemented in the ObservableTitleModel class, so we need to add implementations for the two new methods. 
In fact, the ObservableTitleModel should now be showing an error because these methods are not implemented. 
Open the class and hover over the class name, it should give you the option to 'Add unimplemented methods', select this. 
Now we need to add code for these new methods:
```java
...
@Override
public String getTitleSP() {
    return "";
}

@Override
public void setTitleSP(String value) {
    titleVar.titleSP.write(value);
}
...
```    
The getter returns an empty string, but this does not matter - we could wire it up to get the current value of the set-point using a BaseObserver in the same way we did for reading the current title earlier, but we will leave that as an exercise for the reader!

The setter uses the Writable object to write the new value to the IOC via channel access.

Finally we need to edit the View itself to enable it to bind to titleSP. For this we add a text-box called txtNewTitle and set up the binding:
```java
...
bindingContext.bindValue(WidgetProperties.text(SWT.Modify).observe(txtNewTitle), BeanProperties.value("titleSP").observe(org.csstudio.isis.title.Title.getInstance().model()));
...
```
The key thing to note here is that WidgetProperties.txt takes SWT.Modify; this tells the binding to push the changes back to the model when the text-box is changed.

If we start the GUI it can be seen that as we type in the text-box the title changes; however, it is not ideal as the title set-point is updated with every keystroke which seems a bit unnecessary.

The alternative is to have a set button. First add a string property for the title SP called titleSP like so:
```java
...
public class ObservableTitleModel extends ModelObject implements TitleModel {

private String title;
private String titleSP;
private final TitleVariable titleVar;

private final BaseObserver<String> titleObserver = new BaseObserver<String>() {
...
```
Now we modify the getter and setter to use this variable for storing the new title before it is sent to the IOC:
```java
...
@Override
public String getTitleSP() {
    return titleSP;
}

@Override
public void setTitleSP(String value) {
    firePropertyChange("titleSP", this.titleSP, this.titleSP = value);
}
...
```  
We also add a method to the TitleModel interface and the implementation to the ObservableTitleModle for sending the string to the IOC:
```java
...
@Override
public void sendTitleSP()
{
    titleVar.titleSP.write(titleSP);
}
...
```
The final step is to add a button to the View's `createPartControl` method:
```java
...
Button btnSet = new Button(parent, SWT.NONE);
btnSet.setText("Set");
btnSet.addSelectionListener(new SelectionAdapter() {
    @Override
    public void widgetSelected(SelectionEvent e){
        org.csstudio.isis.title.Title.getInstance().model().sendTitleSP();
    }
});
...
```

## Using a Read-Write control

It is fine to have separate controls on the View for reading and writing, but sometimes it is more convenient to have one control for both.

This is relatively straightforward as there is already a helper class called WritableObservableAdapter that does most of the work.

The first step though is to create a View Model class in our UI plug-in, so create a new class in org.csstudio.isis.ui.title called ViewModel.
This class is where we will connect up the WritableObservableAdapter, but first we need to make some changes to ObservableTitleModel 
and to do that we start by modifying TitleModel to add a methods for accessing the Writeable object and a CachingObservable object (explained later):
```java
package org.csstudio.isis.title;

import org.csstudio.isis.epics.observing.CachingObservable;
import org.csstudio.isis.epics.writing.Writable;


public interface TitleModel {
    String getTitle();
    void setTitle(String value);
    String getTitleSP();
    void setTitleSP(String value);
    void sendTitleSP();
    CachingObservable<String> title();
    Writable<String> titleSetter();
}
```
Now we implement these methods in ObservableTitleModel:
```java
...
@Override
public CachingObservable<String> title() {
    return titleVar.titleRBV;
}

@Override
public Writable<String> titleSetter() {
    return titleVar.titleSP;
}
...
``` 
Next we add some code to ViewModel to connect things up:
```java
package org.csstudio.isis.ui.myperspective;


import org.csstudio.isis.title.ObservableTitleModel;
import org.csstudio.isis.ui.widgets.observable.WritableObservableAdapter;

public class ViewModel {
    
    public final ObservableTitleModel model = org.csstudio.isis.title.Title.getInstance().model();
    
    public final WritableObservableAdapter title = new WritableObservableAdapter(model.titleSetter(), model.title());
    
    public ViewModel() {
        
    }
}
``` 
Some error messages will appear relating to WritableObservableAdapter; to fix, hover over WritableObervableAdaptor and select "Add 'org.csstudio.isis.ui.widgets' to required bundles".
Errors will still remain on model.titleSetter() and model.title(), so hover over one of those and select "Add 'org.csstudio.isis.epics' to required bundles".

Now we need to adjust the View to use the ViewModel, first we strip out all of the code relating to the previous label, text-box and button (including the bindings), and then we add a ViewModel object and a WritableObservingTextBox:
```java
package org.csstudio.isis.ui.myperspective;

import org.csstudio.isis.ui.widgets.observable.WritableObservingTextBox;
import org.eclipse.swt.SWT;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.ui.part.ViewPart;
import org.eclipse.swt.layout.GridData;
import org.eclipse.swt.layout.GridLayout;

public class MyView extends ViewPart {
    public static final String ID = "org.csstudio.isis.ui.myperspective.myview";

    private final ViewModel viewModel = new ViewModel();
    private WritableObservingTextBox rbNumber;
    
    public MyView() {
    }

    @Override
    public void createPartControl(Composite parent) {
        parent.setLayout(new GridLayout(1, false));
        rbNumber = new WritableObservingTextBox(parent, SWT.NONE, viewModel.title);
        rbNumber.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, true, false, 1, 1));
        
    }

    @Override
    public void setFocus() {
    }

}
```
Hopefully once the GUI is started that all works as expected. 

So what is going on and what are these new bits we are using? 

* WritableObservingTextBox is a custom ISIS control for displaying and editing a value where they are different PVs for reading and writing
* WritableObservableAdapter is the object for linking up the two PVs. Essentially it does the same as what we did earlier with reading one PV and writing to another
* View Model - a class for providing presentation logic and state information for a View. The code could live in the View itself, but it is cleaner to put it in a separate class.

http://blogs.msdn.com/b/dphill/archive/2009/01/31/the-viewmodel-pattern.aspx provides a good explanation of View Models and how they fit in with the View and Model.

As you have probably noticed there are a number of methods in the ObservableTitlemodel that is no longer used, these can be removed (don't forgot to remove them from the interface as well!). The BaseObserver can also be removed.
```java
package org.csstudio.isis.title;

import org.csstudio.isis.epics.observing.CachingObservable;
import org.csstudio.isis.epics.writing.Writable;
import org.csstudio.isis.model.ModelObject;

public class ObservableTitleModel extends ModelObject implements TitleModel {

    private final TitleVariable titleVar;
    
    public ObservableTitleModel(TitleVariable titleVar) {
        this.titleVar = titleVar;
        //titleVar.titleRBV.subscribe(titleObserver);
    }

    @Override
    public CachingObservable<String> title() {
        return titleVar.titleRBV;
    }

    @Override
    public Writable<String> titleSetter() {
        return titleVar.titleSP;
    }
}
```