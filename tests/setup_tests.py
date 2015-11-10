from nose.tools import *
from wunderapi.config import Config

def setup():
    api =  Config(config_file = ".config")
    return api

def test_create_config_set_units():
    apiconfig = setup()
    config = configparser.ConfigParser()
    config.read(".config")
    apiconfig['default']['units'] == 'english'



def test_parse_config_with_correct_parms():
    assert False

def test_parse_config_with_incorrect_parms():
    assert False
