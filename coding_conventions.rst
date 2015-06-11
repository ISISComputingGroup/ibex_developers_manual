=======================================
IBEX GUI Development Coding Conventions
=======================================

Unless stated otherwise below we should follow the standard Java conventions.

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