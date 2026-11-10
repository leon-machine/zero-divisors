# Fixes DA: released-norm proposal (referee R1 section 1, verdict OVERSTATED, mathematics sound)

Proposal: proposals/synthesis.norm-released-locally-on-isotropic-fields-tracks-dust-and-never-accelerates (id not
renamed). All fixes applied in place at every level. Nothing rebutted.
runcheck: 7 of 7 check functions pass (PYTHONDONTWRITEBYTECODE=1 python3 colony/runcheck.py .../check.py).
check4: pending (orchestrator). validate: pending (orchestrator).

## Referee fixes
1. Title. Now "Under (Mat), bare functional, isotropic flat slices: the released norm tracks dust" (82 characters).
   The referee's wording is longer than the 90-character limit, so its scope items are carried in this shorter
   form and in full in the one-liner: (Mat), bare functional, isotropic, flat slices. "Never accelerates" is gone
   from the title.
2. Prior art. Both 2019 papers added to the extraction note (Alexander, Cortes, Liddle, Magueijo, Sims, Smolin,
   Phys. Rev. D 100, 083506 and 083507; arXiv 1905.10380 and 1905.10382). I read both abstracts on the web today:
   they confirm Lambda made dynamical by a quasi-topological term with its variation in the torsion, Lambda
   proportional to the matter density under homogeneity and isotropy with a constant depending on the equation
   of state, and an infinite constant for pure radiation. "What is new here" replaced by "What is added here: the
   computation in the store's GTG setting and its identification with the stored clock density; the result itself
   is known for the minimal varying-Lambda theory". The formal Reading, technical, lay and one-liner each say the
   result is known in the literature (no year at statement levels). That their term is the Euler term with
   coefficient proportional to 1/Lambda stays flagged as from memory, not verified.
3. "Never accelerates". Took the referee's second option: clause (v) now carries the one-fluid result with proof
   and check. For p = w rho, -1/3 < w < 1/3: y = -2 s'/(n(1 + 3w)), H^2 = rho~ (1 + 3w)^2/(6(1 - 3w)), deceleration
   parameter (1 + 3w)/2 > 0, connection equation holding identically. I rederived it (not copied): alpha =
   kappa^2 rho~/(6 nu), beta = 2 rho~/(3 nu) with kappa = 1 + 3w, nu = 1 - 3w; it agrees with the referee's values.
   Every "no acceleration" sentence is now "for dust alone" or "for one such fluid with u > 0". Mixtures: "not
   treated" at formal, technical, lay and in the note (the referee's float samples are not used).
4. Frame choice (F3). Setting, formal Reading, one-liner and technical now say the clauses on matter are for matter
   on the derived metric of hb^-1 with u varied at fixed (hb, Omega); with matter on u^-1/2 hb^-1 the norm equation
   is the vanishing of eps(F, F) and the clauses on matter are not derived. The referee's hand result for that
   frame (only p = -rho/3) is not asserted, since neither of us machine checked it.
5. Corollaries (F4). Clause (iii) is headed "a corollary of the stored display" and clause (v) "the value of
   Lambda a corollary of the stored display"; clause (ii) names what is added (algebraic form kept with torsion
   and varying norm, the connection equation, the solved dynamics).
6. Lay and technical (F6): "Of the two ways the store holds ... (a search of the store, not a proof that there are
   no others)"; lay adds "spatially flat", "the simplest form of the action", "one kind of matter".
7. One-liner: "bare frozen-point functional (c_3 = c_5 = 0)", "for one fluid", matter on the derived metric.
F7 minor: "half the Friedmann value for the matter density alone (a quarter of the value for matter plus the
tracked term)" at formal and in the note; the check's Einstein map is now contracted with the reciprocal frame in
the algebra (coverage updated).

## Bridge points (findings/bridges.md)
- B4 (definitional identity). Formal (iii), the proof and the note now say the equality with the stored clock
  density is definitional (one derivative dL/du under two variational principles). The check of (iii) gained the
  test that can fail: at four jets with nonzero torsion it reads rho and p off the frame equation of the
  algebra's own Einstein map and confirms that the norm derivative of the density is n s^3/24 times the stored
  polynomial; a control confirms the torsion-free spatial eigenvalue of the same metric gives a different density. My first
  version of this test failed on a sign in reading p off G(e_i) (e_i squares to -1); corrected, it passes.
- B1 (stored w = -1 no-go). synthesis.frozen-phase-spectrum-not-red@4 clause (iv) is cited in the Reading and the
  proof, added to uses and to untouched_premises; not restated.
- B7 (the w = -1/4 branch). synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands@1 (ii)
  is named in the formal Reading, the proof and the note as the one stored structure with a late-time equation of
  state different from -1 (a dark-matter component, effective w = -1/4, unadopted, no pressure derived), added to
  uses and untouched_premises. findings/attack-DA.md D3 and Decision 4 are corrected to name it and say why it is
  not a fallback (wrong sign of wa, matter-density mismatch; both argued, the bridge-hunter's numbers).
- (P1)/(P2). The proposal uses neither label. findings/attack-DA.md now says "the dark-matter premise P1".
- "No stored structure" and the count of two stored ways are labelled argued (a text search, not a cone audit) at
  formal, technical, lay and in the note (rule 4).

## Rules checked
No new imported Fact or postulate; no assumes edge; no citation of a proposal; no graviton at any level; no number
from memory and no outside date at a statement level; two uses edges added, both to stored entities at their
current versions (4 and 1), each cited by claimref in the proof.

## Changed files
entity.md (title, uses, extraction note, Setting, (ii) to (v), Reading, technical, lay, one-liner), proof-main.tex
((i), (iii), (v), Reading), check.py (Einstein map by contraction; torsion extension test; one-fluid closed form),
coverage.yaml (three omits lines, two untouched premises).

## For the orchestrator
The check changed, so check4's mutation test has to be rerun. New named constants: EOS_LOW, EOS_HIGH, FLUID_C,
LAPSES, QUARTER. The one-fluid samples sit at s = 1 only (elsewhere the closed form is irrational).
