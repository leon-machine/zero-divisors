# Pre-registration 3: the infinite tower (records of unbounded length; rung values as data; a reading law)

Written before computing, 12 November 2026. Leon approved three steps and asked for more care: the earlier tests
were judged weak by the referee (outcomes nearly fixed in advance, a symmetry group chosen without saying so). So
here: every group is named before use and all are reported side by side; each item says whether it is a TEST (the
outcome is open and I say what would surprise me) or a PROOF WITH A SANITY CHECK (no open outcome; the check only
guards against an algebra slip). No item is counted as evidence beyond what it is.

Setting. The algebraic tower A = union of Cl_Q(n,n) (tower.algebraic-limit-even-charge: the Clifford algebra of an
infinite orthogonal sum of hyperbolic planes; every element involves finitely many generators). States under (P).
Computations on finite floors in the Fock module of tower.fock-module-one-qubit-per-rung (v_j by wedge, w_j by
contraction), tied to lib/GA.py by checking the module against GA products on a small floor.

## Step 1. Records of unbounded length
Model (fixed now): system rungs 0, 1, one quantum, amplitudes 3/5 and 4/5. N record pairs; pair j starts with its
quantum on its first rung. Coupling U_j = off_0 + on_0 R_j, R_j the rotor of pair j with cosine c (rational,
|c| < 1; c = 3/5 and c = 0 computed). Interference of an element x: I_N(x) = omega_N(x) minus the weighted sum of
the two branch values.
- 1a TEST. For every element x supported on the system and a set K of k of the N pairs (even or odd, self-adjoint or
  not): I_N(x) = c^(N-k) I_K(x), where I_K is the interference with only the pairs of K coupled. Open point: signs
  for odd x and for K interleaved with the uncoupled pairs. I expect it to hold; a failure on odd elements would
  mean the statement is true only for even elements, and I would say so. N = 3, all 8 subsets K, at least 200
  random elements with integer coefficients per subset, both parities.
- 1b PROOF WITH A SANITY CHECK. For every N there is an even self-adjoint element of square an idempotent, touching
  every record pair, with interference exactly 24/25. So the convergence in 1a is not uniform in x.
- 1c PROOF. The limit of omega_N on A exists and is the mixture with weights 9/25, 16/25: no element of the
  algebraic tower sees interference. For c = 0 this is exact from N > (largest pair touched). The C*-level reading
  (the two branch states are disjoint) is the stored Powers-Stormer import applied to two projections whose
  difference is not Hilbert-Schmidt; cited, not proved.
What this would and would not be: the recorded-sectors premise as a theorem in the limit of unbounded records, for
this model coupling, with interference present at every finite stage. It selects nothing.

## Step 2. Are rung values data on the infinite tower?
Groups, all reported:
  G1 sign changes of finitely many generators;
  G2 conjugations by even or odd unitaries of a finite floor;
  G3 sign changes of any set of generators, finite or infinite (each is an automorphism of A preserving every
     floor and the adjoint; it is the product over all steps of the step symmetries used in the finite result).
- 2a PROOF WITH A SANITY CHECK. Orbits of string states: under G1 and G2, two strings are related exactly when they
  differ at finitely many rungs (tail classes, uncountably many); under G3 all strings are one orbit.
- 2b PROOF WITH A SANITY CHECK. No element of A connects two strings that differ at infinitely many rungs: the
  transition value between their truncations vanishes once a differing rung beyond the element's support is
  included.
- 2c TEST. Is the symmetric state an average of string states only, or equally of other families of sharp even
  states? Candidate: the four pair-entangled even atoms on each pair of rungs. If their uniform average is also the
  symmetric state, reading the symmetric state as ignorance of an actual string is one choice among several and
  needs a premise preferring the occupation context. I expect non-uniqueness. A surprise would be that evenness
  forces the string decomposition.
- 2d SEARCH. Does any stored result prefer the occupation context? Start: obj.singularity.multi-mode-descent and
  singularity.p-reduced-metric-level-reading-many. Report what they say and under which premises.
What each outcome means: the answer to "datum or label" is reported per group, not as one verdict.

## Step 3. A reading law (done whatever step 2 gives, since step 2 has no single verdict)
- 3a PROOF. For fixed rung data s and any unitary coupling of the system to the rungs, the weight of any test after
  the coupling is a quadratic form in the system's state; if it takes only the values 0 and 1 on all rational unit
  vectors it is constant. So no dynamics of the algebra reading fixed data selects an outcome with odds that
  depend on the state. Over Q the argument must not use continuity: a binary quadratic form vanishing at more than
  two points of the projective line is zero.
- 3b PROOF WITH A SANITY CHECK. Given, as premises, an actual string of unbiased values and a rule outside the
  algebra, the rule "read rungs until decided" yields a prescribed rational weight exactly (9/25 computed as an
  exact series) with a finite number of reads with probability one, mean 2.
- 3c LIST. The premises such a selector needs, and which stored statements each meets.
Prediction: 3a holds, so a selector cannot be a law inside the algebra at all; it would be a rule of another kind.
