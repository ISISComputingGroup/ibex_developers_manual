From time-to-time, we run IBEX and genie_python training courses.  This page collects information that you will need to organise and run the IBEX and genie_python train courses.

## When should we run IBEX and genie_python train courses?
There is never an ideal time to run IBEX and genie_python train courses.  Running training courses during cycle is difficult, because scientists are usually heavily involved with their instruments.  Running training courses out of cycle is difficult, because scientists use the opportunity to take holidays, attend conferences, catch up on other work ...  

The best compromise is to run IBEX and genie_python train courses during the shutdown, shortly before the start of a new cycle.  Why shortly before the start of a new cycle?  Because, people tend to forget what they have learned unless they have an opportunity to put it into practice.  So, as a rule of thumb, try to schedule the course 2-3 weeks before the start of cycle.  You could also run the courses during the week before cycle, but you might need this time to make final adjustments to instruments, so try to avoid this time if possible.

Because training has to be synchronised with ISIS cycles, you need to think about planning training sessions well in advance - 3-6 months in advance.

## Planning the IBEX and genie_python training courses
This section summarises the steps you will need to consider when planning the IBEX and genie_python training courses.
### Check with the Mantid team
The Mantid team regularly run a Mantid course and an Introduction to  Python courses.  Check with the Mantid team to discover their plans.  You can often collaborate of training activities.  It is very useful if the Mantid team can deliver the Introduction to  Python course, prior to the genie_python with IBEX course.
### Select a date for the training
As noted above, select a date for the training 2-3 weeks ahead of the cycle.  You may need to select 2 or 3 dates and only make a final decision when you know availability of the venue.  You might also need to book a day or so either side of your chosen date, to allow for set-up and clear-up before/after the course.
### Advertise the training course
Tell instrument scientists and visiting scientists of the proposed dates for the training course and invite them to sign up to attend.  Scientists will typically need 2-3 months advance notice, so make sure you tell them early.  Make sure you tell scientists to respond by a cut-off date - otherwise, it can be tricky trying to squeeze people in if they respond only 2-3 days before the course is due to run.
### Decide which training venue to use
Recent training courses have been presented in R80 (rooms CR16 & CR17) and in the Central Design Facility (CDF) suite in the Atlas Building.  The CDF is a dedicated training and collaborative design facility, operated by RAL Space.  If you wish to use the CDF, you need to book it with RAL Space.

To book the CDF Suite:
* Contact Andrew Caldwell at RAL Space.  Andrew administers CDF activities.  Tell him which days you'd like to run the training.  Andrew will tell you if those days are available.
* Contact Chris Gibbins.  Chris is the IT guy for the CDF.  Chris can help you install IBEX and genie_python images on the dedicated PCs in the CDF suite.

To use CR16 & CR17 in R80
* Book CR16 & CR17 via Outlook.  These rooms are heavily used, so you need to book early to get the dates you want.
* Contact Facilities IT to arrange to have laptops made available to the training delegates.  You will also need to coordinate with Facilities IT to get IBEX & genie_python installed on each laptop.

### Review the training course materials
Make sure you review the training course materials.  Have any new features been added to IBEX or genie_python that might require a change to the course content?  if so, update the course.  It is a good idea to run through the course materials even if there have been no significant changes - just to re-familiarise yourself with the course contents.

### Send Delegate list to CDF
If you have decided to use the CDF suite, you need to tell RAL Space (i.e. Andrew Caldwell) the names of each of the delegates, so that they can arrange access (e.g. swipe passes) to the Atlas building.  RAL Space need 2-weeks notice to do this.  A simple spreadsheet naming each delegate, their e-mail and indicating if the individual is a member of ISIS staff is sufficient.

### E-mail course joining instructions to all delegates
1-2 weeks before the training course is due to run, send an e-mail to all delegates, telling them how to join the course.  Make sure you tell them: 
   * where the course is being held (building, room number)
   * which day(s) the course is running
   * start time, finish time (e.g. if the course is due to start at 9:00AM, tell delegates to arrive at 8:45AM, so that the inevitable late-comers don't disrupt things too much).
   * any other joining instructions (e.g. who to call if they get lost)

### Set up and check the venue & facilities

#### General

A day or two before the course runs, visit the venue to make sure everything is ready.  You do not want to be trying to sort out problems 5 minutes before the course is due to start.  Things to check are:
   * are the desks arranged as you want them?
   * are the audio-visual system (e.g. projector) working correctly?
   * are the laptops/workstations properly setup and working?

#### CDF specific

The workstations at the CDF are generated by cloning a template machine. The source machine will need setting up a few days before to allow time for cloning. Contact Chris Gibbins a week before the training course to arrange a suitable time. The template machine will need the following software installed:

- [MySQL](https://www.mysql.com/downloads/)
- [Notepad++](https://notepad-plus-plus.org/)
- [Java](https://java.com/en/download/)
- [Git](https://git-scm.com/download/win)
- IBEX (server + client)
- [Mantid](http://download.mantidproject.org/) (if appropriate)
- [Mantid training data](https://sourceforge.net/projects/mantid/files/Sample%20Data/TrainingCourseData.zip/download)
- IBEX training configurations (available via a clone of the user manual: https://github.com/ISISComputingGroup/ibex_user_manual.git)

The following changes should be applied to each of the workstations individually:

- Change the resolution from 4K to 1080p
- Rename the instrument config folder in `C:\Instrument\Settings\config` to match the machine name
- Rename the `init_inst_name.py` file in `C:\Instrument\Settings\config\[machine name]\Python\inst` to match the instrument name
- Start the IBEX server and switch to the local instrument
