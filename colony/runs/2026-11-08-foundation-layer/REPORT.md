# 2026-11-08 foundation layer: report

Leon (8 November): the bit postulates looked unconnected (lineage links are not drawn) and search for "bit" did not find
F1; asked which connection is correct, then "do both": part 1, assumes-style links on the new results, lineage on the site
and title-weighted search; part 2, a proper re-root through a foundation layer.

## Tooling
- `foundation: true` marks a postulate as a foundation postulate (schema); `founded_on` (pinned, top-level, claims, objects
  and predictions) roots an entity in the foundation; E203 if its target is not a foundation postulate, E216 if
  `foundation` is set on a non-postulate.
- derive: `founded_on` is logical (cones, staleness, drawn); `conditions` (holds given) excludes foundation postulates;
  `foundation_of` reports them; build writes `foundation` and `is_foundation` per node; the MCP tools report
  `rests_on_foundation`; layout counts foundation postulates as algebra core.
- site: founded_on drawn as a premise link; the reader shows "Foundation" on F1 to F4 and "Rests on the foundation" on the
  rest, and "Motivated by" / "Motivates" for every lineage link; search weights title matches by the share of the title the
  query covers (stop words left out).
- test: foundation postulates are not conditions (tests/test_validator.py).

## Store
F1 to F4 marked foundation, chained F2 on F1, F3 on F2, F4 on F3; the integer and rational results on F3, the completion and
Frobenius results on F4; the algebra core's 33 roots (24 definitions, 9 premise-free results) on F4. 41 entities bumped with
credit. 881 of 2293 entities now rest on the foundation; no "holds given" list changed. Conventions: "The foundation".

## Checks
Layers 1 to 3 clean before the full check; full check 0 errors 0 warnings; build 0 errors (7320 edges); layout, site, lock;
393 tests and the new one OK; headless browser check of search and reader.
