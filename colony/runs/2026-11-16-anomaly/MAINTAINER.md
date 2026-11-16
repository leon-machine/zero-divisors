# Maintainer pass after run 2026-11-16-anomaly (acting for Leon, the maintainer)

Leon has accepted the run's five proposals (now in store/claims/):
  synthesis.colour-angle-term-under-the-stored-maps-and-no-colour-anomalous-phase-of-the-rung-coupling
  synthesis.phase-of-the-quark-mass-determinant-on-the-covariant-completion
  synthesis.conditional-inheritance-of-b-minus-l-and-the-conversion-coefficient-as-a-gram-ratio
  synthesis.spectral-asymmetry-on-real-projective-five-space-from-monogenic-polynomials
  synthesis.order-four-structure-on-real-projective-walls-and-the-signed-count-modulo-sixteen
and made four decisions on 16 November 2026:
  D1. Register the physical colour angle (the coefficient of the colour four-form plus the phase of the quark mass
      determinant) as a free input of the series: a new postulate with a refutation condition, in the format of
      synthesis.matter-asymmetry-registered-free-input, with the literature it needs imported as Facts (the neutron
      dipole bound and its conversion to the angle; the physical angle as the sum, and its shift under a rotation
      with colour coefficient). op.strong-cp is then settled by its own success clause ("or record it as a free
      input with a refutation condition"). In addition, store the exact quarter-turn texture as a conjecture: one-type
      symmetric quark stages, real first stages, one sector's second stage real and the other's at an exact quarter
      turn; then det(M_u M_d) is real with nonzero Jarlskog invariant at tree level, and |V_us| follows from mass
      ratios. It carries its hypotheses (c_q real; delta_q real and nonzero), is not protected by a symmetry, has an
      unfixed sign (zero or a half turn), and the one-loop mass phase is not computed.
  D2. The colour-angle result is accepted as restated (done).
  D3. Import the anomalous weak process (B + L violated, B - L kept), its equilibrium coefficient and the lattice
      freeze-out as Facts, checked at source; restate synthesis.matter-asymmetry-registered-free-input to one light
      doublet (argued, on the level branch) with B - L per unit entropy between 2.45e-10 and 2.68e-10 (the
      broken-phase end 12/37 and the symmetric-phase end 28/79); add assumes edges from the new conditional
      inheritance theorem to neutrino.r-descent-reheats-below-lower-heavy, neutrino.real-breaking-assumption and
      synthesis.matter-asymmetry-registered-free-input. op.matter-asymmetry-origin stays partial.
  D4. The modulo-16 anomaly statement of the literature stays unimported. op.order-four-anomaly-and-sixteen stays
      open and is restated: the count (half the spectral asymmetry, 1/16 per component) is derived; "sixteen, not
      fifteen" is conditional on the unimported statement and on a gauged omega, and for three generations only;
      that the count constrains no stored stage is argued; the one live question is whether omega is gauged where
      the continuous group does not contain it.
Standing choices for this pass (not decisions of substance): the classical background facts named in the accepted
results ((CA1) to (CA3), (L2), (K), torus conjugacy) stay named background and are not imported; the hypotheses
(W) no washout, (T) thermal descent state and (Gr) the gravitational pairing stay hypotheses of the theorem and
become attack items of op.matter-asymmetry-origin; two premise questions raised in review are recorded as open
items and not decided: how the stored CPT conjugation acts on the gauge sector, and which identification of
orientations the common-ceiling-coupling premise uses for the angle.

You are one of two maintainer agents with disjoint ownership (your message lists yours). Edit store/ directly in
LAB = /home/claude/phys-graph (branch run/2026-11-16-anomaly). Never spawn agents, never commit or push, never
touch anything outside LAB. You are not blind: read verify/R1.md, R2.md, R3.md, findings/attack-A.md,
findings/attack-B.md and findings/fixes-*.md of this run for the material (the drafted registration is in
findings/attack-B.md, section S4; the literature checked at source is listed in both findings files).

## Rules
- Read CONTRIBUTING.md, docs/CONTRIBUTING-rules.md and `python3 colony/labcli.py conventions '{}'`; copy the format
  of existing entities of the same kind (a registered free input: synthesis.matter-asymmetry-registered-free-input;
  an imported Fact: any synthesis.imported-* entity; a conjecture: any entity with status conjectured).
- New imported Facts: state only what the source states, with full reference, and say for each item whether it was
  read at source in this pass (use web search and fetch; do it) or is cited from memory. Do not import anything
  the decisions do not name.
- Changing an existing entity: version + 1; keep every file in its folder (orig-proof-main.tex in particular); add
  an `amendments` entry {version, kind: correction | restatement, defect, evidence?} and a credit entry
  {name: Claude Fable 5.2, role: <what changed>, version: <new>, source: maintainer pass 2026-11-16 (anomaly)},
  keeping every existing credit entry unchanged; add under `extraction` an entry
  `maintainer_pass_2026_11_16: {by: maintainer-2026-11-16, date: '2026-11-16', note: <one or two sentences>}`.
  Keep `proposed_by` as it is. A wording-only change keeps the version. New entities carry
  `credit: [{name: Leon Butler, role: direction and decision}, {name: Claude Fable 5.2, role: drafting, source:
  maintainer pass 2026-11-16 (anomaly)}]`.
- Change the least that carries the decision. Do not strengthen any statement. Where a decision makes a stored
  sentence conditional, say on what. Label argued as argued.
- House style: no em dashes; never "honest"/"honestly"; never "load-bearing"; Q(v) for the square of a vector;
  macros only from store/notation.yaml; no mention of agents, runs, referees or method names in store text
  (changelog `by:` and `source:` fields excepted). Geometric algebra language; declare outside_ga where needed.
- store/open_problems.yaml and store/open_problems_settled.yaml are edited by BOTH agents, on different entries.
  Never hold their content across tool calls: make each edit with one short Python read-modify-write script that
  replaces exact strings inside your own entry and asserts each replacement happened exactly once, then verify
  with `python3 -c "import yaml; yaml.safe_load(open('store/open_problems.yaml'))"`.
- Exact arithmetic in any check you touch or write; after changing a check run
  `python3 colony/runcheck.py <folder>/check.py` then `python3 colony/check4.py <folder>` (one at a time; 2 CPUs;
  never kill other processes).
- Validation: after your edits run
  `python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon 2>&1 | tail -40`
  and fix every error or new warning on YOUR entities (pin warnings on dependants of entities whose version you
  raised are expected: list them, do not repin). The other agent is editing other entities at the same time; ignore
  findings that are only theirs. Do not run the full check, `tp repin`, `tp lock`, `tp build` or the site build.
- Write colony/runs/2026-11-16-anomaly/maintainer-<your name>.md: every entity created or changed with old -> new
  version and one line each; dependants whose CONTENT (not just pins) may be affected, with what you think should
  happen to each; anything you could not do and why. Your final reply: a short summary of that file (under 300 words).

## M1 owns (strong CP and the order-four problem)
1. New postulate synthesis.colour-angle-registered-free-input (D1), from the draft in findings/attack-B.md S4,
   tightened to the accepted results as they now stand (the restated colour-angle result and the determinant-phase
   result). It uses both accepted results and the new Facts.
2. New imported Facts for it: (a) the neutron dipole bound and its conversion to the angle (first search the store
   for an existing Fact holding the neutron bound, with find_text "neutron"; extend that one by a version rather
   than duplicating it); (b) the physical angle as the bare coefficient plus the phase of the quark mass
   determinant, and its shift under a rotation with colour coefficient. Where the literature states that a half
   turn conserves CP and its exclusion is model-dependent, say so (the source checked in review is in R1.md).
3. New conjecture (D1): the exact quarter-turn texture, status conjectured, resting on clause(s) of
   synthesis.phase-of-the-quark-mass-determinant-on-the-covariant-completion and on
   synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase; with its refutation condition
   (the parameter-free Cabibbo relation; a computed one-loop mass phase above the neutron bound) and everything it
   does not claim.
4. The accepted colour-angle entity: excuse its two untouched premises (W405: dark-matter.mirror-tower-copy-one and
   synthesis.imported-chern-weil-and-chern-simons-forms) the way the store does it (see how existing entities
   record untouched_premises), without decorative premise() calls.
5. The accepted order-four-structure entity: its hypothesis (H1) names the sibling result; make it a uses edge to
   synthesis.spectral-asymmetry-on-real-projective-five-space-from-monogenic-polynomials at its stored version, if
   the entity format allows it without changing the statement.
6. Open problems (entries you own: op.strong-cp, op.order-four-anomaly-and-sixteen, op.rung-unit,
   op.second-order-breaking, op.r-premises-external):
   - op.strong-cp: settle it. Look at store/open_problems_settled.yaml and at how the most recent settlements were
     recorded and moved; record what is proved, what is argued (completeness over stored fields and maps), the
     decision, and the residual items, which go where they belong: the two premise questions above and the one-loop
     mass phase as attack items of op.second-order-breaking (the up-down phase) or as a short note entity if no
     problem fits. Correct the sentence that the flag is the vacuum's one CP-violating datum (with the stored
     quark-stage phase it is not).
   - op.order-four-anomaly-and-sixteen: restate per D4 (statement, known, attack, success), keeping it open
     (status reformulated). The known text's bordism citation is now checked at source (see findings).
   - op.rung-unit: one sentence in known: the second invariant W(N) is not constrained by the colour angle (no
     phase symmetry of the rung coupling has a colour coefficient).
   - op.second-order-breaking: the up-down phase item now points at the quarter-turn conjecture and at the result
     that the determinant is real exactly there.
   - op.r-premises-external: nothing unless a stored sentence is now false; check its flag item against the
     accepted colour-angle result and leave it if consistent.

## M2 owns (the asymmetry)
1. New imported Facts (D3), each read at source in this pass: (a) the anomalous weak process: B + L changed, B - L
   kept, and that it is in equilibrium above the weak transition ('t Hooft 1976; Kuzmin, Rubakov and Shaposhnikov
   1985); (b) the equilibrium relation between baryon number and B - L (Harvey and Turner 1990; Khlebnikov and
   Shaposhnikov 1996, hep-ph/9607386, eqs. (17) to (19)), as the sources state it, with the conventions under which
   the accepted theorem's Gram ratio reproduces it; (c) the lattice freeze-out and crossover temperatures
   (D'Onofrio, Rummukainen and Tranberg 2014, arXiv:1404.3565). One Fact or three, whichever matches how the store
   groups imports.
2. The accepted theorem synthesis.conditional-inheritance-of-b-minus-l-and-the-conversion-coefficient-as-a-gram-ratio:
   point its hypothesis on the anomalous process at the new Fact(s) (uses), and add the three assumes edges of D3.
   Do not change its statement beyond replacing "not stored" by the reference where the Fact now supplies it.
3. synthesis.matter-asymmetry-registered-free-input: restate per D3 (version + 1, amendment): one light doublet on
   the level branch (argued), B - L per unit entropy between 2.45e-10 and 2.68e-10, conditional on the new Facts;
   say which end is which and that the stored mirror check (dark-tower-matter.mirrors-composition, which uses
   28/79) sits at the symmetric-phase end. Do not change that stored check (Leon's decision of 12 November stands).
4. synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them clause (vi) says the process and the
   coefficient are literature cited from memory: update that sentence to cite the new Fact(s) (wording-only if the
   statement is unchanged).
5. Open problems (entries you own: op.matter-asymmetry-origin, op.qft-structural-inputs):
   - op.matter-asymmetry-origin: status stays partial. Update statement, known and attack: the conditional
     inheritance theorem is written and proved as algebra; the process is imported; the doublet count is argued at
     one; item (a) is done except the equilibrium after the descent; the relaxing-angle item is answered (no phase
     symmetry of the rung coupling has a colour coefficient, proved for that coupling with both family matrices
     invertible; completeness over stored fields argued; the angle is now a registered free input,
     synthesis.colour-angle-registered-free-input, which M1 is creating: cite it by that id); new attack items:
     (W) the washout rate through virtual heavy singlets, which Premise (R) does not imply; (T) the thermal state
     of the descent above the freeze-out; (Gr) the gravitational pairing of B - L on the fifteen (trace -1 per
     family), a candidate in-framework source given a CP-odd datum, with no rate computed.
   - op.qft-structural-inputs: one sentence in known under the doublet count: on the level branch one doublet is
     light at the freeze-out of the anomalous process (argued), with the entity id.
