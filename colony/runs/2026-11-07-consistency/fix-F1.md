# Fix round, referee F1 (fixer FX1, run 2026-11-07-consistency)

Brief: FIX_GTG.md with F = F1, P = 1. Entities: referee_F1.txt (10). All ten were already at lock + 1, so no
version bump. Each changed entity has a credit entry (source: maintainer pass 2026-11-07 (consistency, GTG
review)) and an extraction note `maintainer_pass_gtg_review`. cosmological-horizon has the note only (no fix; one
N repin). Four entities also have a `maintainer_pass_pin_review` note for their R pins. My own scratch scripts are in
/tmp/claude-0/-home-claude/23cbb9be-73ca-5537-8211-47496476158a/scratchpad/FX1/: v6.py, v10.py and v3.py are
independent GA.py and gtg.py recomputations, and mut.py runs one check function from a mutated scratch copy.

Validation:
- runcheck on the four changed check.py files: all functions pass.
- check4 on a proposals/ copy of each of those four: 0 errors, findings I405 and I410 only. The copies were deleted.
- `python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon` (one run): 0 errors, 0 warnings, no
  finding on any of the ten ids.

Note for the orchestrator: commit f346b5c ("referee report F3") picked up some of my working-tree edits mid-round:
frozen-point proof, macdowell-mansouri check, coverage and proof, two-frozen-points proof, stelle-west and
black-hole-data checks. The committed content is the final content. I made no commit.

## Per finding

| # | entity | finding | outcome |
|---|---|---|---|
| 1 | gravity-pre-metric | ACCEPT; variation sign remark | no change needed. Own addition: the opening cited Fact synthesis.imported-gtg-dictionary for "forms as multivector fields", which that Fact does not state. The parenthesis is removed (no edge change). |
| 2.1 | stelle-west | opening attributes tractors and the tractor gauge field to the dictionary | applied: referee's text, with the tractor theorem as a text-only \claimref. Checked: the dictionary's (i) to (vi) say nothing about tractors, and the frozen-point Fact's formal does name the tractor theorem. Uses edge synthesis.imported-gtg-dictionary@2 added; premise() for it added to check_tractor_gauge_field_slots_and_bracket. |
| 3 | black-hole-data | optional tightening of the Wald direction | applied. Verified exactly (v3.py) on all 256 frame quadruples: riem_o(S_sigma) = -eps_uv eps_wz, Ricci map -P_sigma, scalar -2. The mutant +<B sigma> sigma fails. The same assertion was added to check_gtg_black_hole_data with premise(dictionary), and both mutants are caught. Uses edge dictionary@2 added (cited for that step). coverage.yaml updated. |
| 4.1 | collapsing-hole | control uses the background tangent, not the physical velocity | applied. Verified: hb^{-1}(e_t - (1 + beta) e_r) = gamma_0 - gamma_1, and D_{x_t} of it = (beta/2r)(gamma_0 - gamma_1). The control now asserts the physical velocity and that exact value. Mutants caught: the old control, and the sign of beta/2r. |
| 5 | cosmological-horizon | ACCEPT | nothing to fix. |
| 6.1 | frozen-point stiffness | (ninf ^ n0) . ninf, (ninf ^ n0) . n0 wrong in proof (i) | applied: they are ninf and -n0. Verified in Cl(2,4) (v6.py) at rho = 3/7 and -2/5 on a generic field. **Not propagated**: the displayed DI and DX, formal (i) and check_broken_components (which computes the products) are right. The proof's stated values give beta(rho ninf - n0) and +beta ninf, which fail. The component proof (orig-proof-main.tex) has the same two wrong values; it is kept unchanged as history. |
| 7.1, 7.2 | killing-horizon | cite Definition (a) for the frame, (f) for the torsion equation | applied (citations only). The frame equation follows from (f) because gamma^a is constant. |
| 8.1 | macdowell-mansouri | check tests nothing | confirmed: with BG5 = (5,2,-3,7,1) and (1,1,1,1,1) it still passes. **Removed** from check.py, checked_by and coverage.yaml. The proof parenthesis now states why no check is needed. The referee's alternative (grad ^ transgression = P(F,F,F) - P(F0,F0,F0)) is **vacuous on the 5D base**, since both sides are six-forms. On a larger background it would test the imported Chern-Weil Fact, not this result, so I did not add it. |
| 8.2 | macdowell-mansouri | outside_ga declaration inexact | applied: **withdrawn**. The imported Facts declare none, the forms are read as multivector fields, and the component readings are permitted. |
| 9.1 | nondiagonal-kasner | torsion-equation citation | applied: Definition (f). |
| 10.1 | two-frozen-points | the proof uses the converse of the Fact | applied: the step is now computed directly (Omega = grad sigma ^ a / sigma, R = -Q(I) sigma^-2 a ^ b, calR = Q(I) id). Verified with the engine at four (s, m, r), including s < 0 and r < 0 (v10.py): torsion-free, Omega and R as stated, Ricci map 3 Q(I) id. |

Disputed: none. Partly disputed: the referee's alternative check for 8.1 (vacuous in 5D).

## Pins (18 stale, all repinned)

- **N (13)**: the formal is unchanged or the change is notation only.
  - frozen-point-makes-stelle-west-vector 5->6 (x3)
  - de-sitter-static-boost 5->6
  - transport.group-null-rotations 4->5
  - diagonal-kasner-momentum-constraint 3->4
  - positive-null-energy 7->8 (a remark only)
  - frozen-point-integrand 2->3
  - second-quantisation 5->6
  - rule-2-kaluza-klein 6->7
  - variable-exponents 4->5
  - frozen-point-datum-kasner-wall 7->8
  - cosmological-constant-residue 6->7
- **R repinned, use holds (5)**:
  - imported-gtg-dictionary 1->2, (iv) sign reading. collapsing-hole cites (i), (iii) and (vi); killing-horizon cites (ii). Unchanged in content.
  - sheaf.gauge-field-cometric 3->4. Only the r = 0 degeneration description changed; collapsing-hole uses only the PG field on r > 0.
  - macdowell-mansouri-principle 2->3, convention line corrected to the store sign; frame equation unchanged. Cited by frozen-point stiffness (v) and macdowell-mansouri.
- R left: none.

## For Leon

1. synthesis.nondiagonal-kasner-residue-weighted-shear, formal (i), a sign the formal leaves open (optional, raised by
   the referee). The GTG computation fixes it: omega(gamma_0) = +tau^-1 antisym(B) in the Definition's sign. The
   evidence is the prover's check_gtg_torsion_equation_gives_the_boost_block and referee E9 on three further shears; I
   did not recompute it. Proposed text: replace "the $e^{0}$-leg of the rotation block is $\tau^{-1}$ times the
   antisymmetric part of $B$ (up to the sign convention)" with "the $e^{0}$-leg of the rotation block is
   $\omega(\gamma_{0}) = \tau^{-1}\sum_{l<m}\mathrm{antisym}(B)_{lm}\,\gamma_{l}\wedge\gamma_{m}$ in the sign of the
   Definition, $D_{a} = a\cdot\nabla + \Omega(a)\times$".
2. Outside my list (no action taken): the formal of Fact dark-energy.imported-frozen-point-geometry names Theorem
   synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection, which rests on
   dark-energy.stelle-west-vector-frozen-point, which uses that Fact. stelle-west now states that it does not use that
   sentence. Leon may want the Fact's sentence to be a text-only remark.
