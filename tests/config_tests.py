import unittest

from wunderapi.config import Config


class TestConfig(unittest.TestCase):

    def setup_with_default_config_file(self):
        return Config(config_file="tests/resources/test_config")

    def test_parse_config_with_correct_parms(self):
        pass

    def test_parse_config_with_incorrect_parms(self):
        pass

    def test_config_created_with_default_parms_raises_excpetion(self):
        with self.assertRaises(SystemExit) as cm:
            self.setup_with_default_config_file()
        self.assertEqual(cm.exception.code, None)
