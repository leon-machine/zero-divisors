# fixes-SB (fix round, run 2026-11-07-boson-items)

check4: pending (orchestrator). Only runcheck.py was run: both proposals PASS (P4 5/5 functions, P5 3/3).

## P4 synthesis.ladder-bosons-inherit-spin-statistics-from-the-single-modes (OVERSTATED -> restated)
I accept the referee's counterexample: with all weights integer, U(2 pi) = 1, so the bosons obey the connection while
every single mode breaks it. My check now confirms the referee's count (5, 13, 35 uniform assignments at N = 1, 2, 3).
Restated at every level to the referee's true statement:
- Title: "On the ladder the bosons' spin and statistics are fixed by the single modes' spins" (the referee's
  suggestion). The id is unchanged.
- Formal (ii): added "the bosons alone" clause. Ad U(2 pi) fixes every even element iff the 2 s_j all have the same
  parity (all spinor or all integer).
- Formal (iii): retitled "uniform integer and mixed assignments". It adds the all-integer case (U(2 pi) = 1, bosons
  obey the connection, single modes are fermions of integer spin). The counter-model is now stated for mixed
  assignments.
- Formal (iv): added the general argument. A rotor group whose action on vectors has period 2 pi ends at +-1, the
  kernel of std-algebra.spin-double-cover@1 (new premise in uses, touched by the check). The kernel rotors and the
  two-mode rotation are now given as instances. Added a sentence saying half-integer weights need J at half angle.
- Formal Reading, proof Reading, extraction, technical, lay and one-liner: replaced with the referee's text. The
  extraction now says "New to the store" and says this entity holds the general mode-rotation formula (i) and
  graded locality (ii), per the overlap ruling. It cites the proposal
  synthesis.kernel-bivector-is-the-unit-of-hermitian-boson-fields-on-the-tower in plain text, for clause (i) (the
  commutant of the even part of Cl(N,N) is span{1, Gamma}) and for (vi) (the phase circle as the alternating-weight
  case).
- Proof (ii): the boson part is now derived directly on products of two modes. Ad prod_{j in S} omega_j multiplies v_i
  w_j by (-1)^{[i in S] + [j in S]}, so all are fixed iff S is empty or full. The proof notes this is the commutant
  statement span{1, Gamma}.
- Proof (iii): the all-integer case is added. Proof (iv): the double-cover argument is added, with exp(pi J) = -1.
- Check: new function check_bosons_obey_the_connection_exactly_for_uniform_assignments. For N = 1, 2, 3 and all 5^N
  assignments it checks that every product of two modes is fixed iff the assignment is uniform, with counts asserted
  [5, 13, 35]. For all-integer assignments it checks U(2 pi) = 1, modes 2 pi invariant, and modes anticommuting.
  check_rotations_of_the_level_itself_give_integer_spin now touches std-algebra.spin-double-cover and asserts that
  exp(pi J) = -1 and R(2 pi) act trivially on every generator. coverage.yaml is updated.

## P5 synthesis.ladder-states-are-locally-product-with-non-gaussian-fluctuations (SOUND WITH FIXES)
1. Formal (iv): replaced with the referee's text. The result no longer makes a necessity claim ("Their necessity is
   not claimed"). Proof (iv) is aligned to match.
2. Technical: "needs the product structure at each size" became "cannot replace its hypothesis at each size by local
   convergence in the limit".
3. Formal (ii) "whatever their distance" became "every pair alike (the state is permutation symmetric)". The
   extraction and Reading are aligned.
4. Extraction: "New here" became "New to the store". It now names the Dicke states and the Holstein-Primakoff
   (Fock number state) limit. It says the ladder coefficient is the quasi-spin ladder of
   field-theory.how-close-tower-comes-ccr (Inonu-Wigner contraction) after particle-hole conjugation, and that this
   entity holds the coefficient, per the overlap ruling. It cites the proposal
   synthesis.central-limit-of-tower-fluctuation-states-with-the-kernel-unit (iii) for k = 0.
The check is unchanged (the referee's perturbations already fail where they should).
