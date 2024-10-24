With the move to using GitHub V2 projects a new method of automation ws required.

This is achieved using the application forked in https://github.com/ISISComputingGroup/board-automation-app
(Note this is a fork from an organisation related to one of the developers at the time, as organisation level access is required, and rather than develop and troubleshoot in this organisation, a simpler system was considered wise.)

## What this application does at a 'user' level
Note that this is based on our PI boards, which undertake some automation themselves. The term `status` below indicates things such as the column headings on the Current Sprint Board.

If you add a `proposal` label to an issue in one of the included repos then it will be added to the PI and assigned to the next sprint with a `backlog` status
If you add an `added during sprint label` it will be added to the PI and assigned to the current sprint. No status is auto assigned here, so if the status labels are applied first then this might not appear on the board automatically.
If you add an `in progress`, `impeded`, or `review` label it will update the status to match.
If you add a `rework` label it will apply a `Backlog` status ready to be picked up again.
If you move things between columns on the board, it will update the labels applied, according to the following:

```
from backlog to in progress: add in progress label
from backlog to impeded: add impeded label
from backlog to review: add review label
from backlog to done: do nothing
from in progress to backlog: remove in progress label
from in progress to impeded: remove in progress label, add impeded label
from in progress to review: remove in progress label, add review label
from in progress to done: remove in progress label
from impeded to backlog: remove impeded label
from impeded to in progress: remove impeded label, add in progress label
from impeded to review: remove impeded label, add review label
from impeded to done: remove impeded label
from review to backlog: remove review and under review labels, add rework label
from review to in progress: remove review and under review labels, add in progress and rework labels
from review to impeded: remove review and under review labels, add impeded label
from review to done: remove review and under review labels
```

## Adding a new repository in the organisation to be watched by this application
To ensure all aspects of this application work on the repository being considered, ensure that the following labels exist in the repository:
* proposal
* added during sprint
* in progress
* impeded
* review
* under review

Add the repository to the list in organisation settings > GitHub Apps > ibex-git-project-automation > configure

## How this application is structured and what the code does

## Installing/Updating the application whilst JSON Bourne is in use

## Installing the application on a host

## Updating the application

## Installing the application to the organisation
