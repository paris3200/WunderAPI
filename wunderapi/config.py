#!/usr/bin/env python
import configparser
import os
import errno


class Config():
    """
    Reads the default configuration from config file.  If file doesn't exist
    then it is created.

    :param api_key: Weather Underground API developer key
    :param location: Default zipcode
    :param units: english, metric
    """

    def __init__(self, config_file="~/.config/wunderapi/config"):

        self.location = "zipcode"
        self.units = "english"
        # Get the absolute file path
        self.config_file = os.path.expanduser(config_file)
        self.config_dir = os.path.dirname(config_file)
        if not os.path.isfile(self.config_file):
            self.create_config()
        else:
            self.parse_config()

    def parse_config(self, profile='default'):
        """ Reads the config file and imports settings. """
        config = configparser.ConfigParser()
        config.read(self.config_file)
        if not self.api_key:
            self.api_key = config[profile]['api_key']
        elif not self.location:
            self.location = config[profile]['location']

    def create_config(self):
        """ Creates the config file. """
        config = configparser.ConfigParser()
        config['default'] = {'api_key': 'API Key',
                             'location': 'Zipcode',
                             'units': 'english'}

        # Create directory if it doesn't exist
        self.create_dir()

        # Write config file
        with open(self.config_file, 'w+') as configfile:
            config.write(configfile)

    def create_dir(self):
        directory = os.path.expanduser(os.path.dirname(self.config_file))
        try:
            os.makedirs(directory)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(directory):
                pass
            else: raise



def main(api_key=None, location=None):
    config = Config()
    print()


if __name__ == "__main__":
    main()
