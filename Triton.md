> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Cryogenics](Cryogenics) > [Triton](Triton)

# Triton (dilution fridge)

The Triton software runs on a dedicated PC that follows each fridge around. The control system makes a connection over TCP to issue commands to that software.

Settings:
- TCP port : 33576
- Not all the Triton computers respond to a ping.
- Only one connection can be made at any time, additional connections are refused.

Computer names are available in labview modules readme, alternatively ask someone.

There are various generations of Triton systems in use at ISIS. There are sometimes differences in the protocol between different versions of the software (see for example IBEX issue 3030).

# Gotchas

- Oxford software running on the remote PC can occasionally crash. If this happens, you need to VNC to the remote computer using the credentials on the passwords page and manually restart the software.
- Some commands take a very long time to generate a reply (can be in the region of 10+ seconds before the reply comes through). This is particularly noticeable for setting values, especially setting closed loop mode on or off.
- [Older versions of Triton software only - see IBEX issue 3030] There are some indexing errors in the Oxford software. Therefore, if you want to read values relating to channel `T3`, you may need to query the device for some variables using `T3` as expected and for other variables using `T2`.
- Sample channel - if this comes back as `T0`, this indicates that it is running on a dedicated control channel, and is newer hardware.
- Beware of things coming back as strings when you expect numbers. For example many commands will respond with `NONE` or `NOT_FOUND` where you would usually expect a numeric response.
- Because the device responds to some commands very slowly, need to be quite careful about the overall command rate - ensure that the device can actually keep up with all the commands being sent.
