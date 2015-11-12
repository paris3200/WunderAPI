from nose.tools import *
from wunderapi.wunderapi import Wunderapi
import json


def setup():
    api_key = '12345678901234567'
    location = '94101'
    return Wunderapi(api_key, location, units='english')


def mock_result():
    with open('tests/resources/conditions.txt') as data_file:
            result = json.load(data_file)
    return result


def mock_date_result():
    with open('tests/resources/forecast.txt') as data_file:
            result = json.load(data_file)
    data = result['forecast']['simpleforecast']['forecastday']
    for item in data:
        date = item['date']
    return date


def setup_metric():
    api_key = '12345678901234567'
    location = '94101'
    return Wunderapi(api_key, location, units='metric')


def test_get_temp_f():
    api = setup()
    assert_equals(("66.3 %sF" % u"\u00b0"), api.get_temp(mock_result()))


def test_get_temp_c():
    api = setup_metric()
    assert_equals(("19.1 %sC" % u"\u00b0"), api.get_temp(mock_result()))


def test_get_url_current():
    api = setup()
    api_key = '12345678901234567'
    location = '94101'
    assert_equals(api.get_url('conditions'),
                  "http://api.wunderground.com/api/%s/conditions/q/%s.json" %
                  (api_key, location))


def test_get_conditions_english():
    api = setup()
    conditions = "\nCurrent weather for San Francisco, CA \n"
    conditions += "66.3 \u00b0F and Partly Cloudy \n"
    conditions += "Winds: From the NNW at 22.0 MPH Gusting to 28.0 MPH \n"
    conditions += "Relative Humidity: 65%\n"
    assert_equal(conditions, api.get_conditions(mock_result()))


def test_get_conditions_metric():
    api = setup_metric()
    conditions = "\nCurrent weather for San Francisco, CA \n"
    conditions += "19.1 \u00b0C and Partly Cloudy \n"
    conditions += "Winds: From the NNW at 35.4 KPH Gusting to 45.1 KPH \n"
    conditions += "Relative Humidity: 65%\n"
    assert_equal(conditions, api.get_conditions(mock_result()))


def test_get_is_dict():
    api = setup()
    assert isinstance(api.get('conditions'), dict)


def test_format_date_date():
    api = setup()
    assert_equals("June 29", api.format_date(mock_date_result(), "date"))


def test_format_date_date_empty():
    api = setup()
    assert_equals("June 29", api.format_date(mock_date_result()))


def test_format_date_day():
    api = setup()
    assert_equals("Friday", api.format_date(mock_date_result(), "day"))


def test_format_date_day_short():
    api = setup()
    assert_equals("Fri", api.format_date(mock_date_result(), "shortday"))


def test_get_wind_string_english():
    api = setup()
    assert_equal("From the NNW at 22.0 MPH Gusting to 28.0 MPH",
                 api.get_wind_string(mock_result()))


def test_get_wind_string_metric():
    api = setup_metric()
    assert_equal("From the NNW at 35.4 KPH Gusting to 45.1 KPH",
                 api.get_wind_string(mock_result()))
