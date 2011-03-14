import httplib
import json
import urllib

class RestLibException: 
    pass
class HTTPException(RestLibException):
    def __init__(self, status=None, reason=None, exceptionMessage=None):
        self.status = status
        self.reason = reason
        self.exceptionMessage = exceptionMessage
class JSONException(RestLibException):
    def __init__(self, message=None):
        self.message=message

class RestLib:
    def __init__(self, base_url, port=80):
        self.conn = httplib.HTTPConnection(base_url, port=port)
        self.base_url = base_url
    
    # In docstring, say that body can be an open file object that supports fileno() and read() methods.
    def request(self, path, verb="GET", args = None, body = None):
        resource = path
        if args:
            resource += ('?%s' % urllib.urlencode(args))
            
        url = "%s%s" % (self.base_url, resource)
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
        