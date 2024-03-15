from switchboard import *
options_manager = SwitchBoard(id=0, name='options_manager')
options = options_manager.board
options.engine = options_manager.Circuit(id=0, name='engines', board=options_manager)
options.engine + next(Switch(circuit=options.engine, name='offline').listener)
options.engine + next(Switch(circuit=options.engine, name='realtime').listener)
options.engine.ARM()
e = options.engine.offline
print(e)