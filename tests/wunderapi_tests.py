from nose.tools import *
from wunderapi.wunderapi import WunderAPI

def setup():
    api_key = '12345678901234567'
    location = '12345'
    return WunderAPI(api_key, location, units='imperial')

def setup_metric():
    api_key = '12345678901234567'
    location = '12345'
    return WunderAPI(api_key, location, units='metric')

def test_get_temp_f():
    api = setup()
    result = {'current_observation':{'temp_f': 58, 'temp_c': 58}}
    ("58 %sF" %  u"\u00b0")  == api.get_temp(result)

def test_get_temp_c():
    api = setup_metric()
    result = {'current_observation':{'temp_f': 58, 'temp_c': 8}}
    ("8 %sc" %  u"\u00b0")  == api.get_temp(result)

def test_get_url_current():
    api = setup()
    api_key = '12345678901234567'
    location = '12345'
    api.get_url('conditions')  == \
        "http://api.wunderground.com/api/%s/conditions/q/%s.json" % \
        (api_key, location)

def test_get():
    api = setup()
    dict is type(api.get('conditions'))
