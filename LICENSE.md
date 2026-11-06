# Licence

**Epistemic Governance Lab — simulation run archive, v1.0**
Prepared 3 November 2026 from the lab's datapack of 2026-11-02T04:17:56Z; revised 6 November 2026.

Licence holder: Sebastian Bohle, THARP — Thyke Applied Research & Prototyping
<sebastian@tharp.science> · <https://tharp.science>

## What this licence covers

The files identified in section "Package identity" below are released under the
**Creative Commons Attribution 4.0 International licence (CC BY 4.0)**:
<https://creativecommons.org/licenses/by/4.0/>

They are:

- `tables/` — all CSV tables
- `raw/scorecards/`, `raw/manifests/`, `raw/configs/`
- `raw/eglab_mirror.sqlite` and `raw/datapack-MANIFEST.json`
- `README.md`, `load.py`, `example.py`, `SHA256SUMS.txt`

You may copy, redistribute, transform and build on these files for any purpose,
including commercially, provided you give attribution (below) and indicate if
changes were made. Derived datasets are welcome; please state what was derived
from what.

## Package identity

This licence applies to exactly the files whose SHA-256 digests are listed in
`SHA256SUMS.txt`, which covers every file in the package except this one.
The digest of `SHA256SUMS.txt` itself, at release:

```
sha256(SHA256SUMS.txt) = 8105746f03c71ec36a017f126a0cff0ebede7f9904625b158ac0e2ca6abaac0a
files listed            = 1590
```

Verify with `sha256sum SHA256SUMS.txt` and `sha256sum -c SHA256SUMS.txt`. A file
whose digest does not appear in that list is not covered by this licence, and a
package whose `SHA256SUMS.txt` has a different digest is not this release.

## What this licence does not cover

- **The engine.** `epilab` (<https://github.com/tharp-science/epilab>) is a separate work
  under the MIT licence. Private engine commits referenced in
  `engine_provenance.csv` are not released.
- **The raw per-tick event logs.** They remain on the lab host and are not part of
  this package or this licence.
- **The lab's research vault** (working notes, interpretations, specifications).
  Not included, not released. Anything from it shared with you separately is
  shared under its own terms, in writing.
- **The paper.** Bohle 2026, "Governing Epistemic Systems", is a separate work
  with its own terms at SSRN.

CC BY 4.0 applies to the files listed in `SHA256SUMS.txt` and to nothing else at
the lab.

## Attribution

Please cite the data as:

> Bohle, S. (2026). *Epistemic Governance Lab — simulation run archive, v1.0*
> (prepared 3 Nov 2026 from datapack 2026-11-02, revised 6 Nov 2026;
> SHA256SUMS digest 8105746f…baac0a). THARP — Thyke Applied Research & Prototyping,
> https://tharp.science.
> Engine: https://github.com/tharp-science/epilab. Model: Bohle, S. (2026), "Governing
> Epistemic Systems", SSRN, https://doi.org/10.2139/ssrn.6417898.

When you publish a result from this archive, say which instrument it rests on
(`structural_k` or `operational_k`), which run set, and which engine attribution
class (`attribution` in `runs.csv`). The caveats in `README.md`, section 4, are
part of the record; a result stated without them is not a result from this
archive as released.

## No warranty

The data are provided as is. Section 4 of the README lists known defects,
near-constant metrics and unverified units. Nothing here has been peer reviewed.

— Sebastian Bohle, Berlin, November 2026
