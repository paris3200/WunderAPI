Basic Usage
===========

Weather can be ran using the *weather* command.  The help function shows
which options are available. 

.. code-block:: bash

    weather --help

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


    weather --forecast

    ┌──────┬───────────┬─────────────┬─────────────┬───────┬──────────┐
    │ Date │ Condition │ Rain Chance │ Temp Hi/Lo  │ Wind  │ Humidity │
    ├──────┼───────────┼─────────────┼─────────────┼───────┼──────────┤
    │ Thu  │ Clear     │ 10%         │ 50°F / 30°F │ 2 MPH │ 73%      │
    │ Fri  │ Clear     │ 10%         │ 55°F / 42°F │ 6 MPH │ 53%      │
    │ Sat  │ Rain      │ 90%         │ 53°F / 49°F │ 2 MPH │ 83%      │
    │ Sun  │ Rain      │ 90%         │ 64°F / 50°F │ 9 MPH │ 92%      │
    └──────┴───────────┴─────────────┴─────────────┴───────┴──────────┘

