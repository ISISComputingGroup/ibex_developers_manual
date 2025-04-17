> [Wiki](Home) > [Project overview](Project-Overview) > [Notes from Retrospectives](Retrospective-Notes) > [Retrospective Notes 2018.02.14](Retrospective-Notes-2018.02.14)


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
