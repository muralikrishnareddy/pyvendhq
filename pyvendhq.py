import json
import urllib
import httplib
import unittest
import os
import urllib2
import urlparse
from HTMLParser import HTMLParser


__version__ = "0.3.0"

#First Create a Free VendHQ Account which shall be free for 30 days
#<<store name>> has to replace in the below Code with Store Name in your VendHQ
#After "Bearer" <<Personal Token>> has to Replace by generating a Personal Token in you Store VendHQ

#This Sample Code will Print all the Products

class APITestCase(unittest.TestCase):

    def test_api(self):
        ret = self._request('GET','<<store name>>','/api/products',{})
        print ret["products"]
        
    @staticmethod
    def _request(method, domain_prefix, path, params):
        c = httplib.HTTPSConnection(str(domain_prefix)+'.vendhq.com')
        try:
            headers = {'Content-Type': 'application/x-www-form-urlencoded' if method == 'GET' else 'application/json', 'Authorization': 'Bearer <<Personal Token>>'}
            c.request(method, path, urllib.urlencode(params), headers)
            response = c.getresponse()
            return json.loads(response.read())
        finally:
            c.close() 
            

if __name__ == '__main__':
    unittest.main()
