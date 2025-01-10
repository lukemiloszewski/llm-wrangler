from pathlib import Path

import typer

from llm_wrangler.core import CodeSnippetOrganizer

app = typer.Typer()


@app.command()
def scaffold_output(
    input_file: Path = typer.Argument(..., help="Path to the input file containing code snippets"),
    output_dir: Path = typer.Argument(..., help="Directory where the files should be extracted"),
) -> None:
    """Extract code snippets from a file into separate files."""
    organizer = CodeSnippetOrganizer()
    result = organizer.process_file(input_file, output_dir)

    for filename, info in result.items():
        typer.echo(f"Created {filename} at {info['path']} ({info['size']} bytes)")


@app.command()
def get_output_prompt() -> None:
    """Display the prompt template for for LLM prompts."""
    typer.echo(CodeSnippetOrganizer.prompt())


if __name__ == "__main__":
    app()
