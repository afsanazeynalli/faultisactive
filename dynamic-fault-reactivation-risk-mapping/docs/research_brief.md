# Research brief

## Aim
Develop and validate a dynamic, uncertainty-aware workflow for mapping fault-segment mechanical reactivation potential during conventional oilfield water injection, integrating fault geometry, pressure evolution, stress change, operational history, and new observations.

## Testable hypothesis
An ensemble updated sequentially with pressure and operational observations may improve blind prediction and scenario ranking relative to static Coulomb screening and a non-updated coupled-model ensemble. Improvement must be measured on held-out data; it is not assumed.

## Questions
1. How do pressure diffusion and poroelastic stress transfer jointly affect fault stability?
2. Which uncertainties dominate stability-map variability?
3. Does updating improve predictions at held-out times, wells, or fault segments?
4. Can scenario comparisons reduce predicted instability while preserving pressure-maintenance objectives?

## Proposed workflow
1. **Data model:** version and quality-check interpreted fault surfaces, reservoir properties, stress indicators, pressure observations, and injection/production histories. Record units, provenance, uncertainty, temporal alignment, and gaps.
2. **Baseline physics:** reproduce analytical or published numerical benchmarks. Model transient flow and poroelastic stress transfer; add fault transmissibility and constitutive behavior only when supported by data and solver capability.
3. **Uncertainty:** represent fault orientation, friction/cohesion, permeability/connectivity, initial stress, rock properties, measurement error, and model discrepancy. Check identifiability and prior sensitivity.
4. **Sequential update:** define state, parameter, and observation models; compare Bayesian/ensemble methods and prevent information leakage from validation data.
5. **Outputs:** by segment and time, report stability-margin distributions, threshold-exceedance fraction, sensitivity, coverage, and scenario differences. Flag low-information regions.
6. **Validation:** benchmark reproduction, synthetic truth-known cases, then blind held-out field observations where permitted. Compare static ranking, one best-fit realization, non-updated ensemble, and updated ensemble.

## Evaluation
Where meaningful labels and sample sizes exist, assess probability calibration, Brier/log score, pressure/stress prediction error, stability-margin error, missing-data sensitivity, and scenario-rank consistency. Report uncertainty and failed cases. If slip labels are sparse, do not claim validated event prediction.

## Scope and limitations
The included script is an illustrative Monte Carlo wrapper around a simplified Coulomb criterion. It does not solve fluid flow, geomechanics, fault slip, leakage, or seismicity. Formula and sign convention are not universal; site-specific constitutive modeling and validation are required. Mechanical threshold exceedance under model assumptions is not equivalent to fault slip or an earthquake.

## Selected references
- Fan, Z., Eichhubl, P., & Newell, P. (2019). Basement fault reactivation by fluid injection into sedimentary reservoirs: Poroelastic effects. *Journal of Geophysical Research: Solid Earth*, 124, 7354–7369. [DOI](https://doi.org/10.1029/2018JB017062). Demonstrates joint direct pressure and poroelastic effects in modeled cases.
- Passelègue, F. X., Brantut, N., & Mitchell, T. M. (2018). Fault reactivation by fluid injection: Controls from stress state and injection rate. *Geophysical Research Letters*, 45, 12,837–12,846. [DOI](https://doi.org/10.1029/2018GL080470). Experimental results show stress state and injection rate can affect reactivation conditions.
- Park, J.-W., et al. (2020). Modeling of fluid injection-induced fault reactivation using coupled fluid flow and mechanical interface model. *International Journal of Rock Mechanics and Mining Sciences*, 132, 104373. [DOI](https://doi.org/10.1016/j.ijrmms.2020.104373). Coupled TOUGH-FLAC modeling benchmarked against an injection experiment.
- Ground Water Protection Council. (2021 update). *Potential Induced Seismicity: Guide*. [PDF](https://www.gwpc.org/wp-content/uploads/2022/12/FINAL_Induced_Seismicity_2021_Guide_33021.pdf). Operational context and discussion of Fault Slip Potential tools.

## Candidate modeling tools
- [OpenGeoSys hydro-mechanics benchmarks](https://www.opengeosys.org/stable/docs/benchmarks/hydro-mechanics/) include coupled-process examples, including injection/production in a linear poroelastic medium. Benchmarks establish solver behavior; they do not validate a site model by themselves.
- [MOOSE PorousFlow documentation](https://mooseframework.inl.gov/modules/porous_flow/) describes fluid/heat/geomechanics modeling components. Assess fit and version requirements before adoption.
- Record exact solver version, input deck, mesh, boundary conditions, parameter sources, and convergence evidence in an applied study. This starter repo itself only needs Python, NumPy, and Matplotlib.

## Bibliographic and novelty note
The proposal's novelty statement is intentionally framed as a question because adjacent coupled and uncertainty-aware research exists. Perform and document a systematic literature and patent search before claiming novelty. Confirm bibliographic records and reuse permissions before formal publication.
