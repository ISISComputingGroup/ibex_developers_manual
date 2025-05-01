# Script Generator testing

After the first full release of the script generator testing on personal computers revealed a problem with our current testing standards i.e. running on dev machines ensures we have things like git, Python and the JRE already installed and available impeding our ability to simulate a "home environment".

A few options:

- Run up a VM with windows and copy a built version into it for testing (see VM Testing below)
- Have a "clean" windows server to remote desktop into and copy a built version for testing
   - We will have to maintain the cleanliness by preventing setup of Java, Git and Python in it

## VM Testing

https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/

Unzip download and open ova file with virtualbox.

Create shared folder to put script generator in. Auto mount and make permanent selected.

Put built script generator into shared folder then copy from there onto VM (Doesn't like running from shared folder).

Then test whatever you want.

Things to check:

- You are using the bundled python
  - Start task manager and look at the python running the script generator script
- You are using the bundled JRE
- You are using the bundled git

## Licensing

- https://windowsdev.azureedge.net/eulas/WindowsDeveloperVirtualMachineEula20151118.pdf
- `Section 7` describes what we are not allowed to use it for
  - This does not include any of our currently intended purposes
- `Section 1 part c` worries me slightly
  - I think we are using it to demonstrate and internally evaluate software on windows
  - I am not sure whether or not this would be classed as a commercial purpose (I think this means as commercial hosting so I believe it is fine if you take into account `Exhibit A 2cv`)
- `Section 4`
  - We can have a backup copy and reinstall it
  - Does this mean we can keep reinstalling it?
- `Exhibit A 13dii` "you may not use it after the evaluation period"
  - Does this mean that we cannot reinstall it or use the same VM?