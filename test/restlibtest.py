#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Unit test for restlib"""

__license__ = 'Python'
__author__ = 'Mike Kenyon <mike.kenyon@gmail.com'
__version__ = 0.1

import restlib
from MockHTTPConnection import MockHTTPConnection
from Responses import Responses
import unittest

class GoodConnection(unittest.TestCase):
    def testGET(self):
        r = Responses()
        rest = restlib.RestLib('http://www.example.com')
        rest.conn = MockHTTPConnection(r)       
        for k, v in r.GET.iteritems():
            responseObj = rest.request_get(k)
            self.assertEquals(responseObj, v[1])
           
class BadInput(unittest.TestCase):
    def testNotFound(self):
        r = Responses()
        rest = restlib.RestLib('http://www.example.com')
        rest.conn = MockHTTPConnection(r)
        self.assertRaises(restlib.HTTPException, rest.request_get, '/file_not_found')
    def testBadRequest(self):
        r = Responses()
        rest = restlib.RestLib('http://www.example.com')
        rest.conn = MockHTTPConnection(r)
        self.assertRaises(restlib.HTTPException, rest.request_get, '/400')
    def testForbidden(self):
        r = Responses()
        rest = restlib.RestLib('http://www.example.com')
        rest.conn = MockHTTPConnection(r)
        self.assertRaises(restlib.HTTPException, rest.request_get, '/403') 
        


