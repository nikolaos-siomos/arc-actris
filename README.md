# ARC-ACTRIS
[![Tests](https://github.com/nikolaos-siomos/arc-actris/actions/workflows/tests.yml/badge.svg)](https://github.com/nikolaos-siomos/arc-actris/actions/workflows/tests.yml)
[![Docs](https://github.com/nikolaos-siomos/arc-actris/actions/workflows/docs.yml/badge.svg)](https://github.com/nikolaos-siomos/arc-actris/actions/workflows/docs.yml)
[![Python](https://img.shields.io/badge/python-3.9--3.13-blue.svg)](https://www.python.org/)
[![License: AGPL v3](https://img.shields.io/badge/license-AGPL--3.0-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
ARC-ACTRIS is a Python package for molecular Rayleigh and Raman scattering calculations in atmospheric lidar applications.

Full documentation is available at:

https://nikolaos-siomos.github.io/arc-actris/

## Installation

From PyPI:

```bash
pip install arc-actris
```

Development installation with `venv`:

```bash
git clone https://github.com/nikolaos-siomos/arc-actris.git
cd arc
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

Development installation with Conda:

```bash
git clone https://github.com/nikolaos-siomos/arc-actris.git
cd arc
conda create -n arc-actris python=3.11
conda activate arc-actris
pip install -e ".[dev]"
pytest
```

## Basic usage

```python
from arc_actris import arc

rrs = arc(incident_wavelength=355)
cross_section_355 = rrs.cross_section(cross_section_type="full")

print(cross_section_355)
```

Backscattering and molecular linear depolarization ratio, MLDR:

```python
from arc_actris import arc

rrb = arc(incident_wavelength=355, backscattering=True)

print(rrb.cross_section(cross_section_type="full"))
print(rrb.mldr(mldr_type="full"))
```

## Documentation

Full documentation is available at:

https://nikolaos-siomos.github.io/arc-actris/

Alternatively, it can also be built with MkDocs.

Install the development dependencies first:

```bash
pip install -e ".[dev]"
```

Serve the documentation locally:

```bash
mkdocs serve
```

Build the static documentation site:

```bash
mkdocs build
```

## License

ARC-ACTRIS is distributed under the GNU Affero General Public License v3.0. See [LICENSE](LICENSE).
