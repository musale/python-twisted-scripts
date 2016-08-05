from twisted.web.wsgi import WSGIResource
from twisted.internet import reactor
from twisted.internet.task import deferLater
from twisted.web.resource import Resource
from twisted.web.server import NOT_DONE_YET
from twisted.internet import reactor
from twisted.python.log import err

def application(environ, start_response):
	start_response('200 OK', [('Content-type', 'text/plain')])
	return ['Hello, world!']

resource = WSGIResource(reactor, reactor.getThreadPool(), application)