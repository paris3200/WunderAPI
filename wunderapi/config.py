""" Provides the configuration for the weather module. """
import configparser
import os
import errno


class Config():
    """
    Reads the default configuration from config file.  If file doesn't exist
    then it is created.

    :param config_file: Location of config file
    """

    def __init__(self, config_file=None):

        if not config_file:
            config_file = "~/.config/wunderapi/config"

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
        self.location = config[profile]['location']
        self.units = config[profile]['units']
        self.date_format = config[profile]['date_format']

        # If enviroment variable exist for api_key, use it.
        try:
            os.environ['WEATHER_API_KEY']
            self.api_key = os.environ['WEATHER_API_KEY']
        except KeyError:
            self.api_key = config[profile]['api_key']

    def create_config(self):
        """ Creates the config file. """
        config = configparser.ConfigParser()
        config['default'] = {'api_key': 'api_key',
                             'location': '27607',
                             'date_format': 'date',
                             'units': 'english'}

        # Create directory if it doesn't exist
        self.create_dir()

        # Write config file
        with open(self.config_file, 'w+') as configfile:
            config.write(configfile)

    def create_dir(self):
        """ Creates defaults directory if it doesn't exist. """
        directory = os.path.expanduser(os.path.dirname(self.config_file))
        try:
            os.makedirs(directory)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(directory):
                pass
            else: raise
