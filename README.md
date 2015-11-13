# WunderAPI
A command line interface for the weather underground api. 

    Usage: wunderapi [OPTIONS]

    Command line interface for the weather underground API.

    Options:
    -c, --conditions              Returns the current conditions.
    -f, --forecast                Returns the forecast.
    -t, --temp                    Returns the temperature.
    -l, --location TEXT           Zipcode of location
    -u, --units [english|metric]  Format for units.  Defaults to english
    --date [date|day|shortday]    Format for date.  Defaults to date.
    --help                        Show this message and exit.

    
    $wunderapi -f
    ┌─────────────┬───────────┬─────────────┬─────────────┬────────┬──────────┐
    │ Date        │ Condition │ Rain Chance │ Temp Hi/Lo  │ Wind   │ Humidity │
    ├─────────────┼───────────┼─────────────┼─────────────┼────────┼──────────┤
    │ November 12 │ Clear     │ 0%          │ 71°F / 42°F │ 3 MPH  │ 63%      │
    │ November 13 │ Clear     │ 0%          │ 62°F / 35°F │ 11 MPH │ 42%      │
    │ November 14 │ Clear     │ 0%          │ 58°F / 31°F │ 9 MPH  │ 43%      │
    │ November 15 │ Clear     │ 0%          │ 60°F / 33°F │ 2 MPH  │ 46%      │
    └─────────────┴───────────┴─────────────┴─────────────┴────────┴──────────┘



