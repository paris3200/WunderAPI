import unittest

from wunderapi.config import Config


class TestConfig(unittest.TestCase):

    def setup_with_default_config_file(self):
        return Config(config_file="tests/resources/test_config")

    def test_config_read_from_file(self):
        config = Config(config_file="tests/resources/test_custom_config")
        self.assertEqual('english', config.units)
        self.assertEqual('api_key', config.api_key)
        self.assertEqual('27607', config.location)
        self.assertEqual('date', config.date_format)

    def test_config_created_with_default_parms_raises_excpetion(self):
        with self.assertRaises(SystemExit) as cm:
            self.setup_with_default_config_file()
        self.assertEqual(cm.exception.code, None)
