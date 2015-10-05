#!/usr/bin/python
from coverage import coverage
import unittest
import os
import wunderapi

basedir = os.path.dirname(__file__)

cov = coverage(branch=True, omit=['venv/*', 'test.py'])
cov.start()

class TestWeatherF(unittest.TestCase):
    def setUp(self):
        self.api_key = '12345678901234567'
        self.location = '12345'
        self.api = wunderapi(self.api_key, self.location)

    def test_get_temp_f(self):
        result = {'current_observation':{'temp_f': 58, 'temp_c': 58}}
        self.assertEqual(("58 %sF" %  u"\u00b0"), self.api.get_temp(result))

    def test_url_current(self):
        self.assertEqual(self.api.get_url('conditions'), "http://api.wunderground.com/api/%s/conditions/q/%s.json" % (self.api_key, self.location))

class TestWeatherC(unittest.TestCase):
    def setUp(self):
        self.api_key = '12345678901234567'
        self.location = '12345'
        self.api = wunderapi(self.api_key, self.location, 'c')

    def test_get_temp_f(self):
        result = {'current_observation':{'temp_f': 58, 'temp_c': 58}}
        self.assertEqual(("58 %sC" %  u"\u00b0"), self.api.get_temp(result))

    def test_get(self):
        self.assertTrue(dict, type(self.api.get('conditions')))


if __name__ == "__main__":
    try:
        unittest.main()
    except:
        pass
    cov.stop()
    cov.save()
    print("\n\nCoverage Report:\n")
    cov.report()
    print("HTML version: " + os.path.join(basedir, "tmp/coverage/index.html"))
    cov.html_report(directory='tmp/coverage')
    cov.erase()

