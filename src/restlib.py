""" A module for interacting with a REST service using
    either POST or GET."""

__license__ = 'Python'
__author__ = 'Mike Kenyon <mike.kenyon@gmail.com>'
__version__ = 0.1

import httplib
import json
import urllib
import urlparse

class RestLibException: 
    """An exception generated by the RestService framework."""
    pass
class HTTPException(RestLibException):
    """The server returned something other than 200 OK."""
    def __init__(self, status=None, reason=None, exceptionMessage=None):
        self.status = status
        self.reason = reason
        self.exceptionMessage = exceptionMessage
        self.args = status, reason, exceptionMessage
class JSONException(RestLibException):
    """The server's response was not proper JSON."""
    def __init__(self, message=None):
        self.message = message
        self.args = message

class RestService:
    def __init__(self, base_url, port=None, secure=False, key_file=None, cert_file=None):
        """RestService constructor.
        
        base_url = str: The host to which you want to connect.
        [port] = int: Port number, optional.
        [secure] = bool: Use HTTPS if True, optional.
        [key_file] = The name of a PEM formatted file that contains your private key, optional.
        [cert_file] = A PEM formatted certificate chain file, optional."""
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
        """Make a request to the path on the server using GET. Query
        parameters, if any, can be supplied to args using a dictionary
        or a collection of (key, value) tuples."""
        return self.request(path, "GET", args)
    
    def request_post(self, path, args=None, body=None):
        """Make a request to the path on the server using POST. Query
        parameters, if any, can be supplied to args using a dictionary
        or a collection of (key, value) tuples. The body can be a
        string of data or an open file object that supports fileno()
        and read() methods."""
        return self.request(path, "POST", args, body)
    
    def request(self, path, verb="GET", args = None, body = None):
        resource = path
        if args: # Add the query parameters, if any.
            resource += ('?%s' % urllib.urlencode(args))
            
        self.conn.request(verb, resource, body)
        
        responseText = self.conn.getresponse()
        try:
            responseObj = json.loads(responseText.read())
        except ValueError as xcp:
            raise JSONException(xcp.args[0])
                
        if responseText.status != httplib.OK:
            try: # Try to get the exception key from the JSON, if any.
                exceptionMessage = responseObj['exception']
            except KeyError:
                exceptionMessage = None
            raise HTTPException(responseText.status, responseText.reason, exceptionMessage)
        
        return responseObj
        