> [Wiki](Home) > [The GUI](The-GUI) > [Coding](GUI-Coding) > Converting to New Style Tips and Gotchas

# Converting to the new style: tips and gotchas
These are things to keep in mind when converting an existing OPI from the old style to the new one:

* Don't just rely on visual checking of the OPI. Look over the full list of template properties for each widget type. Pay particular attention to fonts and colours. There is a script in `/ibex_gui/base/uk.ac.stfc.isis.ibex.opis/` that automatically checks these properties (along with some others) and produces a report for a given OPI. You can use this in addition to visual checking to ensure your OPI is valid under the new style.
* When copying the properties of a widget to another, it is VERY easy to miss out on things such as Actions, Rules, Scripts, Limits, etc. Missing properties will alter the behaviour of the widget! The **safest option** is to take an existing widget and just change all its colours/fonts/size properties to match those in the template opi.
* You can select multiple widgets of the same type and change their properties in one go! (Use with care: don't change behavioural properties!)
* Different widget type (**don't miss properties** when converting!): many old style OPIs use the Native Text widget for labels and titles. In the template we only use Labels: Native Text doesn't seem to offer any advantage apart from a prettier border (which we rarely use) and prettier tooltip, and it has the disadvantage that text is selectable with a flashing cursor, which seems to indicate the text is editable when it's not.
* Different widget type (**don't miss properties** when converting!): the template uses Native Buttons instead of normal Action Buttons, so they automatically change colour when selecting/hovering over them. They also look more consistent with combo boxes.
* Please check the OPI against [colour blindness design guidelines](Designing-for-Colour-Blindness); in particular, review line styles in graphs.

