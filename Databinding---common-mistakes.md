Start with [An introduction to databinding](An-Introduction-to-Databinding) if you are new to this.

### Missing getter or setter (or incorrectly named)

The getter and setters (if the value can be set from the UI) must exist and be named correctly. For example: `getName` and `setName` for `BeanProperties.value("name")`.

Behind the scenes the databinding library automatically changes the first character to upper-case and then prepends "get" and "set". 

### Incorrectly cased string in binding

With something like the following it is import that the name of the property to bind to is cased correctly:
```java
ctx.bindValue(WidgetProperties.text(SWT.Modify)
            .observe(txtAge), BeanProperties.value("age").observe(person));
```

This assumes there is a getter and setter called getAge and setAge.

For something like getFedId the binding code would look like:

```java
ctx.bindValue(WidgetProperties.text(SWT.Modify)
            .observe(txtId), BeanProperties.value("fedId").observe(person));
```
**The important point to note is the 'f' of "fedId" is lower-case. It will not work if it is upper-case.**
