# References

This page collects scientific and software reference information for ARC-ACTRIS.

## Software citation

If you use ARC-ACTRIS in scientific work, please cite the relevant ARC-ACTRIS software release and the associated scientific publication, if available.

A recommended software citation format is:

```text
Siomos, N., Haimerl, M., and Binietoglou, I. ARC-ACTRIS: Algorithm for Rayleigh and Raman Calculations. Version 1.0.0.
```

Update the citation with the final release version, DOI, and repository URL once the package is archived or released.

## License

ARC-ACTRIS is distributed under the GNU Affero General Public License v3.0.

See the `LICENSE` file in the repository for the full license text.

## Project documentation

The documentation is built with MkDocs.

Install the package and documentation dependencies with either a Python virtual environment or a Conda environment.

### With `venv`

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
mkdocs serve
```

### With Conda

```bash
conda create -n arc-actris python=3.11
conda activate arc-actris
pip install -e ".[dev]"
mkdocs serve
```

To build the static site:

```bash
mkdocs build
```

## Related scientific context

ARC-ACTRIS is intended for atmospheric lidar applications involving molecular Rayleigh and Raman scattering. The package supports calculations of:

- Rayleigh scattering cross sections
- Molecular backscattering cross sections
- Rotational Raman line contributions
- N2 and O2 vibrational Raman modes
- Molecular linear depolarization ratio, MLDR
- Interference-filter-weighted effective backscatter quantities

## Reproducibility

For reproducible calculations, record the following information together with your results:

- ARC-ACTRIS version
- Python version
- NumPy, SciPy, and Matplotlib versions
- Incident wavelength
- Temperature
- Gas molar fractions
- Raman calculation mode
- Whether backscattering was enabled
- Filter parameters, if used
