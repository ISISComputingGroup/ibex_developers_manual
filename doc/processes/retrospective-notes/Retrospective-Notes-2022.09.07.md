# 2022-09-07

| Chair      | Timekeeper | Note Taker |
| :--------   | :---------: | ----------: |
| [Lilith Cole](https://github.com/LilithCole) | [Lowri Jenkins](https://github.com/LowriJenkins) | [Jack Allen](https://github.com/JackEAllen) |

--- 

## Items from last retrospective

_Items discussed in the previous retrospective_

### Sprint

#### Should we delay start of next sprint? - yes and did
- KB suggested sprint planning/start for the coming sprint can be be delayed by a week to finish off large volume of items in ready/in progress
- Agreed upon by all

#### `PlanitPoker` vs. Scrumpy - which is better? - `planitpoker` stick with for now 
Scrumpy Pros:
- Github tickets are more easily tied into the service
- Asynchronous voting - People can vote in advance if they will be away for planning

Cons:
- You can only be in one room at a time, difficult to do priority / points in parallel. We could use both in a hybrid solution but might create more overhead than utility

We will stick with `PlanitPoker` for now but keep Scrumpy in mind as an adequate backup if needed.

## Customer relations

### Are people interested in uniforms (e.g shirts) for representing IBEX on support calls? - retuning to later
- [Jack Harper](https://github.com/rerpha) feels that users can be confused about our role sometimes when we turn up on support calls
- Other support teams have specific outfits to clearly identify themselves as qualified support staff
- This does not need to be mandatory, but it might be nice to have the option
- Not everyone likes uniforms, can we have other items to identify ourselves? e.g. hats
- [Jack Harper](https://github.com/rerpha) will investigate available ISIS "branding" options and report back at next retrospective

### Support phone number: - done
- New label with updated contact information has been printed and displayed in TS1 & TS2 blockhouses. Done!

## Team Interaction

### Coffee attendance is extremely low, should we find an alternative for team building? - tried coffee - attendance better if someone brings cake 
- Attendance has fizzled to near zero - perhaps a symptom of more people being back in the office
- Suggestion to steal Weekly Coffee & Cake idea from Mantid instead. People in the room agreed this sounds like an appropriate rhythm.
- We will do this in a conference room to enable people to join remotely. Should be convenient for conference room availability.
- We have picked Friday afternoon as the regular time for this for now. We can consider varying the days of the week this takes place if this otherwise excludes anyone from attending.

### Should we have standup in G06 instead of the office?: - seems better than the office G34 and G06
- Team generally in favour, (more space, better sound). 
- Availability may present an issue
- We will trial it when the room is next free in the morning.


---


## Items from current retrospective

### How Would People Feel About Trying Moving Stand-up Next Door to the Conference Room G06?
* G06 camera better placed.
* G34 is just nicer!
* Sound quality much better when the room is designed for it!
* Seeing and hearing people in the office much better.
* As some of those working remotely can be hard to hear, one option could be to get people headsets to be more audible.

### Uniforms for the Team
To make it clearer to users that we are from the experiment controls team and not just random members of the general public who have wandered in and started unplugging things, uniforms were discussed.

* [Jack Harper](https://github.com/rerpha) found an online resource for ISIS branded clothing which is used by other groups: 
Found a place to order clothes from: http://www.artisanshirts.co.uk/
The uniform would be optional as not everyone would necessarily like to wear it.

Tasks left to do on this topic:
* Find out if there is a specific procedure for ordering ISIS branded clothing- maybe ask Jamie.
* Check what they can produce
* If there is a specific piece of clothing that someone would prefer to have, let Kathryn know directly ("I might be convinced to wear a this").

### Could we book rooms for an hour for code chats?
The answer: "Yes, just let the organiser know how long you need"

### Could we make the repo_checks jenkins job statuses go to the #Jenkins teams channel rather than #General?
Possible solution discussed:
* We could try and automate builds and stop checks temporarily.
* [Jack Allen](https://www.github.com/JackEAllen) will place an existing GitHub workflow developed for personal use into a repository to be adapted to work through Jenkins. The main piece of work that will need to be undertaken to do this is setting up an authentication token for the Jenkins user to be able to push to the repository as the GitHub workflow developed relies on a personal access token which is not suitable for use in an organisational repository.

Actions Taken:
* Wiki has been updated to include workflow: https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Shared-utility-scripts
* A template repository has been created which can be used as it is, or as a starting point for integration into Jenkins CI/CD: https://github.com/ISISComputingGroup/Update_Submodule_Workflow_Action

### Would it be helpful whilst we are trying something different with planning if I run the next sprint planning meetings as well?
A resounding yes! `:thumbsup:`

### Coffee Attendance
Try running only on Wednesdays and Fridays interchangeably to be inclusive of those working remotely on one of the two suggested days.

### Potentially controversial: should we have a timekeeper for stand-up :question: :question: :question:
stand ups have recently been getting longer and longer, we need to keep them short and sweet. Daily stand-up is constructed for people to speak for a short period of time due to getting tired standing up. Those of us working remotely sit down so happy to talk longer.
When anything slightly in more depth needs to be discussed it should be broken into a separate meeting.

To resolve this:
* Everyone should be more proactive and aware that you can interrupt someone to move on. ("words, then muting people, then violence as a last resort" :punch: )
* Turn up on time! - We should make a start no later than 10:03am.
* To keep things moving, we should move on from looking through status screens to individual status's by 10:15am no matter what.

### Checkstyle - How to Try and Reduce How Often We Check It As Part of Stand-up
Suggestions:
Anyone can merge is checkstyle remains the same or decreases - only admins can merge if needed and checkstyle would goes up.
Automate checkstyle in GitHub to become part of the review (can't be missed this way). Up to developer discretion to allow merging in if checkstyle would increase, but generally only allow to be merged in if checkstyle remains the same or decreases.

The only complexity mentioned with this is we would need to tell Jenkins which branch to compare against master and that master would need pulling to ensure it is up to date.

Action taken:
[Jack Allen](https://www.github.com/JackEAllen) will create an issue to explore the viability of automating through GitHub and label as tech depth. We will leave checkstyle as it is for now, but be stricter with merging in pull requests and be more concise with updates in stand-up - no harm in saying "can I catch you afterwards" to resolve checkstyle increases.

Actions Taken:
- Issue to explore viability of automating through GitHub: https://github.com/ISISComputingGroup/IBEX/issues/7346

### Currently, It is Hard to Find New Developer Issues

Currently, it is hard to find appropriate worthwhile issues for new starters and members in the team early in their careers - Can we be more liberal with adding things? - 

From the discussion held, there doesn't seem to be enough appropriate tickets at the moment which is why it may be hard to find new developer issues.

Older issues are potentially suitable, but not necessarily documented well enough for new starters to pick up.
As people see appropriate tickets, they should update the description if still relevant and add the "new developer" labels to them once checked by Kathryn who is currently going through all tickets.
