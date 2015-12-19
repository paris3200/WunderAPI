#!/usr/bin/env python
import configparser
import os


class Config():
    """
    Reads the default configuration from config file.  If file doesn't exist
    then it is created.

    :param api_key: Weather Underground API developer key
    :param location: Default zipcode
    :param units: english, metric
    """

    def __init__(self, api_key=None,
                 location=None,
                 units='english',
                 config_file="~/.config/wunderapi/config"):

        self.api_key = api_key
        self.location = location
        self.units = units
        # Get the absolute file path
        self.config_file = os.path.expanduser(config_file)
        if not os.path.isfile(self.config_file):
            self.create_config(api_key, location)
        else:
            self.parse_config()

    def parse_config(self):
        """ Reads the config file and imports settings. """
        config = configparser.ConfigParser()
        config.read(self.config_file)
        if not self.api_key:
            self.api_key = config['default']['api_key']
        elif not self.location:
            self.location = config['default']['location']

    def create_config(self, api_key, location):
        """ Creates the config file. """
        config = configparser.ConfigParser()
        config['default'] = {}
        config['default']['api_key'] = self.api_key
        config['default']['location'] = self.location

        with open(self.config_file, 'w') as configfile:
            config.write(configfile)


def main(api_key=None, location=None):
    config = Config(api_key, location)
    print(config.api_key)
    print(config.location)


if __name__ == "__main__":
    main()
