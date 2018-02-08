""" This module is a wrapper for the Weather Underground API.

A Weather Underground developer API is required to use.
"""
import sys
import requests
from . config import Config



class Weather():
    """
    Weather Underground API wrapper.  Requires a developer api_key from weather
    underground.
    """
    def __init__(self, config_file=None, location=None, units=None, date=None):
        """
        :param config_file: Config file location
        :param location: Zipcode of weatherstation.
        :param units: Units for results {english, metric}
        :param units: Format for date results. {date, day, shortday}
        """
        self.config = Config(config_file)
        if location:
            self.config.location = location
        if units:
            self.config.units = units
        if date:
            self.config.date_format = date

    def get_url(self, view):
        """ Returns a url for the api formatted for the specific view."""
        view = view
        url = "http://api.wunderground.com/api/%s/%s/q/%s.json" % \
            (self.config.api_key, view, self.config.location)
        return url

    def get_result(self, view):
        """ Returns api result for view as a dictionary. """
        try:
            result = requests.get(self.get_url(view))
            return result.json()
        except requests.ConnectionError():
            print("\n \033[91m Error: Network connection not found. \n")
            sys.exit()

    def get_temp(self, result=None):
        """ Returns the current observation temperature. """
        if not result:
            result = self.get_result('conditions')
        if self.config.units == 'english':
            temp = result['current_observation']['temp_f']
            return "%s%sF" % (str(temp), u"\u00b0")

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
        if self.config.units == "english":
            return result['current_observation']['wind_string']

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
            if detail == 'extended':
                result = self.get_result('forecast10day')
            else:
                result = self.get_result('forecast')
        days = result['forecast']['simpleforecast']['forecastday']

        # Determine temp key
        if self.config.units == "metric":
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
        if self.config.units == "english":
            return "%s%sF" % (str(temp), u"\u00b0")

        return "%s%sC" % (str(temp), u"\u00b0")

    def format_date(self, data):
        """ Returns string of formatted date based on date format.
            Example:
                date     - November 12
                day      - Thursday

        Keyword arguments:
        data   -- a list containing result data
        """
        if self.config.date_format == "date":
            return data["monthname"] + " " + str(data["day"])
        elif self.config.date_format == "day":
            return data["weekday"]
        elif self.config.date_format == "shortday":
            return data["weekday_short"]

    def format_wind(self, data):
        """ Returns wind speed formatted based on units format.
            Example:
                english     - 10 MPH
                metric      - 10 KPH

        Keyword arguments:
            data  -- a list containing result data
        """

        if self.config.units == "english":
            wind = "%s MPH" % (data['avewind']['mph'])
        else:
            wind = "%s KPH" % (data['avewind']['kph'])
        return wind
