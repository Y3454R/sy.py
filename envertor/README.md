# Envertor

Envertor is a CLI tool that generates an example `.env` file (`.env.example`) from an existing `.env`, automatically detecting value types and replacing them with sensible placeholders.

## Installation

To install the package in development mode:

```bash
cd envertor
pip install -e .
```

## Usage

Since `pyproject.toml` defines a console script entry point, after installing the package you can run:

```bash
envertor -i .env -o .env.example
```

Or with default values:

```bash
envertor
```

## Options

- `-i, --input`: Path to input .env file (default: `.env`)
- `-o, --output`: Path to output example .env file (default: `.env.example`)
- `-v, --version`: Show envertor version
