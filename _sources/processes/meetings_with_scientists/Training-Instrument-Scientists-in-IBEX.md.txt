# Training Instrument Scientists in IBEX

From time-to-time, we run IBEX and genie_python training courses.  This page collects information that you will need to organise and run the IBEX and genie_python train courses.

## When should we run IBEX and genie_python train courses?
There is never an ideal time to run IBEX and genie_python train courses.  Running training courses during cycle is difficult, because scientists are usually heavily involved with their instruments.  Running training courses out of cycle is difficult, because scientists use the opportunity to take holidays, attend conferences, catch up on other work ...  

The best compromise is to run IBEX and genie_python train courses during the shutdown, shortly before the start of a new cycle.  Why shortly before the start of a new cycle?  Because, people tend to forget what they have learned unless they have an opportunity to put it into practice.  So, as a rule of thumb, try to schedule the course 2-3 weeks before the start of cycle.  You could also run the courses during the week before cycle, but you might need this time to make final adjustments to instruments, so try to avoid this time if possible.

Because training has to be synchronised with ISIS cycles, you need to think about planning training sessions well in advance - 3-6 months in advance.

## Recording that a Person would like to attend the next Training Session

We record people who would like to attend the next training session by listing them on a ticket entitled "TRAINING: Invites for next session"

## Training materials

- [Mantid](https://www.mantidproject.org/Documentation)
- [IBEX](/overview/Links-and-Resources)
    - There are various slides at the end of the material: "Reference card", "GUI Reference Card" and "Useful Locations". These are supposed to provide a brief reference of the major IBEX features, GUI elements and a memo sheet for folder locations respectively. Print off a copy of each for each delegate.
- [genie_python](https://github.com/ISISComputingGroup/ibex_user_manual/wiki/genie_python-and-IBEX-%28Introduction%29)

## Planning the IBEX and genie_python training courses
This section summarises the steps you will need to consider when planning the IBEX and genie_python training courses.

### Check with the Mantid team
The Mantid team regularly run a Mantid course and an Introduction to  Python courses.  Check with the Mantid team to discover their plans.  You can often collaborate of training activities.  It is very useful if the Mantid team can deliver the Introduction to  Python course, prior to the genie_python with IBEX course.

### Select a date for the training
As noted above, select a date for the training 2-3 weeks ahead of the cycle.  You may need to select 2 or 3 dates and only make a final decision when you know availability of the venue.  You might also need to book a day or so either side of your chosen date, to allow for set-up and clear-up before/after the course.

Typically we run the introduction as 9:00-12:00, and Introduction to `genie_python` as 13:00-17:00. This has worked well in the past. We have experimented with balancing the time as 9:00-12:30 and 13:00-17:00 but it made the morning feel long and the afternoon feel short.

### Advertise the training course
Tell instrument scientists and visiting scientists of the proposed dates for the training course and invite them to sign up to attend.  Scientists will typically need 2-3 months advance notice, so make sure you tell them early.  Make sure you tell scientists to respond by a cut-off date - otherwise, it can be tricky trying to squeeze people in if they respond only 2-3 days before the course is due to run.
1. During this step check for general training tickets on the backlog because any people who need to be invited will be listed here. 

### Decide which training venue to use
Recent training courses have been presented in R80 (rooms CR16 & CR17) and in the Central Design Facility (CDF) suite in the Atlas Building.  The CDF is a dedicated training and collaborative design facility, operated by RAL Space.  If you wish to use the CDF, you need to book it with RAL Space. The CDF currently has 14 work stations. Historically, attendance has fluctuated between `<50%` and `100%` of those who sign up. It is possible to pair program on the training course. Feedback on this has been mixed so it is best not to overbook courses.

To book the CDF Suite:
* Contact Will Grainger at RAL Space.  Will administers CDF activities.  Tell him which days you'd like to run the training.  Will will tell you if those days are available.
* Contact Chris Gibbins.  Chris is the IT guy for the CDF.  Chris can help you install IBEX and genie_python images on the dedicated PCs in the CDF suite. Chris prefers to have >1 week notice to set up the machines. **If using the CDF suite, it is wise to book the CDF for at least half a day before the training course, so that we have an opportunity to install IBEX on the machines. Otherwise, the room may be in use, preventing installs.**

To use CR16 & CR17 in R80
* Book CR16 & CR17 via Outlook.  These rooms are heavily used, so you need to book early to get the dates you want.
* Contact Facilities IT to arrange to have laptops made available to the training delegates.  You will also need to coordinate with Facilities IT to get IBEX & genie_python installed on each laptop.

To do it remotely
* Ask Chris MS to create some virtual machines and install a training system on them as below
* If you do not have enough VMs then ask users to use IDAAS to log in to DEMO (test that you can do this first). Make sure that you make people aware that this means they may be "fighting" over the same server.
* Contact the participants and let them know how to log in to>  these machines
* Last time we ran remotely we did it in these 4 sessions:
    1. Introduction to IBEX:
        * How to start/stop everything
        * What do the different perspectives do
        * A basic overview of what’s going on behind the scenes
    2. Configurations and Synoptics: 
        * How to create and edit configurations
        * How to create and edit components
        * How to create and edit synoptics
    3. genie_python and Scripting in IBEX: 
        * Basic genie_python commands
        * User and instrument scripts
        * The script server/script generator
    4. Converting between open genie and genie_python: 
        * The major differences between the languages
        * Some example conversions
        * Hands on conversion of a selection of SANS2D user scripts
    
### Review the training course materials
Make sure you review the training course materials.  Have any new features been added to IBEX or genie_python that might require a change to the course content or are their training tickets on the backlog which should be considered?  if so, update the course.  It is a good idea to run through the course materials even if there have been no significant changes - just to re-familiarise yourself with the course contents.

### Send Delegate list to CDF
If you have decided to use the CDF suite, you need to tell RAL Space (i.e. Will Grainger) the names of each of the delegates, so that they can arrange access (e.g. swipe passes) to the Atlas building.  RAL Space need 2-weeks notice to do this.  A simple spreadsheet naming each delegate, their e-mail and indicating if the individual is a member of ISIS staff is sufficient.

### E-mail course joining instructions to all delegates
1-2 weeks before the training course is due to run, send an e-mail to all delegates, telling them how to join the course.  Make sure you tell them: 
   * where the course is being held (building, room number)
   * which day(s) the course is running
   * start time, finish time (e.g. if the course is due to start at 9:00AM, tell delegates to arrive at 8:45AM, so that the inevitable late-comers don't disrupt things too much).
   * any other joining instructions (e.g. who to call if they get lost)

### Set up and check the venue & facilities

#### General

- At least a week before the course, book any tea or coffee requirements with catering.  Start navigating from the [Catering page](https://staff.stfc.ac.uk/core/catering/Pages/default.aspx) on the staff intranet site to plan catering.  
This will lead you to the web-site of the [current catering franchise holder](https://www.ralcatering.com/), from where you can place an order.
Typically we book:
    - Coffee/tea (80%/20%) for 9am and 1pm. Usually we include some biscuits and a bottle of water
    - We typically don't book lunch since most people leave to do other things over the break. 
    - You will need a project code to book with catering. Ask one of the managers (e.g. Freddie Akeroyd) to provide one if you need it.
- A day or two before the course runs, visit the venue to make sure everything is ready.  You do not want to be trying to sort out problems 5 minutes before the course is due to start.  Things to check are:
   * are the desks arranged as you want them?
   * are the audio-visual system (e.g. projector) working correctly?
   * are the laptops/workstations properly setup and working?

#### CDF specific

The workstations at the CDF are generated by cloning a template machine. The source machine will need setting up a few days before to allow time for cloning. Contact Chris Gibbins a week before the training course to arrange a suitable time. The template machine will need the following software installed:

- [MySQL](https://www.mysql.com/downloads/)
    - Visual c++ redistributable. MySQL may manage to install this itself. Otherwise you'll need to download and install it manually. Be sure to get the architecture that matches MySQL (presumably 64-bit)
- [Notepad++](https://notepad-plus-plus.org/)
- [Java](https://java.com/en/download/)
- [Git](https://git-scm.com/download/win)
- IBEX (server + client)
- [Mantid](http://download.mantidproject.org/) (if appropriate)
- [Mantid training data](https://sourceforge.net/projects/mantid/files/Sample%20Data/TrainingCourseData.zip/download)
- IBEX training configurations
    - Clone using `git clone http://spudulike@control-svcs.isis.cclrc.ac.uk/gitroot/instconfigs/inst.git [MACHINE_NAME]`
    - Switch to branch `NDXTRAIN`

Before cloning the machine, it is helpful to apply the following settings to avoid having to do it individually:

- Set the DAE to use appropriate TCB, wiring, spectra and detector tables from the configs. Verify you can start a run on the base machine
- Set notepad++ to [replace tabs with spaces](https://stackoverflow.com/questions/455037/convert-tabs-to-spaces-in-notepad)
- Create desktop shortcuts for IBEX client + server

The following changes should be applied to each of the workstations individually:

- Change the resolution from 4K to 1080p
- Rename the instrument config folder in `C:\Instrument\Settings\config` to match the machine name
- Rename the `init_inst_name.py` file in `C:\Instrument\Settings\config\[machine name]\Python\inst` to match the instrument name
- Delete the `.settings` directory in `C:\Instrument\Apps\Client\configuration`. This will empty the IBEX preference store and notably make sure it starts up pointing at the local instrument rather than the machine it was cloned from.
- Change the PV prefixes on the PVs associated with the Eurotherm component in the training synoptic to match each training machine
- Make sure you can successfully start a run
- Make sure that you can successfully start a scripting session
- Stop the IBEX server (else it won't work properly for the next person who logs in)

We may be able to automate all of those steps. For the time being the first three can be accomplished via a script. The following was a non-generic script that I used for the January 2018 training. I haven't refined it yet in anticipation that we can do something more comprehensive with AutoIt+Python in the future.

```
import shutil
import os
import socket


def delete_stored_gui_settings():
    shutil.rmtree(os.path.join("C:\\", "Instrument", "Apps", "Client", "configuration", ".settings"))


def rename_config_folder():
    root_config_folder = os.path.join("C:\\", "Instrument", "Settings", "config")
    possible_config_folders = [os.path.join(root_config_folder, "DESKTOP-NP89I4S"),
                               os.path.join(root_config_folder, "DESKTOP-NT4N3KQ")]
    config_folder = [p for p in possible_config_folders if os.path.exists(p)][0]
    shutil.move(config_folder, os.path.join(root_config_folder, socket.gethostname()))


def rename_script_module_initializer():
    script_folder = os.path.join("C:\\", "Instrument", "Settings", "config", socket.gethostname(), "Python")
    files_to_delete = [
        os.path.join(script_folder, "init_desktoc9.py"),
        os.path.join(script_folder, "init_deskto24.py"),
        os.path.join(script_folder, "init_desktoc9.pyc"),
        os.path.join(script_folder, "init_deskto24.pyc"),
    ]
    for f in files_to_delete:
        if os.path.exists(f):
            os.remove(f)
    possible_init_paths = [os.path.join(script_folder, "init_desktop_np89i4s.py"),
                           os.path.join(script_folder, "init_desktop_nt4n3kq.py")]
    init_path = [p for p in possible_init_paths if os.path.exists(p)][0]
    shutil.move(init_path, os.path.join(script_folder, "init_{}.py".format(socket.gethostname().lower())))


delete_stored_gui_settings()
rename_config_folder()
rename_script_module_initializer()
```

