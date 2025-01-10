from llm_wrangler import main
from typer.testing import CliRunner


def test_main_runs(runner: CliRunner) -> None:
    result = runner.invoke(main.app)
    assert result.exit_code == 0
