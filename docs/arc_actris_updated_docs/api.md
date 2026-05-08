# API Reference

This page summarizes the public API of ARC-ACTRIS.

## Import

```python
from arc_actris import arc
```

## `arc_actris.arc`

```python
arc(
    incident_wavelength,
    temperature=288.15,
    molar_fractions=None,
    max_J=100,
    backscattering=False,
    mode="rotational_raman",
    filter_parameters=None,
)
```

Main class for Rayleigh and Raman molecular scattering calculations.

### Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `incident_wavelength` | `float` | required | Incident wavelength in air, in nm. |
| `temperature` | `float` | `288.15` | Atmospheric temperature in K. |
| `molar_fractions` | `dict` or `None` | `None` | Atmospheric gas molar fractions. If omitted, a dry-air default mixture is used. |
| `max_J` | `int` | `100` | Maximum rotational quantum number. |
| `backscattering` | `bool` | `False` | If `True`, calculate backscattering cross sections instead of total scattering cross sections. |
| `mode` | `str` | `rotational_raman` | Raman calculation mode. |
| `filter_parameters` | `dict` or `None` | `None` | Optional interference filter settings. |

### Default molar fractions

If `molar_fractions=None`, the default dry-air mixture is used:

```python
{
    "N2": 0.780796,
    "O2": 0.209448,
    "Ar": 0.009339,
    "CO2": 0.000416,
    "H2O": 0.0,
}
```

### Valid modes

| Mode | Description |
| --- | --- |
| `rotational_raman` | Elastic and pure rotational Raman lidar channel applications. |
| `vibrational_raman_N2` | N2 vibrational Raman calculation. |
| `vibrational_raman_O2` | O2 vibrational Raman calculation. |

## `cross_section`

```python
cross_section(cross_section_type="full", normalize=False)
```

Calculate the molecular scattering or backscattering cross section by summing over the relevant molecular lines and gases.

### Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `cross_section_type` | `str` | `full` | Selects which part of the molecular spectrum is included. |
| `normalize` | `bool` | `False` | If `True`, normalize the result by the filter transmission at the incident wavelength. Applies only when a filter is provided and the selected cross-section type supports normalization. |

### Valid `cross_section_type` values

| Value | Description |
| --- | --- |
| `full` | All polarized and depolarized lines. |
| `main_line` | Polarized part and Q branch. |
| `polarized` | Polarized component only. |
| `depolarized` | Depolarized Raman component only. |
| `O` | Anti-Stokes branch only. |
| `Q` | Q branch only. |
| `S` | Stokes branch only. |
| `wings` | Stokes and anti-Stokes branches. |

### Example

```python
from arc_actris import arc

rrb = arc(incident_wavelength=355, backscattering=True)

sigma_full = rrb.cross_section(cross_section_type="full")
sigma_main = rrb.cross_section(cross_section_type="main_line")
sigma_wings = rrb.cross_section(cross_section_type="wings")

print(sigma_full)
print(sigma_main)
print(sigma_wings)
```

## `mldr`

```python
mldr(mldr_type="full")
```

Calculate the molecular linear depolarization ratio, MLDR.

This method requires the object to be initialized with `backscattering=True`.

### Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `mldr_type` | `str` | `full` | Selects which molecular contribution is used for MLDR calculation. |

### Valid `mldr_type` values

| Value | Description |
| --- | --- |
| `full` | MLDR including all relevant molecular lines. |
| `main_line` | MLDR for the main line contribution. |
| `polarized` | Fixed MLDR of the polarized component. |
| `depolarized` | Fixed MLDR of the depolarized component. |

### Example

```python
from arc_actris import arc

rrb = arc(incident_wavelength=355, backscattering=True)

print(rrb.mldr(mldr_type="full"))
print(rrb.mldr(mldr_type="main_line"))
```

## Main attributes

An initialized `arc` object stores several useful attributes.

| Attribute | Description |
| --- | --- |
| `incident_wavelength` | Incident wavelength in nm. |
| `temperature` | Atmospheric temperature in K. |
| `molar_fractions` | Gas molar fractions used in the calculation. |
| `max_J` | Maximum rotational quantum number. |
| `backscattering` | Whether the object calculates backscattering quantities. |
| `linear_molecules` | Linear molecules included in the calculation. |
| `all_molecules` | All molecules included in the calculation. |
| `gas_parameters` | Molecular parameters used internally. |
| `filter_parameters` | Interference filter parameters, if provided. |
| `filter_transmission` | Filter transmission function, if provided. |
| `xsection_pol` | Polarized scattering or backscattering cross sections. |
| `xsection_depol_line` | Depolarized line cross sections. |
| `lamda_pol` | Wavelengths of polarized scattering. |
| `lamda_depol_line` | Wavelengths of depolarized Raman lines. |

## Interference filter parameters

The optional `filter_parameters` dictionary may include:

| Key | Description |
| --- | --- |
| `transmission_shape` | Filter shape: `Gaussian`, `Lorentzian`, `Tophat`, or `Custom`. |
| `AOI` | Angle of incidence in degrees. |
| `ref_index_IF` | Effective refractive index of the interference filter. |
| `extra_shift` | Additional wavelength shift in nm. |
| `filter_path` | Path to an ASCII file containing a custom transmission curve. |
| `filter_file_delimiter` | Delimiter used in the custom filter file. |
| `filter_file_header_rows` | Number of header rows to skip in the custom filter file. |
| `wavelengths` | Wavelength array for a custom filter. |
| `transmissions` | Transmission array for a custom filter. |
| `central_wavelength` | Central wavelength of a theoretical filter. |
| `bandwidth` | Filter bandwidth in nm. |
| `peak_transmission` | Maximum filter transmission. |
| `off_band_transmission` | Off-band transmission for a Tophat filter. |
