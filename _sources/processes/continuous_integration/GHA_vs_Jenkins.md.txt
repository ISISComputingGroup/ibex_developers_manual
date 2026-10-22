# Github Actions versus Jenkins

We have chosen to use Github actions where possible moving forwards to run CI workflows. 

This is because it tends to be very reliable and reduces system administration overhead as we no longer need to keep build servers running, patched and so on. 

For jobs that are long-running or resource intensive, such as building the EPICS top tree, we will continue to run these on Jenkins. Otherwise, the remaining jobs are still on Jenkins due to dependency management issues (ie. they rely on a site-hosted `P2` site).

