# Gollum Wikis

Gollum is a ruby package used to display github wikis on the web.

## On linux

- Runs on shadow as user Gollum, in `/home/gollum`
- Some time after system updates run, `Ruby Gems` needs a rebuild. Try `/tmp/ibex.log`   may need to run e.g. `gem pristine nokogiri --version 1.6.8`

  * Should run this as user Gollum

This theoretically works but we have had issues getting pages to render correctly (on shadow).

## On Windows

This seems to work better. 

Installation instructions:
- Install jRuby (note: it MUST be jRuby, the C implementations of ruby don't work correctly on windows). You will probably want the exe-x64 download.
  * When running through the installer, do not select "configure path for me" as this might mess with our EPICS path.
- In the `jRuby/bin` directory run `gem install gollum`
- Ensure the `python2` command is accessible on your PATH
- Run `python2 -m pip install docutils==0.14` (or a later version if you desire). This includes the rest2html script which gollum uses to render restructured text.
- Clone the user manual using `git clone https://github.com/ISISComputingGroup/ibex_user_manual.wiki.git C:/Instrument/user_manual`
- Run `jRuby\bin\gollum C:/Instrument/user_manual` to run the gollum webserver
- Navigate to [http://localhost:4567/Home](http://localhost:4567/Home) - this should display the wiki