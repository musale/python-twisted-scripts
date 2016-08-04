from twisted.internet.task import LoopingCall
from twisted.internet import reactor

class Countdown(object):
 """
	Consider the LoopingCall class in twisted.internet.task.
	Rewrite the countdown program above to use LoopingCall. 
	You only need the start and stop methods and you don’t need to use the “deferred” return value
	 in any way
 """
    counter = 5
 
    def count(self):
        if self.counter == 0:
            reactor.stop()
        else:
            print self.counter, '...'
            self.counter -= 1
 
lc = LoopingCall(Countdown().count)
lc.start(0.5)
print 'Start!'
reactor.run()
print 'Stop!'
