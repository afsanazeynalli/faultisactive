# Dynamic Fault Reactivation Risk Mapping

A compact research starter pack for uncertainty-aware screening of fault-segment mechanical stability during conventional oilfield water injection.

> **Scope:** this repository contains a reproducible screening prototype, not a coupled reservoir simulator or operational decision system. It computes a Coulomb-style failure function from supplied stress and pressure histories, propagates parameter uncertainty with Monte Carlo sampling, and reports the fraction of samples at or above the selected mechanical threshold. This fraction is not an earthquake, slip, leakage, or rupture probability.

## Research question
Does sequentially updating an uncertainty ensemble with new pressure and operational observations improve held-out prediction and injection-scenario ranking versus static and non-updated baselines? This is a hypothesis to test, not an established research gap or claim of superiority. The novelty claim requires a systematic literature and patent review.

## Quick start

Requires Python 3.10+.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python src/risk_map.py --input data/example_segments.csv --output outputs
```

Writes `outputs/risk_summary.csv` and `outputs/risk_map.png`. Example inputs are synthetic and illustrative. Values use MPa; positive normal stress means compression.

## Contents
- `src/risk_map.py` — Monte Carlo Coulomb screening and visualization.
- `data/example_segments.csv` — synthetic fault-segment/time-step inputs.
- `docs/research_brief.md` — aim, methods, validation plan, limitations, references, and candidate tools.
- `docs/data_dictionary.md` — input definitions and units.
- `CITATION.cff` — citation metadata.

## Core calculation
For each segment/time step and parameter draw: `F = |tau| - mu * (sigma_n - alpha * P) - c`. Here shear traction `tau`, compressive normal traction `sigma_n`, pore pressure `P`, friction `mu`, effective-stress coefficient `alpha`, and cohesion `c` must use consistent conventions and units. `F >= 0` marks exceedance of this simplified threshold under the sampled assumptions. The code samples uncertain friction and cohesion from truncated normal distributions; stress and pressure values are supplied inputs. It does not infer coupled pressure/stress changes or assimilate observations.

## Research path
1. Review fault-slip-potential, probabilistic integrity, coupled flow-geomechanics, and patent literature; refine novelty.
2. Reproduce analytical/numerical benchmarks before using site data.
3. Replace supplied trajectories with a verified coupled pressure-geomechanics model.
4. Define and document an observation model and sequential update; preserve held-out data.
5. Compare static screening, single realization, non-updated ensemble, and updated ensemble with calibration/proper scoring metrics where labels exist.
6. Keep mechanical threshold exceedance distinct from observed slip, leakage, and induced seismicity.

## Data and responsible use
Do not commit confidential, licensed, or personally identifiable well/fault data. Document license and permission for every dataset. Keep raw data out of Git where redistribution rights are unclear. This prototype supports research and method development; it is not a substitute for qualified site-specific geomechanical review, operating limits, or regulatory requirements.

## License
MIT for this starter code. This does not grant rights to third-party datasets, papers, or software cited here. See `LICENSE`.
