> [Wiki](Home) > [The Backend System](The-Backend-System) > [Nicos](Nicos) > NICOS Commands

IBEX interacts with the NICOS back-end using pre-defined commands that are sent to the NICOS daemon via ZeroMQ. These are formatted in JSON as [`command`, [`arg_1`, ... , `arg_n`] ].

You can find the available commands in `EPICS\ISIS\ScriptServer\master\nicos\services\daemon\handler.py`