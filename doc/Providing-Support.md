# Providing Support

There is a long list of things to worry about when you have the support phone or are dealing with a support issue, and this page should provide a starting point to look for guidance on what to do if no one is around.

These pages should be a living document - as people learn things add them to the appropriate place if things change, and you notice, update them. If you are experienced, make sure the rest of us are getting things right and verify what is linked to from here. Just remember, this is a public wiki, so be wary of the detail added.

Don't forget to "Send As" ISIS Experiment Controls in outlook and also cc: ISIS Experiment Controls in the message, that way it will be possible for others to see what has already been discussed. Don't forget to include your name when signing off emails from ISIS Experiment Controls, it's much nicer to deal with a person who is part of a group than an anonymous entity. 

Everyone should start a thread in the "support issues" teams channel for any support work whether that is the emails being dealt with, the calls received, or anything that comes out of people walking into the office.

If remote, make sure you are either on the VPN or accessing a system on-site in some way.

The on call number is `x1763` (as called from a RAL phone, and should be available between 7:00-23:00 7 days a week during cycle.
The email address can be found in the address book as `ISIS Experiment Controls`.

## Contents
- [The types of support](#the-types-of-support)
- [Duties for "first line"](#duties-for-first-line)
- [What does being on call mean?](#what-does-being-on-call-mean)
- [Trouble Shooting](#trouble-shooting)
- [Answering the support phone](#answering-the-support-phone)
- [Basic types of call](#basic-types-of-call)
- [Other Tasks](#other-tasks)

## The types of support
All permanent members of the ISIS Computing Group are expected to be on the support rotas.

Note that being the person on rota means you are responsible for seeing that support items are dealt with. This doesn't mean you have to do them, but you have to make sure they are done.

There is no requirement to change working patterns when on call.

### Some basic support principles

If a scientist/user contacts you directly about an urgent issue, you should politely remind them that there is an on call number, and a generic email, and they will be much more likely to get swifter assistance by calling/emailing it rather than individuals.

If you are working on a problem that you believe has the potential to stop all instruments taking data (e.g. the central beam status is reporting incorrectly or there is a critical bug in a core IBEX component) you should immediately email all instrument scientists using the `ISIS Instrument Scientist` mailing list. You should make them aware of the problem and any workarounds that you have found.

If you encounter an urgent problem that you are really unsure of you can find other team member's numbers in the support phone's contacts list or at `\\isis\shares\ISIS_Experiment_Controls\On Call\Phone Numbers.xlsx`.

### Who is on call when?
The "first line" and on call rotas will be made available via the shared calendar as is currently the case.
There will always be someone who is "first line", but those duties vary in and out of cycle.
On call only exists in cycle.

## Duties for first line
This role is active between 8:30 and 17:00, every weekday, generally with a different person on duty each week.
You will keep an eye on the support emails, and any voicemails, and make sure they are dealt with by someone. Chase up if something doesn't happen.
If you don't have the experience to resolve something, then you should ask the team for help.

Your phone will ring first for support issues, be prepared to answer it.

If you don't have the experience to resolve the issues, then in cycle you should ask whoever is on call for help first, followed by others in the team. Out of cycle ask the team. 

Extra note for the first week of cycle, these are usually busy, be prepared to delegate tasks. It may be necessary to ask specific individuals to undertake tasks, and you may need to keep track of who is dealing with which problem and where they are. It would also be wise to share the issues as appropriate, but do remember that working patterns and individual needs may play a part in who can help with what.


## What does being on call mean?
This role is active between 07:00 and 23:00, everyday in cycle, generally with a different person on duty each week.

An on call week starts on a Friday and finishes a week later. (So that the first on call week of a cycle starts the Friday before cycle starts, and the final on call week ends with cycle.)

During working hours the person scheduled for first line will receive phone calls first, therefore the duties here are more focussed on the out of hours time (07:00 to 08:30 and 17:00 to 23:00).

Your mobile phone will ring, be prepared to answer it, and deal with the issue detailed.

If the person on first line support is inexperienced, be ready to support them and take calls from them.

## Trouble Shooting

There are a number of tips for [trouble shooting](#all_troubleshooting_links) already on the wiki.

## Answering the support phone
<details>
  <summary> Steps to answer the phone. </summary>

  1. Greet the caller with something that tells them they are talking to the right team, e.g. just respond with "ISIS Experiment Controls Support"
  1. Make a note* of the time
  1. Make a note* of the name of the instrument and the name or at least the role of the caller, if possible - sometimes they are quick and you don't get to catch it, or they don't actually say who it is. These calls can also come from visiting users in cabins, or from the Main Control Room (MCR), knowing who called you about the problem can help if others need to follow it up. Check how best to call them back - scientist may call from cabin, but say to email or phone back on their mobile in case they are no longer in the cabin.
  1. Make a note* of the basic problem. Useful details like:
      1. When did the problem start happening (this helps us to know where to look for in log files)
      1. Is it happening now, or only when you try and do something
      1. What events led up to the problem happening e.g. which commands, opened something on GUI, connected new equipment, ...
      1. how urgent is it - do they have a workaround for now etc.  When is a convenient time for us to start to investigate issue.
  1. If you can solve the problem do so, if you can't start finding the appropriate answers in this guide or by reaching out to others (if onsite, ask in office - if offsite, post in teams). It is OK to tell the user you will call them back 

  * Notes can be mental notes - but don't be afraid to write everything down either, you have to write it all down for the out of hours calls anyway.
</details>

## Basic types of call
<details>
  <summary>I can't log in to *** computer</summary>

  1. What is the name of the computer? 
    - If it is the NDX or NDH, we care, look at the next steps, there are a small subset of other systems we support that others might be logging into which will be listed in the older SharePoint along with the access information as appropriate. 
    - Anything else, NDC, NDL, NDW, cabin PCs, or an ISIS or CLRC domain account as opposed to a local instrument account:
      - in office hours refer them to the Facilities IT service desk
      - out of hours, if in cycle then in zoom phone call "ISIS IT Infrastructure on-call" (phone number 94499)
    - If attempting to connect to EMMA, remember the -A
  1. Unable to connect to NDX via RDP
    - Try yourself to RDP, if you can ask reporter to try again, if they can't it is a connectivity issue for the system they are using to site, in hours refer them to the service desk, out of hours this is best efforts. Check the ISIS Computing O365 SharePoint for more information.
    - Check ping to the NDX, and to the NDH
      - If there are any issues with these pings, you can check DRAC. [Basic DRAC information here](https://stfc365.sharepoint.com/sites/ISISExperimentControls/SitePages/Getting%20to%20Instrument%20DRACs.aspx) and instrument [DRAC IDs here](https://stfc365.sharepoint.com/sites/ISISExperimentControls/Lists/Instrument%20Control%20Computers/AllItems.aspx).
  1. Wrong password entered too many times on anything other than NDX
    - We can't resolve this
</details>

<details>
  <summary>I can't see the dataweb for {instrument}</summary>
 
  1. Check whether or not you can see that dataweb, and how extensive the failure is (one instrument, many, all) (TODO: Find out the solution for this, is it always restart the dataweb server/JSON_BOURNE?
  2. Try the troubleshooting section on the [dataweb](#webdashboard_troubleshooting)
  3. If this doesn't work try restarting ndaextweb3

</details>

<details>
  <summary>Device issues</summary>

  1. I can't talk to device/my blocks are showing as disconnected/IOC isn't working
      - Check that the IOC is running
      - Check that the device is turned on
      - Check if your problem is already listed on the [device/ioc wiki pages](Specific-IOCs).
      - If the device is a DAQmx one, look at it in MAX, and perform a self-test
      - Device not responding
          * Stop the IOC (or VI) and try to connect via a more direct route, e.g. Putty
          * Check the cabling, and that ports etc. are correct
          * For serial devices, check using the MOXA web interface that bytes are being sent and received on the correct port. Moxa IPs are listed [here](http://beamlog.nd.rl.ac.uk/inst_summary.xml) and the login details are on the usual passwords page.
      - If the device is unable to interact in any way, refer this to the appropriate hardware team (via the MCR out of hours)
      - If the device responds via a more direct route, but not via the IOC/VI
          * Make sure the settings in the IOC/VI are correct
          * If the IOC/VI have been updated since the device last worked correctly, roll back to a version that is known to work, and raise a ticket to investigate the issue and find a more sustainable solution
  1. I can't use this button to get to more details/why doesn't this bit of the OPI work
      - Check they are in manager mode
  1. I need to add this device to my system
      - Check [the user manual](https://github.com/ISISComputingGroup/ibex_user_manual/wiki) for IBEX, for SECI, if you don't know already ask someone else
  1. My motor won't move
      - Are both limits made?
          - Yes: Something has happened in the physical realm, refer it to EUSG via the MCR
          - No: Go to next consideration
      - Is any of the other information updating for that motor controller?
          - Yes: Go to next consideration
          - No: Under IBEX go to the engineering device screen, under SECI open the advanced motor functions and go to the console tab, do not send any characters but send a command, if the response is anything but `:` then the Galil is in a fault mode of some kind which will involve restarts etc.
              * If the Galil is unresponsive refer it to EUSG via the MCR 
     - Looking at the specific motor:
         - Are you trying to move in the same direction as an active limit switch?
             - Yes: Try moving in the other direction, if you can move that way to a requested position all is fine
         - Are you able to move in either direction?
             - No: Check for hardware faults (potentially as a referral to EUSG via the MCR)
         - If it is able to move, is the encoder tracking in the same direction as the requested motion?
             - No: The motor setup is probably incorrect, recommission the motor
             - Yes: Feel bewildered as this should be a moving motor
  1. My device isn't behaving as I expect
     - Verify that the device expected on that port is the device connected on that port
     - Treat it as a device that is unable to interact
     - Check the error logs (either through the log interface in the GUI, the console logs, or other appropriate method)
     - Verify that the behaviour you're seeing is not a known quirk of the device. These quirks are often detailed on the [device/ioc wiki pages](Specific-IOCs)

</details>

<details>
  <summary>This network device isn't connecting</summary>

  1. If the device has been working on the ISIS network in that specific hall since the start of May 2025 then this is most likely an issue with the device or the port.
  1. If this is a new to that hall, or to ISIS generally device, or it hasn’t been used since sometime before May 2025, then this may be a network access issue, and it will need some help from the Infrastructure team, the MCR will have a number for them.
  
</details>

<details>
  <summary>A service isn't running</summary>

  1. There are a few things that have services which run, especially the databases, and it is possible after a crash/other restart that these don't start up again, starting task manager as an administrator should allow you to start the service in question
  1. If it is not one of our services (e.g. swipe systems, ERA), we cannot resolve the issue, escalate as appropriate (TODO: Make sure the different escalation methods are documented)
  1. If the MCR news service isn't working, then so long as there is space, restarting our [webserver](/systems/Webserver) may help.
  
</details>

<details>
  <summary>Script issues</summary>

  1. My script won't load
     - If `g.load_script` is being used and you see errors of the form `E:  1: error description (error-name)`, these errors are coming from the linter. Detailed linter troubleshooting is available [here](https://github.com/ISISComputingGroup/ibex_user_manual/wiki/Error-Checking-Troubleshooting).
  1. My script isn't behaving in the way I expect it to
     - This is a best efforts, and not everyone can provide the same level of support
     - Look at it with respect to basic coding standards and obvious race condition points
     - (TODO: Complete this section)

</details>

## Other tasks
<details>
  <summary>Checking Nagios</summary>
  
  1. This is usually considered during the daily stand up
  1. Out of cycle we only worry about the most critical items
  1. In cycle there are more things to be aware of and waiting until the next stand up meeting can be too long
  1. Some issues can only be solved by specific individuals, it is still worth making sure they are aware that there is a problem as they might not have seen the issue yet
  1. Any space issues in a computer
     - Check that there isn't just one large raw/nexus file - if there is then the warning should disappear soon or it is a different problem than just space, otherwise go on to the next step
     - Contact the Instrument Scientists to let them know that something needs doing to their system, and ask when you might be able to take over their computer to ensure they have enough space
     - When there is an opportunity delete some of the oldest log files, if the database (IBEX systems only) is large then trim it as per an update
  1. The CPU/memory usage is high
     - Check which processes are high, and the graph to see how long they have been high
     - If this looks like a steady climb, if you can determine the source create a ticket for investigation
     - Contact the Instrument Scientists to let them know that there is an issue, and ask them to restart appropriate items when they have a chance. Note that restarting the IBEX server is least likely to be required.
</details>

<details>
  <summary>Finding Instrument Scientist Phone Numbers</summary>
  
To find contact numbers for instrument scientists and cabin phone numbers for instruments, the following website is available: [Instrument Map](https://www.isis.stfc.ac.uk/Pages/Instruments.aspx). On this page you can either click on the instrument (in the top image), or click the `Contacts And Support > Instrument Scientists` tab and find the instrument you are looking for.
</details>
