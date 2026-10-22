# Program Increment Planning

This meeting covers the overarching themes for the next few months. It will usually be held in the week or so before the first sprint of the Program Increment (PI) in question. This is an opportunity to ensure the whole team are aware of the more mid term goals of the team.

A PI will consist of the sprints between this major release and the next one, these will typically be in January/February and August/September.

In the first sprint in a PI we will create and deploy a release of the work we have just completed. The deploy should occur so that the instrument scientists have at least two full weeks of testing time available before the start of the user cycle. In the third sprint we will undertake dependency updates.

This meeting will usually be chaired by the project manager for the group or other senior team member.

### Preparation

There is a [template](https://github.com/orgs/ISISComputingGroup/projects?query=is%3Aopen+is%3Atemplate) for the PI board into which can be brought the tickets that relate to the work to be undertaken.
Start by using that template to create a project for the coming PI.
Edit the setting to add the sprints to the appropriate field. Assign the pre-populated tickets to the appropriate sprint.
Add the items to be considered in the upcoming PI that are either a significant amount of work, or which the instrument scientists would appreciate visibility of. These can be added as either a link to a ticket in one of the repos, or a note on this board. These will typically have a classification of `Project/Feature`. It is wise to add sub-tickets of these umbrellas as well, as `To do for a Project/Feature`, as if there are dependencies between them they can be assigned to sprints as appropriate.
Items to consider may be carried over from the previous PI, or be new items.
Assign a priority order to the projects and features, and any sub-tickets which have been added so that they can be grouped easily.

### During Meeting

Review the PI about to end, see what is complete and what isn't, and discuss if appropriate.
Ask what has gone well or badly during the PI about to end, as a small retrospective.
Looking to the PI about to start, load each project/feature  from the `Prioritising Table - Projects/Features` tab, so that the aims and purposes of each piece of work can be discussed and agreed. Care should be taken that the details of code and implementation should not be undertaken here too thoroughly.
Where items can be assigned to a specific sprint this should be done. If any priorities are wildly inappropriate that can also be discussed in this meeting, although care should be taken not to become too detailed.

### Extra Notes
#### Preparation = Priority Ordering
Each project/feature should have a number which increments in the style 100, 200, etc. so that the sub-tickets (which could have further sub-tickets) can be numbered 110, 120, 130. If you have anything with more than 9 sub-tickets, or a third layer, increase at the highest level by an order of 10, so that the project would be 1000, the sub-tickets then become 1100, 1110, 1120, 1130 etc. Using this order makes it easier to rearrange, as if item 130 should fit between 110 and 120, simply setting it to 115 will move it to the right place.
After the meeting these numbers can be tidied up appropriately.