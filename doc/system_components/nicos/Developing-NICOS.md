# Updating NICOS Version

We have [forked nicos](https://github.com/ISISComputingGroup/nicos) and added it as a submodule of EPICS at ISIS\ScriptServer\master. To update the version IBEX uses, fetch changes from upstream of the fork onto a branch and then create a PR for that branch.

## Previously we pinned a commit of nicos and used the following process to update nicos

**This is no longer our process for updating but has been kept in case the for is not successful and we need to switch back**

The (read-only copy) of the NICOS repository is at `git://trac.frm2.tum.de/home/repos/git/frm2/nicos/nicos-core.git`. We keep a submodule that points to this repo as part of EPICS base, to update the version IBEX uses you need only go to the submodule, pull the version you want and then follow the instructions as per [here](#git_workflow_reviewing_epics_submodules).

There is some general NICOS documentation [here](https://forge.frm2.tum.de/nicos/doc/nicos-master/)

## Developing NICOS

We have [forked nicos](https://github.com/ISISComputingGroup/nicos) and added it as a submodule of EPICS at ISIS\ScriptServer\master. To make changes commit them to this repository and then talk to the FRM team to get changes pushed back up to their repository.

## Previously we pinned a commit of nicos and used the following process to contribute:

**This is no longer our process for contributing but has been kept in case the for is not successful and we need to switch back**

NICOS is stored at FRM using a git/[gerrit system](https://www.gerritcodereview.com/). Some of their processes are documented [here](https://forge.frm2.tum.de/wiki/projects:nicos:index). Gerrit in general is a wrapper around git and uses very different workflows as those used in IBEX and github in general. To give you some idea from the gerrit documentation:

> As Gerrit implements the entire SSH and Git server stack within its own process space, Gerrit maintains complete control over how the repository is updated, and what responses are sent to the git push client invoked by the end-user, or by repo upload. This allows Gerrit to provide magical refs, such as refs/for/* for new change submission and refs/changes/* for change replacement. When a push request is received to create a ref in one of these namespaces Gerrit performs its own logic to update the database, and then lies to the client about the result of the operation. A successful result causes the client to believe that Gerrit has created the ref, but in reality Gerrit hasn’t created the ref at all.

The FRM guide to getting set up with Gerrit is [here](https://forge.frm2.tum.de/wiki/services:gerrit:using_git_gerrit).

Once set-up the workflow for adding new work to NICOS is:
* Create one commit with all changes 
* Push it to Gerrit using `git push origin HEAD:refs/for/master` (the FRM guide shows you how to put this in your git config)
* Changes will be reviewed in the FRM Gerrit system (https://forge.frm2.tum.de/review/q/status:open)
* Any changes that come from reviews should be added to the same commit using `git commit -amend`

As hinted in the above paragraph, this isn't actually one commit but only looks like it to the user. You can see changes that have been made (including when commits have been amended as patch sets) on the review, for example [here](https://forge.frm2.tum.de/review/#/c/18861/4). To checkout a specific commit you should use the commands specified in the download section of that page (the commit hash mentioned on the page is a lie).