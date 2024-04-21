
Installation
============

It is recommended that you install Weather in a virtual environment to
prevent conflicts with other python packages.  First create the virtual
environment, activate it, and follow the install directions below.

To install Weather begin by cloning the repo and changing to the directory. ::

    git clone https://github.com/paris3200/weather.git
    cd weather

Install the requirements using Pip. ::

    pip install -r requirements.txt

Finally install WunderAPI. ::

    python setup.py install

Configuration
=============

The configuration file should be created in '~/.config/weather/config'.  The
file will be automitcally generated on the first run of the program if it
doesn't exist.  It should take the following format. ::

    [default]
    api_key = api_key
    date_format = shortday
    units = english
    location = 27043

If you don't want to set the api_key in the configuration file you can set it
as the environment variable 'WEATHER_API_KEY'.  This is useful if you keep your
configs in a public git repository.  

The api_key can be obtained from https://www.wunderground.com/weather/api.

