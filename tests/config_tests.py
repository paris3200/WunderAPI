from nose.tools import assert_equal
from wunderapi.config import Config


def setup_with_config_file():
    return Config(config_file="tests/resources/test_config")


def test_parse_config_with_correct_parms():
    pass


def test_parse_config_with_incorrect_parms():
    pass


def test_config_created_with_default_parms():
    config = setup_with_config_file()
    config.parse_config()
    assert_equal(config.date_format, 'date')
    assert_equal(config.units, 'english')
