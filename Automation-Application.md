With the move to using GitHub V2 projects a new method of automation ws required.

This is achieved using the application forked in https://github.com/ISISComputingGroup/board-automation-app
(Note this is a fork from an organisation related to one of the developers at the time, as organisation level access is required, and rather than develop and troubleshoot in this organisation, a simpler system was considered wise.)
As well as automating items in relation to project management, this also displays a burndown chart.

# Automation
<details>
<summary>What this application does at a 'user' level</summary>
Note that this is based on our PI boards, which undertake some automation themselves. The term `status` below indicates things such as the column headings on the Current Sprint Board.

If you add a `proposal` label to an issue in one of the included repos then it will be added to the PI and assigned to the next sprint with a `backlog` status
If you add an `added during sprint label` it will be added to the PI and assigned to the current sprint. No status is auto assigned here, so if the status labels are applied first then this might not appear on the board automatically.
If you add an `in progress`, `impeded`, or `review` label it will update the status to match.
If you add a `rework` label it will apply a `Backlog` status ready to be picked up again.
If you move things between columns on the board, it will update the labels applied, according to the following:

- from backlog to in progress: add in progress label
- from backlog to impeded: add impeded label
- from backlog to review: add review label
- from backlog to done: do nothing
- from in progress to backlog: remove in progress label
- from in progress to impeded: remove in progress label, add impeded label
- from in progress to review: remove in progress label, add review label
- from in progress to done: remove in progress label
- from impeded to backlog: remove impeded label
- from impeded to in progress: remove impeded label, add in progress label
- from impeded to review: remove impeded label, add review label
- from impeded to done: remove impeded label
- from review to backlog: remove review and under review labels, add rework label
- from review to in progress: remove review and under review labels, add in progress and rework labels
- from review to impeded: remove review and under review labels, add impeded label
- from review to done: remove review and under review labels
</details>
<details>
<summary>Adding a new repository in the organisation to be watched by this application</summary>
To ensure all aspects of this application work on the repository being considered, ensure that the following labels exist in the repository:
* proposal
* added during sprint
* in progress
* impeded
* review
* under review

Add the repository to the list in organisation settings > GitHub Apps > ibex-git-project-automation > configure
</details>
<details>
<summary>Installing the application on a host</summary>

This will start with a pull of the application from GitHub.
The instruction for the confiduration settins are held in the repo, and those instructions should be followed.
Starting the app is all that is needed after that by running `app.py` via python.

Note that this has to use Python 3.10 or higher, and due to constraints on the system deployed to and installing on there, a specific python instance was created, which needs to be used for this. At time of writing, this is Python 3.13, with the following packages installed manually:
- plotly
- numpy
- pandas
- tornado
</details>
<details>
<summary>Updating the application</summary>
This should be as simple as synchronising the fork, and pulling to the server it is installed on.
</details>
<details>
<summary>Installing/Updating the application whilst JSON Bourne is in use</summary>
In order to simplify the addition of this application to the existing eco-system, rather than run proxies it has been designed to run alongside an existing Tornado Application JSON Bourne.

Basic installation and update is the same, but an additional step is needed to ensure both sets of code are run, the contents of the automation application, including the updated python, need to be copied into the JSON Bourne directory, and the contents of `webserver_forJSONBourne.py` should be replaced with the contents of `webserver_forJSONBourne_and_git_automation.py`. Alternatively `start_webserver.bat` could be updated to use `webserver_forJSONBourne_and_git_automation.py` instead of the existing `webserver.py`.
The python made available for the automation application will run JSON Bourne, and `start_webserver.bat` should be updated to use that specific python.

</details>
<details>
<summary>Installing the application to the organisation</summary>
The instructions in the GitHub docs provides a good description of how to [register a GitHub Application](https://docs.github.com/en/apps/creating-github-apps/writing-code-for-a-github-app/building-a-github-app-that-responds-to-webhook-events#register-a-github-app)
</details>

# Burndown Chart
<details>
<summary>What this shows</summary>
This shows a column for each day in a sprint with the number of tickets in each status/column on the current sprint board.
</details>
<details>
<summary>How it is updated</summary>
It is updated each day, the first time someone looks at the page.
</details>