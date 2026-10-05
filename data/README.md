# Hydrogen Embrittlement Analysis

Python workflow for modelling hydrogen diffusion in steel and quantifying
hydrogen-induced loss of ductility, with uncertainty analysis and validation.

## Objectives

- Model hydrogen diffusion with Arrhenius temperature dependence
- Validate the numerical solver against the analytical solution of Fick's second law
- Quantify the relationship between hydrogen concentration and ductility
- Estimate fit parameters with 95% confidence intervals
- Test the statistical significance of the observed embrittlement

## Methods

Python | NumPy | SciPy | pandas | Matplotlib | pytest

## Key findings

- Fitted model: RA = RA0 · exp(−k · C_H), with RA0 = [value ± CI] % and k = [value ± CI] per ppm
- The fit recovered the true synthetic parameters within the 95% confidence intervals
- Uncharged vs. highest-hydrogen group: p = [value] (Welch's t-test)

## Results

![Ductility fit](figures/ductility_fit.png)
![Concentration profiles](figures/concentration_profiles.png)
![Arrhenius plot](figures/arrhenius_plot.png)

[2-3 sentences of YOUR physical interpretation]

## Limitations

- The tensile data in `data/synthetic_tensile.csv` is **simulated**, generated
  from a known model to validate the analysis. It is not experimental data.
- Diffusion uses lattice diffusivity from [source]; trapping is not modelled.
- The embrittlement model is empirical, not a mechanistic fracture model.

## How to run

    pip install -r requirements.txt
    python -m pytest
    python -m src.generate_data

Then open `notebooks/01_analysis.ipynb` and run all cells.

## Repository structure

    data/        synthetic dataset and documentation
    notebooks/   analysis notebook
    src/         diffusion model and data generator
    figures/     output figures
    tests/       unit tests

## References

[Full citation of your diffusion source]