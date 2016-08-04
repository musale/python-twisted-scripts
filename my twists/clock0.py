from twisted.web.server import Site # factory associating listening port with the protocol implementation
from twisted.internet import reactor
from twisted.web.resource import Resource

import time

class ClockPage(Resource):
	"""SubClasses the Resource class since it has the dynamic rendering behaviour that we need"""

	isLeaf = True #indicates that the clock page resource will never have any children
	def render_GET(self, request):
		"""Called whenever the URI we hook the resource to is requested with the GET method.
		the returned byte is what is sent to the browser."""
		return "<html><body>%s</body></html>" % (time.ctime(),)

resource = ClockPage()
factory = Site(resource)

reactor.listenTCP(8880, factory)
reactor.run()		