from twisted.internet.task import LoopingCall
from twisted.internet import reactor

class Countdown(object):
 
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
