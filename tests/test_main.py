from typer.testing import CliRunner

from llm_io import main


def test_main_runs(runner: CliRunner) -> None:
    result = runner.invoke(main.app)
    assert result.exit_code == 0
