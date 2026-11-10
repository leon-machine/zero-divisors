# Bridges, run 2026-11-09-bridges

Read: attack-C1A.md, attack-C1B.md, attack-C2A.md, attack-C2B.md (first pass about 22:20, second pass after all
four had results and registered proposals). Tests are store lookups (get_claim, find_text, search_claims) and
small exact counts (binomials, one sign); no long derivations. Labels: stored (read off a stored statement),
computed (small exact count done here), argued (short reasoning from stored statements, not checked by a script),
memory (literature from memory, unchecked). Scratch: work/bridge/st.py (a lookup helper only).

## Links to relay

### B1. The order-four charge of a mass term: C1B's two charges are omega and omega times the centre of su(2)_L
Concerns: C1B (X4 proposal), C2B (Y3 proposal P2 and its "Unexpected links" line), C2A (Y3).
Entities: synthesis.mass-terms-are-pair-terms-of-the-arrays-and-only-the-charge-separates-majorana-from-dirac
(proposal, C1B); synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element (proposal, C2B);
standard-model.majorana-element (proved v7); families.imported-decomposition-grade-dictionary;
synthesis.neutral-singlet-bit-decided-by-gauge-algebra-leaving-u5 (proved v3).
Why. C2B writes "a Dirac term commutes with omega and a Majorana term anticommutes". By the stored grade
dictionary every mass form on the sixteen has odd Clifford grade (one, three, five for the 10, 120, 126), and
omega anticommutes with every generator (C2A, computed), so EVERY mass form is odd under omega, the Dirac forms
included. That is C1B's row "N: -2 on both". What separates the two is compensation by a gauge element: the
grade-one Dirac form is a doublet of su(2)_L, so it is even under omega times the centre -1 of su(2)_L, while T
commutes with su(3), su(2)_L and Y (stored), so no element of the Standard Model group can compensate and T stays
odd. On the sixteen omega z_2 is the unit on the eight singlet components and minus the unit on the eight doublet
components: C1B's charge L, "opposite on the two arrays; 0 on Dirac, 2 on Majorana". So the two proposals state
one structure, and the dictionary is N <-> omega, L <-> omega z_2. Consequences to check before the fix round:
(1) C2B's link sentence, and any clause of P2 that says or implies that Dirac terms keep omega, should name
omega modulo the Standard Model group (or omega z_2); "a vev along T breaks omega to the grading" stands as
proved, but the rung vev also breaks omega itself, and what it leaves is omega z_2. (2) C1B's "number violation
is relative to the charge" (the flip automorphism) gets an invariant form: the class of the order-four element
modulo the unbroken gauge group. (3) The signed count for omega z_2 is 8 - 8 = 0 on sixteen and 8 - 7 on fifteen,
the "balanced" case of C2B's arithmetic; uniform and balanced counts differ by a gauge element, so they are the
same condition. Label: argued from stored statements plus signs; the one fact to verify by script is that the
stored grade-one doublet form is odd under the centre of su(2)_L (it is a doublet, so this is immediate).

### B2. One sign, four readings: P^2 = (-1)^m in Cl(2m,0)
Concerns: C1A and C1B (X1), C2A and C2B (Y2, Y3).
Entities: synthesis.signed-directions-and-the-integer-clifford-algebra (proved v2);
synthesis.blade-square-signs-f2-quadratic-form; synthesis.quarter-turn-rotors-of-the-even-subalgebra-form-a-state-design-of-order-three
(proposal, C1A); the two Y3 and Y2 proposals; synthesis.wall-rung-count-is-height-of-dying-line-class.
Why. The volume element P of 2m Euclidean generators has P^2 = (-1)^{m(2m-1)} = (-1)^m (computed). (a) X1: m odd
is C1A's hypothesis I^2 = -1 (the unit of the even subalgebra is P), m even is C1B's failing case where the
stored form q descends to classes. (b) Y3: the slot module's ten Majoranas are m = 5, so omega = P has square -1
and is an order-four element of the stored group of signed blades (q(V) = 1), central in its even subgroup; at
m = 4 (eight generators) there is no such element, only involutions. (c) Y3, walls: the rotor lift of the
antipodal map of S^{2m-1} is P, so RP^{2m-1} carries the order-four (twisted spin) structure exactly when m is
odd; this is C2B's w_2 = x^2 on RP^5, since w_2(RP^{2m-1}) = m(2m-1) x^2 = m x^2. (d) Y2: the rotor lift of the
quarter turn J in m planes is R_J = prod (1 + B_i)/sqrt 2, and (1 + B)^2 = 2B, so R_J^2 = P exactly: the lens
deck rotor is a square root of the volume element, of order eight exactly when m is odd, which is C2B's
w_2(L^5(4)) = u != 0 and the earlier run's "Z8 on L^5(4)" (the two reasons C2B contrasts are the same sign).
Use: C1A's design theorem applies as it stands to the slot module (ten generators, I = omega, D = 16), and its
design group commutes with omega; C2A's remark that the rung obstruction disappears "at Z8" and C2B's exclusion
of L^5(4) can cite one identity. Label: computed (the sign, R_J^2 = P by hand algebra), argued (identifications).

### B3. Gauge quarter turns on the sixteen have two orbits, 45 + 210 = su(16) over so(10)
Concerns: C1A (scope of the X1 design theorem), C1B (K1c), C2A and C2B (Y4, C7/N4).
Entities: C1A's and C1B's X1 proposals; synthesis.eviction-keeps-one-replica-saddle (the dependant);
standard-model.under-s-composites-state-space-spinor; the C7 computation in both C2 findings (no entity).
Why. Conjugation by a bivector quarter turn exp(pi/4 e_i e_j) sends a blade e_S to +-e_i e_j e_S when exactly one
of i, j lies in S, that is, it transposes two indices. So bivector turns alone act on blade classes through
permutations of the n = 2m indices and their orbits on the even classes modulo the volume element are the
weights up to complement (computed): 3 at n = 4; 15 at n = 6; 28 + 35 at n = 8 (C1B's split); 45 + 210 at
n = 10; 66 + 495 + 462 at n = 12. The number of orbits is floor(m/2) for every m, so the failure of bivector
turns from eight generators on does not depend on the parity of m; what depends on the parity of m is only
whether the higher-grade classes have real quarter-turn rotors (B2). C1B's "Unexpected links" sentence on a
"Bott-type dependence ... through e_v^2 = (-1)^m" should be restricted accordingly. At ten generators the two
orbits are the 45 bivector classes and the 210 four-vector classes, 255 = 16^2 - 1: exactly C2B's decomposition
of su(16) level 1 over so(10) level 4 (45 currents plus the 210 of weight 1). So the finite group made of gauge
rotors of the slot module is not a second-order design on the sixteen (two invariants in the second moment, one
per orbit), and C1A's theorem on the sixteen needs the four-blade rotors, which are the 210 directions outside
the gauge algebra. This is a statement about which averages the entropy comparisons may attribute to gauge
dynamics. Label: computed (orbit counts), argued (the consequence for second moments; not checked on states).

### B4. A test number for C1B: the Arf type alternates with m mod 4 (the tower clock inside X1)
Concerns: C1B (X1, the q-descent argument), C1A (its tower-clock remark).
Entities: synthesis.blade-square-signs-f2-quadratic-form; dark-matter.imported-eight-towers-mod-8-clock.
Why. For m even the stored form q(S) = |S|(|S|-1)/2 mod 2 descends to the 2^{2m-2} - 1 nonzero even classes.
Counts (computed): n = 4: 3 classes with q = 1, 0 with q = 0; n = 8: 28 and 35; n = 12: 528 and 495. These are
the minus, plus, minus types of a quadratic form in dimensions 2, 6, 10 over F_2, so the type alternates with
n mod 8 = 4, 0, 4: quaternionic against real even subalgebra in the stored clock. Prediction for C1B's argument
that the real normaliser preserves q: at twelve generators its orbits on classes are 495 + 528 (and bivector
turns alone give 66 + 495 + 462, with 66 + 462 = 528). This is the only mod-8 structure I can tie to X1; it is a
cheap exact test of the stated reason for the 28 + 35 split. Label: computed (counts), argued (that these are the
normaliser's orbits at n = 12).

### B5. Y1's extension count read in the towers' own dimensions sharpens X2
Concerns: C1A (X2 proposal), C1B (X2 findings), C2A (Y1).
Entities: synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants
(proved v4); synthesis.field-strength-heat-kernel-coefficients-of-the-dark-towers-fix-no-scale-ratio (proposal,
C1A); dark-tower-matter.three-dimensional-phases (proved v4); rule2.imported-parity-anomaly;
synthesis.imported-heat-kernel-coefficients-and-background-field-gauge.
Why. The stored flat kernel is a transverse operator T applied to s^{-2}, the square of the massless Dirac
kernel. In dimension d the same construction gives T applied to |x|^{-(2d-4)}, of scaling degree 2d - 2, so the
freedom degree is omega = d - 2. (i) d = 3: |x|^{-2} is locally integrable (2 < 3), so the transverse part needs
no extension at all, and T(delta) has order 2 > omega = 1: the field-strength coefficient has no freedom and no
logarithm. The only local term of order one is the parity-odd epsilon d delta, the Chern-Simons level, which is
exactly the datum the stored phases result uses (level 1/2 from the parity anomaly). So for the
three-dimensional towers C1B's input (c) "a regulator or completion" is not needed for the field-strength term;
the extension calculus leaves the level and nothing else. (ii) d = 5: |x|^{-6} fails local integrability by one
power; the extension exists and is homogeneous (no logarithm: the excess 2d - 4 - d = d - 4 is odd; rule from
memory), and T(c delta) is allowed (2 <= 3) with c of mass dimension one, so the freedom is one constant
proportional to a mass or a cut-off. That is C1B's "regulator-dependent power, zero in a scale-free scheme" in
the stored calculus. (iii) A logarithm multiplying T(delta) needs d - 4 = 0: C1A's "a logarithm only at d = 4"
gets a second derivation that does not use the heat-kernel Fact, and in d = 6 the logarithm would multiply a
four-derivative term, not F^2. Label: computed (integrability thresholds, omega = d - 2), argued (the rest;
the homogeneous-extension rule is memory, to be named with C2A's (SD) rules if used).

### B6. The descent supports the superselected reading in C1B's decision 3
Concerns: C1B (X1, decision 3), C2A and C2B (Y4, N6).
Entities: singularity.descent-parity-average (proved v5); synthesis.eviction-keeps-one-replica-saddle;
C1B's X1 proposal.
Why. Both C2 attackers found for N6 that the Petz map of the order-two expectation with an invariant reference
is the inclusion and a state is recovered exactly when it commutes with the parity. The stored descent IS that
expectation (parity average onto the even algebra). A pure state that survives the descent unchanged lies in one
parity sector, so the ensemble of descended pure states of a window is the sector ensemble, whose mean purity is
C1B's (dA + dB)/(dA dB + 2), not Lubkin's value. So the choice C1B lists as a matter of reading has a stored
ground for the superselected column whenever the comparison is made after a descent; whether the eviction
comparisons are made before or after is the remaining question for Leon. Also N6's "open problem only if a
stored evicted state fails to commute with the parity" and C1B's "eviction's state is a member of the finite
ensemble" are the same check from two sides. Label: stored (the descent), argued (the application).

### B7. Minor: the five-rung algebra and the slot module's algebra are isomorphic by a stored theorem
Concerns: C2A (Y4, C5, the flagged coincidence Cl(5,5) against Cl(10,0)).
Entities: synthesis.signed-directions-and-the-integer-clifford-algebra (proved v2).
Why. The stored theorem says two signatures of the same dimension give isomorphic algebras, over the integers
already, exactly when their Gauss sums agree. Counts (computed): both Cl(10,0) and Cl(5,5) have 496 blades of
square -1 and 528 of square +1, Gauss sum 32. So "no map is stored" can be sharpened to "isomorphic over the
integers by the stored classification, with no preferred isomorphism". This does not make the coincidence a
link between the wall and the slot module; it removes the "different real form" caveat only.

## Links rejected

- Finite-ensemble moments as subspace counts against the mod-16 question (orchestrator's first candidate). The
  stored F_2 data (q, its polar form, the Gauss sum) carry an invariant that is an eighth root of unity at most
  (the clock); a mod-16 invariant needs a Z4-valued refinement and an index or eta statement, none stored. The
  Galois number G_3(2) = 16 at replica number four is a coincidence of numbers. The Klein twist is a polynomial
  in the grading (C2B), so it is a scalar on each parity sector and is invisible to C1's sector averages. What
  survives of the candidate is B2 and B3.
- Bott-type dependence of X1 against a mod-8 dependence of the rung count (second candidate). The rung results
  show period-two behaviour in n and thresholds 1, 2, 4 (C2B), no stored or computed mod-8 statement; C2A's
  Clifford-module remark on L^7(4) is a count of one module dimension. The shared structure is the sign of B2
  only; the mod-8 content on the C1 side is B4.
- "Three fields carry xi_R" against the edge-mode reading (third candidate, N7). C2A's N7 computation already
  gives the answer: Sakharov weights are -4 s^2 (-1)^{2s}, remainder zero, no edge term in the character; a
  helicity-s state weighs like a scalar of xi_R = (1 + 2 s^2)/6. Joined with C1A's X3 remark this gives an exact
  coincidence (computed): at the isotropic point the stored tilt order is nu^2 = (3/2) xi_R = 1/4 + s^2/2, so
  scale invariance (nu = 3/2, xi_R = 3/2, C1A's seven-generation zero) is the weight of a helicity-2 state, and
  the fitted window is s^2 in [4.068, 4.144]. Rejected as structure: the attachment's modules are conformal, so
  on the isotropic point (a Weyl-flat field) every one of them has nu = 1/2, and the stored gravitational-wave
  modes keep the stored index. Two formulas, no shared field. Worth one line in C1A's and C2A's notes so the
  coincidence is not rediscovered as a lead.
- xi_R through the massive vector's weight -(3 + 6 xi_R alpha) as a fourth carrier (my own candidate). It is
  stored, C1B already uses it, and it is gauge-parameter dependent; it adds a caveat to "which field", not a link.
- Kasner helicity against the helicity lift (R12): both C2 attackers killed it (a homonym). Agreed on lookup.
- Mass-as-pair-term against "the Klein twist's charge" (fifth candidate as first posed): the Klein twist carries
  no charge at all; the live form of the candidate is B1.
- Y1's V(x,x) coefficient against xi_R (C2A's own link): plausible but nothing stored fixes either coefficient;
  no test available by lookup.

## Status of what was sent
All seven links are in this file for the orchestrator to relay; none was sent directly. B1 asks for a wording
check in two registered proposals before the referee round; B3 and B4 each name an exact count an attacker can
confirm in minutes; B5 is a scoping sharpening for X2 and a second derivation for one clause.
