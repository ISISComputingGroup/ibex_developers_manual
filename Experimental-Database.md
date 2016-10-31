The experimental database keeps track of:

1. experiments (`experiment` table)
1. experiment team members (`experimentteams` table)
1. users in the team  (`user`)
1. roles in the team  (`role`)

The data is loaded from an external XML script.

## Testing

The loading can be tested from the experimental database loader:

`console -M localhost EXPDB`

This has a menu press `M` to see the menu.

Set the experimental data file path with `F` (there are some test files in `ISIS\ExperimentalDatabase\master\DatabaseController\tests\testxml.xml`)

And update with `U`.


