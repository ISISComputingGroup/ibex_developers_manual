> [Wiki](Home) > [Project overview](Project-Overview) > Notes from Retrospectives

# Notes from Retrospectives
<a name="top"></a>

This page records notes made during Sprint Retrospective meetings (most recent meeting at the top)

[Sprint Ending 2018-09-26](Retrospective_Notes_2018.09.26)

## Sprint_2018_02_15
#### Date of Sprint Retrospective: 14-03-2018

1. Build Performance
   * builds are now much faster.
   * there is still room for improvement.

1. Windows 10 testing
   * Windows 7 will be supported by Microsoft for only two more years.
   * over time, instrument machines will migrate to Windows 10 (probably the new LTS version of Windows 10)
   * we need to be prepared for this
   * also need to consider what happens to SECI during this time period

1. Prune the Backlog
   * we agreed the backlog should be pruned.  Be ruthless about it! (we can always re-open tickets if we are too ruthless).

1. In coming sprints we will prioritise Script Server work, then E4 migration and then support for LSS scripting & graphing (because scripting & graphing will benefit from the Script Server and E4 work).
   * Kevin will follow up with Andrew Caruana to get more details of LSS scripting requirements.

1. How do we track user requests? We will create a process that adds a re-request label and consult this during planning
    - Can we do better about managing expectations? Probably not but can increase the visibility of the request using re-request label
    - Is it acceptable to tell people a feature can not be achieved because of engineering constraint? Yes if it is not an experimental critical feature; but probably check with the group first. If it is experiment critical we need to flag this and be creative.

1. How do we create scientist release notes? They should be created during the release by the release builder (see wiki).

1. Workflow for genie python development? See ticket 3046

## Sprint_2018_01_18
#### Date of Sprint Retrospective: 14-02-2018

1. Testing API Changes
   * we made a change to genie_python (changed enumerated types) but did not create unit tests to test the changes.  This came back to bite us.
   * we had a similar issue with #2942 - changes to DB records had impacts elsewhere, which caught us out.
   * Lesson: make sure there are tests that test your changes.

1. SM300 Motor
   * We estimated 8 points for this (thinking it was a big ticket).  In reality, it required much more effort than 8 parts.
   * Creating a motor_record was more complex than we expected.
   * we didn't really have a good understanding of SM300 motors

1. Identify IOCs we can contribute back to EPICS Community
   * We have quite a collection of IOCs now.  Some could be of value to others.
   * Identify IOCs that would be useful to others.  Work out the best way to package them up for distribution. DO to organise a meeting to discuss further.

1. Deployment
   * We left deployment until the last minute, mainly because we were waiting for GEM & SANDALS tickets to be completed.
   * We should recognise that we don't have to delay the release for late tickets.  We can proceed with the release and hot-fix any instruments that require the late tickets.

1. Build Speed
   * Full, clean builds on Windows take rather a long time - up to 8h.
   * We should investigate ways to speed up the build.  Consider as a topic for stand-down day.

1. Identify Motion Control Tickets
   * create a motion control label in GitHub to allow the Motion Control group to easily identify tickets of interest to them - DO to action

1. Shadow Instrument Scientists
   * Individual members should shadow instrument scientists for  time-to-time - to watch them using IBEX and to learn how it could be improved, to better support the things they need to do.

[Return to top of page](#top)