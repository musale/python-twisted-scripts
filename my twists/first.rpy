import time

from twisted.web.resource import Resource

class ClockPage(Resource):
    isLeaf = True
    def render_GET(self, request):
        return "<html><body>%s</body></html>" % (time.ctime(),)

resource = ClockPage()
