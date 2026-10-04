import numpy as np
from src.diffusion import arrhenius_diffusivity, concentration_profile


def test_diffusivity_increases_with_temperature():
    low = arrhenius_diffusivity(1e-7, 10e3, 300)
    high = arrhenius_diffusivity(1e-7, 10e3, 400)
    assert high > low


def test_surface_concentration_equals_boundary_value():
    c = concentration_profile(0.0, 100.0, 1e-11, 5.0)
    assert np.isclose(c, 5.0)


def test_concentration_decreases_with_depth():
    x = np.array([0.0, 1e-5, 1e-4])
    c = concentration_profile(x, 3600, 1e-11, 5.0)
    assert np.all(np.diff(c) < 0)


def test_concentration_never_negative():
    x = np.linspace(0, 1e-2, 50)
    c = concentration_profile(x, 3600, 1e-11, 5.0)
    assert np.all(c >= 0)