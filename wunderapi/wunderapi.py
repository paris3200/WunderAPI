#!/usr/bin/env python
import requests
import os


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
        result = result['current_observation']
        temp = result[self.units]
        if self.units == 'temp_f':
            return "%s %sF" % (str(temp), u"\u00b0")
        else:
            return "%s %sC" % (str(temp), u"\u00b0")

    def print_temp(self):
        """ Prints the current observation temperature. """
        result = self.get('conditions')
        print(self.get_temp(result))

    def print_conditions(self):
        """ Prints a summary of the current conditions. """
        result = self.get('conditions')
        result = result['current_observation']

        conditions = "\nCurrent weather for %s \n" % (result['display_location']['full'])
        conditions += "%s and %s \n" % (self.get_temp(), result['weather'])
        conditions += "Winds: %s \n" % (result['wind_string'])
        conditions += "Relative Humidty: %s\n" % (result['relative_humidity']) 
        
        print(conditions)

