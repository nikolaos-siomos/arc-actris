# Installation

This page explains how to install ARC-ACTRIS for normal use and for development.

## Install from PyPI

Once the package is published, install it with:

```bash
pip install arc-actris
```

Then check that the package imports correctly:

```bash
python -c "from arc_actris import arc; print(arc)"
```

## Development installation with `venv`

Clone the repository and create a local virtual environment:

```bash
git clone https://github.com/nikolaos-siomos/arc.git
cd arc
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

Run the test suite:

```bash
pytest
```

The `-e` flag installs the package in editable mode. This means changes made inside `src/arc_actris/` are available immediately without reinstalling the package.

## Development installation with Conda

You can also use Conda to manage the Python environment and then install ARC-ACTRIS with `pip` in editable mode:

```bash
git clone https://github.com/nikolaos-siomos/arc.git
cd arc
conda create -n arc-actris python=3.11
conda activate arc-actris
pip install -e ".[dev]"
pytest
```

Using Conda is useful if you already manage scientific Python environments with Conda or Miniconda.

## Runtime dependencies

ARC-ACTRIS requires Python 3.9 or newer and depends on:

- NumPy
- SciPy
- Matplotlib

Development and documentation dependencies are installed through the optional `dev` dependency group:

```bash
pip install -e ".[dev]"
```

This installs testing, packaging, and documentation tools such as `pytest`, `build`, `twine`, `mkdocs`, and `mkdocs-material`.

## Build the package

From the repository root:

```bash
python -m build
```

This creates source and wheel distributions in the `dist/` directory.

## Check the package before upload

```bash
twine check dist/*
```

## Build the documentation

Serve the documentation locally:

```bash
mkdocs serve
```

Build the static site:

```bash
mkdocs build
```
