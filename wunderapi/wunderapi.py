#!/usr/bin/env python
import requests
import sys

from . config import Config


class Wunderapi():
    """
    Weather Underground API wrapper.  Requires a developer api_key from weather
    underground.
    """
    def __init__(self, api_key, location, units=None, date_format=None):
        """
        :param api_key: Developer api key.
        :param location: Zipcode of weatherstation.
        :param units: Unit for temperature {'english', 'metric'}.
        :param date_format: Date format {'date', 'day', 'shortday'}
        """
        self.api_key = api_key
        self.location = location
        if not units:
            self.units = "english"
        else:
            self.units = units
        if not date_format:
            self.date_format = "date"
        else:
            self.date_format = date_format

    def get_url(self, view):
        """ Returns a url for the api formatted for the specific view."""
        view = view
        url = "http://api.wunderground.com/api/%s/%s/q/%s.json" % \
            (self.api_key, view, self.location)
        return url

    def get_result(self, view):
        """ Returns api result for view as a dictionary. """
        try:
            r = requests.get(self.get_url(view))
            return r.json()
        except:
            print("\n \033[91m Error: Network connection not found. \n")
            sys.exit()

    def get_temp(self, result=None):
        """ Returns the current observation temperature. """
        if not result:
            result = self.get_result('conditions')
        if self.units == 'english':
            temp = result['current_observation']['temp_f']
            return "%s%sF" % (str(temp), u"\u00b0")
        else:
            temp = result['current_observation']['temp_c']
            return "%s%sC" % (str(temp), u"\u00b0")

    def get_conditions(self, result=None, ):
        """ Returns a multiline string summary of the current conditions. """
        if not result:
            result = self.get_result('conditions')

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


    def get_forecast(self, result=None, detail='simple'):
        """
        Returns an array of the forecast with the first element containing
        the table headings.
        """
        if not result:
            result = self.get_result('forecast')
        days = result['forecast']['simpleforecast']['forecastday']

        # Determine temp key
        if (self.units == "metric"):
            temp_key = "celsius"
        else:
            temp_key = "fahrenheit"

        forecast = []
        # Table headings
        forecast.append(["Date", "Condition", "Rain Chance", "Temp Hi/Lo",
                         "Wind", "Humidity"])
        for day in days:
            date = self.format_date(day['date'])
            condition = day['conditions']
            rain = str(day['pop']) + "%"
            temp = "%s / %s" % (self.format_temp(day["high"][temp_key]),
                                self.format_temp(day["low"][temp_key]))
            wind = self.format_wind(day)
            humidity = str(day['avehumidity']) + "%"
            forecast.append([date, condition, rain, temp, wind, humidity])
        return forecast

    def format_temp(self, temp):
        """ Returns string containing temperature with units. """
        if (self.units == "english"):
            return "%s%sF" % (str(temp), u"\u00b0")
        else:
            return "%s%sC" % (str(temp), u"\u00b0")

    def format_date(self, data, style=None):
        """ Returns string of formatted date.
            Example:
                date     - November 12
                day      - Thursday
                shortday - Thur

        Keyword arguments:
        data   -- a list
        style  -- desired format (date, day, shortday)
        """
        if not style:
            style = self.date_format

        if(style == "date"):
            return data["monthname"] + " " + str(data["day"])
        elif(style == "day"):
            return data["weekday"]
        elif(style == "shortday"):
            return data["weekday_short"]

    def format_wind(self, data):
        if (self.units == "english"):
            wind = "%s MPH" % (data['avewind']['mph'])
        else:
            wind = "%s KPH" % (data['avewind']['kph'])
        return wind
