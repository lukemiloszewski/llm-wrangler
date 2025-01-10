# README

`llm-wrangler` is a CLI utility to develop with the inputs and outputs of llm-generated content.

## Installation

```shell
pip install llm-wrangler
```

## Usage

```shell
# show prompt needed for correct llm output
llm-wrangler get-output-prompt

# scaffold code structure form llm output
llm-wrangler scaffold-output examples/input.txt output
```

- run with `uv`:

```shell
uv tool run llm-wrangler scaffold-output input.txt output_folder
```

## Development

- to publish to `pypi`, configure token:

```shell
poetry config pypi-token.pypi ...
```

## Future Scope

- input/output template integration
- cookiecutter integration
