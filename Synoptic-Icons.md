> [Wiki](Home) > [The GUI](The-GUI) > [Other](GUI-Other) > Synoptic icons

# Creating Icons
(Note: this page will not discuss the creative process involved in creating an icon)

### Tools

[GIMP](http://www.gimp.org/) is a powerful, free image editing program that can be used to create icons for Synoptics.

(An alternative is [Inkscape](https://inkscape.org/) which is a vector graphics editor and possibly more suited to icon creation and editing.  Please see the [Basic Tutorial](https://inkscape.org/en/doc/tutorials/basic/tutorial-basic.html) for an introduction to the program.)

First, create a new file and find the "Layers"-window in the GIMP taskbar under `Windows > Dockable Dialogs > Layers`. Delete the background layer from the list. Create a new layer by right-clicking the layers window or from the `Layer` tab in the taskbar. Make sure the Layer Fill Type is set to "Transparency". Draw your Icon on this layer.

You can specify which icon should appear in the synoptic with the file `uk.ac.stfc.isis.ibex.ui.devicescreens/ComponentIcons.java`.  The case name in the switch statement should match the `<type>` key for the device in `opi_info.xml`.  e.g. `<type>PUMP</type>` and ```case PUMP:
                return "pump";``` where the returned value is the icon's base filename.

If you need to add new icons for the synoptic, these are under `uk.ac.stfc.isis.ibex.ui.devicescreens/icons` (both full size icons for the actual synoptic and thumbnails for the synoptic editor and device screens perspective). Please follow these guidelines when creating new synoptic icons (e.g. `icon.png`) and ensure thumbnail icons have a `_tb` suffix (e.g., `icon_tb.png`).

### Icon Conventions
* Thumbnail icon image files have height of 28px and a width of 28px including margins.
* Synoptic icon image files have a maximum height of 100px and a width of (icon width + 20px) including margins.
* The icon image should be a `.png` file.
* The fill colour of the icons is `0xAAA19C`. The border colour is black.
* The icon background should be transparent.

### Centred Icons
To centre your new (or a pre-existing) icon, open the file in gimp and follow these steps:
* Crop the image with `Image > Autocrop Image`. This removes all empty space around the Icon.
* The icon should now have a height of 100px or less. If this is not the case, scale it down under `Image > Scale Image`
* Open `Image > Canvas Size`. Unlink Width and Height by clicking the little chain next to the number entry fields.
* Set Height to 100px and width to (current width) + 20px.
* Click on `center` and finish by clicking `Resize`. The icon should now sit right in the centre of the canvas. and have some margins around it.

### Non-Centred Icons
If you don't want the icon to be centred on the beamline in the synoptics window: 
* Click and drag on the ruler above the canvas to produce a guideline. Position it at a vertical position of 50 px (see ruler on left). This simulates where the beamline will appear relative to the icon in the synoptics view.
* Select and move your Icon in the desired vertical position.
