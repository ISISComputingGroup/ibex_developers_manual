### Items from Retrospective before last:
 - The office mic is still often illegible.
   - as of this meeting still an issue.

### Items from Previous Retrospective:
 - Centralise the snag lists to the ibex project sharepoint.
   - not discussed as Kathryn did not have access to reflectometry.

 - Cull icp-write members for security:
   - Require users to have 2-factor authentication on github.
     - This will remove everyone who doesn't have it already enabled.
     - This may handle most of those who need to be removed.
     - This will only effect write access.
   - Look into removing members who have not been members of the project in some time.
     - Change them to read-only?

 - New team members still running into permissions problems on some repositories:
   - Often issue is to do with different permission settings for writing and merging.
   - Might be possible to automate adding new members to permissions using github actions.
     - Jack Allen to look into this.

 - Best way to handle reminders about updating submodules.
   - Ideas:
     - Message on teams?
     - todo in issue template?
     - pre-commit message check?
   - Repo-checks do actually catch this, but this usually delays being noticed until the next standup.

 - Adding to/Editing wiki sections.
   - Try and make things more verbose, but if information would be duplicated then using links instead.
     - Finding things can be extremely difficult on the wiki, so:
       - Try and make names of pages clear and relevant.
       - The wiki likely needs a cleanup, probably still the best option for documentation though.
       - Searching better at top left within repository, rather than using the wiki provided search-bar.


### Items from this sprint:
  - Discussion of how we want to handle versioning, differences between Major/Minor/Patch:
    - What we would classify as a major change and what the scientist would may differ greatly.
    - If we want to change this, we might have to change how we deploy, or how we number versions, or both.
      - If these things change we may also have to alter our build system to avoid changing more than is necessary.
   - Discussion of deployment at other facilities.
     - There doesn't seem to be a common approach among them.
     - More use of static builds with unrolled DBs?
     - multiples versions of asyn at a lot of other facilities.
       - We've avoided this for ease of testing.
   - Discussion to be continued at next retrospective.

 - This sprint was very short:
   - Seemed to work fairly well, and was well tracked by shadow.
   - Was useful as a tech-debt sprint, similar to Mantid's post-release period.
   - Up to date calenders would make it easier for sprints similar to this to be planned in future.