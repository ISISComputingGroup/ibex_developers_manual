There is a long list of things to worry about when you have the support phone or are dealing with a support issue, and this page should provide a starting point to look for guidance on what to do if no one is around.

These pages should be a living document - as people learn things add them to the appropriate place if things change and you notice update them. If you are experienced, make sure the rest of us are getting things right and verify what is linked to from here. Just remember, this is a public wiki, so be wary of the detail added.

Don't forget to "Send As" Experiment Controls, that way it should be possible for others to see what has already been discussed

If remote, make sure you are either on the VPN or accessing a system on-site in some way

## Contents
- [What does being on call mean?](#what-does-being-on-call-mean)
- [Trouble Shooting](#trouble-shooting)
- [Answering the support phone](#answering-the-support-phone)
- [Basic types of call](#basic-types-of-call)
- [Other Tasks](#other-tasks)

## What does being on call mean?
Most important:
  - It means you are responsible for seeing that support items are dealt with. This doesn't mean you have to do them, but you have to make sure they are done
  - You answer the support phone when it rings
In hours:
  - You keep an eye on the Experiment Controls inbox and follow through to see that any issues are resolved, these are echoed in Teams where they can be discussed and uses the same indications as the flash reviews to indicate whether or not the issue is being or has been dealt with
  - You keep an eye on Nagios (either via the website or if you receive mssages that way) and look to resolve issues as appropriate - ask if help is needed or it is unclear
Out of hours:
  - Just focus on the most important things!

## Trouble Shooting

There are a number of tips for [trouble shooting](trouble-shooting-pages) already on the wiki.

## Answering the support phone
<details>
  <summary> Steps to answer the phone. </summary>

  1. Greet the caller with something that tells them they are talking to the right team, e.g. just respond with "ISIS Experiment Controls Support"
  1. Make a note* of the time
  1. Make a note* of the name of the insturment and the name or at least the role of the caller, if possible - somtimes they are quick and you don't get to catch it, or they don't actually say who it is. These calls can be from users in cabins, or from the MCR, knowing who called you about the problem can help if others need to follow it up.
  1. Make a note* of the basic problem.
  1. If you can solve the problem do so, if you can't start finding the appropriate answers in this guide or by reaching out to others.

  * Notes can be mental notes - but don't be afraid to write everything down either, you have to write it all down for the out of hours calls anyway.
</details>

## Basic types of call
<details>
  <summary>I can't log in to *** computer</summary>

  1. What is the name of the computer? 
    - If it is the NDX or NDH, we care, look at the next steps, there are a small subset of other systems we support that others might be logging into (TODO: List of the systems we are willing to look at). 
    - Anything else, NDC, NDL, NDW:
      - in office hours refer them to the service desk
      - out of hours if you can help do so, but this is a best efforts offering, and you might not be able to do anything. If you can't resolve the issue out of thes service desk hours, there is no easy escalation option. An inability to log in due to incorrect passwords will fail over after a length of time, but most of us cannot access Active Directory to reset it, so they will have to find a way around it differently.
    - If attempting to connect to EMMA, remember the -A
  1. Unable to connect to NDX via RDP
    - Try yourself to RDP, if you can ask reporter to try again, if they can't it is a connectivity issue for the system they are using to site, in hours refer them to the service desk, out of hours this is best efforts. (TODO: pages with info for best efforts on network connections for on site, referal info to service desk etc. for out of hours)
    - Check ping to the NDX, and to the NDH
    (TODO: Complete this section)
  1. Wrong password entered too many times on anything other than NDX
    - We can't resolve this
</details>

<details>
  <summary>I can't see the dataweb for {instrument}</summary>
 
  1. Check whether or not you can see that dataweb, and how extensive the failure is (one instrument, many, all) (TODO: Find out the solution for this, is it always restart the dataweb server/JSON_BOURNE?)

</details>

<details>
  <summary>Device issues</summary>

  1. I can't talk to device/my blocks are showing as disconnected/IOC isn't working
    - Check that the IOC is running
    - Check that the device is turned on
    - Check the cabling etc.
    - If the device is a DAQmx one, look at it in MAX, and perform a self-test
    - (TODO: Complete this section)
  1. I can't use this button to get to more details/why doesn't this bit of the OPI work
    - Check they are in manager mode
  1. I need to add this device to my system
    - (TODO: Fill in this whole section, or link to the users manual)
  1. My motor won't move
    - Is any of the other information updating?
      Yes: Go to next consideration
      No: Under IBEX go to the engineering device screen, under SECI open the advanced motor functions and go to the console tab, do not send any characters but send a command, if the response is anything but `:` then the Galil is in a fault mode of some kind which will involve restarts etc. (TODO: What to do with a dead Galil)
    - (TODO: Complete this section)
  1. My device isn't behaving as I expect
    - (TODO: Fill in this whole section)

</details>

<details>
  <summary>A service isn't running</summary>

  1. There are a few things that have services which run, especially the databases, and it is possible after a crash/other restart that these don't start up again, starting task manager as an administrator should allow you to start the service in question
  1. If it is not one of our services (e.g. swipe systems, ERA), we cannot resolve the issue, escalate as appropriate (TODO: Make sure the different escalation methods are documented)
  
</details>

<details>
  <summary>Script issues</summary>

  1. My script won't load
    - (TODO: Fill in this whole section)
  1. My script isn't behvaing in the way I expect it to
    - This is a best efforts, and not everyone can provide the same level of support
    - Look at it with respect to basic coding standards and obvious race condition points
    - (TODO: Complete this section)

</details>

## Other tasks
<details>
  <summary>Checking Nagios</summary>
  
  ### Checking Nagios
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
