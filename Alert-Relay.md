This is a python file `/isis/cgi/sendmess.py` living on control-svcs and invoked as `http://control-svcs.isis.cclrc.ac.uk/isiscgi/sendmess.py`

It is only possible to invoke this file when on RAL site, and you also need to pass a correct passcode (see IBEX access sharepoint) as one of the parameters for it to send a message. The parameters passed are:
```
mobiles: a semicolon separated mobiles list for sms text
emails: a semicolon separated email list
pw: correct passcode
inst: instrument name for slack/teams alerts
message: the message
```

An IOC usually posts to this service from the :AC: (alert control) system loaded by the run control IOC

To do the alerting it will use `sendAlert.db` from `support/webget`. This combines several PVs with mobiles, emails etc. and encodes into the format required for a http POST using the aSub function `webFormURLEncode`. It then sends this to control-svcs using the aSub function `webPOSTRequest`

To see the debug output of what `sendAlerts.db` is sending set `epicsEnvSet("WEBGET_POST_DEBUG","1")` in the `st.cmd` of the runcontrol IOC. This is suppressed by default as it may contain sensitive user data.