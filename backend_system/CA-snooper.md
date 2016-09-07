> [Wiki](Home) > [Useful tools](Useful-tools) > CA snooper

You can run casnooper from a cmd window after you have started your IOC/client and use it to check for any mistyped PV names. It will print a summary of all pv name requests - valid pvs will connect after a single request, invalid ones will keep retrying and so come high on the list of name queries

```
casnooper -t15 -c20
```

Will run for 15 seconds and print out the connection status of the 20 top requests for PV names on your local subnet. A ```NC``` next to a name means it is not connected. 

The PV retry interval automatically drops off, so if your ioc/client has been running for a while you may need to increase the collection time. Starting csAnooper before you start your ioc/client is a good way to make sure you pick up all requests.
