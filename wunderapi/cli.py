#!/usr/bin/env python
import click
from wunderapi.wunderapi import Wunderapi as weather
from terminaltables import SingleTable



def print_temp(api):
    click.echo(api.get_temp())


def print_conditions(api):
    click.echo(api.get_conditions())


def print_forecast(api):
    print_table(api.get_forecast())


def print_table(data):
    table = SingleTable(data)
    print(table.table)


@click.command()
@click.option('--conditions', '-c', multiple=False, is_flag=True,
              required=False, help="Returns the current conditions.")
@click.option('--forecast', '-f', is_flag=True, required=False,
              help="Returns the forecast.")
@click.option('--temp', '-t', is_flag=True, required=False,
              help="Returns the temperature.")
@click.option('--location', '-l', required=False,
              help="Zipcode of location")
@click.option('--units', '-u', type=click.Choice(['english', 'metric']),
              required=False, default="english",
              help="Format for units.  Defaults to english")
@click.option('--date', type=click.Choice(['date', 'day', 'shortday']),
              help="Format for date.  Defaults to date.")
def cli(conditions, forecast, temp, location, units, date):
    """Command line interface for the weather underground API."""
    api = weather('36f5a21f2a7c691c', '27018', units, date)
    if conditions:
        print_conditions(api)
    elif forecast:
        print_forecast(api)
    elif temp:
        print_temp(api)
    else:
        print_conditions(api)

if __name__ == '__main__':
        cli()
