# Epistemic Governance Lab — simulation run archive, v1.1

705 runs of an agent-based simulation of how authority concentrates in a network of nodes
that assert, contest and settle claims under six swappable governance primitives. Every run
carries its full configuration, a scorecard of ~40 outcome metrics, a provenance record of the
engine version that produced it, and its place in the lab's cohort / hypothesis structure.

Prepared 3 November 2026 from the lab's nightly datapack (generated 2026-11-02T04:17:56Z).
Revised 6 November 2026. DOI (all versions): https://doi.org/10.5281/zenodo.24001501.
Repository: https://github.com/tharp-science/eglab-buildday-dataset.
Engine: https://github.com/tharp-science/epilab (MIT). Model description: Bohle 2026,
"Governing Epistemic Systems", SSRN doi:10.2139/ssrn.6417898.

**Licence for the data: CC BY 4.0, scoped to the files listed in `SHA256SUMS.txt`. See
`LICENSE.md`, which also anchors the package by the digest of `SHA256SUMS.txt`.** The engine's
MIT licence does not cover these files.

---

## 1. The problem this archive is offered against

*How do independent research agents surface conflicting assumptions without a central
reconciler, keeping the disagreement and the provenance rather than collapsing them?*

The archive is a good testbed for that because it already contains unreconciled disagreement
of three kinds, all visible from the tables alone (run `example.py`):

1. **The corpus disagrees with itself.** 55 configurations have three or more completed
   replicate runs; 29 of them land in more than one attractor basin across seeds. Identical
   assumptions, different outcomes. Nothing in the data says which seed is "right".
2. **Two instruments disagree about the same quantity.** "How many authority centres did the
   run end with?" is measured two ways. `structural_k` is Gini-based: the final authority Gini
   snapped to the nearest configuration-implied attractor value. `operational_k` is
   capture-based: the number of distinct agents that are top owner of at least one governance
   channel (forward or reversion) at a share of 80% or more, so it is 2 only when both channels
   are captured by different agents. On the 577 Grid-07 runs where both exist they disagree on
   100. In every one of the 100, two agents sit at the weight cap (`structural_k` = `k2`) but
   only one channel has a ≥80% owner (`operational_k` = 1; 42 forward-only, 58 reversion-only).
   The disagreement is between "two agents at the weight cap" and "two channels each captured
   by one agent". The lab's headline Grid-07 result — unpublished; vault evidence notes EV-006
   and EV-007 — is that the probability of a single centre rises from 0.52 to 0.78 as
   eligibility overlap goes from 0 to 1. It exists under the first instrument (logistic slope
   1.14, p = 0.0002) and is not significant under the second (0.81 to 0.86; slope 0.56, p =
   0.13, n = 577). Neither instrument has been retired; both are in `metrics.csv` (the mirror
   adds the classifier keys to the scorecard metrics; the raw `scorecard.json` files do not
   carry them).
3. **The apparatus disagrees with its own history.** 121 runs executed on engine code that was
   not the commit checked out when they started (`engine_provenance.csv`, `attribution`
   column); 85 predate the first commit (their event logs match engine code committed later).
   The lab's provenance record states that scorecards were re-scored in July 2026, so a
   scorecard was not necessarily produced by the engine that produced its event log; which
   scorecards were re-scored is not itemised, and the batch-01 `_retroactive` scorecards are
   recovered originals. "Which code produced this number" has a documented but non-trivial
   answer per run.

A research loop that handles this archive honestly has to carry all three without resolving
them by fiat. That is the exercise.

### Loop tasks that fit a day

- **Disagreement ledger.** Two or more agents each answer "does eligibility overlap drive
  single-centre collapse?" from the tables; each must declare which instrument it used and why,
  and the loop records the conflict with provenance instead of averaging or voting.
- **Artefact detection.** Give an agent `metrics.csv` without telling it how `structural_k` is
  made. Can it discover from the data that the label is a deterministic function of
  `authority_concentration_gini` (check 3 in `example.py`), and flag any conclusion built on
  it as instrument-dependent?
- **Replicate adjudication.** For the 29 multi-basin configurations: is the split explained by
  anything in the config or metrics, or is it genuine basin competition? Agents must keep the
  unresolved cases as unresolved.
- **Provenance-aware claims.** Every claim the loop emits names the run set, the instrument,
  and the engine attribution class it rests on; claims with mixed attribution are marked.

---

## 2. Files

```
README.md                      this file
CITATION.cff                   citation metadata (DOI, version); GitHub reads it for "Cite this repository"
LICENSE.md                     CC BY 4.0 for the files listed in SHA256SUMS.txt; scope, attribution, exclusions
SHA256SUMS.txt                 digest of every file in the package except LICENSE.md
load.py                        pandas loader:  from load import load; d = load()
example.py                     the three disagreement checks above
tables/
  runs.csv                     705 rows, one per run: identity, config summary, outcome, provenance  (START HERE)
  metrics.csv                  705 rows, 39 scalar scorecard metrics, wide
  metrics_nested_long.csv      per-key counts for the three nested metrics (1,630 rows)
  metrics_dictionary.csv       every metric: coverage, type, range, description where known
  engine_provenance.csv        705 rows: which engine commit produced each run, and how that was decided
  scorecard_hypotheses_long.csv 290 rows: per-run hypothesis verdicts embedded in scorecards (early experiments only)
  cohorts.csv, campaigns.csv, hypotheses.csv, condition_points.csv, designs.csv,
  cohort_metrics.csv, closeouts.csv, notes.csv, note_links.csv
                               the lab's research-management layer: which runs belong to which
                               cohort, campaign and hypothesis, with status, dates and links.
                               Structure only; rationale text redacted (see section 6)
raw/
  scorecards/<run_id>/scorecard.json    703 files (of the 4 aborted runs, 2 have none)
  manifests/<run_id>/run-manifest.json  703 files: run_id, seed, created_at, source_config_path, full config
  configs/*.yaml                        166 experiment configuration files (the full battery; 64 were run)
  eglab_mirror.sqlite                   the relational mirror all tables were derived from (14 tables;
                                        four redacted as in section 6)
  datapack-MANIFEST.json                generation record of the source datapack
```

**Not included:** the raw per-tick event logs (632 GB logical). They live on the lab host only.
Every quantitative result in the lab's 25 July 2026 preprint-comparison brief was derived from
these scorecards plus the database. The March 2026 preprint's Figure 1 (Gini time series) and
its §4.3 event-log inspection required event-level data that is not in this package; its
scorecard-level figures (§4.1 rates, Table 1 Gini values) are present in the `_retroactive`
scorecards. No event-level access is needed for the tasks above.

---

## 3. Data model in five sentences

A **run** is one execution of the engine from a **config** (YAML) and a **seed** for a fixed
number of ticks (5,000 for 687 runs). The config declares **node groups** (persona, count,
optional per-group authority types and reversibility tolerance), **claim groups** (ground truth,
difficulty, ambiguity), a **network** (Watts-Strogatz small world, p = 0.1 in every run; k = 6
in 673 runs, k = 4, 12 or 20 in the remaining 32), and which of the six **primitives** are on
(boundary, lineage, authority, mediation, confidence, reversibility; a seventh, observation,
exists in the engine and is off in every run here). At the end the engine writes a
**scorecard** of metrics; a classifier then assigns a **final basin** label. Runs are grouped
into **cohorts** under **campaigns**, which test **hypotheses**; that layer is in the small CSVs
and in `notes.csv`.

### Key columns in `runs.csv`

| column | meaning |
|---|---|
| `run_id` | `<experiment_id>_<seed>_<UTC timestamp>`; joins everything |
| `experiment_family` | `exp_000` to `exp_009`; **exp_007 (Grid-07) is 581 of 705 runs** and the only family with a dense design |
| `cfg_experiment_id` | configuration identity; runs sharing it are replicates differing only by seed |
| `eligibility_overlap` | Grid-07 design variable in {0, 0.125, ..., 1}: how much the eligible actor sets of the governance channels overlap. 579 runs have it |
| `final_basin` | classifier label: `k0`, `k1`, `k2`, `k3`, `off_attractor`, `na`, or `k2:caps(a,b)` for heterogeneous-cap designs |
| `node_groups` | compact composition string, e.g. `fnl_founding_nodex3;fnh_founding_nodex5;pn_peripheral_nodex52;...` |
| `prim_*`, `mediation_mode` | which primitives were on; mediation `structured` in 674 runs, `none` in 9 |
| `weight_cap`, `revisability_rate` | dynamics parameters (5.0 and 0.005 in the Grid-07 scaffold) |
| `attribution` | engine provenance class: `match_head_class` 493, `match_other_commit` 121, `match_pre_git` 85, `untested` 5, `unmatched` 1 |
| `matched_commit` | the engine commit that reproduces the run's event log byte for byte (first match found, not proven unique) |
| `config_schema` | `node_groups` (687 runs) or `legacy_nodes` (18 early runs with an explicit node list) |

### Key columns in `metrics.csv`

`authority_concentration_gini` (and `_start`), `structural_k`, `operational_k`, `epistemic_accuracy`,
`epistemic_stability_index`, `contested_claim_resolution_rate`, `interpretive_drift_rate`,
`false_consensus_rate`, `cycling_events_count`, `total_reversions`, channel-capture measures
(`forward_channel_top1_share`, `channel_top1_owner_overlap`, ...). Coverage differs by metric
because the scorecard vocabulary grew over the campaign: `operational_k` exists for 637 runs,
`false_consensus_rate` for 206. `metrics_dictionary.csv` has coverage and ranges for all of them.

---

## 4. Caveats to read before drawing any conclusion

- **`structural_k` is a function of Gini, not of ownership.** Each label corresponds to exactly
  one final-Gini value (except `k2`, whose range 0.019 to 0.073 spans several sub-designs). Any
  result stated in terms of `structural_k` is a result about weight accumulation, not about how
  many actors hold authority. Use `operational_k` for ownership questions, and say which you used.
  The March 2026 preprint's k is inferred from Gini in the same way; channel ownership was
  verified there by event-log inspection for one run, not measured across runs. This caveat
  applies to the preprint as much as to this archive.
- **Classifier limitation, identified while preparing this release (October 2026), not yet
  fixed.** For heterogeneous-cap designs the attractor label space is degenerate (e.g.
  caps(5,5,5,5,3) and caps(7,5,3,3,3,3) imply identical Gini) and the classifier has no tie
  handling. The 18 `k2:caps(...)` runs in this archive all landed exactly on their attractor and
  were not affected, but the classifier will silently pick a label if you add runs near those
  values.
- **Scorecard provenance and engine provenance are separate questions.** The lab's provenance
  record states that scorecards were re-scored in July 2026, so a scorecard was not necessarily
  produced by the engine that produced its event log (`attribution`, `matched_commit`). Which
  scorecards were re-scored is not itemised; the batch-01 `_retroactive` scorecards carry the
  March 2026 original values.
- **The public engine snapshot predates some runs.** `epilab` lacks successor-selection and
  shock-event code present in later private commits, so byte-exact replay from public code is
  not possible for every run. `matched_commit` refers to the private history.
- **Several metrics are near-constant** across this corpus (e.g. `epistemic_accuracy` is 0.35 in
  almost every run; `interpretive_drift_rate` is about 0.499 throughout). They are not broken;
  the standard scaffold does not move them. Treat them as uninformative here, not as findings.
- **`contested_claim_resolution_rate` is not a proportion.** It is governance transitions out
  of the `contested` state per tick (`epilab/engine/scorecard.py`). Compare only within
  dynamics regime: no-cycling runs sit at a floor of claims/ticks (0.02 for 100 claims over
  5,000 ticks); live-cycling runs run at about 25 per tick. `b3_absorbing_state_artefact` marks
  the boundary.
- **4 aborted runs** (`status`), 2 without scorecards; 5 runs `untested` and 1 `unmatched` in
  provenance. Keep them; do not impute.
- **Numbers in this README** (counts, the two gradients, the 100-run disagreement set) were
  computed from these tables by `example.py` and checked against the lab's sources on
  6 November 2026. Re-run it rather than quoting them.

---

## 5. Quick start

```
pip install pandas              # the only dependency
cd eglab-buildday-dataset
python example.py
```

```python
from load import load, scorecard, manifest
d = load()
j = d["joined"]                                  # runs x metrics, 705 rows
g7 = j[(j.experiment_family == "exp_007") & (j.status == "completed")]
g7.groupby("eligibility_overlap")[["authority_concentration_gini", "operational_k"]].mean()
scorecard(j.run_id[0])                           # the raw JSON for one run
manifest(j.run_id[0])["config"]["node_groups"]   # its full config
```

SQL users: `raw/eglab_mirror.sqlite` is the source of every table; `runs.config_json` holds the
full config per run and `run_metrics.metrics_json` the full scorecard metrics block.

---

## 6. Provenance of this package

Source: the lab's nightly datapack (`eglab-datapack.sh` on host `epistemic-lab`), mirrored by
Syncthing, read on 3 November 2026. Tables derived from the datapack's SQLite mirror; raw
scorecards, manifests and configs copied unchanged. This edition was first assembled for the
Claude Impact Lab build day in Berlin (7 November 2026) and was first released as v1.0.

**What was held back.** The lab's research vault (138 markdown notes) is not in this package;
it is the researcher's working notes. The research-management tables (`notes.csv`,
`cohorts.csv`, `campaigns.csv`, `hypotheses.csv`) carry structure only — ids, types, status,
dates and links. Note titles and vault paths, cohort purposes and theses, campaign theses and
hypothesis titles were removed before release because they contain unpublished results and
working hypotheses. They were removed from the CSVs and from `raw/eglab_mirror.sqlite` (tables
`notes`, `cohorts`, `campaigns`, `hypotheses`; columns dropped, database vacuumed). The mirror
is therefore a redacted copy of the lab's database, not a byte-identical one; every other table
in it is unchanged.

Prepared with AI assistance (Claude, Anthropic) at the owner's request. Reviewed against the
lab's sources (preprint, vault, engine code, provenance records) on 6 November 2026; reviewed,
licensed and revised by the owner on 6 November 2026. v1.1 (same day) adds the Zenodo DOI and
`CITATION.cff`; the data files are unchanged from v1.0 (Zenodo 10.5281/zenodo.24001502).

**How to cite.** Bohle, S. (2026). *Epistemic Governance Lab — simulation run archive, v1.1.*
THARP — Thyke Applied Research & Prototyping. CC BY 4.0. https://doi.org/10.5281/zenodo.24001501
(concept DOI, resolves to the latest version; each version has its own DOI on Zenodo). The
SHA256SUMS digest of this release is stated in `LICENSE.md`; this file and `CITATION.cff` are
inside the sums, so it cannot appear in them.

Contact: Sebastian Bohle, THARP — Thyke Applied Research & Prototyping (https://tharp.science).
