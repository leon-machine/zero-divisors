# Run 2026-11-07-ga-units: bridge survey, the imaginary unit as a pseudoscalar, and the Hadamard chain

## 1. Bridge survey (read-only), op.hypothesis-s, op.r-premises-external, op.deposit-state-is-hadamard
Report: survey/bridge_survey_2026-11-07.md (per-problem reports beside it). No premise derived. Findings
carried into the store: the open-problem records (7 November paragraphs and attack items), two notebook
entries, and the results below. One survey reading was corrected at review: the energy sign of a Z-adapted
flag's vacuum is not independent of the stored flag bit; on each conjugate pair they flip together.

## 2. The handedness test (pre-registered, killed)
survey/PREREG.md, survey/handedness.py (55 exact checks). With the unit I4 the (N+) orientation datum is
odd under P and CP and is not the chirality of massless spinors. Filed and accepted as
synthesis.massless-frequency-sign-relative-to-i4-is-not-the-chirality.

## 3. New results (accepted after a blind review and a fix round; check4 and validate_draft clean)
- synthesis.massless-frequency-sign-relative-to-i4-is-not-the-chirality (SOUND WITH FIXES)
- synthesis.z-adapted-witt-flags-energy-sign-follows-the-flag-bit (OVERSTATED as filed; restated;
  accepted by Leon under a new id)
- synthesis.fock-slot-module-is-cpt-closed-only-over-one-doublet (SOUND WITH FIXES)
- synthesis.joint-clifford-clause-is-a-klein-convention-on-the-composite-space (SOUND WITH FIXES)
Reviews: referee.md; fixes: fixes-filer.md; gates: check4-*.log, validate-*.log.

## 4. The Hadamard chain rests on no postulate (maintainer clause split, three cuts)
split.md. synthesis.hadamard-scaling-limit-premise held given 18 postulates through citations of algebraic
and analytic clauses; four results now carry those clauses and hold given nothing:
synthesis.canonical-part-of-a-spinor-on-a-null-plane, synthesis.null-vacuum-on-a-horizon-generator,
synthesis.null-vacuum-singularity-under-reparametrisation-and-dilation,
synthesis.stationary-generator-states-and-the-edge-scaling. The scaling theorem, the microlocal theorem,
local normality at the edge and the bulk-Hadamard result now hold given nothing. Blind review: all four
SOUND WITH FIXES (referee-split.md), fixes applied (split.md round 4).

## 5. No bare imaginary unit where a pseudoscalar does the work (Leon's rule, 7 November)
SWEEP.md (rules), RULINGS.md (Leon's rulings R1-R4), sweep-*.md (groups A1, A2, B, C1, C2, D1, D2, E),
consistency-K1.md, consistency-K2.md (with group F). The unit is now I4 (the right unit on values that are
not even), right multiplication by I6 for conformal spinors, or a plane's bivector; numbers are read in
span{1, I4}. A bare i stays only where no pseudoscalar can replace it (boundary-mode, atom and window flows;
complexifications that commute with vectors; i0 shifts of spacetime vectors; complex analysis in its own
right; imported Facts in their source's form), and each such entity declares outside_ga. The language
check (tp/galang.py) now flags a bare imaginary unit; tests in tests/test_galang.py. Conventions and the
contributing rules state the rule.

## 5a. Every imaginary unit resolved (Leon, 11:16: "Try to resolve all imaginary units")
RESOLVE.md (the unit principle U1-U6, superseding R1 and the "what stays" lists), core.md, referee-core.md,
resolve-G1.md to resolve-G5.md. A complex number is written with the pseudoscalar that commutes with
everything it multiplies: I4 (left on even values, the right unit on others; numbers, abstract Hilbert
spaces, the continuum modes, complex analysis of scalar functions, theta functions); the transverse
bivector J = e2 e3 = I4 sigma on the radial atom and its boundary modes (the even unit of the atom's
quaternionic centraliser); the central pseudoscalar of the odd extension, I5 in Cl(2,3) and I7 in Cl(3,4),
where the unit must commute with every vector (complexifications, complex null vectors, tube points, i0
shifts of vectors, the continued rotor on vectors); hat-I = I_V e for the cosmological horizon's atom, which
has no single transverse plane; imported Facts restated with their source's form kept in
extraction.source_formal. Two new core results carry the units, both reviewed blind (SOUND WITH FIXES,
fixes applied) and holding given no postulate: std-algebra.complexification-is-the-odd-extension and
synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom. The store now has no bare imaginary
unit in any level or proof of any entity; the seven outside_ga declarations left are for Pauli or Dirac
matrices, a cross product or a named field, none for i. The language check flags a bare imaginary unit even
when outside_ga is declared.

Readings recorded for Leon (each entity states its reading): n-mode boundary spaces are read with J (they
are built from the radial atom and tower planes); abstract complexifications over an arbitrary tower ground
use the scalar span{1, I4}; the Pati-Salam defining representations are read in span{1, I4} (I6 if the 16 is
meant as the conformal spinor); letter clashes with J were renamed (g, L_a, \mathcal{J}). Further possible
sign slips recorded, not fixed: hadamard-dirac-states-scale proof step 7, and the coherence-phase sign in
quadratic-flows (already listed).

## 6. Leon's decisions this run
Unit rulings R1-R4; proposal 2 accepted under a new id; the CPT premise's sentence on the CPT operator of
quantum field theory restated (dark-matter.premise-cpt-covariance v3); P2's scope not extended; a note on
(N+)'s orientation datum (note.synthesis.n-plus-orientation-datum).

## 7. Open items for Leon
- Possible sign slips recorded by the sweep, not fixed (no conclusion depends on them): the coherence
  phase in synthesis.quadratic-flows-cannot-thermalise-descent (formal versus proof), the one-particle
  Hamiltonian sign in synthesis.boost-evolution-on-generators-is-one-unitary-group, an intermediate
  expression in synthesis.real-structure-breaks-source-stabiliser-to-z2 (ii).
- A possible sign conflict on I6 acting on CS (correspondence.incidence-relation-chart versus the twistor
  entities' convention line).
- synthesis.operator-join-ordering-constants keeps I6 on a space other entities now write with I4.
- The two boost-bivector signs are recorded in the conventions.

## Costs (approximate subagent tokens)
Survey 0.69M; sweep 2.2M (eight groups); consistency 0.7M; clause split 0.58M; filer 0.41M; referees 0.53M.
About 5.1M in all.
