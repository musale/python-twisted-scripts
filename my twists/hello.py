def hello():
	print "Hello from the reactor loop"
	print "Lately I feel like I am stuck in a rut"

from twisted.internet import reactor
reactor.callWhenRunning(hello)

print "Starting reactor"
reactor.run()