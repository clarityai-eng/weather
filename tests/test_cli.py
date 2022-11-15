from click.testing import CliRunner
from weather.cli import cli


class TestWeather:
    def test_cli(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["temperature"])
        assert result.exit_code == 0
        assert -90.0 <= float(result.output) <= 60.0
