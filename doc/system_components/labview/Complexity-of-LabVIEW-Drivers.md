# Complexity of LabVIEW Drivers

One indicator as to how easy or difficult an IOC might be would be the existing LabVIEW Driver where it exists.

This will only be an indicator and is not guaranteed to reflect the actual complexity of the device.

There is a spreadsheet available at http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Forms/AllItems.aspx?RootFolder=%2Fisis%2Fcomputing%2FICPdiscussions%2FLabVIEW%20Modules%20Analysis, which has a set of results that can be consulted. The best sorting at the option seems to be Max Complexity * Max Nodes.

In that same folder are the LabVIEW 2017 VIs and the analyser configuration to reproduce the tests. Note that this is not nice LabVIEW code, it is quick and dirty, and the first 5 tabs in the spreadsheet is a copy and paste from the results file created by each case at the front of `analyze and write.vi`. Copying the LabVIEW folders into the same location on a computer running LabVIEW 2017 should allow you to re-run the tests, provided the folders are all in the standard locations.

The test configuration looks simply at the complexity and the number of nodes. The data is then formatted for the results.

There are tabs with a whole host of comparisons for the data returned, more can be tried. Note that the Instron is highlighted in Red, and the AM INT2-L is in green to help highlight the disparity in their complexity as a starting point for our own relative listings.