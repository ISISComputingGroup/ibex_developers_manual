# Triton (dilution fridge)

- TCP port : 33576
- Only one TCP connection can be made to the Triton computers at any one time. Additional connections are refused.
- Not all the Triton computers respond to a ping. There is a task to try and clean these maintenance issues in due course.

Computer names are available in labview modules readme, alternatively ask someone.

# Triton systems

There are at least two generations of Triton systems in use at ISIS. The LabVIEW driver and IOC aim to be compatible with both generations.

Internally the difference is in the lakeshore model number. The newer systems use a dedicated control channel whereas the older systems use one of the "normal" channels as the control channel.

# Gotchas

- Oxford software running on the remote PC can occasionally crash. If this happens, you need to VNC to the remote computer using the credentials on the passwords page and manually restart the software.
- Some commands take a very long time to generate a reply (can be in the region of 10+ seconds before the reply comes through). This is particularly noticeable for setting values, especially setting closed loop mode on or off.
- There are some indexing errors in the Oxford software. Therefore, if you want to read values relating to channel `T3`, you may need to query the device for some variables using `T3` as expected and for other variables using `T2`.
- Sample channel - if this comes back as `T0`, this indicates that it is running on a dedicated control channel, and is newer hardware.
- Beware of things coming back as strings when you expect numbers. For example many commands will respond with `NONE` or `NOT_FOUND` where you would usually expect a numeric response.
- Because the device responds to some commands very slowly, need to be quite careful about the overall command rate - ensure that the device can actually keep up with all the commands being sent.
