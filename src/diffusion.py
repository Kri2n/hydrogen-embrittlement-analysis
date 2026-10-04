"""Hydrogen diffusion in steel: basic physics functions."""

import numpy as np
from scipy.special import erfc

# Gas constant, J/(mol K)
R = 8.314

# Example values for hydrogen in BCC iron (lattice diffusion).
# TODO: check these against a cited paper or textbook and add the reference here.
D0_EXAMPLE = 7.23e-8   # m^2/s   (pre-exponential factor)
Q_EXAMPLE = 5.69e3     # J/mol   (activation energy)
#references values from [1] K. Kiuchi and R. B. McLellan, “The solubility and diffusivity of hydrogen in well-annealed and deformed iron,” Acta Metallurgica, vol. 31, no. 7, pp. 961–984, Jul. 1983, doi: 10.1016/0001-6160(83)90192-X.

def arrhenius_diffusivity(D0, Q, T):
    """Diffusion coefficient (m^2/s) at temperature T (kelvin).

    D = D0 * exp(-Q / (R*T))
    D0 in m^2/s, Q in J/mol.
    """
    return D0 * np.exp(-Q / (R * T))


def concentration_profile(x, t, D, C_surface):
    """Hydrogen concentration at depth x (m) after time t (s).

    Analytical solution of Fick's second law for a semi-infinite solid
    with a constant surface concentration:
        C(x, t) = C_surface * erfc(x / (2*sqrt(D*t)))
    """
    return C_surface * erfc(x / (2.0 * np.sqrt(D * t)))