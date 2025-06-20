# GUI Coding Conventions

:::{note}
New conventions should not be added to this document without first being discussed at a 
[code chat](/processes/meetings/Code-Chats-and-Lightning-Talks) or a group code-review session.
:::

## Style Conventions

Unless stated otherwise below, we should follow the standard Java conventions for style where possible.

## Documentation

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
     *
     * @param topping the topping to add
     * @return true if the topping was added
     */
    public boolean addTopping(Topping topping) {
        if (toppingList.size() < MAX_TOPPINGS) {
            toppingList.add(topping);
            return true;
        }
        
        return false;
    }
}
```
For getters, it is acceptable to skip the first sentence and do the following as it saves repetition:
```java
/**
 * @return true if the block is enabled
 */
public boolean getEnabled() {
    return enabled;
}
```

Inline comments should have a space between the // and the text, and start with a capital letter:
```java
// This is a good comment
    
//this is a bad comment
```

## Code formatting

For Java use the standard conventions built in to Eclipse. 

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

## Naming conventions

### General

We use the [standard Java naming conventions](https://www.oracle.com/java/technologies/javase/codeconventions-namingconventions.html):
- Class names are CamelCase and usually nouns, e.g. `FileReader` not `ReadsFile`
- Method names are Mixed Case (also known as Lower CamelCase), e.g. `sayHello`
- Package names are lowercase, e.g. `uk.ac.stfc.isis.dae`
- Variable names are Mixed Case, e.g. `calculateMeanSpeed`
- Constants are uppercase spaced by underscores, e.g. `SECONDS_PER_FORTNIGHT`

### Getters and Setters

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

## Coding Conventions

### GUI code should use a model-view-viewmodel (MVVM) pattern

This maintains a separation between pure GUI code and the back-end. It also makes it easier for us to test our code.
See the [previous GUI Chat slides](/processes/meetings/Code-Chats-and-Lightning-Talks) for more information.

### Use data-binding for GUI items

For connecting UI elements to data from the View Model, prefer to use [databinding](Databinding) where possible.

### Don't mess with finalizers

In Java versions >=9, `finalize` is deprecated and marked for removal from Java. The IBEX checkstyle configuration
is configured to disallow finalizers - this check must not be disabled or overridden.

The remaining options for supported clean-up mechanisms (in preference order) are:
- Implement `AutoCloseable` and use the class in a try-with-resources statement to ensure the relevant resource is closed
- Use a `Closeable` and manually call `close` to ensure the relevant resource is closed
- Refactor to avoid needing to close the resource at all
- Use a *supported* automatic clean-up mechanism such as `PhantomReference` or `Cleaner` only as a last resort.
While these are *better* than finalizers, they still suffer from high complexity and are tricky to get right. 
In particular, it is easy to accidentally create reference loops meaning that objects will never be cleaned.

### Return a empty collection or stream, not null

For methods that return arrays/lists/maps/sets/streams etc. don't return null. It is cleaner to return an empty
instance as the calling code does not need to check for null.

```java
// Avoids this extra check in the caller
if (cars != null && cars.contains("mustang") {
   ...
}
```
See Effective Java Item 43 "Return empty arrays or collections, not nulls"

### Prefer StringBuilder for string concatenation

Using `+` is fine for, say, joining two or three short strings, but it is inefficient for larger numbers of strings and
longer strings. Use `StringBuilder` instead.

See Effective Java Item 51 "Beware the performance of string concatenation"

### Prefer `Optional` over `null`

New APIs should not return null to indicate a missing value. Instead, return an `Optional` wrapping the value which may
not exist. Where external code returns null to indicate a missing value, this should be wrapped in an optional as soon
as reasonable.

To convert a maybe-null value to an optional, use:
```java
String s = null;
Optional<String> stringWhichMightNotExist = Optional.ofNullable(s);
```

To convert an Optional to a maybe-null value, use:
```java
Optional<String> mightNotExist = Optional.empty();
String str = mightNotExist.orElse(null);
```

### Streams

Streams should be used where they make an algorithm clearer.

When using streams, put each operation on its own line.

Good:
```java
public Stream<String> getNames() {
    return getThings()
        .map(thing -> thing.getName())
        .filter(name -> name != "")
        .sorted();
}
```

Bad:
```java
public Stream<String> getNames() {
    return getThings().map(thing -> thing.getName()).filter(name -> name != "").sorted();
}
```
