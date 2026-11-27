# Report, run 2026-11-27-null-surface-three

Request (Leon, 27 November 2026): take the three ideas found worth having in V. Chandrasekaran, arXiv:2611.34924,
and work each out in the graph's own terms, with agents: (1) the second-order stress of the first-order
gravitational field as a source; (2) the corner area as the generator of the relative boost of a null-plane
pair; (3) null-surface data at any field strength. Standing instruction: the graph's own results and methods
first; the paper is a guide to what to look for and is credited as the prompt.

Method: lean form of the standing method. One constructive attacker per target (three attackers, Claude Fable
5.2), each with kill conditions registered before computing; one blind referee per entry (three, Claude Opus
5.5), each with independent exact-arithmetic tests on fresh data; one fix round by the authors; a second pass
(Claude Opus 5.5) on everything added after the first review and on consistency between the three entries; three
small fixes from the second pass applied centrally. All three entries SOUND WITH FIXES at first review; after
the fix round and the second pass all three ACCEPT. No adversarial attacker and no bridge pass were run; one
cross-link between attackers was relayed by hand (the plane wave in the Kerr-Schild gauge).

Central gates after the last edit: tp.lint 0 errors 0 warnings on each entry; 12, 10 and 7 check functions
pass; mutation tests clean (no W413); store layers 1, 2, 3, 5 with 0 errors and the same 3 warnings as main;
468 unit tests pass. The full layer-4 run is left to CI.

## What was established

### 1. synthesis.second-order-stress-of-the-first-order-gravitational-field (op.einstein-from-the-field-theory)
Premises: the two results of 26 November and the stored weyl-flat result. No imported Fact pinned.
- proved: the quadratic part G2[H1] of the Einstein map is a symmetric map for every H1, on and off solutions.
- proved: its flat divergence is a sum of terms each carrying the first-order map or its derivative, so it
  vanishes on first-order solutions; the off-solution form is given. Kill condition K1 did not fire.
- proved: under a displacement, a rotation gauge change or a second-order reparametrisation it changes by the
  first-order map of an explicit quadratic field X (K2 did not fire). So t = +G2/(8 pi G) is NOT invariant at
  any point; every change is the divergence of an explicit bivector; fluxes through a complete null plane are
  unchanged by changes of compact support.
- proved: in the light-cone gauge the null-null component is <sigma,sigma> + theta^2/2 plus a second derivative
  along the generator depending on the second-order parametrisation; its integral along each generator equals
  that of the stored density <sigma,sigma>/(8 pi G) under a stated fall-off.
- proved (exact finite computation): one plane wave has the stress along its momentum; in the exponential
  parametrisation this is Isaacson's form at each point without the average.
- proved given (M1), (M2), second order only: the matter's second-order stress is not conserved in the flat
  sense, the sum with t is; among multiples of t only t itself, with the matter's constant, balances. This is
  NOT a derivation of condition (C) of the field-equation result: (M2) is that condition for the matter.
- instance (proved, computed): the plane wave in the Kerr-Schild gauge has no quadratic part at any point,
  though it focuses crossing null planes; the gauges differ by a displacement growing across the plane together
  with a rotation gauge change. The fall-off condition cannot be dropped.
- sign: the store's equation is G = -8 pi G T, so t carries a plus sign.

### 2. synthesis.corner-area-variation-of-a-null-plane-pair-is-the-charge-of-the-relative-boost (op.derive-loc-and-r-loc)
Premises: the first-order null-plane result, the two-free-directions result, the stored dual-plane theorem, and
the imported null-plane modular first law (clause (vii)(b) only). The imported Noether-charge entropy Fact is
not a premise and is not in the past cone.
- proved: pairing the stored symplectic current with a displacement is twice the field equation along the flow
  plus the divergence of an explicit bivector potential; the six bivectors it is built from span the
  rotor-covariant, reflection-even ones.
- proved: at the corner the potential's boost component is minus the rate times the transverse trace, in every
  gauge; the area density derived from the position gauge field is 1 + (1/2) tr_perp h at first order.
- proved: for a vacuum first-order field and a flow that is the relative boost near the corner and the identity
  away from it, the part of the generator linear in the field is a pure corner term, the area variation over
  8 pi G in magnitude, sign fixed by orientation (K2, K3 did not fire).
- K1 FIRED in its literal form: for the exact boost the displacement vanishes, the linear part is identically
  zero, and the generator from the stored current is a quadratic bulk term, not positive definite unless the
  expansion vanishes. Both true statements are filed and tied together by the first-order focusing equation.
- proved given the hypotheses of the first-order theorem: the first law about any cut by two routes that agree.
- proved for any field strength in the gauge: focusing in area form; given the null-null field equation (F),
  the second-order area combination. No separate check of the last statement.
- proved: the dual of the boost plane is the corner plane; the continued boost on values. Proved given the
  imported Fact and hypothesis (S): the relative-entropy statement with 1/(4G).
- argued only: the weight exp(-delta A/(4 G hbar)). NOT derived: the area entropy itself, anything on a
  background of nonvanishing field strength, the period (imported), (Loc) as an entropy statement.

### 3. synthesis.null-surface-data-at-any-field-strength-the-focusing-equation-integrated (op.gravitational-field-at-null-momentum)
Premises: the two results of 26 November. No imported Fact pinned.
- proved: the root area density rho defined from the position gauge field obeys rho' = theta rho/2, and the
  focusing equation is the linear equation rho'' = -(1/2)(<sigma,sigma> - K.R(K)) rho.
- proved: two integrated forms, in the parameter s (d s = d lambda/rho) with no monotonicity condition, and
  with rho as parameter where rho' is nonzero; the second agrees, as far as two text extractions show, with the
  prompting paper's formula. The typeset paper was not read directly.
- proved given the null energy condition (P): the focusing bound 2/|theta|, in the weaker form that the smooth
  stretch with rho > 0 ends within that distance.
- proved: the component of the field equation along the generators leaves the shape history free and slaves
  the area to it, with two constants per generator. The characteristic initial value theorem is NOT claimed.
- proved and checked: the plane wave of any amplitude is an exact field whose curvature is the stored
  first-order curvature with no correction; any shape history is realised (the same on every generator);
  orders one to four in the amplitude; an exact vacuum wave taking a null plane to a caustic.
- relations proved, reading argued: the area as a clock on each monotonic stretch; nothing on which flow is time.
- no kill condition fired; no error found in the stored focusing clause it rests on.

## Decisions for the maintainer (none taken here; open-problem records not edited)
1. Whether op.einstein-from-the-field-theory records clause (viii) of entry 1 with attack items (every order;
   deriving (M2) from the stored response of matter).
2. Reference parametrisation at second order (entry 1): linear in H1 as filed, or exponential.
3. Whether results citing the imported Noether-charge Fact at first order should cite entry 2 clause (iv);
   whether op.derive-loc-and-r-loc takes an attack item for the corner charge on a field that is not weak.
4. Hypothesis (S) and the argued weight paragraph of entry 2: register, keep local (as filed) or remove.
5. Which open problem entry 3 sits under; whether its plane-wave clause is split off and lib/gtg.py takes a
   plane-wave constructor; whether entry 2 clause (vi)(b) is re-pinned to entry 3.
6. Whether the first-order null-plane result's Reading and Limits cite entries 1 and 3.

## Literature status
References added: Isaacson1968, Deser1970, CarlipTeitelboim1995, DonnellyFreidel2016, AbbottDeser1982,
Sachs1962, Penrose1965, Rendall1990, CiambelliFreidelLeigh2024. Bibliographic fields verified by the referees
against index or publisher pages, except the last page of Isaacson and the journal locator of Deser, which
match memory only. Cited by name from memory, no key: Gupta 1954, Feynman's lectures, Freud 1939, Brinkmann,
Bondi-Pirani-Robinson, Kerr-Schild, Hawking-Ellis, Jacobson 1995, Gao-Wald. arXiv:2611.34924 was read through
its abstract page and text extractions, not the typeset PDF; the entries say so.
