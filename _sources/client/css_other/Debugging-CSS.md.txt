# Debugging CSS Views

Sometimes we find issues in our code that originate from CSS. This page originates from [ticket #1206](https://github.com/ISISComputingGroup/IBEX/issues/1206) and some of the resources that were used to analyse the problem. This page may grow owing to future issues; please feel free to add to it.

## Source inspection within ECLIPSE

Note that whilst in ECLIPSE debug mode, you should be able to see most of the source you're accessing via breakpoints and the normal step into, step over commands, including CSS. However, if the source is being loaded via reflection, as is the case in the above issue, you will only be able to see the code at call time, you won't be able to navigate to specific definitions which can be frustrating.

Note that you may have to go through numerous layers of system code for which the source is unavailable. The debug stepping commands will still work, you just need to keep at it until you get to an inspection enabled class.

## Breakpoints

My experience in ECLIPSE is that breakpoints will work in 3rd party CSS code, provided you can inspect the class in question (see above). The one caveat is that you can toggle a breakpoint at a specific line, and even make it conditional, but the breakpoint icon may not appear alongside the code. If you look at the Breakpoints window, it should still appear there, and it should work. So don't worry!

## Source on GitHub

As was the case in the attached issue, we might not be using the most up to date version of CSS. How do you know whether it has been changed in the source repo? Fortunately CSS is all open source. Unfortunately, the repo structure is quite hard to navigate. For instance, the package `org.csstudio.security.ui` is located [here](https://github.com/ControlSystemStudio/cs-studio/tree/master/core/utility/utility-plugins/org.csstudio.security.ui):

`https://github.com/ControlSystemStudio/cs-studio/tree/master/core/utility/utility-plugins/org.csstudio.security.ui`

Owing to efforts to clean up the file structure, it also means many files have moved. The Github `history` option for a file doesn't take that into account. I know of no way then to look at the full file history via Github. You have to do it by cloning the repo and then use the command:

`git log --follow ./path/to/file`

## Source inspection within the file system

If you're trying to figure out what is going on in the code and the limitations on source inspection within ECLIPSE is stopping you, you can always look at the source that you're using directly through the file system. The `.jar` files used can be unzipped with most archiving programs (I use 7Zip). Simply navigate to the package in question and look in the `.source*` jar file. For instance, the source for `org.csstudio.security` on my system is located at:

`C:\Instrument\Dev\workspace\.metadata\.plugins\org.eclipse.pde.core\.bundle_pool\plugins\org.csstudio.security.source_1.1.0.20140923-1503.jar\`

## Plugin customisation

Note that many of the CSS plugins use some degree of customization. This is set in the file `plugin_customization.ini`. For me it's located at:

`C:\Instrument\Dev\ibex_gui\base\uk.ac.stfc.isis.ibex.product\plugin_customization.ini`

Packages with customization options should contain a `*.prefs` file defining the available options.

