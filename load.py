"""load.py — stdlib+pandas loader for the eglab build-day dataset.
Usage:  from load import load; d = load()   # d["runs"], d["metrics"], d["joined"], ...
"""
import json, os, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__))
def load(root=HERE):
    t = lambda n: pd.read_csv(os.path.join(root, "tables", n), low_memory=False)
    d = {n[:-4]: t(n) for n in os.listdir(os.path.join(root, "tables")) if n.endswith(".csv")}
    d["joined"] = d["runs"].merge(d["metrics"], on="run_id", how="left")
    return d
def scorecard(run_id, root=HERE):
    with open(os.path.join(root, "raw", "scorecards", run_id, "scorecard.json")) as f: return json.load(f)
def manifest(run_id, root=HERE):
    with open(os.path.join(root, "raw", "manifests", run_id, "run-manifest.json")) as f: return json.load(f)
