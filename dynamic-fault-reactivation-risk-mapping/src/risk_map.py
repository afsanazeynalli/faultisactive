"""Illustrative Monte Carlo Coulomb-threshold screening from supplied trajectories."""
from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

REQUIRED = {
    "segment_id", "time", "shear_mpa", "normal_mpa", "pore_pressure_mpa", "alpha",
    "friction_mean", "friction_sd", "cohesion_mean_mpa", "cohesion_sd_mpa",
}

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="Input CSV")
    parser.add_argument("--output", type=Path, default=Path("outputs"))
    parser.add_argument("--draws", type=int, default=20000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    if args.draws < 1:
        parser.error("--draws must be positive")
    df = pd.read_csv(args.input)
    missing = REQUIRED - set(df.columns)
    if missing:
        parser.error("missing columns: " + ", ".join(sorted(missing)))
    if df.empty:
        parser.error("input contains no rows")
    rng = np.random.default_rng(args.seed)
    probs, means, lows, highs = [], [], [], []
    for row in df.itertuples(index=False):
        mu = np.maximum(0.0, rng.normal(row.friction_mean, row.friction_sd, args.draws))
        cohesion = np.maximum(0.0, rng.normal(row.cohesion_mean_mpa, row.cohesion_sd_mpa, args.draws))
        f = abs(row.shear_mpa) - mu * (row.normal_mpa - row.alpha * row.pore_pressure_mpa) - cohesion
        probs.append(float(np.mean(f >= 0.0)))
        means.append(float(np.mean(f)))
        lows.append(float(np.quantile(f, 0.025)))
        highs.append(float(np.quantile(f, 0.975)))
    df["threshold_exceedance_fraction"] = probs
    df["cff_mean_mpa"] = means
    df["cff_p2_5_mpa"] = lows
    df["cff_p97_5_mpa"] = highs
    args.output.mkdir(parents=True, exist_ok=True)
    summary_path = args.output / "risk_summary.csv"
    plot_path = args.output / "risk_map.png"
    df.to_csv(summary_path, index=False)
    pivot = df.pivot(index="segment_id", columns="time", values="threshold_exceedance_fraction")
    fig, ax = plt.subplots(figsize=(max(6, 1.2 * len(pivot.columns)), max(3, 0.55 * len(pivot.index))))
    im = ax.imshow(pivot.to_numpy(), vmin=0, vmax=1, cmap="magma", aspect="auto")
    ax.set_xticks(range(len(pivot.columns)), [str(x) for x in pivot.columns], rotation=35, ha="right")
    ax.set_yticks(range(len(pivot.index)), [str(x) for x in pivot.index])
    ax.set_xlabel("Time")
    ax.set_ylabel("Fault segment")
    ax.set_title("Illustrative Coulomb threshold exceedance fraction")
    fig.colorbar(im, ax=ax, label="Fraction of parameter draws with F ≥ 0")
    fig.tight_layout()
    fig.savefig(plot_path, dpi=180)
    plt.close(fig)
    print(f"Wrote {summary_path} and {plot_path}")
    print("Interpretation: model-conditional mechanical threshold exceedance only; not slip/seismicity probability.")

if __name__ == "__main__":
    main()
