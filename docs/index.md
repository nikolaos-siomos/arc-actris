# ARC-ACTRIS

ARC-ACTRIS is a Python package implementing the Algorithm for Rayleigh and Raman Calculations.

It calculates molecular scattering and backscattering cross sections, Raman line contributions, and molecular linear depolarization ratios for atmospheric lidar applications.

## Main features

- Rayleigh and Raman scattering calculations
- Molecular backscattering cross sections
- Molecular linear depolarization ratio, MLDR
- Dry and moist air mixtures
- Rotational Raman and vibrational Raman modes
- Optional interference filter transmission handling

## Quick example

```python
from arc_actris import arc

rrb = arc(
    incident_wavelength=355,
    backscattering=True,
)

cross_section = rrb.cross_section(cross_section_type="full")
mldr = rrb.mldr(mldr_type="full")

print(cross_section)
print(mldr)
