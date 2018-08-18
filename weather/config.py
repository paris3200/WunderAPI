""" Provides the configuration for the weather module. """
from configparser import ConfigParser
import os
import sys
import errno


class Config():
    """
    Reads the default configuration from config file.  If file doesn't exist
    then it is created.

    :param config_file: Location of config file
    """

    def __init__(self, config_file=None):

        xdg_config = os.environ.get('XDG_CONFIG_HOME')

        if not config_file:
            if not xdg_config:
                config_file = "~/.config/weather/config"
            else:
                config_file = xdg_config + "/weather/config"

        # Get the absolute file path
        self.config_file = os.path.expanduser(config_file)
        if not os.path.isfile(self.config_file):
            self.create_config()

        self.parse_config()

    def parse_config(self, profile='default'):
        """ Reads the config file and imports settings. """
        config = ConfigParser()
        config.read(self.config_file)
        self.location = config[profile]['location']
        self.units = config[profile]['units']
        self.date_format = config[profile]['date_format']

        if config[profile]['api_key'] != 'api_key':
            self.api_key = config[profile]['api_key']
        else:
            # If enviroment variable exist for api_key, use it.
            try:
                self.api_key = os.environ['WEATHER_API_KEY']
            except KeyError:
                pass

        try:
            if self.api_key == 'api_key':
                raise AttributeError(
                    'API_KEY not set in config file or environment.'
                )
        except AttributeError as err:
            print(err)
            sys.exit()

    def create_config(self):
        """ Creates the config file. """
        config = ConfigParser()
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
            else:
                raise
