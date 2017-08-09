> [Wiki](Home) > [The GUI](The-GUI) > [Coding](GUI-Coding) > Conventions

Contains the style and coding conventions of the IBEX GUI.

# Style Conventions #

Unless stated otherwise below we should follow the standard Java conventions for style where possible.

## Code documentation ##

Classes and public methods should be documented using the Javadoc syntax. For example:

```java
/**
 * A make-your-own pizza.
 *
 * This class allows a custom pizza to be order by the customer.
 * Note: it does not calculate the price.
 */
public class CustomPizza extends Pizza {
    private final static int MAX_TOPPINGS = 6;
    private List<Topping> toppingList;

    /**
     * The default constructor.
     */
    public CustomPizza() {
        toppingList = new ArrayList<Topping>();
    }

    /**
     * Add a topping to the pizza.
     * @param topping the topping to add
     * @return true if the topping was added
     */
    public boolean AddTopping(Topping topping) {
        if (toppingList.size() < MAX_TOPPINGS) {
            toppingList.add(topping);
            return true;
        }
        
        return false;
    }
}
```

## Code formatting ##

For Java use the standard conventions built in to the IBEX developer's version of Eclipse. 

An example of what it looks like:
```java
void foo2() {
    if (true) {
        return;
    }

    if (true) {
        return;
    } else if (false) {
        return;
    } else {
        return;
    }
}
```
In Eclipse, a quick way to auto-format the code correctly is to use Ctrl+Shift+F.

## Code comments ##

Comments should have a space between the // and the text, and start with a capital letter:
```java
// This is a good comment
    
//this is a bad comment
```

## Checkstyle ##

Code should be run through Checkstyle via Eclipse and corrected (within reason) before being committed.
The Checkstyle plug-in is installed as part of the IBEX developer's version of Eclipse.

The Checkstyle configuration file for Eclipse is more picky that the one used on Jenkins as it warns about 'magic numbers' and 'Java-docs'.

By right-clicking on a file one can tell Checkstyle to check that file.

Warnings must be fixed where possible.

Checkstyle has a suppress warning flag that tells it to ignore certain warning; warnings that are allowed to be suppressed are:

* Magic numbers - if it is related to a GUI layout then suppress them.

* Name must match pattern - ignore GUI names that don't match the recommended pattern (e.g. gd_switchToCombo)
    
Suppression example:

```java
@SuppressWarnings({ "checkstyle:magicnumber", "checkstyle:localvariablename" })
public void getSecondsInHours(int hours) {
    int seconds_per_hour = 60 * 60;    // Magic numbers and a bad variable name
    return hours * seconds_per_hour;
}
```
## Naming conventions ##

### General ###

In general we use the standard Java naming conventions, e.g.:

* Class names are CamelCase and usually nouns, e.g. `FileReader` not `ReadsFile`

* Method names are Mixed Case (also known as Lower CamelCase), e.g. `sayHello`

* Package names are lowercase, e.g. `uk.ac.stfc.isis.dae`

* Variable names are Mixed Case, e.g. `calculateMeanSpeed`

* Constants are uppercase spaced by underscores, e.g. `SECONDS_PER_FORTNIGHT`

### Getters and Setters ###

Getters and Setters should follow the JavaBeans convention, namely:

* **Getter** - starts with "get"
    
* **Boolean Getter** - can start with "is" or "get"
    
* **Setter** - starts with "set"

For example:
```java
class Point {
    private double x;
    private double y;
    private boolean visible;
    
    public Point(double x, double y) {
        this.x = x;
        this.y = y;
        this.visible = true;
    }
    
    public double getX() { return x; }
    public void setX(double x) { this.x = x; }

    public double getY() { return y; } 
    public void setY(double y) { this.y = y; }
    
    public boolean isVisible { return visible; }
    public void setVisible(boolean visible) { this.visible = visible; }
}
```    

# Coding Conventions and Guidelines #

A mix of IBEX specific and general Java coding conventions and guidelines.

### GUI code must use a View Model ###

This maintains a separation between pure GUI code and the back-end. It also makes it easier for us to test our code.
See the previous GUI Chat slides for more information.

Some legacy code does not have a View Model, this is on the list to fix.

### Use data-binding for GUI items ###

For connecting UI elements to data from the View Model use data-binding. 
It seems that if a  mix of data-binding and more traditional SWT wiring up is used (e.g. AddPropertyChangeListener) then the data-binding will stop working*, so always using data-binding should avoid this problem.

*This does need more investigation to find out why it occurs.

### Single Responsibility Principle (SRP) ###
Every class should have a single responsibility: it should have a single purpose in the system, and there should be one reason to change it.

### Avoid god classes ###
This somewhat reiterates what was stated in the SRP - usually a class should only be responsible for one thing.
A class with many methods and many responsibilities is usually a bad thing.

### Avoid long methods ###
Methods that are long can be difficult to understand for other people (or the author six months later). Try to split them out to multiple methods.

### Methods and functions are good ###
Q: How many times should one write the same code before splitting it out into its own method?

A: Once ;)

Using methods/functions makes code easier to write, read and test. There is no lower limit to how short a method can be if it helps with overall comprehension.

### Don't Repeat Yourself (DRY) ###
Repeated code is bad!
Repeated code is bad!

Break it out into a separate method or class.
Break it out into a separate method or class.

### Don't mess with finalizers ###
It is extremely rare to need to override Object.finalize.

Google Tip: Don't do it. If you absolutely must, first read and understand Effective Java Item 7, "Avoid Finalizers" very carefully, and then don't do it.

### Return a empty collection, not null ###
For methods that return arrays/lists/maps/sets etc. don't return null. It is cleaner to return an empty instance as the calling code does not need to check for null.

```java
// Avoids this extra check in the caller
if (cars != null && cars.contains("mustang") {
   ...
}
```
See Effective Java Item 43 "Return empty arrays or collections, not nulls"

### Favour interfaces over concrete classes (DIP) ###
Also known as the [Dependency Inversion Principle](https://en.wikipedia.org/wiki/Dependency_inversion_principle):
```
A. High-level modules should not depend on low-level modules. Both should depend on abstractions.
B. Abstractions should not depend on details. Details should depend on abstractions.
```
Makes for more loosely coupled code, and can make unit testing easier.

Easier to explain with an example:

```java
// Without DIP - requires changes to AddressFinder if we decide to use a NoSQL database.
public class AddressFinder {
    private SqlConnection connection;

    public AddressFinder(SqlConnection con) {
        connection = con;
        connection.open();
    }
    
    ...
}
``` 

```java
// With DIP - AddressFinder doesn't need to change if we swap to a NoSQL (if NoSQL implements DbConnection)
public interface DbConnection {
    void open;
    ...
}

public SqlConnection implements DbConnection {
    public void open() {
    ...
    }
}

public class AddressFinder {
    private DbConnection connection;

    public AddressFinder(DbConnection con) {
        connection = con;
        connection.open();
    }
    
    ...
}
```
### Refer to objects by their interfaces ###
Follows on from DIP. It is preferable to have variables and parameters be typed by their interface.

For example:

```java
// Prefer this kind of variable declaration
List<String> name = ArrayList<String>();

// Over this
ArrayList<String> name = ArrayList<String>();

// Prefer this kind of method signature
public List<String> filterListByName(List<String> data) {

// Over this
public ArrayList<String> filterListByName(ArrayList<String> data) {
```

See Effective Java Item 52 "Refer to objects by their interfaces"

### Prefer StringBuilder for string concatenation ###
Using `+` is fine for, say, joining two or three short strings but it is inefficient for larger numbers of strings and longer strings. Use StringBuilder instead.

See Effective Java Item 51 "Beware the performance of string concatenation"


