from nose.tools import assert_in

from wunderapi.cli import cli

from click.testing import CliRunner


def setup():
    runner = CliRunner()
    return runner


def test_print_temp():
    runner = setup()
    result = runner.invoke(cli, ['--temp'])
    assert result.exit_code == 0
    assert_in('F',  result.output)


def test_print_conditions():
    runner = setup()
    result = runner.invoke(cli, ['--conditions'])
    assert result.exit_code == 0
    assert_in('Current weather',  result.output)


def test_print_forecast():
    runner = setup()
    result = runner.invoke(cli, ['--forecast'])
    assert result.exit_code == 0
    assert_in('Date',  result.output)
    assert_in('Condition',  result.output)
    assert_in('Rain Chance',  result.output)
    assert_in('Temp',  result.output)


def test_print_extended_forecast():
    runner = setup()
    result = runner.invoke(cli, ['--extended'])
    assert result.exit_code == 0
    assert_in('Date',  result.output)
    assert_in('Condition',  result.output)
    assert_in('Rain Chance',  result.output)
    assert_in('Temp',  result.output)
