# 2025-07-29
## Sprint 2025-07-10 Retrospective (2025-07-29)

| Chair | Timekeeper | Note Taker |
|-------|------------|------------|
| SC    | IG         | LJ         |

## Items from previous Retrospective
 - Notes not uploaded

## Items from this retrospective:
###  Network Ports
 - Having a R55 network port exempt from NAC has been useful for various bits of setup. maybe we could ask for a few more R55 and or R80 ports spread around the office (and label them) so that if bring registered equipment for testing we can more easily?
    - Isn't that fairly simple just patching?
        - Unfortunately not, virtual private network
    - is it just the NAC Exempt, or is it R55/R80
        - It's a bit of both, NAC Exempt is useful, but R55/R80 is also useful
            - R55/R80 IP address situation, maybe it would be better if we could get a NAC exempt R3 port?
        - Even if equipment has tools to configure, its difficult if you don't have mac address/ip address
    - Movable equipment might need to be move between networks as well. we may need to push back that we need a different process for network access
    - Can FIT do this? or would they just send you Anthony
        - they send you a questionnaire asking for mac address and windows version, so useless for say, a lindy switch
            - FIT don't really look after this, there just forwarding on to DI.
    - Weren't we talking to Anthony about this?
        - Yes but don't know what the answer is yet/haven't chased up.
    
### NDW1926 Linux build?
 - Build Nodes NDW1926 can't run win11, can we convert it to a linux box so we can actually have "our" linux build server, as the rest is on the cloud, or will that just become another system to maintain that we don't want.
    - we could put windows server long term support on it, or force upgrade it to win11 and see how long it lasts?
        - Might catch us out, have a build fail due to unsupported OS on the machine etc. and end up on a debugging rabbit hole
        - ESU licence used to be 3 years for £100, £200, £400 for support. At the moment they are very cheap, but we don't know for certain that its the same
        - could downgrade it to win-server 2019 long term support and get support til 2029
    - SCD Cloud is no longer stable, is it important to move away from it
        - Nothing critical relies on the cloud
            - Actually release_branches do, could we move those to shadow? 
                - Rare that cloud is down long enough to actually effect this
                - its mostly just checking-out and tagging things, could we move this to a github action?
                    - Jack looking into it
                    - If this doesn't work, could also run on the same system as the automation.


### IBEX Wiki things needed to be done
  - JH gonna put the message in the list of things to do in the Documentathon
  - decision that needs to be made, Demos and associated pages, either keep them here in "code" or move them to the dev manual, or time tables and notes get added to the ticket to that set of demos.
      - Yes we'll do that, timetables and Notes will now be on the demo ticket.
  - Do we have any broken links now?
      - There shouldn't be, all links in the program should be to the user manual, not the ibex manual
      - links are hardcoded in the code, no one location to check them, might be better to have a property file as a single source of truth about all links we are using.
          - That's potentially a lot of little changes in the gui, but worth doing.
          - Might be helpful for it to work in different languages if needed to.
              - Welsh?
          - SC will make a ticket, but no time for it this sprint, maybe next sprint or the one after.
    

### #8349 was in backlog for a long time, why?
  - FA has made some changes and put it in review
  - Looks to be issues that occur on pearl but not dev machines
      - Previously tested on different ioc with same plugins, now testing on same ioc in simulation so hopefully more likely to work


## 😠😢😄
 - 😄 IOC tests caught the fact that a modbus dependency update switched the definitions of some data-types between signed and unsigned.
    - Nice because this is exactly what the tests are there for
    - It was listed as a major breaking change, so not unexpected
 - 😄 No urgent items for release.
 - 😢 to lose JD
 - 😄 to see that SOPHOS is going away

