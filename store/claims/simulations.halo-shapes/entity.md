---
id: simulations.halo-shapes
kind: claim
version: 2
title: Halo shapes
status: conjectured
region: simulations
subject: dark-matter
tags:
- halos-and-clusters
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14b, deposited version
review: typed
lineage:
  motivated_by:
  - simulations.imported-cluster-shapes
  - simulations.confinement-scale-does-not-matter
locators:
  paper: T14b
  number: Obs 7.2
  label: obs:halo
  line: 486
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: simulations.imported-mirror repinned 5 -> 6 after reviewing its G1 restatement (the cold mirror is an exception to P2 at its version-1 reach, P2 as scoped leaves xi free, and the cold mirror then needs a non-equilibrium descent; the simulated content is unchanged); the use here holds as cited.'
  typing:
    by: ai-typing-pass
    note: 'Kept conjectured: this is a simulation output the paper labels observation level, with no proof
      text to copy; motivated by the imported cluster-shape measurement it is compared with and by the
      corollary that makes the sheet matter a fluid. Levels pass: the lay said reading (C) stays within
      the spread of the CDM runs, but only one of its two seeds does, so it now says so, and it keeps
      the isolated-assembly setting, premise S3 and the observation level; the one-liner keeps the observation
      level.'
  env: observation
  flags:
  - conjecture with no referenced motivation
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises:
    - simulations.s1-one-species-per-tower
    - simulations.s2-sheet-fluid
    - simulations.s3-mirror-cluster
    - simulations.s4-our-matter
    - simulations.s5-halos
    - simulations.c-odd-towers-collisionless
    - simulations.imported-unit-ball-rule-family
    - simulations.imported-mirror
    added_dependants: []
    added_about: []
    verdict: connected
    note: 'Simulation output: given a premise-only derivation assuming S1 to S5 and C and using the imported
      composition and mirror; no proof text, since a conjecture carries none.'
derivations:
- name: simulation
  uses:
  - simulations.imported-unit-ball-rule-family@4
  - simulations.imported-mirror@6
  assumes:
  - simulations.s1-one-species-per-tower@2
  - simulations.s2-sheet-fluid@2
  - simulations.s3-mirror-cluster@1
  - simulations.s4-our-matter@1
  - simulations.s5-halos@1
  - simulations.c-odd-towers-collisionless@2
  note: 'Simulation output at observation level: the runs are set up under Premises S1 to S5, and reading
    (C) under Premise C, with the composition of the imported unit-ball rule and the mirror; no proof
    text, since the result is computed, not proved.'
---

## formal
Isolated assembly from eight progenitors makes rounder halos than infall along filaments, so the measure is the ratio to the CDM run (Table \ref{tab:halo}), and with two seeds the criterion is whether both seeds of a composition lie below both of CDM's. In reading (W) they do: the ellipticity is $0.43$ of CDM's (seed ratios $0.56$ and $0.35$), and the sheet fluid, supported by its pressure, is cored (its density is flat within the noise inside about $75$ kpc) and rounder than the collisionless dark matter (inside $300$ kpc, $c/a$ of $0.78$ and $0.85$ against $0.59$ and $0.44$ in the two seeds). It is also less concentrated: $38$ percent of the mass within $300$ kpc, near its measured share of $0.41$ within $r_{200}$, but only $10$ to $12$ percent inside $50$ kpc, where settled mirror matter is $39$ to $43$ percent. In reading (C) the ratio is $0.77$ ($0.63$ and $0.85$), and the second seed overlaps CDM's range: rounder, not excluded. Inside $300$ kpc in seed $11$ its $c/a$ matches CDM's ($0.62$ against $0.64$) and its $b/a$ is larger ($0.93$ against $0.71$), so the halo is closer to oblate symmetry than CDM's. In reading (C), $39$ and $29$ percent of the mass inside $50$ kpc (seeds $11$ and $23$) is settled mirror matter: the over-cooling of a dissipative gas simulated without feedback (Premise S3), which also makes the inner profiles unreliable. The compositions with the mirror settled from the start sit at $0.75$ to $0.78$ of CDM; at equal sheet fluid, the mixed count with its mirror gas gives $0.49$ and without it $0.75$, and the mirror gas without sheet fluid, reading (C), gives $0.77$: the mirror gas and the sheet fluid together round the halo more than either alone. Computed; observation level.

## technical
In simulations of a cluster assembled in isolation from eight progenitors, with two seeds, the projected ellipticity is compared with the cold dark matter (CDM) run of the same seed, since isolated assembly makes even CDM halos rounder than real clusters. In reading (W) both seeds lie below both of CDM's: the ellipticity is $0.43$ of CDM's, and the sheet fluid is cored inside about $75$ kpc, rounder than the collisionless dark matter and less centrally concentrated.

In reading (C) the ratio is $0.77$ and one seed overlaps CDM's range, so the halo is rounder but not excluded; there the over-cooling of mirror gas simulated without feedback (premise S3) settles much of the inner mass and makes the inner profiles unreliable. The mirror gas and the sheet fluid together round the halo more than either alone. These are computed results at observation level.

## lay
Simulations of a galaxy cluster built in isolation from the proposed dark-matter mixture, two versions of each, were compared with the same cluster built from standard cold dark matter. If part of the dark matter flows as a fluid, the cluster comes out clearly rounder than the standard one in both simulated versions. If it does not, the cluster is only somewhat rounder and one of its two versions falls within the spread of the standard runs, so it is not ruled out by this test; there the inner profiles are unreliable, because the simulated mirror gas over-cools without feedback (premise S3). These are computed results at observation level.

## one-liner
In simulated cluster assembly, at observation level, reading (W) gives halos rounder than CDM in both seeds (ellipticity $0.43$ of CDM's), while reading (C) gives $0.77$ and overlaps CDM's range: rounder, not excluded.
