"""Unit tests for restlib, using a live source.

   Tests in this suite are not meant to thoroughly test restlib because
   we do not control the data that is received. To thoroughly test
   restlib, we have the restlibtestmock suite.
   
   Rather, this suite is designed to ensure that restlib does actually
   work in "real work" conditions.
   
   It does feel wrong using others' resources for testing purposes,
   but given the magnitude of page hits that reddit receives,
   this test will be a drop in the ocean."""
   
__license__ = 'Python'
__author__ = 'Mike Kenyon <mike.kenyon@gmail.com'
__version__ = 0.1 

import restlib
import unittest
import urlparse

class RestLibTestLive(unittest.TestCase):

    def testGETNoScheme(self):
        """Ensure that GET works when used without a protocol."""
        rest = restlib.RestService('www.reddit.com')       
        responseObj = rest.request_get('/user/sure_ill_draw_that/.json')
        #print responseObj
    
    def testGETWithScheme(self):
        """Ensure that GET works when used with a protocol."""
        rest = restlib.RestService('http://www.reddit.com')
        responseObj = rest.request_get('/user/sure_ill_draw_that/.json')
        #print responseObj
    
    def testGETQuery(self):
        """Ensure that GET works when given a query."""
        rest= restlib.RestService('www.reddit.com')
        resource = '/user/sure_ill_draw_that/.json'
        responseObjControversial = rest.request_get(resource, {'sort': 'controversial'})
        responseObjTop = rest.request_get(resource, {'sort': 'top'})
        self.assertNotEqual(responseObjControversial, responseObjTop, 'controversial should not equal top!')
        #print responseObj
    
    def testGETTrailingSlash(self):
        """Ensure that GET works with a trailing slash."""
        rest = restlib.RestService('www.reddit.com/')
        responseObj = rest.request_get('/user/sure_illasdfdfs_draw_that/.json')
        # Will raise JSONException if 404'd
        
    def testGETNonRooted(self):
        """Ensure that GET works even without a rooted resource."""
        rest = restlib.RestService('www.reddit.com')
        responseObj = rest.request_get('user/sure_ill_draw_that/.json')
        # Will raise JSONException if 404'd
    