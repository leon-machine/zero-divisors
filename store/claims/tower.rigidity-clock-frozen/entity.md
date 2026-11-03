---
id: tower.rigidity-clock-frozen
kind: claim
version: 5
title: Rigidity; the clock is frozen
status: proved
region: tower
subject: tower
tags: [towers-by-residue, clifford-classification, obstruction-types]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T03, deposited version
review: typed
about:
- obj.transport.obstruction-types
- obj.tower.tower
derivations:
- name: main
  uses:
  - tower.commuting-copies@5
  - tower.matrix-amplification-structural-properties@3
  - tower.morita-equivalence-algebra-amplification@1
  - transport.existence-classification-type-c@4
  - std-algebra.sta-matrix@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T03.py
  tags:
  - num:3.6
- kind: check
  ref: check.py::check_clock_and_centre_frozen
- kind: check
  ref: check.py::check_full_corner_is_ground
- kind: check
  ref: check.py::check_physical_tower_is_quaternionic
locators:
  paper: T03
  number: Thm 3.6
  label: thm:rigidity
  line: 270
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.sta-matrix where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: residue, centre and omega^2 constant along floors (no type C over a simple ground), the full corner equal to the twisted ground, and the physical tower as Mat_{2^(k+1)}(H). Version 2 -> 3. Sample inputs moved to module level; anticommutation of the twisted generators now checked for both orders; no change to what is tested. Version 3 -> 4.'
  env: theorem
  typing:
    by: ai-typing-pass
    note: 'All four edges are genuine premises of the proof, including the imported Morita fact.'
---

## formal
Along the tower: the transport charge $d = p - q \bmod 8$ is constant; the division-ring type, simplicity class, and centre of every floor equal those of the ground floor; every floor is Morita equivalent to the ground floor; and the obstruction taxonomy of \cite{ButlerT1} is floor-independent: in particular a type-C obstruction (a central idempotent) never arises by transport from a simple ground algebra, at any height. The physical tower is $\Cl(1{+}k, 3{+}k) \cong \Mat_{2^{k+1}}(\HH)$, frozen at clock position $6$. Bott periodicity manifests as immediate freeze, not eventual return.

## technical
Along the tower the transport charge $d = p - q \bmod 8$ is constant, since $(p{+}k) - (q{+}k) = p - q$. Each floor is a matrix algebra over the ground floor, so its division-ring type, simplicity class and centre equal those of the ground floor, and it is Morita equivalent to the ground floor. The obstruction taxonomy is therefore floor-independent; in particular a type-C obstruction, a central idempotent, never arises by transport from a simple ground algebra, at any height.

For the physical tower, $\Cl(1{+}k, 3{+}k) \cong \Mat_{2^{k+1}}(\HH)$ sits at clock position $6$ for every $k$: Bott periodicity shows up as immediate freeze, not eventual return.

## lay
Building the tower by adding pairs of opposite-signed directions never changes the essential type of the algebra. Every floor has the same underlying number system, the same centre and the same kinds of obstruction as the ground floor. For the spacetime algebra, every floor is a matrix algebra over the quaternions, so the eight-step Bott clock does not advance along the tower: it stays where it starts.

## one-liner
Every floor of the tower shares the ground floor's charge, division-ring type, centre, simplicity class, Morita class and obstruction taxonomy, so the physical tower $\Cl(1{+}k, 3{+}k) \cong \Mat_{2^{k+1}}(\HH)$ is frozen at clock position $6$.
