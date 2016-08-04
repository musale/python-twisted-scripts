class Countdown(object):
	counter1 = 5
	counter2 = 8
	counter3 = 15

	def count(self):
		if self.counter1 == 0 and self.counter2 == 0 and self.counter3 == 0:
			reactor.stop()

		else:
			if self.counter1 != 0:
				print self.counter1, '...'
				self.counter1 -= 1
			if self.counter2 != 0:
				print self.counter2, '...'
				self.counter2 -= 1
			if self.counter3 != 0:
				print self.counter3, '...'
				self.counter3 -= 1
			reactor.callLater(1, self.count)


from twisted.internet import reactor

reactor.callWhenRunning(Countdown().count)

print 'Start'
reactor.run()
print 'Stop'
