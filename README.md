# README

`llm-wrangler` is a CLI utility to generate the code structure from the output of llm-generated content.

## Installation

```shell
pip install llm-wrangler
```

## Usage

- use an LLM to generate code snippets (which may be scoped across multiple modules)
- convert those code snippets into a suitable output format using `llm-wrangler prompt`
- save the output to a temp file (e.g. `llm_output.txt`)
- scaffold the code structure in your local dev environment using `llm-wrangler scaffold-output llm_output.txt output_folder`

- run with `uv`:

```shell
uv tool run llm-wrangler prompt
uv tool run llm-wrangler scaffold-output llm_output.txt output_folder
```

## Development

- to publish to `pypi`, configure token:

```shell
poetry config pypi-token.pypi ...
```

## Future Scope

- integrate file marker templates
- integrate cookiecutter templates to conform project structure 
- integrate direct access to LLM API's (remove reliance on web interfaces and temp files)
- ability to install dependencies needed for the environment (e.g. by loading `requirements.txt`)
- ability to create a git repository from the scaffolded output
- ability to create a github repository from the scaffolded output
- ability to publish the scaffolded output to a pypi repository (if it is a python package)
- ability to reference the input content as either a file path, a URL path, or the clipboard content
