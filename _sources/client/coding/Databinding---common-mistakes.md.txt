# Databinding - common mistakes

Start with [An introduction to databinding](Databinding) if you are new to this.

### Missing getter or setter (or incorrectly named)

The getter and setters (if the value can be set from the UI) must exist and be named correctly. For example: `getName` and `setName` for `BeanProperties.value("name")`.

Behind the scenes the databinding library automatically changes the first character to upper-case and then prepends "get" and "set". 

### Incorrectly cased string in binding

With something like the following it is import that the name of the property to bind to is cased correctly:
```java
ctx.bindValue(WidgetProperties.text(SWT.Modify)
            .observe(txtAge), BeanProperties.value("age").observe(person));
```

This assumes there is a getter and setter called `getAge` and `setAge`.

For something like `getFedId` the binding code would look like:

```java
ctx.bindValue(WidgetProperties.text(SWT.Modify)
            .observe(txtId), BeanProperties.value("fedId").observe(person));
```
**The important point to note is the 'f' of "fedId" is lower-case. It will not work if it is upper-case.**

### The getter or setter "silently" throws an exception

If any code in the getter throws an unhandled exception then the binding won't work because the value cannot be read.
If a setter throws an unhandled exception before the firing the property change then the listeners will not receive the change signal. Both result in the binding being broken.

If a binding seems to work intermittently then there might be something in the getter or setter causing this, e.g. an object used in a getter that switches between being null and initialised based on something else.

**The exceptions will appear in the console inside Eclipse and IBEX but won't cause an error pop-up to appear.**

### The binding works but the initial value is not put in the widget

When the binding first happens it will call the getter to set the widget properties to whatever is in the model. If this doesn't happen the getter is probably non-existent or misspent. 