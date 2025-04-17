> [Wiki](Home) > [Project tools](Project-tools) > [Working with git and github](Working-with-git-and-github) > Useful Git commands

A list of random, but useful git commands
=====================================================

Git command                                   | What it does 
--------------------------------------------- | ----------------------------------------------------------
`git checkout [branch-name]`                  | Checkout a branch that already exists (local or remote)
`git checkout -b [branch-name]`               | Create and checkout a branch locally
`git checkout master`                         | Checkout the master branch
`git clone [url] [dir]`                       | Clone a repo from url to a directory
`git fetch origin`                            | Update and pull from origin
`git pull`                                    | Get the latest copy of the repo
`git pull origin master`                      | Get the latest master from the origin
`git checkout -- [file-name]`                 | Revert file-name to the version in the repo
`git remote update`                           | Updates all of your local branches that are set to track remote ones, does not merge any commits.
 \-                                       | -
`git branch -a`                               | List all branches locally and origin
`git branch -d [branch]`                      | Delete a branch
`git remote prune origin`                     | Remove listings of deleted remote branches. Delete remote branches will still appear when you do git branch -a unless you use this command before.
`git remote prune origin --dry-run`           | Shows what deleted remote branches would be removed by using git remote prune origin. Only shows what would be removed, does remove anything.
 \-                                       | -
`git add [file-name]`                         | Add a file to the staging area for committing
`git add \*.[type]`                           | Add all files of type to the staging area for committing
`git add -u`                                  | Add all modified files to the staging area for committing
 \-                                           | -
`git mv [file-name] [folder]`                 | Move a file to a new folder
 \-                                           | -
`git commit -m "[descriptive-message]"`       | Commit the staged area with a descriptive message
`git commit -m "Jenkins retest this please" --allow-empty` | Asks Jenkins to retest a pull request. `allow-empty` flag allows you to do it without any associated changes
 \-                                           | -
`git merge [branch-name]`                     | Merge the changes from [branch] to the one you have currently checked out, typically master to your dev branch
`git submodule update --merge`                | Update all submodules and merge them
`git submodule update --remote`               | Update the submodule references on the remote system to the current commits
`git submodule update`                        | Update your local submodules to those referenced on the remote system
`git rebase master`                           | USE ONLY ON LOCAL BRANCHES - reapply your changes to the most recently pulled master
`git submodule update --init`                 | 'clear out' any submodules with new commits
`git submodule status <path>`                 | status of the submodule(s) at this moment, e.g. what the current checkout commit of the submodule is
`git submodule status --cached <path>`        | status of the submodule(s) as they appear in the index, e.g. the expected commit associated with EPICS working copy
 \-                                           | -
`git push -u origin [branch-name]`            | Push a new branch to the origin
`git push origin [branch-name]`               | Push a branch to the origin
 \-                                           | -
`git status`                                  | Get the status information
`git status -s`                               | Get a summarised status, note that M means Modified, ?? Mean untracked
 \-                                           | -
`git clean -f`                                | Remove unstaged files
`git clean -f -d`                             | Remove unstaged files and directories
 \-                                           | -
`git ls-remote --get-url`                     | Get the remote URL of a repository
 \-                                           | -
`git stash`                                   | Put all current modifications onto a stack
`git stash apply`                             | Apply the changes from the last stash
`git stash drop stash@{0}`                    | Drop the most recent stash from the stack
`git stash pop`                               | Apply and drop the most recent stash from the stack
`git stash branch [branch-name]`              | Creates a new branch from the commit when the branch was stashed, applies the stash, and if successful drops the stash
`git stash clear`                             | Delete all stashes
 \-                                           | -
`git rm [file-name]`                          | Remove a file from the staging area
 \-                                           | -
`git log`                                     | View the commit history
`git log -[n]`                                | Limit the number of entries shown by the log
`git log -p`                                  | Show the diffs as well as the log
`git log --stat`                              | Abbreviated stats for each commit
 \-                                           | -
`git commit --amend`                          | Allows you to amend you last commit (missing files, or alter message)
 \-                                           | -
`git reset HEAD [file-name]`                  | Unstage a file
`git reset --hard [sha]`                      | Reset the branch to a specific checkout
`git reset -- soft HEAD ~`                    | Reverse the commit to the previous one
`git reset HEAD ~`                            | unstage all files
 \-                                           | -
`git log -1 HEAD`                             | Get the commit info for the most recent commit
 \-                                           | -
`git config -l --global  |  grep http`        | Check for global proxies
`git config -l  |  grep http`                 | Check for local proxies
`git config --global --unset-all http.proxy`  | Remove http proxies from global config
`git config --global --unset-all https.proxy` | Remove https proxies from global config
`git config --unset-all http.proxy`           | Remove http proxies from local config
`git config --unset-all https.proxy`          | Remove https proxies from local config

## Remove/Move tags

1. `git tag` list tags
1. `git tag -d <tagname>` remove the tag locally
1. `git push origin :refs/tags/<tagname>` push the removed tag to remote
1. `git tag <tagname> <commitId>` create the new tag pointing at the right place
1. `git push origin <tagname>` push the new tag to the repo

## Set local branch to be the same as remote

To set the local master branch to be the same as remote do:

```
git fetch origin
git reset --hard origin/master
```

This can be in response to  the error:

```
remote: error: GH006: Protected branch update failed for refs/heads/master.
remote: error: At least 1 approving review is required by reviewers with write access.
```