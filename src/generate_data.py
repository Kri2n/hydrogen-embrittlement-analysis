"""Generate SYNTHETIC hydrogen-embrittlement tensile data.

This data is simulated, NOT experimental. It exists so the analysis code can
be validated: because we know the true parameters used to create the data,
we can check that the analysis recovers them.
"""

from pathlib import Path
import numpy as np
import pandas as pd

# True parameters used to create the data (the analysis should recover these)
TRUE_RA0 = 60.0    # reduction in area of uncharged steel (%)
TRUE_K = 0.35      # embrittlement rate (per ppm hydrogen)
NOISE_SD = 2.0     # scatter in measurements (% reduction in area)
SEED = 42          # fixed seed so results are reproducible


def synthetic_ductility(C_H, RA0=TRUE_RA0, k=TRUE_K, noise_sd=NOISE_SD, rng=None):
    """Reduction in area (%) vs hydrogen concentration (ppm).

    Model: RA = RA0 * exp(-k * C_H) + Gaussian noise
    """
    rng = rng or np.random.default_rng(SEED)
    C_H = np.asarray(C_H, dtype=float)
    RA = RA0 * np.exp(-k * C_H) + rng.normal(0, noise_sd, size=C_H.shape)
    return np.clip(RA, 0, None)  # reduction in area cannot be negative


def make_dataset(repeats=5):
    """Build a table with several repeat tests at each hydrogen level."""
    rng = np.random.default_rng(SEED)
    levels = np.array([0, 0.5, 1, 2, 3, 5, 7, 10])  # ppm
    C_H = np.repeat(levels, repeats)
    RA = synthetic_ductility(C_H, rng=rng)
    return pd.DataFrame({
        "H_conc_ppm": C_H,
        "RA_percent": RA.round(2),
        "data_type": "synthetic",
    })


if __name__ == "__main__":
    out = Path(__file__).resolve().parent.parent / "data" / "synthetic_tensile.csv"
    out.parent.mkdir(exist_ok=True)
    df = make_dataset()
    df.to_csv(out, index=False)
    print(f"Saved {len(df)} rows to {out}")