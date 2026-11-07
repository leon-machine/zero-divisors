# GA and other issues on GA-owned entities, from reader R10 (conformal-spacetime, mass, neutrinos)

R10's GA-owned ids: correspondence.one-statement-three-languages, correspondence.ordering-filtration,
mass.casimir-form-join, mass.chart-form-spin-isomorphism, neutrino.rank-one-seesaw-ordering-sum-double,
pairing.displacement-pairs-point-mode-vacuum-parallel, pred.no-neutrinoless-double-beta,
synthesis.attachment-conformal-energy-is-generated-by-z, synthesis.majorana-scale-is-126-doublet-vev,
synthesis.no-120-excludes-hierarchical-second-stage, synthesis.one-type-second-stages-are-twins,
synthesis.operator-join-ordering-constants, synthesis.two-loop-running-cannot-fix-majorana-coupling.
R10 edited none of them.

## 1. synthesis.operator-join-ordering-constants (known open item: I6 on a space others write with I4)
- The formal level quantises the moment as M^_A := I_6 sum_i (1/2)(Zbar_i . A Z^i + A Z^i . Zbar_i) and reads
  "numbers, and the coefficients of polynomials in the oscillators" in span{1, I_6}. Its users and siblings on the
  same palatial oscillator / Fock space read that space's scalars in span{1, I_4}:
  synthesis.operator-join-seed-has-no-diagonal-matrix-elements (the U(1) exp(I_4 phi tr h^/hbar), "on the palatial
  Fock space numbers and the module's complex structure are read in span{1, I_4}") and
  synthesis.operator-join-positive-energy-no-finite-energy-zero-modes (numbers and the module's complex structure in
  span{1, I_4}; exp(2 I_4 / hbar ...)). One space, two units, no sentence saying which acts where.
- Effect on results: none found. The displayed join, the ordering constants -N Lambda hbar^2/3 and
  -(5 Lambda/12) hbar :tr h: are real; I_6 enters only squared (Q(P^) is quadratic in the moments).
- Proposed fix (notation only): keep I_6 as the moment's factor (inherited from mass.exact-join, where it is the
  chart's complex unit of CS), and add one sentence: "the scalars of the palatial Fock space on which these
  operators act are written I_4 in the results built on this one (U1); I_6 is the factor of the classical moment,
  equal to +-I_4 on the two chiral halves at a point, and the two are not identified; every quantity displayed here
  is real, so the choice does not enter." Alternatively rewrite the coefficient field as span{1, I_4} by U1 (abstract
  Fock space) and keep I_6 only inside M^_A.

## 2. synthesis.attachment-conformal-energy-is-generated-by-z
- Uses the module scalar I_7 = I_6 e (h = <psi, I_7 Z phi>, Z = -+I_7 ...), while
  synthesis.z-adapted-witt-flags-energy-sign-follows-the-flag-bit identifies "the unit of attachment (i)" with
  +R_{I_6} "as a convention". R10 checked (exact computation, lib/GA.py, Cl(3,4)) that on CS the sign relating left
  I_6 and the scalar I_7 = I_6 e depends on the orientation of I_6: with I_6 = a_1a_2b_1b_2b_3b_4 (T09 basis) and
  w_3 = b_3 + I_7 b_4 it is -I_7, with the store's I_6 = I_4E = -a_1a_2b_1b_2b_3b_4 (I_7 and W rebuilt from it) it is
  +I_7. Suggest a sentence naming the orientation used for I_6 in the attachment's frame (e_0, e_1, e_2, e_3, nu,
  e_-) and the resulting sign, so the "+R_{I_6}" convention of the z-adapted result is a stated consequence.

## 3. mass.chart-form-spin-isomorphism (matrices)
- The chart's unit is I_6 by right multiplication (the mass papers' convention line); T09's Fock-model results use the
  scalar I_7. On CS, I_6 = +-I_7 by orientation (item 2). No formula was found that carries a T09 expression with I_7
  into the mass chart with I_6 at first order (the incidence relation, the one shared formula, is written with I_6 on
  both sides). Worth one sentence in the convention line: "on CS, I_6 equals +-I_7, the T09 module scalar, by
  orientation".

## 4. No other GA issue found on these ids at the depth read (formal and one-liner levels; proofs of
   correspondence.one-statement-three-languages and correspondence.ordering-filtration read in full and found sound).

## Second pass (proofs read in full)
5. synthesis.attachment-conformal-energy-is-generated-by-z, clause (iv): it places Z in the cone C_pi of
   synthesis.positive-conformal-energy-gives-positive-null-translations because "I_7 Q(Z/2) = E >= 1". That cone is
   defined by -I_4 d pi(Y) >= 0 on the GNS space (scalars span{1, I_4}). With d pi(Y) = Q(Y) (Q(Z/2) = -I_7 E,
   anti-Hermitian), the two agree only if the GNS scalar I_4 acts on the attachment's module as -I_7; with
   I_4 = +I_7 the same computation puts Z in -C_pi (the backward cone, which that proposition calls the choice of time
   orientation). The attachment's own clause (ii) (I_7 h P_a positive semidefinite for future a) is consistent in its
   own convention; the bridge sentence needs "the Hilbert space's unit, written I_4 there, is -I_7 here" (or the cone
   rewritten as I_7 d pi(Y) >= 0). No sign of a stated result changes once the identification is written.
6. mass.casimir-form-join, proof (2), "The constant": "E = diag(-1/2, -1/2, 1/2, 1/2), the grading element, in the
   basis n_inf, n_0, x-slot" mixes a CS matrix with the ambient basis; read "E, diag(...) on CS in the frame
   e_1, ..., e_4; the sum over the ambient basis n_inf, n_0, x-slot". Wording only.
7. Checked in full and found sound (no GA issue beyond the above): proofs of correspondence.one-statement-three-languages,
   correspondence.ordering-filtration, mass.chart-form-spin-isomorphism (all three blocks recomputed),
   mass.casimir-form-join (constant kappa = -1 and clause (3)), neutrino.rank-one-seesaw-ordering-sum-double,
   pairing.displacement-pairs-point-mode-vacuum-parallel (values recomputed), synthesis.majorana-scale-is-126-doublet-vev,
   synthesis.no-120-excludes-hierarchical-second-stage (b^4 > 0.0874), synthesis.one-type-second-stages-are-twins,
   synthesis.operator-join-ordering-constants (every constant recomputed: -N Lambda hbar^2/3, -(5 Lambda/12) hbar :tr h:,
   Weyl -5N Lambda hbar^2/12), synthesis.two-loop-running-cannot-fix-majorana-coupling (v = (6, 0, 15/4), determinant
   coefficient 201/4).
