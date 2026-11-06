"""example.py — three sanity checks a loop could start from.  Run:  python example.py"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pandas as pd
from load import load
d = load(); j = d["joined"]; c = j[j.status == "completed"]
print(f"runs: {len(j)}  completed: {len(c)}")

# 1. Same config, different seed, different attractor: the corpus disagrees with itself.
g = c.groupby("cfg_experiment_id").agg(n=("run_id", "size"), basins=("final_basin", "nunique"),
                                        basin_set=("final_basin", lambda s: "|".join(sorted(set(s)))))
multi = g[(g.n >= 3) & (g.basins > 1)]
print(f"\n[1] config ids with >=3 completed runs: {(g.n>=3).sum()}; of those landing in >1 basin: {len(multi)}")
print(multi.sort_values("n", ascending=False).head(8).to_string())

# 2. Two instruments for "how many authority centres", and they disagree.
#    structural_k : Gini-based (nearest attractor value)   operational_k : ownership-based (channel owners)
e = c[(c.experiment_family == "exp_007") & c.eligibility_overlap.notna()].copy()
e["struct_single"] = (e.structural_k == "k1").astype(int)
e["op_single"] = (e.operational_k == 1).astype(float).where(e.operational_k.notna())
tab = e.groupby("eligibility_overlap").agg(n=("run_id", "size"),
                                            P_single_by_structural_k=("struct_single", "mean"),
                                            P_single_by_operational_k=("op_single", "mean"))
print("\n[2] P(single authority centre) by eligibility overlap, exp_007 — under each instrument:")
print(tab.round(3).to_string())
b = e[e.operational_k.notna()]
print("\n    cross-tabulation where both instruments are present:")
print(pd.crosstab(b.structural_k, b.operational_k.astype(int)).to_string())
print("    -> the rows where structural_k says k2 and operational_k says 1 are the disagreement set.")

# 3. The measurement-artefact check: structural_k is a deterministic bucketing of the final Gini.
s = c[c.structural_k.notna()]
per_label = s.groupby("structural_k").authority_concentration_gini.agg(["min", "max", "size"])
print("\n[3] final Gini range per structural_k label (one value per label => label is a function of Gini):")
print(per_label.round(4).to_string())
