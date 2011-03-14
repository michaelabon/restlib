#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Unit test for restlib"""

__license__ = 'Python'
__author__ = 'Mike Kenyon <mike.kenyon@gmail.com'
__version__ = 0.1

from restlib import RestLib
from MockHTTPConnection import MockHTTPConnection
from Responses import Responses
import unittest

class GoodConnection(unittest.TestCase):
    def testGET(self):
        r = Responses()
        restlib = RestLib('http://www.example.com')
        restlib.conn = MockHTTPConnection(r)       
        for k, v in r.GET.iteritems():
            print k
            responseObj = restlib.request_get(k)
            self.assertEquals(responseObj, v[1])
            
        


