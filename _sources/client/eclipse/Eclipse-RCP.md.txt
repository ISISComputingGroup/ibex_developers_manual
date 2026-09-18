# Eclipse RCP

We have two books which should serve as a reasonable introduction to the Eclipse RCP platform: 'Eclipse Rich Client Platform' by McAffer, Lemieux and Aniszczyk, and 'Eclipse 4 Application Development' by Vogel. Most of the contents of the latter book can be found on the Vogella website along with a large number of additional Eclipse RCP and JFace tutorials.

### E4 and compatibility views (e.g. `org.eclipse.ui.console`)

Although we run an E4 product, we are able to load E3-style plugins via the eclipse compatibility layer. However, [any UI element referred to via the compatibility layer must be defined as a shared element in the client E4XMI, not defined in a snippet](https://www.eclipse.org/forums/index.php/t/358552/) as this does not work correctly with certain UI actions - for example, resetting layouts.