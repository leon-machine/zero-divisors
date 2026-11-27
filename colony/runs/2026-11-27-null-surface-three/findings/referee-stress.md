# Referee report: synthesis.second-order-stress-of-the-first-order-gravitational-field

Blind referee. Read: RUN.md, R1, R2, the stored Definition, and the entity in full (entity.md, every line of
proof-main.tex, check.py). I read nothing under findings/attack-* or work/.

## Verdict: SOUND WITH FIXES

All eight clauses are mathematically correct as formal statements. I checked every central identity
independently, in a different formalism (see below), and they hold exactly. What needs fixing is wording.
Several sentences outside the clause statements (the last sentences of (iv) and (viii), the Reading, the
technical level, the lay level and the one-liner) claim more than the clauses prove. The credit to
Chandrasekaran2026 also says something about the paper that the abstract, the only part read for this entry,
does not contain. One Reading sentence uses the second-order field equation without saying so.

## Independent verification (scripts in /home/claude/scratch/referee-stress/)

Method: these scripts do not use GTG or gtg.Field, and they import nothing from check.py. tpoly.py is my own
ring of truncated polynomials in (x0..x3, eps), with Fraction coefficients, spatial degree <= K and eps
degree <= 2. From hb = id + eps H1 + eps^2 H2 it builds the coframe hb^{-1} as an eps-series, the metric
g = sum_a eta_a theta^a theta^a, the inverse metric from the tetrad E_a = hb(e_a), the Christoffel symbols,
the Riemann, Ricci and Einstein tensors (usual sign), and the frame components G_usual(E_a, E_b). GA.py is used
only for Omega1 and the bivector algebra of the divergence terms. All data are fresh: other seeds, other null
momenta ((13,12,5,0), (17,8,0,15)), and other displacements, bivector fields and profiles.

- t1: the map with matrix e_k . calG(e_c) = -G_usual(E_k, E_c) has eps-coefficient E[-(H1+H1^T)] at the
  point, with H1 not symmetric. So the store's Einstein map is minus the usual one. This settles point 1
  independently: G = -8 pi G T gives t = +G2/(8 pi G) = -G2_usual/(8 pi G), the standard sign of the
  literature. (ii) holds: G2 is symmetric, with 16 nonzero entries, for H1 neither symmetric nor a solution.
- t2: (iii) holds exactly, in all four directions, on an H1 of degree 3 that is neither symmetric nor a
  solution. All twelve terms are nonzero. Of the 8 sign patterns of the three terms, only the stated one
  (-,-,-) fits, so each sign is determined. The Omega1 of (i) is used, so this also tests Omega1.
- t6: the formula (*) of the proof of (iii) and (viii) holds. I computed the eps^2 coefficient of the
  Levi-Civita divergence nabla_mu T^mu_nu E_c^nu, with T^mu_nu = E_k^mu M[k][c] theta^c_nu, for a generic
  symmetric M1, a non-symmetric M2 and a non-symmetric H1. It equals
  div M2(c) + gdot.H1(udot) + u.w + c.(Omega1(d_a).M1(a)) exactly. This is the step (viii) rests on.
- t3: (iv) holds. Off solutions, the displacement law holds exactly; flipping the sign of any one of the
  three parts of the quadratic field fails. The rotation law holds off solutions, and so does the
  parametrisation law (generic q). On a fresh solution (two null waves, a displacement and a rotation gauge;
  H1 - H1^T has 10 nonzero entries), the changes equal G1[X_xi] and G1[X_B], each nonzero in all 16 components.
- t7: the displaced flat field itself, H1 = -xi_ (G1 = 0), has G2 = G1[-xi_ xi_], nonzero in 14 components.
  This is the cleanest example of point 4. It also gives a proof of "at every point" (fix 1).
- t4: (vi) holds off solutions, which the entry's check does not test. On three symmetric H1 with H1(n) = 0
  that are not solutions (E[h] has 16, 16 and 14 nonzero entries), n.G2_r(n) = <sigma,sigma> + theta^2/2 +
  (1/8 - r/4) d_n^2 <h,h> for r = 0, 1, 1/2 and 3/7. All 12 cases agree.
- t5: (vii) holds on two waves along nbar with cubic profiles, for r = 0, 1, 1/2 and 2, all 16 components.
  (v): E[x](a) = div W_a[x] on a polynomial symmetric x (not a symbol), and the null-null identity of (v)
  also holds on it.
- I ran tp.checkone once: all 10 checks pass. tp.lint: 0 errors, 0 warnings.

## Points settled

1. Sign and constant. Correct. R2 (vii) and R1 (vi) both give calG = -8 pi G T. The eps^2 coefficient gives
   G1[H2] = -8 pi G (T2 + t) with t = +G2/(8 pi G). In the exponential parametrisation and the gauge (LC),
   n.t(n) = (<sigma,sigma> + theta^2/2)/(8 pi G) >= 0, the same sign as n.T(n) for dust and as R1's P >= 0.
   For one wave, e0.t(e0) > 0. In the parametrisation in which t is defined (r = 0) it has no sign at a point,
   which is correctly stated. Its integral is positive under (F).
2. (ii) is proved correctly (R2 (i), (ii) at each eps), and I verified it on a non-symmetric non-solution.
3. (iii) is correct, signs included (t2, t6).
4. (iv): all three laws and the X fields are correct (t3). The statement "not invariant ... at any point"
   rests only on one sample point, so it is overstated as worded (fix 1). The claim is true, and t7 plus a
   scaling argument proves it.
5. (v): the superpotential identity and the null-null identity are correct (t5). For P_c with c not n, only
   invariance under changes of compact support is claimed, with "when it converges", and that is proved.
   Nothing more is claimed for P_c in the formal level, and the Limits say only P_n is evaluated. The P_n
   condition ("fast enough for the boundary integrals to vanish") is in effect the conclusion restated
   (optional 5). The one-liner and the lay level drop the support qualifier (fixes 5 and 6).
6. (vi): the identity uses only R1 (iii) and (iv), which are free of the field equation, so it holds off
   solutions as claimed (t4). The integrated statement uses the first-order vacuum equation, and says so ("on
   a first-order solution"), through R1 (ii) (d_n^2 tau = 0). (F) is enough for both the theta^2 term and the
   d_n^2 <h,h> term, but convergence of the integrals is not stated (fix 7). The last sentence of (vi) holds
   only on solutions, because the X-law does (fix 7).
7. (vii) is worded correctly in the formal level: one wave, along nbar, and the exponential parametrisation
   for the "at every point" form. The Source paragraph says "clause (vii) being its [Isaacson's] form for one
   wave without the average". That is true only at r = 1/2. The entry's own t (r = 0) differs from it by
   (1/64 pi G) <h,h>'' (a.k) k, which only the average removes (fix 8).
8. (viii) is not circular. (M2) is the covariant conservation of the matter alone and does not mention t; the
   conclusion follows from (iii) and (*), both verified independently. "Proved" is the right label for what
   is displayed. Two sentences overreach. "The first-order field is itself a source of the second-order field
   through t, with the constant 8 pi G ... and no other" claims more than is proved: what is proved is that
   any quadratic self-source must have the flat divergence of t, and that among multiples of t only t itself
   qualifies. The Reading's "Clause (viii) shows that this [source T2 + t] is forced" overreaches the same way
   (fixes 2 and 3). The last two sentences of (viii) do guard well against reading it as a derivation of (C)
   or as holding beyond second order. Notation clash: tau already denotes the trace (tau = tr h, tau_x,
   tau_2), and (viii) reuses it for the quadratic source. The dust check is a real test, not a tautology: T2
   is built from the geodesic and continuity equations, not from the Einstein map. It tests (iii) off solutions
   (G1 = -kappa T1 is nonzero) together with the claim that this dust satisfies (M2). After the gauge change,
   T2 is moved by the assumed covariance law rather than re-derived, so that half tests covariance.
9. Checks, one by one:
   - (i): a real test of (i) and of Omega1. It cannot pass if the clause is false at that point.
   - (ii)/(iii) off solutions: a real test. The `dropped += 1` counter tests nothing (it always counts 3).
     Sign flips of single terms are not tested; dropping a term is (t2 does test sign flips).
   - The two conservation-on-solution checks: real tests, and duplicates of each other on other data.
   - Displacement and rotation/parametrisation: real tests. They contain no premise() call, although they
     compare against G1_of, which is the stored first-order map, identified with G^(1) by clause (i), which
     rests on R1 and the Weyl-flat result (fix 9). Each also has a `dropped` counter that tests nothing.
   - (v): tests the identity on 4 symbols (M, p) x 4 directions. That is a test, not a finite proof, because
     the identity is bilinear in (M, p (x) p). The flux statements are not tested (they are analytic).
   - (vi): tests the identity on solutions only. "Identically, H1 need not be a solution" is untested by the
     check; t4 covers it.
   - (vii): a complete finite proof for r = 1/2 (21 arguments determine a quadratic form on 6 variables).
   - (viii): see point 8.
   Premise calls are otherwise present where they are relied on.
10. Rules. No em dashes, no "honest", "load-bearing" or "curved spacetime", no bare imaginary unit, no agent
    or run names in the body. The Theorem label is used only for stored results. The title is 62 characters.
    No literature is used as a premise. The proof's preliminaries use frame-vector sums (g^mu, sum_mu
    a_mu nabla x^mu). These are GA frame expansions, not tensor-index arguments, and I accept them. The one
    rule issue is the Reading's use of the second-order field equation without naming it (fix 3), against
    RUN's rule on clause (f).
11. Citations. Chandrasekaran2026: the abstract (fetched 27 Nov) is about quantising vacuum GR on
    intersecting null cones, Hilbert space, pair creation, causal diamonds, entropy and one-loop semiclassical
    Einstein equations. It does not mention shear. The entry says only the abstract page was read, yet it
    describes the paper as posing the structure "with the shear of their generators as the datum" (that
    description came from R1's reading of the body). "The question taken from it" also suggests that the paper
    poses the self-source question (fix 8). Isaacson1968: the DOI 10.1103/PhysRev.166.1272 resolves at APS
    (Phys. Rev. 166, 1272), and the title of paper II matches. I could not confirm the last page (1280) or the
    abstract wording. Deser1970: the arXiv page gr-qc/0411023 confirms title, author and DOI
    10.1007/BF00759198 (the store entry has doi: null). The page shows no journal reference, so "GRG 1 (1970)
    9-18" is unverified by me, though it agrees with my memory. Gupta 1954 (Phys. Rev. 96, 1683), Feynman
    1962-63, Freud 1939 and the Einstein and Landau-Lifshitz pseudotensors are accurate as worded, as far as my
    memory goes (not verified).
12. Levels. Formal: correct apart from fixes 1, 2 and 7. Technical, lay and one-liner: each claims more in
    one or two places (fixes 1, 4, 5 and 6).

## Required fixes

1. entity.md, formal (iv), last sentence. "t is not invariant under first-order gauge changes, at any point,
   even on solutions (computed: ...)". Replace with: "t is not invariant under first-order gauge changes,
   even on solutions: at every point of every first-order solution some displacement changes it, since
   replacing xi by s xi changes t by s times a term linear in xi minus s^2 G1[xi_ xi_]/(8 pi G), and
   G1[xi_ xi_] is nonzero at a given point for suitable polynomial xi (computed; on the flat field itself,
   H1 = -xi_ has G2 = G1[-xi_ xi_] != 0). On a solution that is neither symmetric nor a plane wave the change
   is nonzero in all sixteen components, for xi and for B (computed)." If the scaling argument is not wanted,
   drop "at any point" here and in the technical level ("So the quadratic part is not invariant, at any
   point") and in the one-liner ("t is not invariant at any point").
2. entity.md, formal (viii). (a) Rename the quadratic source tau (it clashes with tau = tr h) to, for example,
   chi, in "G1[H2] = -8 pi G (T2 + tau)", "tau = t", "tau = mu t". (b) Replace "So wherever the first-order
   field acts on the matter, the first-order field is itself a source of the second-order field through t,
   with the constant 8 pi G of its coupling to the matter and no other, and the condition fixes the flat
   divergence of that source and nothing more." with: "So wherever F != 0, a second-order equation of this
   form needs a source quadratic in H1 whose flat divergence is that of t; t meets this condition, and among
   the multiples of t only t itself, with the constant 8 pi G of the matter coupling, does. The condition fixes
   the flat divergence of that source and nothing more." Also replace "where the first-order field acts on it"
   by "where F != 0".
3. entity.md, Reading. (a) In "Gravitational waves gravitate", before "the null-null component of the
   second-order equation", insert "if the field equation calG = -8 pi G T (clause (f) of the Definition;
   Theorem R2 under (Q) and (C)) holds through second order,". RUN forbids silent use of clause (f). (b) In
   "The whole-stress clause", replace "Clause (viii) shows that this is forced, at this order," with "Clause
   (viii) shows that a source with the flat divergence of t is forced, at this order,".
4. entity.md, technical, the paragraph beginning "Finally". Replace "The second-order equation can only be
   solved for a conserved source, so the field's own stress must enter with the same constant." with "The
   second-order equation can only be solved for a conserved source, so it needs a quadratic self-source with
   the flat divergence of the field's own stress; among multiples of that stress only the one with the same
   constant qualifies."
5. entity.md, lay. (a) "They change it only by terms of a special kind, which have no net flow through a
   complete surface." Change to "... which have no net flow through a complete wall of light when the
   relabelling or turning is confined to a bounded region." (b) "So gravity must be a source of gravity with
   the same constant." Change to "So gravity must be a source of gravity, and the field's own energy and
   momentum, entering with exactly the same constant, balance the books." Optionally add "(this fixes how the
   source flows, not every detail of it)". (c) In "the total energy crossing along each light ray is exactly
   the quantity found there", add "for waves that die away at both ends of the ray".
6. entity.md, one-liner. (a) "while its flux through a complete null plane is" becomes "while its flux
   through a complete null plane is, for changes of compact support". (b) "so at second order the field is a
   source through its own stress with the same constant 8 pi G" becomes "so at second order the field needs a
   self-source with the flat divergence of t, and among multiples of t only t, with the same constant 8 pi G,
   qualifies".
7. entity.md, formal (vi). (a) In the integrated statement, insert "when the integrals converge" (for the
   lambda-integral and for P_n). (b) The last sentence "Out of the gauge (LC) ..." should begin "On a
   first-order solution, out of the gauge (LC) ...". After "x = -(X + X^T)" add "with X the field of (iv) of
   the rotation and displacement that bring H1 to (LC), composed".
8. entity.md, Source of the idea (and the matching sentence of the extraction note). (a) Replace "which poses
   the canonical structure of the gravitational field on null cones with the shear of their generators as the
   datum; the question taken from it here is" with "which quantises the gravitational field from data on
   intersecting null cones (its use of the shear as the datum is as described in the first cited theorem,
   whose author read its text); the question asked here, which it prompted, is". (b) Replace "clause (vii)
   being its form for one wave without the average" with "clause (vii) in the exponential parametrisation
   being its form for one wave without the average; in the parametrisation in which t is defined the two
   differ by a second derivative in the phase, which the average removes".
9. check.py: add `premise(R1_ID)` (and `premise(WEYL_FLAT_ID)`) inside
   check_displacement_changes_the_quadratic_part_by_the_first_order_map_of_a_quadratic_field and
   check_rotation_gauge_and_parametrisation_change_the_quadratic_part_the_same_way. Both rely on G1_of, the
   stored first-order map identified with G^(1) by clause (i). RUN requires premise calls inside each function
   that relies on them.

## Optional suggestions

1. check (vi): add one non-solution case in the gauge (LC), since the clause says "identically, H1 need not
   be a solution" (t4 shows it passes).
2. check (v): make it a finite proof by running the 10 symmetric basis maps against the 10 polarised p (x) p
   (p, q and p + q), or say in the proof that the check is a test and the identity is proved analytically.
3. Remove the `dropped += 1` counters. They test nothing; pin a meaningful count instead.
4. store/references.yaml, Deser1970: the DOI 10.1007/BF00759198 is on the arXiv page. Adding it means
   rewriting the entry rather than appending to the file, so it is a maintainer decision.
5. (v): state the P_n condition explicitly: the y-integral of [1/2 d_n(tau_x - nbar.x(n)) - grad_perp.x(n)]
   tends to zero at both ends, and the transverse boundary integrals of x(n) and of grad_perp(n.x(n)) vanish.
6. (vi): say that calling the right side "the null energy P" of R1 (vi) carries R1's hypotheses (L), (D),
   (V), (N). The equality of the integrals is unconditional.
7. The displaced flat field H1 = -xi_ (t7: G2 nonzero in 14 components) would make the Reading's "No
   density at a point" concrete. It is a one-line addition to the displacement check.
8. Source paragraph: non-localisability is usually argued from the equivalence principle; "goes back to the
   pseudotensors" is acceptable but could say "is reflected in".
