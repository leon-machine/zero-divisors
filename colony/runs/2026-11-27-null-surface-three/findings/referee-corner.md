# Blind referee: synthesis.corner-area-variation-of-a-null-plane-pair-is-the-charge-of-the-relative-boost

I did not read the author's findings file or work folder. I read RUN.md, R1 and R2, the stored Definition, the four pinned premises, the Wald Fact, op.derive-loc-and-r-loc, and the entry in full (entity.md, proof-main.tex, check.py).

## Verdict: SOUND WITH FIXES

The mathematics is right. Every identity I tested independently holds, on data different from the entry's. That includes the headline coefficient: the corner term is -(1/8 pi G) times the integral of w a_1, with a_1 = (1/2) tr_perp h. The factor 2 between tr_perp h and the area variation is correct, and so is the factor 2 between 1/16 pi G and 1/8 pi G. The fixes concern wording. Several sentences claim more than the formal clauses prove, or more than the clauses' own labels allow:
- the header sentence on clause (f);
- calling the cut-off flow's linear term "the generator";
- "boost energy of the two components" for a form that is not positive definite;
- "independent of the gauge";
- "delta A/4G" in the one-liner;
- the sign of the paper's weight;
- the Abbott-Deser identification;
- no word on the imported field-equation Facts that sit in the past cone.

## Required fixes

1. **entity.md, formal preamble, "the field equation of clause (f) is not assumed anywhere".** This is contradicted by hypothesis (F) of (vi)(c), which is the null-null component of that equation. Clauses (v) and (vii)(b) also use the first-order field equation of R1(vi), which holds under R1's (L), (D), (V), (N). Replace the sentence with: "the field equation of clause (f) is not assumed, except that clause (vi)(c) takes its null-null component as the named hypothesis (F); clauses (v), (vi)(c) at first order and (vii)(b) use the first-order field equation of clause (vi) of the first-order theorem, under that theorem's hypotheses (L), (D), (V), (N)."

2. **Formal (iv) and (v), labels and the constant.** The coefficient 1/16 pi G, and with it 1/8 pi G, is R1(vi)'s constant, which is fixed under (L), (D), (V), (N). The source form of (v) needs the same hypotheses.
   - Change the label of (v) to "(The exact boost and the first law; proved, the form with a source given (L), (D), (V), (N) of the first-order theorem.)".
   - In (iv), change "The magnitude 1/8 pi G is twice the constant 1/16 pi G of the stored current and is not adjustable" to "The magnitude 1/8 pi G is twice the constant 1/16 pi G of the stored current, which the first-order theorem fixes under its (L), (D), (V), (N); given that constant it is not adjustable".

3. **Formal (iv), what "the generator" of the pair is.**
   - The generator of the pair is defined as the sum of the two window generators. This is a definition (the light-front setting), and it is stated only in the Reading's Limits. Add to the "Fluxes and generators" paragraph: "For the pair, the generator of a flow is defined as the sum of the generators of its two halves; that is, the flux of the current through N_+ together with N-bar_+ is taken as the symplectic form of the pair (the light-front setting of the first-order theorem, not proved here)."
   - In (iv), replace "the generator is H = ..." with "the part of the generator linear in h is H = ...". Then add: "This is the generator of a flow that is the relative boost near C and the identity away from it. For the exact boost of both halves the linear part vanishes identically (Delta_{xi_B} = 0), and the corner term enters only through the balance of (v), against the far cut and the matter flux."

4. **One-liner.** Two places say more than is proved.
   - "so on solutions the generator of the relative boost of the two half-planes is delta A/8 pi G" should read "so on solutions the part linear in h of the generator of a flow that is the relative boost of the two half-planes near the corner, and trivial away from it, is delta A/8 pi G".
   - "the entropy change of crossing matter is delta A/4G" is wrong as written. delta A is defined as the first-order area of the corner, but the entropy statement concerns (area of the far cut continued back less area of the corner), less the relative entropy. Replace with: "the vacuum-subtracted entropy of the state on N_+ is (area of the far cut continued back less area of the corner)/4G at first order, and at most that".

5. **Reading, "for the exact boost the generator vanishes identically on solutions, because the flat field is invariant".** This contradicts (vi)(a), where the exact boost has a nonzero quadratic generator H^(2). Also, the linear part vanishes identically, not only on solutions. Replace with: "for the exact boost the part of the generator linear in h vanishes identically, because Delta_{xi_B} = 0; what the identity of (i) then gives is a balance: the boost energy that crosses the half-plane (of matter at first order and, given (F), of the field at second order) equals the difference of the area terms at its two ends over 8 pi G, (v) and (vi)(c)."

6. **(vi) heading, (vi)(a), (vi)(c), technical and lay: "boost energy of the field's own two components".**
   - H^(2) = (1/8 pi G) int lambda (<sigma,sigma> - theta^2/2) contains the trace term with the opposite sign. It is not positive definite, and the trace is not one of the two components. On vacuum first-order fields in the gauge, theta is constant along each generator but need not vanish on a window, so the term survives.
   - Change the (vi) heading to "(Second order: the quadratic boost generator; ...)".
   - Add to (a): "It is the boost-weighted null energy of the two components plus a trace term of the opposite sign; it is not positive definite unless theta = 0 (on vacuum first-order fields in the gauge theta is constant along each generator)."
   - In (vi)(c), the last sentence and the technical level: say "the quadratic generator of (a)", not "the boost energy of the field's own two components".
   - Lay level: "gravitational waves crossing the wall count in exactly the same way as matter, one order further on" should read "given the field equation at second order, gravitational waves crossing the wall count with the same coefficient as matter, one order further on, together with a term from the expansion of the light rays that enters with the opposite sign".

7. **Extraction note "independent of the gauge" and Reading "no dependence on the gauge".** By the entry's own (ii), under a displacement along C the density changes by 2 w div_perp zeta_perp. Its integral is a flux through the edge of the window, plus -2 int grad w . zeta_perp when w is not constant. Replace both with "independent of the gauge up to a divergence along the corner under displacements along it (clause (ii))".

8. **Extraction note, circularity and the past cone.** "Clauses (i) to (vi) use no imported Fact" is true of the pins, but the note does not say that imported field-equation Facts sit in the past cone. I walked `uses` over the whole store (252 entries; the labcli `cone` output stops at 200). The paths are:
   - synthesis.imported-einstein-cartan-matter-coupling, through first-order-gravitational-field-has-two-free-directions... (pinned) and gravitational-pair-production-from-the-operator-source-at-first-order;
   - hawking.imported-exterior-exactly-general-relativity, interior.imported-equivalence-einstein-equations and singularity.imported-equivalence-einstein-equations, through the same pinned result's clause (viii), synthesis.dimmed-burst-time-rescaled-copy and hawking.greybody-inheritance-under-interface-premise;
   - synthesis.imported-lovelock-and-anderson-duchamp-natural-lagrangians, through R1 and synthesis.weyl-flat-variations-...

   synthesis.imported-wald-noether-charge-entropy is not in the past cone. That part is clean.

   Add to the note: "The past cone contains imported Facts that state the field equation (synthesis.imported-einstein-cartan-matter-coupling, hawking.imported-exterior-exactly-general-relativity with the two imported equivalence Facts, and synthesis.imported-lovelock-and-anderson-duchamp-natural-lagrangians), through the pinned two-free-directions result and the first-order theorem. The clauses used here (the kernel of the stored Einstein map at null momentum, which is algebraic from the stored first-order curvature, and the current, flux, focusing equation and constant of the first-order theorem) do not rest on them. synthesis.imported-wald-noether-charge-entropy is not in the past cone." Change "clauses (i) to (vi) use no imported Fact" to "clauses (i) to (vi) pin no imported Fact".

9. **Formal (vii)(b).**
   - (a) "and half a period gives 1/8G" has no proved content in this clause, which concerns an entropy and not a weight. Delete it, or move it to the Reading's paragraph on the weight.
   - (b) "the entropy change of what crosses N_+ is the area change over 4G" should read "the entropy difference Delta S of rho on the algebra of N_+ (clause (iii) of the Fact) is the area combination of (v) over 4G".
   - (c) State (S) so that its extent is visible. Proposed wording: "(S): semiclassical coupling at first order: the first-order field solves the equation of (v) (hence under (L), (D), (V), (N)) with source the expected stress rho(T) - omega_0(T), supported in 0 < lambda < Lambda, y in U, for a state rho with S(rho||omega_0) finite and finite Delta<K>. (S) is not a consequence of any stored result."

10. **Source of the idea, sign of the paper's weight.** "weights a corner of area A by the exponential of A/4G hbar" drops the sign. The paper's (5.23b) is C_D^dagger C_D = P_D e^{-A/(4 G hbar)} P_D. Each half-turn i pi gives e^{-A/(8 G hbar)}, and two copies glued give the full 2 pi. Write "by exp(-A/4G hbar)", which also agrees with the entry's own Reading.

11. **Source of the idea, Abbott-Deser.** "the potential of clause (i) is, for a field that preserves the flat product, the potential of the conserved charges of the first-order field [AbbottDeser1982]" asserts an identity of potentials that was not checked. The entry itself says the paper was cited from memory. Two potentials that obey the same equation, div Psi = -2 E[h](xi), can differ by a divergence-free bivector, and that difference matters on a window with a corner. Replace with: "plays, for a field that preserves the flat product, the role of the Abbott-Deser potential of the conserved charges of the first-order field [AbbottDeser1982] (not compared term by term here)".

12. **Lay level, second outcome.** "equals the difference between the areas at the far end of the wall and at the corner" leaves out the continuation of the far cut back along its tangent. It is false as worded unless the far cut has stopped focusing. Write: "equals the area at the far end, as it would be if continued back along the light rays to the corner, less the area at the corner".

13. **Technical level, fourth paragraph.** "the second-order area deficit of the corner over 8 pi G" misdescribes the quantity. Replace with "the second-order area combination of (v) (the far cut continued back, less the corner) over 8 pi G, given the null-null field equation at second order".

## Optional suggestions

- Title: put "first-order" in it ("First-order corner charge of the relative boost of a null-plane pair"). At present only the id ("area variation") signals first order.
- (i), uniqueness: add that the six listed bivectors are all the bivectors bilinear in h and xi with one derivative that are even under reflection. That is what makes "the only one" meaningful. The rank-6 statement is correctly worded and correctly computed.
- (vi)(c): the notation "h = 2 epsilon s_1" mixes the coefficient with the order. Use h = 2 s_1, with sigma and theta the coefficients of epsilon.
- check.py, check (vii):
  - The part for (b) re-tests (v). The test `2*boost_energy == F(1,4)*area_change` follows from `boost_energy == F(1,8)*area_change`.
  - `premise(MODULAR)` is called, but nothing from the Fact enters: the 2 pi is hard-coded.
  - Either say in the label that only the arithmetic 2 pi/8 pi G = 1/4G is tested, or drop the (b) part.
- check.py: `coef == COEF` (check (i)) and `(gb - g) == 0` (check (iv)) are vacuous by construction. Harmless.
- Carlip-Teitelboim: their opening angle is the Euclidean one. "the Euclidean opening angle at the horizon" is more exact than "the opening angle of the boost".
- "Units hbar = c = 1" in the formal preamble, with hbar written explicitly in the Reading. Harmless, but either say "hbar restored in the Reading" or drop hbar there.

## Answers to the twelve points

1. **Clause (i).** Verified independently on cubic polynomial h and xi in no gauge.
   - My omega, E and Psi were written from R1's displayed formula and from the standard linearised Einstein tensor, in lower components. They do not use the entry's helpers.
   - My transcription of omega passes antisymmetry and div omega = <E h1, h2> - <h1, E h2>.
   - I computed the rank of the six candidate divergences myself: 6. So the coefficients (1, -1, -1, 1, -1/2, 0) are unique among the six, and the wording is correct (see the optional point on completeness of the six).

2. **Clauses (ii) and (iii).**
   - (ii) holds for a general xi: w xi_B plus terms in the ideal (t, z)^2, and also with an arbitrary weight w. Delta_xi vanishes on C.
   - (iii): the physical bivector is hb^{-1}(e_1) ^ hb^{-1}(e_2), the outermorphism of hb^{-1} as clause (a) of the Definition requires (physical vectors are hb^{-1}(a)). In R1's convention hb^{-1} = id + s gives h = 2s; in general h = H + H^T for hb^{-1} = id + H, and the antisymmetric part drops at first order. Then a^2 = 1 + tr_perp h and a_1 = (1/2) tr_perp h. This agrees with the standard induced metric -delta_ij + h_ij, for which sqrt(det(delta - h)) = 1 - (h_11 + h_22)/2 and tr_perp h = -(h_11 + h_22).
   - Against R1(vi): the quadratic action density of R1 has magnitude 1/(64 pi G) on the TT part, and its current is omega/16 pi G. Both are the standard Fierz-Pauli normalisation.
   - The corner coefficient 2/(16 pi G) = 1/(8 pi G) is therefore the standard kappa/8 pi G with kappa = 1 for x.B. No factor-2 error.

3. **Clause (iv), the headline.**
   - I verified it on a general vacuum polynomial solution of degree 4. It came from the 570-dimensional kernel of E, not from plane waves, and was not in the gauge.
   - I used my own window (lambda in [0,3], x in [-1,1], y in [0,1]), my own cut-off (1 + xy) x-and-y bumps, and an extra part of xi in (t,z)^2.
   - Results: the flux through N_+ is -int g tr_perp h = -1222/33075. The flux through N-bar_+ is +1222/33075. Off shell the remainder is 2 int n.E(xi).
   - The sign is consistent across (iv), (v), the Reading and the standard first law. The corner piece of the exact future boost's total generator is -delta A/8 pi G, the same as (iv) with w_N = 1.
   - The headline is fair only if the cut-off and linear-order qualifiers are stated (fixes 3 and 4). The Reading's "generator vanishes" is inconsistent (fix 5).

4. **Clause (v).** Verified independently:
   - div Psi_{xi_B} = -2 E(xi_B) for generic h;
   - the split of n.(div Psi) and of n-bar.(div Psi);
   - in the gauge: -B.Psi = tau - lambda d_n tau, the transverse term vanishing, and n.E(n) = (1/2) d_n^2 tau;
   - the first law with a source (T := -E/8 pi G) on my own window, int lambda T_nn = (1/8 pi G)(far - near). It is correct.

5. **Clause (vi).**
   - (a): I verified the density formula with my own Lie derivative. I also verified the covariance identity for general (ungauged) fields, which underlies the variation of H^(2), and E[L h] = L E[h]. The trace sign -theta^2/2 is right, but "boost energy" is not an accurate name for a form that is not positive definite (fix 6).
   - (b): verified on a new field that is not weak, with dependence on u = t - z as well, at a new point. Results: theta = d ln a, and a'' = a(theta^2/2 - <sigma,sigma> + n.R(n)); the opposite sign of theta^2 fails. The gauge hypothesis (s symmetric, s(n) = 0) is stated properly.
   - (c): the derivation is complete: one integration of (b), (F), and an order-by-order expansion that I checked by hand. (F) is stated properly, and "proved given (F)" is the right label. It has no check of its own.

6. **Clause (vii).**
   - (a): correct, and correctly limited to values; it agrees with the dual-plane theorem's (i) and (ii).
   - (b): every step is either pinned or proved, and the imported Fact is named as imported. The factor 2 pi/8 pi G = 1/4G is applied to the right quantity: Delta<K> equals the boundary combination of (v) over 8 pi G. (S) understates what it assumes, and "half a period gives 1/8G" should go (fix 9).

7. **The Reading's weight.** It is marked "argued", "not proved here, and not a premise of the store". The lay and technical levels mark it as argued, and the one-liner does not mention it. Nothing claims that A/4G itself is derived: the Reading and the lay level both say that only changes are reached. The one-liner's "delta A/4G" mislabels the quantity (fix 4).

8. **Circularity.** The Wald Fact is not in the past cone. Imported field-equation Facts are, and the entry does not say so (fix 8). The clauses actually used do not rest on them.

9. **Checks.** All seven pass (checkone run once). Each tests its clause.
   - Check (iv) uses plane waves plus a displacement. My general-solution test closes that gap.
   - The (b) part of check (vii) tests only arithmetic (optional fix).
   - Premises are called in the functions that rely on them.
   - (vi)(c) is declared as having no check.

10. **Rules.** No em dash, no "honest", no "load-bearing", no "curved spacetime", no Christoffel, no bare imaginary unit. Session and agent names appear only in the front matter, where required. T_{uu} appears once, as a labelled translation of the Fact's notation. The title is under 90 characters. Theorem and Proof are used only for clauses proved in the entity. No literature is used as a premise.

11. **Citations.** The credit to Chandrasekaran: "prompted by" and "takes the question from it" are fair. The paper's text does say "dA/(8 pi G_N) is conjugate to a local relative boost angle gamma = Gamma_R - Gamma_L" (Sections 3.6 and 4.2) and gives the weight exp(-A/4 G_N hbar) in (5.23). The abstract alone mentions neither. Only the sign is wrong in the entry (fix 10). Reference fields:
   - **CarlipTeitelboim1995:** authors, title, Class. Quantum Grav. 12 (1995) 1699-1704, arXiv gr-qc/9312002 and DOI 10.1088/0264-9381/12/7/011 all **verified** (arXiv abstract page; also the bibliography [51] of arXiv:2611.34924). The description is accurate (Euclidean opening angle; optional fix).
   - **DonnellyFreidel2016:** authors, title, JHEP 09 (2016) 102, arXiv 1601.04744 and DOI 10.1007/JHEP09(2016)102 all **verified** (Springer article page; bibliography [12] of the prompting paper). The description is accurate.
   - **AbbottDeser1982:** authors **verified** (bibliography [4] of arXiv hep-th/0103255). Title, Nucl. Phys. B 195 (1982) 76-96 and DOI 10.1016/0550-3213(82)90049-9 **verified** (Scilit record). There is no arXiv number, correctly omitted. The description as worded overclaims (fix 11).

12. **Four levels.** The one-liner, lay and technical levels each say more than the formal statement in the places given in fixes 4, 6, 12 and 13. Otherwise they say the same as the formal level.

## What I verified independently, and how

All of it is in /home/claude/scratch/referee-corner/. It uses my own exact polynomial ring over Fractions (poly.py) and my own lower-component linearised fields (lin.py), plus lib/GA.py and lib/gtg.py for the field that is not weak. Nothing is imported from the entry's check.py.

- **t1_identity.py:**
  - my omega is antisymmetric and has divergence <E h1,h2> - <h1,E h2>;
  - identity (i) holds on three fresh cubic (h, xi) pairs in no gauge;
  - the six candidate divergences have rank 6;
  - the entry's coefficients reproduce the identity.
- **t2_corner.py:**
  - the corner value (ii) holds for xi = w xi_B plus (t,z)^2 terms;
  - a general degree-4 vacuum solution was computed by exact elimination (kernel dimension 570, not in the gauge);
  - the flux on N_+ and N-bar_+ for my own cut-off boost and window is -/+ int g tr_perp h exactly;
  - the off-shell remainder is 2 int n.E(xi).
- **t3_boost.py:**
  - Delta_{xi_B} = 0 and div Psi_{xi_B} = -2 E(xi_B);
  - the splits on N and on N-bar;
  - in the gauge: -B.Psi = tau - lambda d tau, the transverse term vanishing, and n.E(n) = (1/2) d^2 tau;
  - the first law with a source on a new window;
  - the (vi)(a) density with my own Lie derivative;
  - the covariance identity on general fields;
  - E[L h] = L E[h].
- **t4_focus.py:** a new field that is not weak (s(n) = 0, with u and v dependence), checked torsion-free. At a new point: theta = d ln a and the area-form focusing equation hold exactly, and the wrong sign of theta^2 fails.
- **By hand:**
  - R1's normalisation against Fierz-Pauli, hence 1/16 pi G for the current and kappa/8 pi G at the corner;
  - the orientation of R1's dP against the entry's definition of the generator;
  - the sign of the corner term against the standard first law;
  - the order-epsilon^2 expansion in (vi)(c);
  - the GA identities of (vii)(a).
- **Past cone:** walked over the `uses` of every entity in store/.
- **Web:** arXiv:2611.34924 (abstract and full text), and the sources listed in point 11.
- **Gate:** `python -m tp.checkone` was run once: all 7 checks passed. No mutants run, no lint run, no git, no store edits.
