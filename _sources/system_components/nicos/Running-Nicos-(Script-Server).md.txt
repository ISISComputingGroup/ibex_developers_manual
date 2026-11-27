# Running NICOS

As of [issue 7135](https://github.com/IsisComputingGroup/ibex/issues/7135), NICOS is no longer started automatically as part of a default instrument startup. Instead, the `NICOSDAEMON` ioc must be added to the configuration. On instruments, adding this IOC to their "base" component is likely to be best.

To test the script server is working, open the "Script Server" perspective in the ibex client. Check that the connection status label says "No Error". Write a simple script and send it to the server. You should be able to see the output from NICOS in the output text field.

For testing purposes you can also start the Nicos GUI by navigating to the `bin/` directory and run `python nicos-gui` and connect to the local daemon. However, as the NICOS GUI does not use ZeroMQ you will have to comment out `servercls='nicos.services.daemon.proto.zeromq.Server'` in `nicos-core/master/custom/demo/setups/special`. Both `nicos-daemon` and `nicos-gui` need to be restarted for this change to take effect.