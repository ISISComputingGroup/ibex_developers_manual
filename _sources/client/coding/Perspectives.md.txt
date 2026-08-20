# Perspectives

:::{note}
If you are implementing a brand new perspective, first follow the
[adding a plugin or feature guide](Adding-a-Plugin-or-Feature-to-Maven-Build) to define the new plugin.
:::

## Defining a perspective

Perspectives are defined in `base\uk.ac.stfc.isis.ibex.e4.client\Application.e4xmi`, under the "snippets" section.

The `Application.e4xmi` file controls how a perspective is laid out. This is done using a hierarchy of:
- **Part Sash Containers**: these allow multiple items to appear side-by-side, either vertically or horizontally.
- **Part Stacks**: these allow multiple items to appear in a tabbed view.
- **Parts**: these are an individual view. Use a part if the view appears in only one perspective (for example, a DAE
configuration view, which only appears in the DAE perspective).
- **Placeholders**: an individual view which is shared between multiple perspectives (for example the blocks view).

Part stacks can be defined as "not rendered" in the `Application.e4xmi` - this means they will not be shown at first,
but the perspective still defines where the part will appear once some other code renders it. Example of this are:
- The plotting view in the scripting perspective, which is only rendered after plotting using matplotlib in the
scripting console.
- OPIs in the device screens perspective, which are only rendered once a device screen is clicked on.

## Keyboard shortcuts

Keyboard shortcuts for changing perspective are also defined in `base\uk.ac.stfc.isis.ibex.e4.client\Application.e4xmi`,
under "Binding Tables". These key bindings are linked to commands, which then execute handlers. Both commands and
handlers are also specified in the `Application.e4xmi`.

## Icons

Find or create a PNG icon which is appropriately sized (`24x24` pixels). The icon path is specified in the
`Application.e4xmi` file along with the other properties of a perspective.

:::{important}
If you find an icon online, you must ensure it is licensed appropriately and added to the
[list of icon licenses](https://github.com/ISISComputingGroup/ibex_gui/blob/master/base/uk.ac.stfc.isis.ibex.ui.help/resources/iconlicences.txt)
which appears using help -> "icon licenses" in the IBEX GUI.
:::

## Hiding Perspectives

Perspectives can be hidden using the preferences -> "select visible perspectives" menu in IBEX. These settings can be
changed either locally, for a given client session, or remotely, where the set of perspectives to show by default will
be stored by the IBEX server. If you cannot set remote perspectives, you probably do not have write access to the
instrument.

## Troubleshooting

If a new perspective is not being shown in the switcher during development, the GUI may have cached a set of
perspectives in its workspace. To clear this, go to run -> "run configurations" in Eclipse, and
ensure that the "clear workspace" option is selected for the IBEX product.
