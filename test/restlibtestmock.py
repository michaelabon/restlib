"""Unit tests for restlib, using a mock framework"""

__license__ = 'Python'
__author__ = 'Mike Kenyon <mike.kenyon@gmail.com'
__version__ = 0.1

import restlib
import httplib
from MockHTTPConnection import MockHTTPConnection
from Responses import Responses
import unittest

class GoodConnection(unittest.TestCase):
    def testGET(self):
        r = Responses()
        rest = restlib.RestService('http://www.example.com')
        rest.conn = MockHTTPConnection(r)       
        for k, v in r.GET.iteritems():
            responseObj = rest.request_get(k)
            self.assertEquals(responseObj, v[1])
    def testGETArgs(self):
        r = Responses()
        rest = restlib.RestService('http://www.example.com')
        rest.conn = MockHTTPConnection(r)
        for k, v in r.ARGS.iteritems():
            responseObj = rest.request_get("/has/args", args=eval(k))
            self.assertEquals(responseObj, v)
    def testPOST(self):
        r = Responses()
        rest = restlib.RestService('http://www.example.com')
        rest.conn = MockHTTPConnection(r)
        for k, v in r.POST.iteritems():
            responseObj = rest.request_post(k, body = v[2], args = v[3])
            self.assertEquals(responseObj, v[1])
class BadInput(unittest.TestCase):
    def testNotFound(self):
        r = Responses()
        rest = restlib.RestService('http://www.example.com')
        rest.conn = MockHTTPConnection(r)
        self.assertRaises(restlib.HTTPException, rest.request_get, '/file_not_found')
        
    def testBadRequest(self):
        r = Responses()
        rest = restlib.RestService('http://www.example.com')
        rest.conn = MockHTTPConnection(r)
        self.assertRaises(restlib.HTTPException, rest.request_get, '/400')
        
    def testForbidden(self):
        r = Responses()
        rest = restlib.RestService('http://www.example.com')
        rest.conn = MockHTTPConnection(r)
        self.assertRaises(restlib.HTTPException, rest.request_get, '/403') 
        
    def testNotFoundPOST(self):
        r = Responses()
        rest = restlib.RestService('http://www.example.com')
        rest.conn = MockHTTPConnection(r)
        self.assertRaises(restlib.HTTPException, rest.request_post, '/file_not_found')
        
    def testBadRequestPOST(self):
        r = Responses()
        rest = restlib.RestService('http://www.example.com')
        rest.conn = MockHTTPConnection(r)
        self.assertRaises(restlib.HTTPException, rest.request_post, '/400')
        
    def testForbiddenPOST(self):
        r = Responses()
        rest = restlib.RestService('http://www.example.com')
        rest.conn = MockHTTPConnection(r)
        self.assertRaises(restlib.HTTPException, rest.request_post, '/403') 
        
class BadServerResponse(unittest.TestCase):
    def testUnterminatedJSON(self):
        r = Responses()
        rest = restlib.RestService('http://www.example.com')
        rest.conn = MockHTTPConnection(r) 
        self.assertRaises(restlib.JSONException, rest.request, "/unterminatedJSON", verb="GET_TEST")
    def testOverterminatedJSON(self):
        r = Responses()
        rest = restlib.RestService('http://www.example.com')
        rest.conn = MockHTTPConnection(r) 
        self.assertRaises(restlib.JSONException, rest.request, "/overterminatedJSON", verb="GET_TEST")
    def testNoJSON(self):
        r = Responses()
        rest = restlib.RestService('http://www.example.com')
        rest.conn = MockHTTPConnection(r) 
        self.assertRaises(restlib.JSONException, rest.request, "/noJSON", verb="GET_TEST")
        
class SSL(unittest.TestCase):
    def testUseSSLByParam(self):
        rest = restlib.RestService('https://www.example.com', secure=True)
        self.assertTrue(isinstance(rest.conn, httplib.HTTPSConnection), "SSL by param does not use HTTPSConnection")
    def testDoNotUseSSLByParam(self):
        rest = restlib.RestService('http://www.example.com', secure=False)
        self.assertFalse(isinstance(rest.conn, httplib.HTTPSConnection), "No SSL by param uses HTTPSConnection")
    def testConfuseSSLYesParamNoScheme(self):
        self.assertRaises(ValueError, restlib.RestService, 'http://www.example.com', secure=True)
    def testConfuseSSLNoParamYesScheme(self):
        self.assertRaises(ValueError, restlib.RestService, 'https://www.example.com', secure=False)
