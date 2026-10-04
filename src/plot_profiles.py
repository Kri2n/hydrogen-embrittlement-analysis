"""Plot hydrogen concentration profiles for several charging times."""

from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
from src.diffusion import concentration_profile

# Illustrative effective diffusivity (m^2/s). Trapping makes this much lower
# than lattice diffusivity. Replace with a cited value for your steel.
D_EFF = 1e-11
C_SURFACE = 1.0  # normalised surface concentration

depth_m = np.linspace(0, 5e-3, 400)           # 0 to 5 mm
times_h = [1, 6, 24, 72]                       # charging times in hours

fig, ax = plt.subplots(figsize=(7, 4.5))
for t_h in times_h:
    c = concentration_profile(depth_m, t_h * 3600, D_EFF, C_SURFACE)
    ax.plot(depth_m * 1000, c, label=f"{t_h} h")

ax.set_xlabel("Depth from surface (mm)")
ax.set_ylabel("Normalised hydrogen concentration, C / Cs")
ax.set_title("Hydrogen penetration vs charging time (illustrative D_eff)")
ax.legend(title="Charging time")
ax.grid(alpha=0.3)
fig.tight_layout()

out = Path(__file__).resolve().parent.parent / "figures" / "concentration_profiles.png"
fig.savefig(out, dpi=300)
print(f"Saved {out}")