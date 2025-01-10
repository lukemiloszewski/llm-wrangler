# README

`llm-wrangler` is a CLI utility to develop with the inputs and outputs of llm-generated content.

## Installation

```shell
pip install llm-wrangler
```

## Usage

```shell
# show prompt needed for correct format
llm-wrangler get-output-prompt

# 
llm-wrangler scaffold-output examples/input.txt output
```

## Development

- to publish to `pypi`, configure token:

```shell
poetry config pypi-token.pypi ...
```

## Future Scope

- input/output template integration
- cookiecutter integration
