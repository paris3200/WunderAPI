#!/usr/bin/env python
import requests


class Wunderapi():
    """
    Weather Underground API wrapper.  Requires a developer api_key from weather
    underground.
    """
    def __init__(self, api_key, location, units='english'):
        """
        :param api_key: Developer api key.
        :param location: Zipcode of weatherstation.
        :param units: Unit for temperature {'english', 'metric'}.
        """
        self.api_key = api_key
        self.location = location
        self.units = units

    def get_url(self, view):
        """ Returns a url for the api formatted for the specific view."""
        view = view
        url = "http://api.wunderground.com/api/%s/%s/q/%s.json" % \
            (self.api_key, view, self.location)
        return url

    def get(self, view):
        """ Returns api result for view as a dictionary. """
        r = requests.get(self.get_url(view))
        return r.json()

    def get_temp(self, result=None):
        """ Returns the current observation temperature. """
        if not result:
            result = self.get('conditions')
        if self.units == 'english':
            temp = result['current_observation']['temp_f']
            return "%s %sF" % (str(temp), u"\u00b0")
        else:
            temp = result['current_observation']['temp_c']
            return "%s %sC" % (str(temp), u"\u00b0")

    def get_conditions(self, result=None, ):
        """ Returns a summary of the current conditions. """
        if not result:
            result = self.get('conditions')

        conditions = "\nCurrent weather for %s \n" % \
            (result['current_observation']['display_location']['full'])
        conditions += "%s and %s \n" % \
            (self.get_temp(result), result['current_observation']['weather'])
        conditions += "Winds: %s \n" % \
            (self.get_wind_string(result))
        conditions += "Relative Humidity: %s\n" % \
            (result['current_observation']['relative_humidity'])
        return conditions

    def get_wind_string(self, result=None):
        """ Returns a formatted wind string based on unit type. """
        # Calm based on the Beaufort Scale for light air.
        if result['current_observation']['wind_mph'] <= 3.4:
            return "Calm"
        if self.units == "english":
            return result['current_observation']['wind_string']
        else:
            # Weather Underground doesn't have a metric wind string
            return ("From the %s at %s KPH Gusting to %s KPH" %
                    (result['current_observation']['wind_dir'],
                     result['current_observation']['wind_kph'],
                     result['current_observation']['wind_gust_kph']))

    def format_date(self, data, style=None):
        """ Format date.

        Keyword arguments:
        data   -- a list
        style  -- desired format (date, day, shortday)
        """
        if(style is None or style == "date"):
            return data["monthname"] + " " + str(data["day"])
        elif(style == "day"):
            return data["weekday"]
        elif(style == "shortday"):
            return data["weekday_short"]
