- Some instruments never want more than one scripts running simultaneously
  - This is the "default" case for more than one instrument
- Some instruments want to run multiple control scripts in parallel:
  - LARMOR for example run a script that flips polarisation alongside a user script. Similar workflow on Vesuvio.
- There is a use case for one "control" script and one "visualisation" script simultaneously
  - the visualisation script can be purely read-only
- Muons make no distinction between script, script server, script generator.
  - Play about with some ideas in scripting
  - Then go to script generator to make full experimental script
  - Like the idea of editing a script which is sat in a queue

- Improve script server training materials.
  - But also has to be explainable to a (scientific) user in a short amount of time.
  - Has to be possible to run single lines (e.g. function calls with parameters)



# Ideas

- Only enable write from within script server?
  - We would have to provide an override for some specific use cases

- Disable writing while acquisition is running (e.g. oak ridge). This could run into issues at ISIS. 

- Enable load/execute in script server from within normal console window?
  - have a genie_python command `g.queue_on_server()`?
  - Future of `g.load_script()`
  - 

- As a user: go to script server, load script, execute it? 
  - I might want to edit my script.

- load_script still loads script locally, but when I execute this function it should run on the script server?

- Nicos has a command for `list_commands`. We've currently only made it aware of g_p commands

- Use standard python? e.g. `def main(): ... main()`

# Solution?

- `g.run_file` : loads and runs locally (right now)
- `g.queue_file` : loads and runs in the script server (queues)
- `g.dry_run` (queues in simulation mode - might be further in the future)
- Need a (small) scripting console in the nicos perspective
- Might need to disable queuing a script from within a script in the queue. Separate client/server g_p.