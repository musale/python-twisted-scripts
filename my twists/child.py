from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.web.static import File

root = Resource() # resource which will correspond to the root of the URL hierachy. all URLs are it's children

# create new resources and attach them to root
root.putChild("foo", File("/tmp"))
root.putChild("bar", File("/lost+found"))
root.putChild("baz", File("/opt"))

factory = Site(root)
reactor.listenTCP(8880, factory)
reactor.run()
