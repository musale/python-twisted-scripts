from twisted.web import server, resource
from twisted.web.server import Site # a factory which glues a listening port to HTTP protocol
from twisted.web.static import File # resource which glues the the HTTP protocol implementation to the system
from twisted.internet import reactor # accepts TCP connections and moves the bytes into and out of the them

# resource = File("/tmp") # and instance of file resource pointed at the directory to serve

# factory = Site(resource) # instance of the Site factory with that resource

# reactor.run() # start the reactor!!

class Simple(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        return "<html>Hello, world!</html>"

site = server.Site(Simple())
reactor.listenTCP(8080, site)
reactor.run()
