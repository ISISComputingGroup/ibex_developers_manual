# Data binding

Note: there are some helpful tips to common errors/mistakes [here](Databinding---common-mistakes).

Note: an explanation of how to connect a view to a PV is [here](Connecting-a-View-to-a-PV)

## Create the example plug-ins ##

First create an Eclipse plug-in for the back-end:

* Start the plug-in wizard via File->New->Plug-in Project

* On the first page of the wizard enter `org.databinding.example.backend` as the name

* On the second page:

    * Deselect "Generate an activator, a Java class that controls the plug-in's life cycle"
    * Deselect "This plug-in will make contributions to the UI"
    * Select "No" for "Would you like to create a 3.x rich client application?"
    * Click "Finish"
    
Next create a plug-in for the UI side:

* Start the plug-in wizard via File->New->Plug-in Project

* On the first page of the wizard enter `org.databinding.example.frontend` as the name

* On the second page:

    * Select "Generate an activator, a Java class that controls the plug-in's life cycle"
    * Select "This plug-in will make contributions to the UI"
    * Select "Yes" for "Would you like to create a 3.x rich client application?"
    * Click "Next"
    * Select "RCP application with a view"
    * Click "Finish"

## Creating the Person class (the model)

In the backend plug-in create two new classes, one called `ModelObject` and one called Person.
Enter the following code for the `ModelObject`:
```java
package org.databinding.example.backend;

import java.beans.PropertyChangeListener;
import java.beans.PropertyChangeSupport;

public class ModelObject {
    private final PropertyChangeSupport changeSupport = new PropertyChangeSupport(this);

    public void addPropertyChangeListener(PropertyChangeListener listener) {
        changeSupport.addPropertyChangeListener(listener);
    }

    public void removePropertyChangeListener(PropertyChangeListener listener) {
        changeSupport.removePropertyChangeListener(listener);
    }

    protected void firePropertyChange(String propertyName, Object oldValue,
            Object newValue) {
        changeSupport.firePropertyChange(propertyName, oldValue, newValue);
    }
}
```
The ModelObject contains the code that is essential for data-binding. 

Behind the scenes when you create a binding the data-binding framework automatically calls `addPropertyChangeListener` for the UI widget being bound 
(not strictly true - it is a bean object that is associated with the widget). The `removePropertyChangeListener` is called when the widget binding is disposed, e.g. when the GUI is closed.

The `firePropertyChange` method is used to inform the listeners when the value has changed.
Note: if `oldValue` and `newValue` are the same then the event is not raised.

The Person class is the class that is going to be used as the model the UI binds to. Add the following code:
```java
package org.databinding.example.backend;

public class Person extends ModelObject {
    private String name;
    private int age;
    private String idNumber;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        firePropertyChange("name", this.name, this.name = name);
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        firePropertyChange("age", this.age, this.age = age);
    }
    
    public String getIdNumber() {
        return idNumber;
    }

    public void setIdNumber(String id) {
        firePropertyChange("idNumber", this.idNumber, this.idNumber = id);
    }

    public Person(String name, int age) {
        setName(name);
        setAge(age);
        setIdNumber("0000");
    }
}
```
Whenever a setter is called the `firePropertyChange` is called which informs all the listeners that the value has changed.
Other than that it is a pretty standard Java class.

## Basic data-binding

In the frontend plug-in's MANIFEST.MF add the backend plug-in to the list of dependencies. Also, add the following dependencies:

* `org.eclipse.core.databinding`
* `org.eclipse.core.databinding.beans`
* `org.eclipse.core.databinding.property`
* `org.eclipse.jface.databinding`

Open the View class and change it to the following:
```java
package org.databinding.example.frontend;

import org.databinding.example.backend.Person;
import org.eclipse.swt.SWT;
import org.eclipse.swt.layout.GridData;
import org.eclipse.swt.layout.GridLayout;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.widgets.Text;
import org.eclipse.ui.part.ViewPart;
import org.eclipse.core.databinding.Binding;
import org.eclipse.core.databinding.DataBindingContext;
import org.eclipse.core.databinding.observable.value.IObservableValue;
import org.eclipse.jface.databinding.fieldassist.ControlDecorationSupport;
import org.eclipse.jface.databinding.swt.WidgetProperties;
import org.eclipse.core.databinding.beans.BeanProperties;

public class View extends ViewPart {
    public static final String ID = "org.databinding.example.frontend.view";

    private Person person;
    
    public View() {
        person = new Person("John", 25);
    }	

    public void createPartControl(Composite parent) {
        GridLayout glParent = new GridLayout(2, false);
        glParent.marginHeight = 5;
        glParent.marginWidth = 5;
        glParent.horizontalSpacing = 1;
        glParent.verticalSpacing = 0;
        parent.setLayout(glParent);
        
        Label lblName = new Label(parent, SWT.NONE);
        lblName.setText("Name: ");
        lblName.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, false, false, 1, 1));
        
        Text txtName = new Text(parent, SWT.BORDER);
        GridData gdText = new GridData(SWT.LEFT, SWT.CENTER, true, false, 1, 1);
        gdText.minimumWidth = 100;
        txtName.setLayoutData(gdText);

        Text txtReadName = new Text(parent, SWT.BORDER);
        GridData gdReadText = new GridData(SWT.LEFT, SWT.CENTER, true, false, 1, 1);
        gdReadText.minimumWidth = 100;
        txtReadName.setLayoutData(gdReadText);
        txtReadName.setEditable(false);
        
        Label lblAge = new Label(parent, SWT.NONE);
        lblAge.setText("Age: ");
        lblAge.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, false, false, 1, 1));
        
        Text txtAge = new Text(parent, SWT.BORDER);
        GridData gdAge = new GridData(SWT.LEFT, SWT.CENTER, true, false, 1, 1);
        gdAge.minimumWidth = 100;
        txtAge.setLayoutData(gdAge);
        
        // DATABINDING START
        DataBindingContext ctx = new DataBindingContext();
        
        IObservableValue target = WidgetProperties.text(SWT.Modify).observe(txtName);
        IObservableValue model = BeanProperties.value("name").observe(person);
        ctx.bindValue(target, model); 

        // Bind on one line
        ctx.bindValue(WidgetProperties.text(SWT.Modify)
                .observe(txtReadName), BeanProperties.value("Name").observe(person));
        
        // Use default validation - binding code on one line
        Binding bindValue = ctx.bindValue(WidgetProperties.text(SWT.Modify)
            .observe(txtAge), BeanProperties.value("age").observe(person));
            
        ControlDecorationSupport.create(bindValue, SWT.TOP | SWT.RIGHT);
        // DATABINDING END
    }

    public void setFocus() {

    }
}
```
    
The binding of the name is a simple as it gets; an `IObservableValue` is created for both the widget and the name in the Person class 
and these are bound together in the `DataBindingContext` object.
 
For age, because it is an int it is possible to make the widget show an error message when is contains a value that is not an int 
using `ControlDecorationSupport` as shown.

If the UI is started then it is possible to see the data-binding in action, by using the debugger it is possible to see that the 
`setName` method is called every time a change is made to the widget text, i.e. every time a letter is added or removed.

## Validators

In the previous example, a warning was shown when the age entered was invalid - this is basic validation, it might be that more advanced validation is desired.
For example, it might that we want to ensure a string is only made up of digits.

Create a new class called `NumbersOnlyValidator` and add the following code:
```java
package org.databinding.example.frontend;

import java.util.regex.Pattern;

import org.eclipse.core.databinding.validation.IValidator;
import org.eclipse.core.databinding.validation.ValidationStatus;
import org.eclipse.core.runtime.IStatus;

public class NumbersOnlyValidator implements IValidator {

    private final Pattern numbersOnly = Pattern.compile("\\d*");

    public IStatus validate(Object value) {
        if (value != null && numbersOnly.matcher(value.toString()).matches()) {
            return ValidationStatus.ok();
        }
        return ValidationStatus.error(value + " contains a non-numeric!");
    }
}
```
All custom validators implement `IValidator`. In this example, pattern matching is used to check that the value (in this case a string) contains only digits.
Otherwise it returns an error status.

Now modify View by adding the following directly before DATABINDING END:
```java
Label lblId = new Label(parent, SWT.NONE);
lblId.setText("ID: ");
lblId.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, false, false, 1, 1));

Text txtId = new Text(parent, SWT.BORDER);
GridData gdId = new GridData(SWT.LEFT, SWT.CENTER, true, false, 1, 1);
gdId.minimumWidth = 100;
txtId.setLayoutData(gdId);

IValidator validator = new NumbersOnlyValidator();

UpdateValueStrategy strategy = new UpdateValueStrategy();
strategy.setBeforeSetValidator(validator);
Binding bindValue2 = ctx.bindValue(WidgetProperties.text(SWT.Modify)
        .observe(txtId),
        BeanProperties.value("idNumber").observe(person), strategy,
        null);
ControlDecorationSupport.create(bindValue2, SWT.TOP | SWT.RIGHT); 

```
This code creates a label and text-box for the ID field of the Person class. 
An instance of `NumbersOnlyValidator` is created and added to a `UpdateValueStrategy` object.
The `UpdateValueStrategy` object defines how a data-binding responses to value changes - in this case it calls the validator before setting the value.
The strategy is added as the third parameter of the `bindValue` method call, this is because the third parameter represents the strategy for updating the model based on the widget.
The fourth parameter is null because there is currently no update strategy for updating the widget based on the model (the default is used).

By running this example it can be seen that a warning appears if a non-numeric character is entered for the ID.

## Converters

Converters are similar to validators in that they are used as part of the update strategy; however, they are used to convert either the data from the model or the data send to the model by the widget.
In this example, two converters are created: one to convert the name to upper-case; and, one to convert to lower-case.

Create two new classes called `ToLowerConverter` and `ToUpperConverter`.

Add the following code to `ToLowerConverter`:
```java
package org.databinding.example.frontend;

import org.eclipse.core.databinding.conversion.Converter;

public class ToLowerConverter extends Converter {

    public ToLowerConverter() {
        super(String.class, String.class);
    }

    public Object convert(Object fromObject) {
        return fromObject.toString().toLowerCase();
    }
} 
```
    
Likewise for ToUpperConverter:
```java
package org.databinding.example.frontend;

import org.eclipse.core.databinding.conversion.Converter;

public class ToUpperConverter extends Converter {

    public ToUpperConverter() {
        super(String.class, String.class);
    }

    public Object convert(Object fromObject) {
        return fromObject.toString().toUpperCase();
    }
}

```
Now replace the code between the DATABINDING START and the DATABINDING FINISH with:
```java
DataBindingContext ctx = new DataBindingContext();

UpdateValueStrategy strategy1 = new UpdateValueStrategy();
strategy1.setConverter(new ToLowerConverter());

UpdateValueStrategy strategy2 = new UpdateValueStrategy();
strategy2.setConverter(new ToUpperConverter());

IObservableValue target = WidgetProperties.text(SWT.Modify).observe(txtName);
IObservableValue model = BeanProperties.value("name").observe(person);

// First strategy goes towards the model, second goes towards the widget (target)
ctx.bindValue(target, model, strategy1, strategy2);

```
Note: The data-binding for age has been deleted, so the age text-box will be empty when this is run.

Running this example should show the name in upper-case and it ran through the debugger it can be seen that if the value is modified the `setName` method in Person receives a lower-case string.

## Update strategies

There are other things that can be done with update strategies, in this example the model is only updated when the update button is clicked (unlike in the first example where the person's name changes each time it is modified).

Replace the code between the DATABINDING START and the DATABINDING FINISH with:
```java
final DataBindingContext ctx = new DataBindingContext();

UpdateValueStrategy<Object, String> strategyOnPress = new UpdateValueStrategy<Object, String>(UpdateValueStrategy.POLICY_ON_REQUEST);

IObservableValue target = WidgetProperties.text(SWT.Modify).observe(txtName);
IObservableValue model = BeanProperties.value("name").observe(person);
ctx.bindValue(target, model, strategyOnPress, null);

Button btnUpdate = new Button(parent, SWT.NONE);
btnUpdate.setText("Update");
txtAge.setLayoutData(new GridData(SWT.LEFT, SWT.CENTER, true, false, 1, 1));

btnUpdate.addSelectionListener(new SelectionAdapter() {
    @Override
    public void widgetSelected(SelectionEvent arg0) {
        ctx.updateModels();
    }
});

```
In this example, the Update strategy is initialised with POLICY_ON_REQUEST. This means the updates are only send to the model (the Person object) when told to.
The models are updated when `updateModels` is called by the `DataBindingContext` which in this example is on a button click.

Running this example in the debugger shows that the `setName` method is only called when the button is clicked rather than on every modification.

## Binding a Java List to a List Control

Most of this is taken care of by the databinding library via `ListViewer` and `ObservableListContentProvider`. Here is an example of it in action:

```java
ListViewer myViewer = new ListViewer(parent, SWT.BORDER | SWT.V_SCROLL | SWT.SINGLE);
ObservableListContentProvider contentProvider = new ObservableListContentProvider();
myViewer.setContentProvider(contentProvider);
myViewer.setInput(BeanProperties.list("names").observe(myViewModel));

// To get the List Control itself - it is org.eclipse.swt.widget.List not a standard Java List
List myList = myViewer.getList();
```

`ListViewer` is a wrapper around the List control that provides extra functionality and `ObservableListContentProvider` make the databinding work.