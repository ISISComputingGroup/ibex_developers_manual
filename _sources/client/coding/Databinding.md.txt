# Databinding

:::{seealso}
- [How to connect a view to a PV](Connecting-a-View-to-a-PV) for a higher-level description of how to pass data from an EPICS
PV through backend classes (model & view model), and into a UI element.
- [The Eclipse data binding documentation](https://github.com/eclipse-platform/eclipse.platform.ui/blob/master/docs/JFaceDataBinding.md)
has more detailed explanations about advanced data binding options.
:::

## Backend

The `ModelObject` class is a central helper for data binding in the IBEX GUI, which is implemented by backend classes.
It provides the following key methods:

### `firePropertyChange`

The `firePropertyChange` method is used to inform the listeners when the value has changed. A typical implementation of
a getter and setter in a backend class uses `firePropertyChange` as follows:

```java
    private String foo;

    public String getFoo() {
        return this.foo;
    }

    public void setFoo(String value) {
        firePropertyChange("foo", this.foo, this.foo = value);
    }
```

If `oldValue` and `newValue` are equal and non-null, then the event is not raised.
If you want a change to always fire, even if `oldValue` and `newValue` are the same, pass `null` as the `oldValue` to
`firePropertyChange`.

Not all listeners will use the `newValue` provided to the change event; some listeners will instead only use the event
as a trigger to call the explicit getter.

### `addPropertyChangeListener` & `removePropertyChangeListener`

The data-binding framework automatically calls `addPropertyChangeListener` when a UI widget being bound.
The `removePropertyChangeListener` is called when the widget binding is disposed, for example when the GUI is closed.

## Frontend

A typical frontend class binds to its view model, in a constructor, like:

```java
    Label lblFoo = new Label(this, SWT.NONE);
    
    DataBindingContext bindingContext = new DataBindingContext();

    bindingContext.bindValue(WidgetProperties.text().observe(lblFoo), 
        BeanProperties.value("foo").observe(viewModel));
```

For a control that a user can write to, use `WidgetProperties.text(SWT.Modify)`. This will notify the model whenever
the user input in a control changes.

:::{important}
Create the binding context on the thread which should receive events. For UI code, this is the
UI thread - so the binding context is normally created in the view's constructor, alongside instantiating UI elements.
**Do not create the binding context in a static initializer.**
:::

## Update strategies

The call to `bindValue` accepts two optional extra arguments, which are update strategies. These allow extra steps to
be performed during the databinding operation, for example validation or conversion.

In a call like:
```java
UpdateValueStrategy strategy1 = new UpdateValueStrategy();
UpdateValueStrategy strategy2 = new UpdateValueStrategy();
bindingContext.bindValue(target, model, strategy1, strategy2);
```
The first strategy is used for data going from the target (UI widget) towards the model; the second strategy is used
for data coming from the model towards the target (UI widget).

### Validators

It is possible to implement validators, which verify that a value is "valid" before passing it onto the model.
Validators implement the `org.eclipse.core.databinding.validation.IValidator` interface and are assigned to an update
strategy:

```java
UpdateValueStrategy strategy = new UpdateValueStrategy();
strategy.setBeforeSetValidator(new MyValidator());
```

[The `uk.ac.stfc.isis.ibex.validators` package](https://github.com/ISISComputingGroup/ibex_gui/tree/master/base/uk.ac.stfc.isis.ibex.validators/src/uk/ac/stfc/isis/ibex/validators)
in the GUI contains commonly-used data binding validators which may be used as reference implementations.

### Converters

Converters are similar to validators in that they are used as part of the update strategy; however, they are used to
convert either the data from the model or the data sent to the model by the widget. They implement the
`org.eclipse.core.databinding.conversion.Converter` interface. Similar to validators, they are attached to an update
strategy:

```java
UpdateValueStrategy strategy = new UpdateValueStrategy();
strategy.setConverter(new MyConverter());
```

## Databinding lists

Most of this is taken care of by the databinding library via `ListViewer` and `ObservableListContentProvider`:

```java
ListViewer myViewer = new ListViewer(parent, SWT.BORDER | SWT.V_SCROLL | SWT.SINGLE);
ObservableListContentProvider contentProvider = new ObservableListContentProvider();
myViewer.setContentProvider(contentProvider);
myViewer.setInput(BeanProperties.list("names").observe(myViewModel));

// To get the List Control itself
org.eclipse.swt.widget.List myList = myViewer.getList();
```

`ListViewer` is a wrapper around the List control that provides extra functionality and `ObservableListContentProvider`
makes the databinding work.

## Troubleshooting

### Missing or incorrectly named getter or setter (or incorrectly named)

Behind the scenes the databinding library automatically changes the first character to upper-case and then prepends 
"get" and "set".

With something like the following it is import that the name of the property to bind to is cased correctly:
```java
bindingContext.bindValue(WidgetProperties.text(SWT.Modify)
            .observe(txtAge), BeanProperties.value("age").observe(person));
```

This assumes there is a getter and setter called `getAge` and `setAge`.

For something like `getFedId` the binding code would look like:

```java
bindingContext.bindValue(WidgetProperties.text(SWT.Modify)
    .observe(txtId), BeanProperties.value("fedId").observe(person));
```

:::{important}
The 'f' of `fedId` is lower-case in this example. It will not work if it is upper-case.
:::

### The getter or setter "silently" throws an exception

If any code in the getter throws an unhandled exception then the binding won't work because the value cannot be read.
If a setter throws an unhandled exception before the firing the property change then the listeners will not receive the
change signal. Both result in the binding being broken.

If a binding seems to work intermittently then there might be something in the getter or setter causing this, e.g. an
object used in a getter that switches between being null and initialised based on something else.

The exceptions will appear in the console inside Eclipse and IBEX, but won't cause an error pop-up to appear.

### The binding works but the initial value is not put in the widget

When the binding first happens it will call the getter to set the widget properties to whatever is in the model. 
If this doesn't happen, the getter is probably non-existent or not implemented correctly. 
