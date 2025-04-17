# 2019-12-02

## Should we make support tickets private?

The concern is that we include sensitive information in support tickets and that this may either break GDPR or cause security concerns.

We have decided that we should not make support tickets private. The sensitive information that could be in these tickets (or in regular development tickets) should be placed in the icp shares and a link provided to that information which can only be followed in house.

## We should have more demos at review

Yes. The standard should be to demo a ticket and only if there is no reasonable way to do this we will "mention" it. It is worth encouraging people to demo rather than mention prior to the sprint review.

## We should have fewer single points of failure

Yes. When handing out responsibilities and jobs we should be more careful to not place the full responsibility in the same person's hands each time. This could be done by pair programming, or splitting tasks into smaller tasks and distributing these subtasks between people.

We should be aware that it is an issue and consider this at standup and when defining how we run planning.

## Should the supporter check Nagios oddities spotted during standup? Should these be ticketed as support tickets?

Our current process is to note the oddities at standup and pass any issues out to people at that point. This is good because we share out the issues to people who may not have come across them before reducing single points of failure. 

It, however, has been noted that we have a few persistent Nagios issues that should either be ignored or chased down. We should create a ticket to deal with these, maybe as part of our fix all tests day?

We should not put too much time into this as Freddie is setting up a new monitoring system. It has also been noted that not only Freddie should do this. We should do it collaboratively to reduce single points of failure.

## Dealing with unique challenges of talking to hardware and limited testing

We should make more use of our test instruments/have a more structured approach to using them. No concrete plans were put into place about how to make this reality.

## Sprint planning took 3 hours, is this ok?

In short: We are agreeing to spend more time on sprint planning (3 hours with structure breaks). We aim to take a more conscious approach to not talk about implementation and instead focusing on acceptance criteria.

We came to the conclusion that the extra time is ok. We possibly have not been spending enough time planning. We have a large team with relatively long sprints.

However, we recognise that we need to take a more structured approach and be conscious of how we are running planning meetings. In regards to this, we have decided to lengthen planning to 3 hours with a structure break in the middle. 

We must also consider our productivity in the meetings. It has been recognised that we often spend more time discussing implementation than we should. Though some discussion is necessary to understand pointing we often go a step further than is necessary. We have planning poker for a reason and we do not need to talk in as much detail to decide upon points. If we must discuss detailed implementation in a group this should be done in smaller more focused discussions at another point.

We should focus on creating acceptance criteria for tickets and either agree on them in the meeting or if we cannot we should have a process for dealing with this. What was suggested was to create spike/exploratory tickets with the information we have and then spin out new tickets with solid acceptance criteria. We do this to a certain extent but maybe a more structured approach should be taken?

We have also noted that we may need to structure our tickets better with flow charts and acceptance criteria in a standard format.

It was also noted that preplanning has often taken longer than expected as well and we should consider how the whole process fits together and affects each other rather than just planning. 