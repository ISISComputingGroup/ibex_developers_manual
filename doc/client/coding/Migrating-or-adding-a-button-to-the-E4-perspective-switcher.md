# Adding a button to the E4 Perspective switcher

## Migrating an E3 perspective to E4

1. Open the Application.e4xmi from `uk.ac.stfc.isis.ibex.e4.client`
1. Go to `Snippets`
1. Click `Add` to add a new perspective
1. Set the perspective up using an existing migrated perspective as a template
    1. Set a sensible ID
    1. Give it a label
    1. If you want your perspective to be invisible toggle the visible checkbox
    1. Set the icon
    1. Add controls. This should be a hierarchy of part sash containers. You can see how it should be set up from the existing perspectives. Don't forget to set the container data where appropriate; it sets the relative size of sibling components.
1. Add the perspective-specific parts
    1. In the alarms perspective, you'll see one part in the final part sash container called alarms. Do the same thing in your new perspective, but give it an appropriate name
    1. Change the ID of your new part to the ID of the view class you want the perspective to open
1. Add the dependency of the view you've added to the `plugin.xml` in the `...e4.client` plugin
1. Add the new dependency to `...feature.xml` (in `uk.ac.stfc.isis.ibex.feature.base`)
1. Synchronize `ibex.product` (in `...e4.client.product`)
1. Open IBEX
1. Check the new perspective scales appropriately and change the layout accordingly if needed

## Creating a brand new E4 perspective

Making a brand new E4 perspective would probably look similar to the steps above, minus the E3 steps. However, a new E4 perspective has yet to been attempted.

## Hiding Perspectives

Perspectives can be hidden by adding perspective IDs to the Eclipse preference store at the preference key `uk.ac.stfc.isis.ibex.preferences/perspectives_not_shown` (at `/uk.ac.stfc.isis.ibex.e4.client/plugin_customization.ini`). e.g. 

```
uk.ac.stfc.isis.ibex.preferences/perspectives_not_shown=uk.ac.stfc.isis.ibex.client.e4.product.perspective.scriptGenerator
```
Note: Multiple perspectives can be hidden using a comma separated list of perspective IDs. e.g.

```
uk.ac.stfc.isis.ibex.preferences/perspectives_not_shown=uk.ac.stfc.isis.ibex.client.e4.product.perspective.scriptGenerator,uk.ac.stfc.isis.ibex.client.e4.product.perspective.dae
```