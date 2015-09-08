=======================================
IBEX GUI Development Coding Conventions
=======================================

Unless stated otherwise below we should follow the standard Java conventions where possible.

Code Documentation
------------------

Classes and methods should be documented using the Javadoc syntax. For example:

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

Checkstyle
----------

Code should be run through Checkstyle via Eclipse and corrected (within reason) before being committed.
The Checkstyle plug-in can be installed via the Eclipse Marketplace.

There is a Checkstyle configuration file called checkstyle_config_eclipse.xml in the GUI repository that should be used inside Eclipse.
It is more picky that the one used on Jenkins as it warns about 'magic numbers' and 'Java-docs'.
Our Checkstyle configuration can be chosen in Eclipse via Preferences->Checkstyle

By right-clicking on a file one can tell Checkstyle to check that file.

Warnings that should be fixed where possible:

    * Whitespace warnings (can be auto-fixed, see the Code Formatting section)

    * Missing Javadoc comments (particular the class one)

Warnings that should be reviewed before committing:

    * Magic numbers - if it is related to a GUI layout then ignore, otherwise think about whether to fix it. Unfortunately Checkstyle can be a little overzealous sometimes...

    * Name must match pattern - ignore GUI names that don't match the recommended pattern (e.g. gd_switchToCombo)

Any other warnings can probably be ignored, but feel free to fix them if you want.
    
Checkstyle also has a suppress warning flag that tells it to ignore certain warnings, for example:

.. code::

    @SuppressWarnings({"checkstyle:magicnumber", "checkstyle:localvariablename"})
    public void getSecondsInHours(int hours) {
        int seconds_per_hour = 60 * 60;    // Magic numbers and a variable name that does not conform to the recommended style!
        return hours * seconds_per_hour;
    }

Code Formatting
---------------

For Java use the standard conventions built in to Eclipse. This can be set via Window->Preferences->Java->Code Style->Formatter; the one required is called "Eclipse [built-in]".

An example of what it looks like:

.. code::

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

In Eclipse, a quick way to auto-format the code correctly is to use Ctrl+Shift+F.

Getters and Setters
-------------------

Where possible getters and setters should follow the JavaBeans convention, namely:

    * **Getter** - starts with "get"
    
    * **Boolean Getter** - can start with "is" or "get"
    
    * **Setter** - starts with "set"

For example:

.. code::

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
    
Code Comments
-------------

Comments should have a space between the // and the text, and start with a capital letter::

    // This is a good comment
    
    //this is a bad comment
    
Use Data-binding
----------------

For connecting UI elements to data from the back-end use data-binding. 
It seems that if data-binding and more traditional SWT wiring up is used (e.g. AddPropertyChangeListener) then the data-binding will stop working*, so always using data-binding should avoid this problem.

*This does need more investigation to find out why it occurs