| Chair      | Timekeeper | Note Taker |
| :--------:   | :---------: | :----------: |
| LC | DM | TL |

## Items from last retrospective:
- **IBEX training course:** FA did an EPICS course for new starters, but not one for IBEX from a user perspective. We may have effort available to do this in the next PI.
- **Project management delegation:** Tasks will start being allocated as appropriate to distribute the project management workload (unless people volunteer)
- **Office screen reinstatement:** 
    - We have not found a new machine for this yet. 
    - We could use one of the old unused datastreaming machines
    - New machine does not even necessarily need windows, just a very lightweight OS capable of running a web browser 
    - JH has offered to use a Friday afternoon to set a machine up.
- **Winter Meal Out:** DM and WS to start looking into options the day after retrospective.
- **CCFE Tour:** Has not yet progressed beyond the idea stage.

***

## Items from this retrospective:
- **(GLAD) New features:** Just relaying some positive feedback from instrument scientists, particularly regarding new Alarms functionality and Moxa Mappings perspective.
- **Wiki restructuring:** ES has progressed this work as part of the recent "Friday", but still ongoing
- **Central Mysql service:** JH has talked to SCD about implementing a central Mysql service. We need a proper discussion on how exactly this should be implemented but we have a contact in SCD now and we know that it is possible.
- **Should we have Standup every day?:** 
    - Motivation for retrospective comment was that it was perceived to be getting in the way of things like support during cycle while not adding that much (e.g. "I'm going to continue working on my ticket")
    - There was a sentiment that by not having it every day we would lose more than we gain
    - Checking on services regularly is important
    - We have decided to keep it but should make more effort to keep it brief:
        - Chair to prepare more by looking at checks and services ahead of the meeting / fixing minor issues as appropriate. There may be a bit of a transitional period as we collectively build the habit, others may remind the chair of this process for the time being
        - Be more strict in mentioning what you achieved the day before in individual updates
- **PI board for planning**: We have decided to try running the next planning meeting off of the PI board instead of the IBEX Project Board
- **Merchandise:** There is a strong desire among new graduates and industrial placement students to get ISIS merchandise. 
    - We do not want to make wearing this mandatory
    - Raise with FA for follow up. JH has the contact of the supplier and will start to collect an order from the team

***

### Other comments (Mad/Glad/Sad)
- **Flat Github structure:** We don't have a good way of grouping tickets hierarchically. This would make it easier to do IOCs in parallel if its split up into sub-tickets
    - We have tried this before but found that IOCs are not usually "big" enough to warrant lots of sub-tickets, and it can make development more awkward in places where developing the whole thing in parallel is more convenient
    - A more structured approach to categorizing tickets hierarchically might be useful e.g. for larger features like Client, Script Generator, etc.
- **Documentation:** Is lacking in places
    - It's up to everyone to keep this up to date. If you notice something missing, feel free to add it
    - Sometimes the person looking for the information does not have the required knowledge to add the information, but they can ask for help with writing it, or try to write it after they have acquired the knowledge e.g by asking someone, and then getting them to validate it afterwards
    - Generally, making more frequent use of diagrams in the documentation may make information much more accessible than a wall of text. e.g. A diagram showing the flow of information / macros / db loads etc. in an IOC would be very helpful.

#### GLAD:
- KB happy with everyone pulling together to get PEARL running