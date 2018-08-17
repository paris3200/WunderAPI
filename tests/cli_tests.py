import unittest
from weather.cli import cli
from click.testing import CliRunner


class TestCLI(unittest.TestCase):

    def setup(self):
        runner = CliRunner()
        return runner


    def test_print_temp(self):
        runner = self.setup()
        result = runner.invoke(cli, ['--temp'])
        #self.assert result.exit_code == 0
        #self.assertIn('F',  result.output)


    def test_print_conditions(self):
        runner = self.setup()
        result = runner.invoke(cli, ['--conditions'])
        self.assertEqual(result.exit_code,  0)
        self.assertIn('Current weather',  result.output)


    def test_print_forecast(self):
        runner = self.setup()
        result = runner.invoke(cli, ['--forecast'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Date',  result.output)
        self.assertIn('Condition',  result.output)
        self.assertIn('Rain Chance',  result.output)
        self.assertIn('Temp',  result.output)


    def test_print_extended_forecast(self):
        runner = self.setup()
        result = runner.invoke(cli, ['--extended'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Date',  result.output)
        self.assertIn('Condition',  result.output)
        self.assertIn('Rain Chance',  result.output)
        self.assertIn('Temp',  result.output)

    def test_default_prints_condition(self):
        runner = self.setup()
        result = runner.invoke(cli)
        self.assertEqual(result.exit_code,  0)
        self.assertIn('Current weather',  result.output)

