def not_found(environ, start_response):
    """Called if no URL matches."""
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return ['Not Found']

def hello(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["Hello!"]


def hellojson(env, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    return ["{\"status\":\"Hello!\"}"]


application=hellojson
#application=not_found
