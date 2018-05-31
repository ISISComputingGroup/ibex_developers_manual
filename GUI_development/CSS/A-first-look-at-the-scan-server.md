> [Wiki](Home) > [The GUI](The-GUI) > [CS Studio](GUI-CSS) > A first look at the scan server

The server runs as a headless Eclipse application. The server is accessed from the clients via a TCP port.

Inside CSS there are perspectives for editing, monitoring and plotting scans.

![Client 1](GUI_development/images/css/client1.png)

The editor perspective allows scans to be created using a number of building blocks, the blocks are: loops; delays; sets; sub-scans; wait for; log value; comments; and, Python script snippets.

The scripts are constructed using “drag and drop” and the values are set via the Properties window.
The finished scripts are submitted to the script server for processing.

Scans can also be created and submitted directly from the Python command line.

The script can be “simulated” before it is run. For this, the script is unwound and each step is shown and the total duration is estimated. This allows the user to view each step of the scan.

![Client 2](GUI_development/images/css/client2.png)

The Scan Monitor is used to monitor the condition of the current scan and the queued and finished scans. It is possible to modify queued scripts.

![Client 3](GUI_development/images/css/client3.png)

The variables of the scan can be viewed using the Scan Plot.

![Client 4](GUI_development/images/css/client4.png)