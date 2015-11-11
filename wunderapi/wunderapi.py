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
        if units is 'metric':
            self.units = 'temp_c'
        else:
            self.units = 'temp_f'

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
        temp = result['current_observation'][self.units]
        if self.units == 'temp_f':
            return "%s %sF" % (str(temp), u"\u00b0")
        else:
            return "%s %sC" % (str(temp), u"\u00b0")

    def get_conditions(self, result=None):
        """ Returns a summary of the current conditions. """
        if not result:
            result = self.get('conditions')

        conditions = "\nCurrent weather for %s \n" % \
            (result['current_observation']['display_location']['full'])
        conditions += "%s and %s \n" % \
            (self.get_temp(result), result['current_observation']['weather'])
        conditions += "Winds: %s \n" % \
            (result['current_observation']['wind_string'])
        conditions += "Relative Humidty: %s\n" % \
            (result['current_observation']['relative_humidity'])
        return conditions

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
