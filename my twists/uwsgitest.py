from twisted.web.wsgi import WSGIResource
from twisted.internet import reactor
def application(environ, start_response):
	start_response('200 OK', [('Content-type', 'text/plain')])
	return ['Hello, world! from UWSGI with love']

resource = WSGIResource(reactor, reactor.getThreadPool(), application)
