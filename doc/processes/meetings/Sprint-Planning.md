# Sprint Planning

Sprint planning is the process where we decide what will appear in next sprint, and make a judgement call on the size/complexity of the piece of work. This is undertaken in two meetings, in the first, the prioritisation meeting, the person currently responsible for managing our core work, other members of the leadership team, and anyone else who is interested, will assign tickets to being high/medium/low priority.

During a sizing meeting, the second meeting, the whole group will ensure that tickets are suitably clear in the expectations and assign a size of small, medium, large, or extra-large. Note that these have no other references except to themselves as sizes, and there is no equivalency table in existence to time, it is the amount of work compared to each other that is being considered.

All team members should add the proposal label to tickets that should be considered whenever they are aware of this. These will automatically be added to the appropriate Program Increment project in GitHub.

### Befor the prioritisation meeting
1. Check that any proposed tickets are in the appropriate sprint.
2. Make sure that any tickets needed for that sprint are listed within it.

### During the prioritisation meeting
1. With the search based only for the next sprint:
    1. For each ticket on the board:
       1. Check the ticket, and agree whether it is needed now, or whether it should be delayed.
       2. If it is needed now, or need not be delayed, assign it to `High`, `Medium`, or `Low` as appropriate.
       3. If it is not needed, assign it to a future sprint in the PI, or to the next PI as appropriate.
2. With the search set to look at the backlog for the current sprint:
   1. For each ticket on the board:
      1. Check whehter or not the ticket is still needed, or if it should be delayed.
      2. If it is still needed, check that the `High`, `Medium`, or `Low` assignment is still appropriate.
      3. If it is not needed, assign it to a future sprint in the PI, or to the next PI as appropriate.
3. With the search set for both the current and next sprint, make sure that the number of tickets being put into the new backlog is appropriate, and that the relative priorities are still appropriate

### During the sizing meeting
1. Post a link to the planning poker site to the chat. This information is available in the `Planning` tab on the IBEX Developers MS Teams `announce` channel.
1. For each ticket on the board:
    1. Read the ticket and understand the issue
    1. Make sure the acceptance criteria makes sense
    1. Estimate the ticket using planning poker site, discuss, agree, and record that value via the label and/or project field. There is no need to do this if it already has a size.

### After the sizing meeting
1. For tickets being added, remove proposal labels and make sure that size labels and fields match. This is most readily done using the table views.
2. Update the sprint value for every item in the sprint that has just finished to be the sprint just starting, for every column except `Done`.
3. Move the search filters on the planning and current sprint table and boards to the next sprint value.
4. Using the `Change Sprint` button on the appropriate automation tool page (the link to that page is available in the `Planning` tab on the IBEX Developers MS Teams `announce` channel) move the automation tool into the new sprint. You can verify this by reloading the daily `burndown` chart.

These activities are done through the current Program Increment (PI) project on GitHub, unless otherwise stated.
