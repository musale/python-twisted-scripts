import traceback

def stack():
	print 'The Python Stack:'
	traceback.print_stack()

from twisted.internet import reactor
reactor.callWhenRunning(stack)
reactor.run()
