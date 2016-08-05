from twisted.internet.task import deferLater
from twisted.web.resource import Resource
from twisted.web.server import NOT_DONE_YET
from twisted.internet import reactor

class DelayedResource(Resource):
    def _delayedRender(self, request):
        request.write("Sorry to keep you waiting.")
        request.finish()

    def _responseFailed(self, err, call):
        call.cancel()

    def render_GET(self, request):
        call = reactor.callLater(5, self._delayedRender, request)
        request.notifyFinish().addErrback(self._responseFailed, call)
        return NOT_DONE_YET

resource = DelayedResource()