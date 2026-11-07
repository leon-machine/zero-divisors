---
id: standard-model.frozen-point-first-rung-component
kind: claim
version: 5
title: The frozen point is a first-rung component
status: proved
region: standard-model
subject: mass
tags: [frozen-point, hyperbolic-plane, cosmological-constant]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
- name: Claude Opus 5.5
  role: 'consistency pass, stale unit in the formal and technical levels, H_1 complexified by I_4 as in the proof'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  uses:
  - standard-model.imported-fock-model-twistor-space@5
  - standard-model.imported-frozen-point-grip-thirteenth-refutation@6
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_frozen_point_is_a_rung_vector
- kind: check
  ref: check.py::check_rung_plane_is_a_pair_mode
locators:
  paper: T12
  number: Prop 9.26
  label: prop:firstrung
  line: 1756
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5. The formal and technical levels still said that H_1 is a pair mode over the complex unit I_6, the reading the proof and the GA conversion corrected to I_4 on 21 October (I_6 anticommutes with e_+ and e_-, so it does not complexify H_1; I_4 commutes with them); the two levels now say I_4, as the proof and the check do; no change of mathematics.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: I = nInf - (Lambda/6) nO in H_1 with Q(I) = Lambda/3, the complex unit I_4 commuting with H_1, and H_1 as one pair mode with its dual. Version 3 -> 4.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'Both uses are cited in the proof as premises and are kept. Levels pass: conditions already
      kept; technical and one-liner now write Q(I) for the vector square.'
  source_title: 'The frozen point is a first-rung component'
  source_formal: |-
    In the root paper's conventions for the first completion $\R^{1,3} \to \R^{2,4} = \R^{1,3} \oplus H_{1}$, with $\nO^{(1)} = \tfrac12(e_{-} - e_{+})$, $\nInf^{(1)} = e_{-} + e_{+}$, the frozen point of Fact \claimref{standard-model.imported-frozen-point-grip-thirteenth-refutation} is
    \[
    I \;=\; \nInf^{(1)} - \tfrac{\Lambda}{6}\,\nO^{(1)}, \qquad \ip{I}{I} = -2 \cdot 1 \cdot \bigl(-\tfrac{\Lambda}{6}\bigr) = \tfrac{\Lambda}{3},
    \]
    a vector of the first rung's hyperbolic plane with no spacetime component, equal to the null point at infinity at $\Lambda = 0$. The cosmological scale is therefore already a rung component: the norm of the scale tractor is the product of its two coefficients in the first rung's null pair, and the plane $H_{1}$ is, over $\C$, one of the three pair modes of $W$.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'The complexification of H_1 is read with the complex unit I4 (H_1 + I4 H_1; I4 commutes with H_1, which is orthogonal to spacetime). V_C keeps its formal complexification: no pseudoscalar of Cl(2,4) commutes with the spacetime vectors. Corrected 21 October from an earlier I6 reading. The frozen-point computation is unchanged.'
---

## formal
In the root paper's conventions for the first completion $\R^{1,3} \to \R^{2,4} = \R^{1,3} \oplus H_{1}$, with $\nO^{(1)} = \tfrac12(e_{-} - e_{+})$, $\nInf^{(1)} = e_{-} + e_{+}$, the frozen point of Fact \claimref{standard-model.imported-frozen-point-grip-thirteenth-refutation} is
\[
I \;=\; \nInf^{(1)} - \tfrac{\Lambda}{6}\,\nO^{(1)}, \qquad Q(I) = -2 \cdot 1 \cdot \bigl(-\tfrac{\Lambda}{6}\bigr) = \tfrac{\Lambda}{3},
\]
a vector of the first rung's hyperbolic plane with no spacetime component, equal to the null point at infinity at $\Lambda = 0$. The cosmological scale is therefore already a rung component: the norm of the scale tractor is the product of its two coefficients in the first rung's null pair, and the plane $H_{1}$, complexified by the unit $I_{4}$ as $H_{1} \oplus I_{4}H_{1}$ ($I_{4}$ commutes with $H_{1}$, which is orthogonal to spacetime), is one of the three pair modes of $W$.

## technical
In the conventions of the first completion $\R^{1,3} \to \R^{2,4} = \R^{1,3} \oplus H_{1}$, with $\nO^{(1)} = \tfrac12(e_{-} - e_{+})$ and $\nInf^{(1)} = e_{-} + e_{+}$, the frozen point is $I = \nInf^{(1)} - \tfrac{\Lambda}{6}\nO^{(1)}$, with $Q(I) = \Lambda/3$. It is a vector of the first rung's hyperbolic plane with no spacetime component, and equals the null point at infinity when $\Lambda = 0$.

So the cosmological scale is already a rung component: the norm of the scale tractor is fixed by the product of its two coefficients in the first rung's null pair, and the plane $H_{1}$, complexified by the unit $I_{4}$ as $H_{1} \oplus I_{4}H_{1}$, is one of the three pair modes of $W$.

## lay
The framework builds its extra dimensions as a ladder of rungs, each adding a pair of directions. This result shows that the vector encoding the cosmological scale lies entirely in the first rung, with no part along ordinary spacetime. Its length, which carries the cosmological constant, is set by the product of its two coordinates in that rung.

## one-liner
The frozen point is $I = \nInf^{(1)} - \tfrac{\Lambda}{6}\nO^{(1)}$, a vector of the first rung's hyperbolic plane with $Q(I) = \Lambda/3$.
