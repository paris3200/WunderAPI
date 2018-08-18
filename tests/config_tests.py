import unittest
from unittest.mock import patch
from nose.tools import nottest

from weather.config import Config


class TestConfig(unittest.TestCase):

    def setup_with_default_config_file(self):
        return Config(config_file="tests/resources/test_config")

    def test_config_read_from_file(self):
        config = Config(config_file="tests/resources/test_custom_config")
        self.assertEqual('english', config.units)
        self.assertEqual('27607', config.location)
        self.assertEqual('date', config.date_format)

    """
    Travis-CI has a api_key set as an encrypted environment variable.  Due
    to this, this test will not pass.  Remove the @nottest decarator for local
    testing
    """
    @nottest
    def test_config_created_with_default_parms_raises_excpetion(self):
        with self.assertRaises(SystemExit) as cm:
            self.setup_with_default_config_file()
        self.assertEqual(cm.exception.code, None)

    def test_config_directory_uses_XDG_CONFIG_HOME(self):
        with patch.dict('os.environ', {'XDG_CONFIG_HOME': 'tests/resources/'}):
            config =Config()
            self.assertEqual('english', config.units)
            self.assertEqual('28621', config.location)
            self.assertEqual('date', config.date_format)

