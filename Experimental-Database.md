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

## XML Format Example

```
<Experiments>
	<Experiment>
		<PI>
		  <Name>John</Name>
		  <Organisation>Science and Technology Facilities Council</Organisation>
		</PI>
		<Local>
		  <Name>Dr Timothy Charlton</Name>
		  <Organisation />
		</Local>
		<Others />
		<StartDate>2015-03-19T08:00:00Z</StartDate>
		<Duration>1</Duration>
		<RB>1530009</RB>
	  </Experiment>
	<Experiment>
		<PI>
		  <Name>Dr Timothy Charlton</Name>
		  <Organisation>Science and Technology Facilities Council</Organisation>
		</PI>
		<Local>
		  <Name>Dr Timothy Charlton</Name>
		  <Organisation />
		</Local>
		<Others />
		<StartDate>2015-04-19T08:00:00Z</StartDate>
		<Duration>1</Duration>
		<RB>1530008</RB>
	  </Experiment>

	<Experiment>
		<PI>
		  <Name>Dr Timothy Charlton</Name>
		  <Organisation>Science and Technology Facilities Council</Organisation>
		</PI>
		<Local>
		  <Name>A</Name>
		  <Organisation />
		</Local>
		<Others>
		  <User>
		    <Name>New</Name>
		    <Organisation>New Org</Organisation>
		  </User>
		</Others>
		<StartDate>2015-04-29T08:00:00Z</StartDate>
		<Duration>2</Duration>
		<RB>1530010</RB>
	  </Experiment>
	  
 </Experiments>
 
```
