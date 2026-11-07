# Filer U: Item 4 (the unit for Hermitian boson fields)

Status: filed. One proposal:
`proposals/synthesis.kernel-bivector-is-the-unit-of-hermitian-boson-fields-on-the-tower/`
(title "The kernel bivector is the even unit of Hermitian boson fields on the tower", 75 characters;
subject quantum-fields; holds given no postulate; no imported Fact among its premises).

## Pre-registered kill conditions (written before computing)
- K1: for some N in {1, 2, 3} the commutant of the transport (plane) subalgebra of Cl(N, N+2) is not
  span{1, J, Gamma g1, Gamma g2}, or its even part is not span{1, J}: then (c) is false as stated. Not triggered.
- K2: for some N in {1, 2, 3} an element of Cl(N, N) commuting with the even part squares to -1. Not triggered.
- K3: [phi, pi] differs from 2 J sum_k (n_{2k} - n_{2k+1}) by any nonzero element for M = 1 or 2. Not triggered.
- K4: the level pseudoscalar is not +-J Gamma, or Gamma is not prod(1 - 2 n_j). Not triggered (I_n = +J Gamma in
  the generator order e_0 e_1 e_2 e_3 then the tower planes).
- K5 (reading): if, with the radial plane counted in the ground Cl(1,3), J were still the only even unit
  commuting with the remaining tower planes, drop the contrast clause. TRIGGERED: the even commutant is then
  Cl^+(1,3), containing I_4, e_1e_2, e_1e_3 and J, all of square -1. The uniqueness of J is stated only for the
  reading in which every hyperbolic plane, the radial one included, is a transport plane, and the contrast is
  stated in (iii).

## Duplicate check (store at the run's baseline)
Read: std-algebra.complexification-is-the-odd-extension@2, synthesis.wedge-reflections-compose-to-the-two-pi-rotor-...@5,
synthesis.plane-commutant-even-ground@3, std-algebra.even-subalgebra-isomorphism@1,
synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum@1,
synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom@1, tower.commuting-copies@5,
tower.volume-elements-planes@5, tower.structure-tower-c-norms@10; search_claims on six queries.
- Stored, cited, not refiled: the N = 1 case of (b)-(d) (transverse-bivector (i), (iii): quaternion centraliser
  of the radial atom, even unit +-J, J* = -J, J sigma = +I_4, I_4 P_+- = +-J P_+-); the commutant of the planes
  on a floor is the twisted copy of the ground (tower.commuting-copies), so (c) for general N is that theorem
  read with ground Cl(0,2); only the even ground algebra survives in the limit (plane-commutant-even-ground (i));
  the centre of Cl^0(N, N) is span{1, omega}, omega^2 = +1 (plane-commutant-even-ground (ii) at r = 0); the block
  remark "a Weyl form with self-adjoint fields would need a central unit" (fluctuation-forms (vii)); the edge
  operator, hopping ladder and block commutators (fluctuation-forms (ii), (iii), (v)).
- Not used as premises: std-algebra.complexification-is-the-odd-extension (U3, the vector unit; not needed),
  std-algebra.even-subalgebra-isomorphism (not needed), the wedge-reflections entity (it holds given (N+) and
  postulates; I_4 B = J is re-derived in one line as J = I_4 sigma), synthesis.n-plus-null-ground-state (cited
  by claimref in the argued reading only, so the result does not hold given (N+)).
- New: (i) for every N the commutant of the even part in the whole Cl(N, N) has no odd part, so no unit;
  (ii)-(iii) general N, unique even unit +-J, fixed by kernel rotors, and the contrast with the ground-Cl(1,3)
  reading; (iv) I_n = J Gamma on every level, Ad(I_n) the grade involution, = fermion parity on transport;
  (v) phi_X = X + X*, pi_X = J(X* - X) self-adjoint with [phi, pi] = 2 J [X, X*] and the mixed identities;
  collective pairs [phi, pi] = 2 J sum (n_2k - n_2k+1), 2 (M - 2j) J on the polarised ladder; density modes
  2 q J on edge-clean elements, [rho_q, rho_q'] = 0 on finite windows; a lemma giving the full Hermitian
  canonical relations for any commuting unit u; (vi) the reflection e_3 -> -e_3 as a *-automorphism fixing
  transport and reversing J, I_4, I_n, pi; the phase circle U = e^{theta J Q/2} with U S U* = e^{theta J} S.

## Established (labels)
- Proved, general N, and checked exactly with lib/GA.py: (i) N = 1, 2, 3; (ii) N = 1, 2, 3; (iii) N = 1, 2, 3 and
  contrast at N = 2; (iv) N = 1, 2, 3; (v) M = 1, 2 blocks and a window of four modes; (vi) N = 4 at a rational
  point. The commutant computation is blade-wise; the proof states why that is valid (conjugation by a basis
  blade maps every basis blade to plus or minus itself, so commutants of sets of blades are spanned by blades).
- Argued (labelled "Reading (argued)"): the sign of J, which (vi) shows equals the orientation of I_4 given
  sigma, is the orientation datum Premise (N+) assumes, now shared by the fermion phase flow and [Phi, Pi] = +J.

## Gates
- runcheck: 7/7 functions pass (about 1 s).
- validate_draft: ok; info only (I213 subject: 10% of 10 logical neighbours in quantum-fields, most in tower;
  kept as quantum-fields with the tags; I305 store-wide).
- check4 on the work copy and again on proposals/<id>: 0 errors, 0 other findings, check result pass (no W413).
- Registered with propose_claim (proposal.json present). propose_claim rejects coverage.yaml as a proof file
  (E102), so the draft was sent without it and coverage.yaml was copied into the proposal folder afterwards; the
  final check4 ran on the folder with it.
- Style: no em or en dashes, no banned words, no bare imaginary unit, no \mathbb{C}.
- Work files: colony/runs/2026-11-07-boson-items/work/U/ (draft json, validate output, check4 logs).

## Unexpected links
- Overlap to watch: attacker SA's route R1 uses U(theta) = exp(theta J Nhat/2) = prod_k (1 + (e^{theta J/2} - 1) n_k)
  (total number) and R4 uses J Gamma = +-I_n. This proposal has the relative-number version e^{theta J Q/2} (the
  boson phase circle) and I_n = J Gamma; SA should cite (iv) and (vi) rather than re-prove them.
- The lemma in (v) applies on the band domain D of fluctuation-forms (vi) with whatever unit commutes with the band
  modes there; on the horizon's continuum modes the store's unit is I_4 (U1), on a tower level with the radial
  plane among the transport planes it is J (U2). (iii)'s contrast shows the two coexist on tower planes beyond the
  radial one, I_4 = J sigma.

## Decisions for Leon
1. Which reading of "transport step" the series uses for bosons. If the radial plane (the completed-pair atom) is
   a transport plane, J is the unique even unit (this proposal). If only the tower planes beyond Cl(1,3) are, the
   even commutant is Cl^+(1,3) and both I_4 (U1) and J commute with transport; then the unit principle needs a rule
   for which one boson fields on tower planes use (they agree on sigma = +1). Recommendation: state in U2 that J is
   the unit whenever the radial atom's modes are among the modes, and keep U1's I_4 for the horizon continuum.
2. Whether the argued identification of the sign of J with the (N+) orientation datum should be added to the
   (N+) entity's note (maintainer pass) or left as this proposal's reading. Recommendation: leave it as the reading
   here; it does not change (N+).
3. Subject: quantum-fields (kept) or tower (validator info I213). Recommendation: keep quantum-fields.
