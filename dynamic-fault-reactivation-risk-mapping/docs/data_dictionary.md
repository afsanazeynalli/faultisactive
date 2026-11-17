# Data dictionary

Input is a UTF-8 CSV with one row per fault segment and time step.

| Column | Unit/type | Meaning |
|---|---|---|
| `segment_id` | text | Stable fault-segment identifier |
| `time` | text | Time label (ISO date or simulation step) |
| `shear_mpa` | MPa | Shear traction magnitude |
| `normal_mpa` | MPa | Total normal traction; compression positive |
| `pore_pressure_mpa` | MPa | Pore pressure at the segment |
| `alpha` | dimensionless | Effective-stress coefficient |
| `friction_mean` | dimensionless | Mean friction coefficient for sampling |
| `friction_sd` | dimensionless | Standard deviation for friction sampling |
| `cohesion_mean_mpa` | MPa | Mean cohesion for sampling |
| `cohesion_sd_mpa` | MPa | Standard deviation for cohesion sampling |

The example is synthetic. Code treats shear, normal stress, pore pressure, and alpha as fixed inputs; only friction and cohesion are sampled. Extend the observation/model layer before representing other uncertainty sources. Use a coherent unit system and document stress sign conventions.
