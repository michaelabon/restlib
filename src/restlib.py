import httplib
import json
import urllib
import urlparse

class RestLibException: 
    pass
class HTTPException(RestLibException):
    def __init__(self, status=None, reason=None, exceptionMessage=None):
        self.status = status
        self.reason = reason
        self.exceptionMessage = exceptionMessage
        self.args = status, reason, exceptionMessage
class JSONException(RestLibException):
    def __init__(self, message=None):
        self.message = message
        self.args = message

class RestLib:
    def __init__(self, base_url, port=None, secure=False, key_file=None, cert_file=None):
        (scheme, netloc, path, query, fragment) = urlparse.urlsplit(base_url)
        base_url = netloc + path
        if secure:
            if scheme == "http":
                raise ValueError()
            if not port:
                port = httplib.HTTPS_PORT
            self.conn = httplib.HTTPSConnection(base_url, port=port, key_file=key_file, cert_file=cert_file)
        else:
            if scheme == "https":
                raise ValueError()
            if not port:
                port = httplib.HTTP_PORT
            self.conn = httplib.HTTPConnection(base_url, port=port)
        self.base_url = base_url
    
    def request_get(self, path, args=None):
        return self.request(path, "GET", args)
    
    def request_post(self, path, args=None, body=None):
        return self.request(path, "POST", args, body)
    
    # In docstring, say that body can be an open file object that supports fileno() and read() methods.
    def request(self, path, verb="GET", args = None, body = None):
        resource = path
        if args:
            resource += ('?%s' % urllib.urlencode(args))
            
        url = resource
        self.conn.request(verb, url, body)
        
        responseText = self.conn.getresponse()
        try:
            responseObj = json.loads(responseText.read())
        except ValueError as xcp:
            raise JSONException(xcp.args[0])
                
        if responseText.status != httplib.OK:
            try:
                exceptionMessage = responseObj['exception']
            except KeyError:
                exceptionMessage = None
            raise HTTPException(responseText.status, responseText.reason, exceptionMessage)
        
        return responseObj
        