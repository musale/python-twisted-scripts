from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.web.resource import NoResource

from calendar import calendar

class YearPage(Resource):
    def __init__(self, year):
        Resource.__init__(self)
        self.year = year

    def render_GET(self, request):
        return "<html><body><pre>%s</pre></body></html>" % (calendar(self.year),)

class Calendar(Resource):
  def getChild(self, name, request):
		try:
			year = int(name)
		except ValueError:
			return NoResource()
		else:
			return YearPage(year)

root = Calendar()
factory = Site(root)
reactor.listenTCP(8880, factory)
reactor.run()
