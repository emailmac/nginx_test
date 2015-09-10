def not_found(environ, start_response):
    """Called if no URL matches."""
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return ['Not Found']

def hello(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["Hello!"]

def not_found(environ, start_response):
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return ['Not Found']

def method_failure(environ, start_response):
    start_response('420 Method Failure', [('Content-Type', 'text/plain')])
    return ['420 Error']

def method_failure_json(env, start_response):
    start_response('401 Method Failure', [('Content-Type', 'application/json')])
    return ["{\"status\":\"ERROR!\"}"]


def method_failure_420(env, start_response):
    start_response('420 Method Failure', [('Content-Type', 'application/json')])
    return ["{\"status\":\"ERROR!\"}"]

application=method_failure_420
#application=method_failure_json
#application=method_failure
#application=not_found
#application=hello
