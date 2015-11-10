#!/usr/bin/env python
import click
from wunderapi import Wunderapi

@click.command()
@click.option('--conditions', '-c', multiple=True, is_flag=True, required=False,
              help="Returns the current conditions.")
@click.option('--forecast', is_flag=True, required=False,
              help="Returns the forecast.")
@click.option('--temp', is_flag=True, required=False,
              help="Returns the temperature.")
@click.option('--location', required=False,
              help="Zipcode of location")
@click.option('--units', '-u', multiple=True, required=False,
              help="Units {english, metric} Defaults to english")
def main(conditions, forecast, temp, location, units):
    """Command line interface for the weather underground API."""
    api = Wunderapi('36f5a21f2a7c691c', '27018', 'F')
    if conditions:
        api.print_conditions()
    elif forecast:
        pass
    elif temp:
        api.print_temp()


if __name__ == '__main__':
    main()
