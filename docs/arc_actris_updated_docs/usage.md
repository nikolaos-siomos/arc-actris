# Usage

ARC-ACTRIS is intended to be imported as a Python package.

```python
from arc_actris import arc
```

The main entry point is the `arc` class.

## Basic scattering cross section

```python
from arc_actris import arc

rrs = arc(incident_wavelength=355)
cross_section_355 = rrs.cross_section(cross_section_type="full")

print(cross_section_355)
```

This calculates the Rayleigh scattering cross section at 355 nm by summing the polarized and depolarized molecular scattering components.

## Backscattering cross section and MLDR

To calculate backscattering quantities, initialize the object with `backscattering=True`.

```python
from arc_actris import arc

rrb = arc(
    incident_wavelength=355,
    backscattering=True,
)

bsc_cross_section_355 = rrb.cross_section(cross_section_type="full")
mldr_355 = rrb.mldr(mldr_type="full")

print(bsc_cross_section_355)
print(mldr_355)
```

The `mldr` method is available only for backscattering calculations.

## Temperature

The atmospheric temperature is given in Kelvin. If no temperature is provided, ARC-ACTRIS uses `288.15 K`.

```python
from arc_actris import arc

rrs = arc(
    incident_wavelength=532,
    temperature=285.15,
)

print(rrs.cross_section(cross_section_type="full"))
```

## Custom atmospheric mixture

The `molar_fractions` dictionary defines the relative contribution of the atmospheric gases.

```python
from arc_actris import arc

molar_fractions = {
    "N2": 0.780796,
    "O2": 0.209448,
    "Ar": 0.009339,
    "CO2": 0.000416,
    "H2O": 0.0,
}

rrb = arc(
    incident_wavelength=532,
    temperature=285.15,
    molar_fractions=molar_fractions,
    backscattering=True,
)

print(rrb.cross_section(cross_section_type="full"))
print(rrb.mldr(mldr_type="full"))
```

## Single-gas calculation

To calculate the contribution of one gas, set its molar fraction to `1.0` and the others to `0.0`.

```python
from arc_actris import arc

n2_only = {
    "N2": 1.0,
    "O2": 0.0,
    "Ar": 0.0,
    "CO2": 0.0,
    "H2O": 0.0,
}

rrb = arc(
    incident_wavelength=355,
    molar_fractions=n2_only,
    backscattering=True,
)

print(rrb.cross_section(cross_section_type="full"))
```

## Raman calculation mode

The `mode` argument selects the type of Raman calculation.

Available modes:

- `rotational_raman`
- `vibrational_raman_N2`
- `vibrational_raman_O2`

Example:

```python
from arc_actris import arc

rrb = arc(
    incident_wavelength=355,
    backscattering=True,
    mode="vibrational_raman_N2",
)

print(rrb.cross_section(cross_section_type="full"))
```

## Cross-section types

The `cross_section` method accepts the following `cross_section_type` values:

| Type | Description |
| --- | --- |
| `full` | All polarized and depolarized lines. |
| `main_line` | Polarized part and Q branch. |
| `polarized` | Polarized part only. |
| `depolarized` | Depolarized Raman part only. |
| `O` | Anti-Stokes branch only. |
| `Q` | Q branch only. |
| `S` | Stokes branch only. |
| `wings` | Stokes and anti-Stokes branches. |

Example:

```python
from arc_actris import arc

rrs = arc(incident_wavelength=355)

print(rrs.cross_section(cross_section_type="polarized"))
print(rrs.cross_section(cross_section_type="depolarized"))
print(rrs.cross_section(cross_section_type="wings"))
```

## MLDR types

The `mldr` method accepts the following `mldr_type` values:

| Type | Description |
| --- | --- |
| `full` | MLDR for the full molecular spectrum. |
| `main_line` | MLDR for the main line contribution. |
| `polarized` | Fixed MLDR of the polarized component. |
| `depolarized` | Fixed MLDR of the depolarized component. |

Example:

```python
from arc_actris import arc

rrb = arc(incident_wavelength=355, backscattering=True)

print(rrb.mldr(mldr_type="full"))
print(rrb.mldr(mldr_type="main_line"))
```

## Interference filter example

An interference filter can be included through the `filter_parameters` dictionary. Filter calculations are meaningful for backscattering applications.

```python
from arc_actris import arc

filter_parameters = {
    "transmission_shape": "Gaussian",
    "central_wavelength": 355.0,
    "bandwidth": 0.5,
    "peak_transmission": 1.0,
}

rrb = arc(
    incident_wavelength=355,
    backscattering=True,
    filter_parameters=filter_parameters,
)

print(rrb.cross_section(cross_section_type="full"))
print(rrb.cross_section(cross_section_type="full", normalize=True))
print(rrb.mldr(mldr_type="full"))
```
