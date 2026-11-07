# Consistency pass, reader R10: conformal-spacetime, mass, neutrinos (205 entities)

Depth read (stated so the counts are not over-read): every level and proof of the 205 entities was scanned by
script (house style, bare units, unit tokens per level, legacy macros, Q(v), galang); the first 21
conformal-spacetime claims (T09 core: Fock model, Chevalley pairing, spinor identification, skew lines, chiral
planes, incidence chart, reality, local twistor transport, ordering results) were read in full with their proofs; for
the other 112 claims, objects and predictions the formal and one-liner levels were read, and the proofs or arithmetic
of about twenty were checked by hand; the 72 notes were read at their formal openings. tp check (layers 1-3) after
the edits: no error or warning on any R10 entity (store-wide: E111 on
synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase, W222 on two non-R10 entities).

## Fixed (old -> new version)
1. correspondence.incidence-relation-chart 6 -> 7: clause (4)(iii) wrote I_6 = e_0...e_5 with no frame and "acts on
   CS as -I_7"; now names the T09 basis (I_6 = a_1a_2b_1b_2b_3b_4 gives -I_7) and the opposite orientation (the
   store's I_6 = I_4E = -a_1a_2b_1b_2b_3b_4 gives +I_7), the clause holding for either. Exact computation in the
   extraction note; script colony/runs/2026-11-07-consistency/work-R10/i6_on_cs.py.
2. correspondence.local-twistor-transport-ascended-spinor-connection 9 -> 10: the proof reads Penrose's i as I_7, the
   incidence relation as I_6; one sentence now says so and that the composite, quadratic in the unit, is unaffected.
3. standard-model.frozen-point-first-rung-component 4 -> 5: formal and technical still said H_1 is a pair mode "over
   the complex unit I_6" (corrected to I_4 in the proof and check on 21 October; I_6 anticommutes with e_+-); now I_4.
4. standard-model.transported-frozen-point 5 -> 6: proof wrote the square of I as the inner product; now Q(I).
5. angle.imported-conformal-model-null-rotations 5 -> 6: proof used U without defining it; definition added.
6-14. Legacy twistor macros (\T, \PT, \T', \Sc, \Sc') written as \CS, \PCS, \CSm, \Som, \Spi in nine notes:
   note.correspondence.setting-incidence-encodes-completion 1 -> 2, note.correspondence.setting-introduction 1 -> 2,
   note.correspondence.setting-machine-verification 4 -> 5, note.correspondence.setting-successor-problems 3 -> 4,
   note.correspondence.setting-what-proved-what-imported-what 1 -> 2, note.lepton.abstract 2 -> 3,
   note.mass.setting-conformal-generators-chart 1 -> 2, note.standard-model.setting-setting-imports 1 -> 2,
   note.mass.setting-grip-composite-frozen-point 2 -> 3.

## For Leon
L1. pred.leptonic-cp-trivial and neutrino.real-breaking-assumption: a hypothesis left implicit. The assumption makes
   the Dirac and Majorana neutrino matrices real in the vacuum's basis; delta_CP in {0, pi} also needs the
   charged-lepton matrix real in that basis. Evidence: synthesis.circulant-charged-leptons-excluded-with-real-neutrino-sectors
   (iv)(c): the (complex) Koide circulant with the electron on the democratic line and a real P_12-breaking m_nu gives
   cos delta_CP = 0. Proposed fix: add to the assumption's formal level "and the charged-lepton matrix is real in the
   same basis (the textures of neutrino.breaking-relation)", and to the prediction's technical level and one-liner
   "with a real charged-lepton matrix"; or record the circulant branch as a namesake tension. (Postulate formal text:
   not edited.)
L2. The orientation of I_6 relative to the module scalar I_7 is a store-wide convention not written down. Proposed
   line for store/conventions.md (The imaginary units): "In the T09 Fock model (w_3 = b_3 + I_7b_4, I_7 = I_6e),
   I_6 = I_4E acts on CS as +I_7; the opposite orientation a_1a_2b_1b_2b_3b_4 acts as -I_7. Results using the
   mass-chart unit I_6 and the T09 scalar I_7 together name the orientation." It bears on
   synthesis.z-adapted-witt-flags-energy-sign-follows-the-flag-bit ("+R_{I_6}, a convention") and
   correspondence.reality-conjugation-twistor-form-factor (5) ("+-I_7").
L3. synthesis.operator-join-ordering-constants (GA-owned): I_6 as the scalar of the palatial oscillator polynomials,
   where its siblings on the same Fock space use I_4 (U1). No result changes (all displayed quantities are real).
   Decide: keep I_6 only as the moment's factor and read the Fock space in span{1, I_4}, with a which-acts-where
   sentence (details in ga-issues-R10.md).
L4. families.imported-dictionary-exact-join (restatement): "massless exactly when B_Lambda = 0 and scalar Gram matrix"
   is true but weaker than the current mass.exact-join (5) and synthesis.many-twistor-join (v) (h = 0). Proposed
   wording: "B_Lambda = 0 and h = 0". Formal level of a proved restatement: not edited.

## Known open items settled in these subjects
- Sign of I_6 on CS (correspondence.incidence-relation-chart, note.correspondence.what-factor-i-what-remains-conventional):
  settled by exact computation; the sign is orientation-dependent (-I_7 for a_1a_2b_1b_2b_3b_4, +I_7 for the store's
  I_4E); no contradiction with the mass entities' convention line (I_6 by right multiplication equals left
  multiplication on even elements, and both sides write Penrose's unit as I_6). The note no longer carries a
  "-unit" statement (its v4 text only names I_6 as the factor); unchanged. Chart fixed (item 1).
- I_6 against I_4 in synthesis.operator-join-ordering-constants: recorded (L3, ga-issues-R10.md); it is GA-owned.
- The other four open items of the brief are not in R10's subjects.

## Duplicates
None found under two ids. Restatements, correctly kept as restating Facts: T09 Thm 5.3 in
standard-model.imported-pair-systems-two-chirality-halves, lepton.imported-twistor-state-pair-system-excitations,
one-relation.imported-pure-spinors-incidence-chart; the mass bracket in families.imported-face-valued-bracket-quantum-numbers
and neutrino.imported-mass-bracket-quantum-numbers (original standard-model.mass-bracket-charged-singlet); the area
formula in rungs.imported-mass-symplectic-area (original mass.mass-symplectic-area-two-twistor-formula).

## Other observations (no action)
- Seesaw conventions differ between entities of one subject (mD MR^-1 mD^T in neutrino.breaking-relation,
  MD^T MR^-1 MD in synthesis.untuned-fit-caps-lightest-heavy-neutrino, -M MR^-1 M^T on the Pati-Salam route); each is
  self-consistent and the bounds used are transpose-invariant.
- Arithmetic checked and correct: breaking relation and lambda_A = 4/9; theta23 textures; S_3 inverse; weight
  composite, bracket fixed by the join, weight polynomial, de Sitter exceptional series; boost-dilation rotor;
  displacement pairing; transported frozen point norms; ceiling range; m_D = 1.44 sqrt(f_J) GeV; alpha < 7.3e8 GeV;
  Fock-model dual pair; Chevalley exponent table; chirality-split brackets and duality eigenvalues; local twistor
  composite.
- n0.ninf: -1 in angle.imported-conformal-model-null-rotations and the T12 rung results, +1 in T09, T11 and pairing
  results; each states its own.

## Counts
Entities read: 205 (129 claims, 1 object, 3 predictions, 72 notes; depth above). Changed: 14 (5 claims, 9 notes).
For Leon: 4. Cross-subject: 2 (xsubject-R10.md). GA issues sent: 3 entities (ga-issues-R10.md). Duplicates: 0.
tp check runs used: 1.

## Second pass (coordinator's request: the full read)
What was read: the proofs, in full, of all 86 of the 112 remaining claims, objects and predictions that have proofs
(every step and every number of the T09, T11, T12, T13, T15 and synthesis proofs on R10's list); the full formal
level of the 26 without proofs (Facts, postulates, predictions, conjectures, refutations); the full formal level of
all 72 notes. Each was checked against points 1-8 of CONSISTENCY.md. Arithmetic recomputed by hand where the
proof states it (examples: exact-join's component identity; the many-twistor remainder and its positivity; every
constant of the operator join; the point-spectrum bound mu >= 1; the three-twistor worked example m^2 = 52/9; the
anomaly solution set of the empty twistor; tan 2(theta_e - theta_u) = 286 sqrt2/4357; the solar and complex sum-rule
bounds; the two-loop coefficients). No proof was found to fail its statement.

### Fixed in the second pass
15. note.correspondence.setting-palatial-relation-two-quantisations-one 1 -> 2: the note displayed
    [Z, Zbar] = +hbar and said it is realised by Zbar = hbar d/dZ, which gives -hbar; now says so and names the
    realisation Zbar = -hbar d/dZ of the Lemma and its check.
16. note.mass.what-join-says 3 -> 4: "massless exactly when B = 0 and scalar Gram matrix" brought to the current
    exact-join (5): the multiple is zero (h = 0).
17. note.correspondence.setting-what-proved-what-imported-what (already 1 -> 2 in the first pass; no second bump):
    "the factor $i$" (a bare imaginary unit) is now "the factor $I_6$", as the reality proposition states it.

### New For-Leon items
L5. synthesis.attachment-conformal-energy-is-generated-by-z (GA-owned) (iv) puts Z in the cone C_pi of
    synthesis.positive-conformal-energy-gives-positive-null-translations via I_7 Q(Z/2) = E >= 1, while C_pi is
    defined by -I_4 d pi(Y) >= 0. With d pi = Q this needs the GNS scalar I_4 to act as -I_7 on the module; with
    +I_7 the same step gives the backward cone. Unstated identification of two units on which a sign (the time
    orientation of the conclusion) depends. Proposed fix: one sentence in the attachment's (iv) naming
    I_4 = -I_7 on that space, or the cone written with the module's unit. (Also in ga-issues-R10.md, item 5.)
L6. mass.imported-unitary-representations-de-sitter-group (status imported, Dixmier) carries in its formal level a
    series-internal assertion: that mass.casimir-form-join's C_2(I_perp) is "in this same normalisation, with no
    shift". synthesis.operator-join-casimir-shifts (iii) says this normalisation hypothesis "is not proved here" and
    gives an argument; synthesis.operator-join-point-spectrum-on-positive-energy-modules uses it for sharpness. An
    import is carrying a series claim that the store elsewhere calls argued. Proposed fix: move the sentence to a
    remark (or to casimir-shifts as its stated hypothesis), keeping the Fact to Dixmier's classification; formal
    text of an imported Fact, not edited.

### Observations (no action)
- note.mass.setting-successor-problems (5) still says the many-twistor extension is "not proved or scripted here
  beyond N = 2"; true of T11 at deposit, since proved in synthesis.many-twistor-join. Paper running text, left.
- The positive-energy oscillator realisations differ in scale between synthesis.operator-join-point-spectrum-...
  ([a, a+] = 1, scale s) and synthesis.operator-join-positive-energy-no-finite-energy-zero-modes ([a, a+] = hbar/2,
  s = 1); consistent (lambda s^4 = -1 against lambda = -1 at the matched scale).
- note.correspondence.setting-machine-verification reads the reality chart with I_7 (m(I_7 x-hat), -2 det(I_7 x-hat)
  = 2 det x-hat) where the proposition writes I_6; consistent, since I_6 = +-I_7 on CS and the identities are even in
  the unit.

### Counts after both passes
Entities read in full: 205. Changed: 16 (5 claims, 11 notes). For Leon: 6 (L1-L6). Cross-subject: 2. GA issues sent:
5 entities. Duplicates: 0. tp check runs: 2 (no error or warning on any R10 entity).
