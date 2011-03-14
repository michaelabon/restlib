import restlib
import unittest
import urlparse

class RestLibTestLive(unittest.TestCase):
    def testGETNoScheme(self):
        rest = restlib.RestLib('www.reddit.com')       
        responseObj = rest.request_get('/user/sure_ill_draw_that/.json')
    def testGETWithScheme(self):
        rest = restlib.RestLib('http://www.reddit.com')
        responseObj = rest.request_get('/user/sure_ill_draw_that/.json')
    def testGETQuery(self):
        rest= restlib.RestLib('www.reddit.com')
        resource = '/user/sure_ill_draw_that/.json'
        responseObjControversial = rest.request_get(resource, {'sort': 'controversial'})
        responseObjTop = rest.request_get(resource, {'sort': 'top'})
        self.assertNotEqual(responseObjControversial, responseObjTop, 'controversial should not equal top!')