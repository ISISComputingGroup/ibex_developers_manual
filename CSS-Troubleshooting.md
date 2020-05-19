This page contains information on how to troubleshoot some common issues with the GUI. 

**Opening some OPIs in OPI editor throws a Malformed URL Exception**

This might happen if you recently pulled in EPICS-CSS . A probably reason this happens is that your workspace and file system are out of sync. You can fis this by collapsing the workspace, then deleting everything under uk.ac.stfc.isis.ibex.opis (but do NOT delete contents on disk!), and then reimporting everything again fron IBEX GUI/base/uk.ac.stfc.isis.ibex.opis .