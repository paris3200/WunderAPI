[![Build Status](https://travis-ci.org/paris3200/WunderAPI.svg?branch=master)](https://travis-ci.org/paris3200/WunderAPI) [![Coverage Status](https://coveralls.io/repos/github/paris3200/WunderAPI/badge.svg?branch=master)](https://coveralls.io/github/paris3200/WunderAPI?branch=master)
[![Documentation Status](https://readthedocs.org/projects/wunderapi/badge/?version=latest)](http://wunderapi.readthedocs.io/en/latest/?badge=latest)

# WunderAPI
WunderAPI is a command line wrapper for the weather underground API.  WunderAPI requires an API key that is available from Weather Underground.  

    $ weather --help

    Usage: weather [OPTIONS]

      Command line interface for the weather underground API.

    Options:
      -c, --conditions     Returns the current conditions.
      -f, --forecast       Returns the forecast.
      -e, --extended       Returns the 10 day extended forecast.
      -t, --temp           Returns the temperature.
      -l, --location TEXT  Zipcode of location
      -u, --units TEXT     Format for units.  {english, metric}
      --date TEXT          Format for date.  {date, day, shortday}
      --config_file TEXT   Path to config file.
      --help               Show this message and exit.

    
    $ weather -c

    Current weather for Raleigh, NC 
    36.5°F and Clear 
    Winds: Calm 
    Relative Humidity: 52%

    $ weather -f
    ┌─────────────┬───────────┬─────────────┬─────────────┬────────┬──────────┐
    │ Date        │ Condition │ Rain Chance │ Temp Hi/Lo  │ Wind   │ Humidity │
    ├─────────────┼───────────┼─────────────┼─────────────┼────────┼──────────┤
    │ November 12 │ Clear     │ 0%          │ 71°F / 42°F │ 3 MPH  │ 63%      │
    │ November 13 │ Clear     │ 0%          │ 62°F / 35°F │ 11 MPH │ 42%      │
    │ November 14 │ Clear     │ 0%          │ 58°F / 31°F │ 9 MPH  │ 43%      │
    │ November 15 │ Clear     │ 0%          │ 60°F / 33°F │ 2 MPH  │ 46%      │
    └─────────────┴───────────┴─────────────┴─────────────┴────────┴──────────┘


## Documentation
Documentation is available on [Read The Docs](http://wunderapi.readthedocs.io/en/latest/).


