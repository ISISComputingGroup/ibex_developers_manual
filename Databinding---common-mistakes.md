Start with [An introduction to databinding](An-Introduction-to-Databinding) if you are new to this.

### Incorrectly cased string in binding

With something like the following it is import that the name of the property to bind to is cased correctly:
```java
ctx.bindValue(WidgetProperties.text(SWT.Modify)
            .observe(txtAge), BeanProperties.value("age").observe(person));```