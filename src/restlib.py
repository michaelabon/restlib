import httplib
import json
import urllib
import urlparse

class RestLibException: pass
class HTTPException(RestLibException): pass

class RestLib:
    def __init__(self, base_url, port=80):
        self.conn = httplib.HTTPConnection(base_url, port=port)
        self.base_url = base_url
    
    def request_get(self, path, args = None):
        resource = path
        if args:
            resource += ('?%s' % urllib.urlencode(args))
            
        url = "%s%s" % (self.base_url, resource)
        self.conn.request("GET", url)
        
        responseText = self.conn.getresponse()
        responseObj = json.loads(responseText.read())
                
        if responseText.status != httplib.OK:
            try:
                xcpMsg = responseObj['exception']
            except KeyError:
                xcpMsg = None
            raise HTTPException(responseText.status, responseText.reason, xcpMsg)
        
        return responseObj
        