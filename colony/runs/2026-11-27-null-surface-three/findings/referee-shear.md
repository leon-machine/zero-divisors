# Referee report: synthesis.null-surface-data-at-any-field-strength-the-focusing-equation-integrated

Blind referee. I did not read the author's findings or work files.

## Verdict: SOUND WITH FIXES

The mathematics is correct. Every clause I tested independently holds on data different from the entry's. That includes the factor 1/4 in the shape-shear relation, the kernel (s - t), the factor 1/2 in Xi, the sign of the curvature term, and the pinned series values. What needs fixing is wording at several levels that claims more than the formal statement proves, one disjunction in (iv) that is stronger than its proof, a gap in the normalisation in (vi)(c), and an untested identity in check.py.

## Required fixes

1. **Wording overclaim: "what the datum is".**
   - Files: entity.md, three places: the extraction note ("what the datum is at any field strength (the shape history ...)"), the Reading, Beyond first order ("the datum is the shape history"), and the lay level ("It says what the free data are on one such surface").
   - What is wrong: the entry proves that one equation along each generator leaves the shape history free and fixes rho up to two constants. It does not prove that the shape history is the complete free data on the hypersurface. The other components of the field equation on N are not examined: the K-m components govern the transverse data along the generators, and further data live on a cut.
   - Change the extraction note to: "what the component of the field equation along the generators leaves free at any field strength (the shape history ...) and what it slaves to it".
   - Change the Reading to: "the component of the field equation along the generators leaves the shape history free".
   - Change the lay sentence to: "It shows that one of Einstein's equations, along each ray, leaves the shape free and fixes the area from it; it does not show that the shape is all the data on the surface, or that such data determine gravity everywhere."

2. **Clause (iv), formal statement and proof.** "within that affine distance either the generator leaves the region where the field or phi is defined, or rho -> 0".
   - What is wrong: the proof shows only that rho cannot stay smooth and positive, with the generator inside the region where field and phi are smooth, over the whole closed interval. It does not exclude phi (and K, theta) ceasing to be smooth while rho stays positive. Excluding that needs the Jacobi equation, which (vii) uses for plane waves and (iv) does not prove in general.
   - Required change: "within that affine distance the stretch on which the field and phi are smooth and rho > 0 ends: the generator leaves the region where they are defined or smooth, or rho -> 0, a caustic". Alternatively, prove that rho -> 0 at the end of the stretch.

3. **The bound without its hypothesis at lower levels.**
   - Technical level: "Concavity of rho gives the classical bound: a generator whose expansion is negative reaches a caustic, or leaves the region, within affine distance two over the expansion." Insert "under the null energy condition, (P)," and change "two over the expansion" to "two over the magnitude of the expansion".
   - Lay level: "once a bundle starts to converge it must come to a focus within a definite distance". Append "provided any matter it meets has positive energy and the field around the rays extends that far".
   - One-liner: "reaches a caustic within 2/|theta|". Append "or leaves the region where the field and the hypersurface are smooth".

4. **The realisation is the same on every generator; lower levels drop this.**
   - Lay: "every possible history of squeezing can be produced by choosing the wave". Change to "every possible history of squeezing along a ray can be produced by choosing the wave (the same history then holds on every ray of the surface)".
   - Technical: "any trace-free shear history is obtained by choosing the profile". Append "the same on every generator, a plane wave being homogeneous across its fronts".
   - One-liner: "realises every shear history along a generator". Append "(the same on every generator)".

5. **Lay attribution.** "All of this is classical physics from the 1950s and 1960s, by Raychaudhuri, Sachs and Penrose".
   - What is wrong: the entry itself credits the area-parameter form to Chandrasekaran (2026) and the alpha = 1 parameter to Ciambelli, Freidel and Leigh (2023/24).
   - Change to: "The focusing equation, the role of shear and the focusing by plane waves are classical (Raychaudhuri, Sachs, Penrose, 1950s and 1960s); the integrated forms are recent."

6. **Lay clock sentence.** "The clock stops where nothing crosses the surface, and it ends at a focus."
   - What is wrong: this omits the turning point p = 0 of (viii).
   - Change to: "The clock fails at the moment the area stops growing and starts to shrink, and wherever nothing crosses the surface; it ends at a focus."

7. **Clause (vi)(c), second statement: normalisation gap.**
   - File: proof-main.tex, (vi)(c).
   - What is wrong: the proof builds E = O A with E(lambda_0) = O(lambda_0) A(lambda_0), not the identity. It then invokes (b), where E(lambda_0) = id and G = E^T E.
   - Required change: add one sentence. "With E_b the map of (b) (E_b(lambda_0) = id) for this S, E = E_b C with C = E(lambda_0) constant, so x_i = m(E(e_i)) are linear combinations with constant coefficients of the separations of (b), hence carried separations, with Gram matrix E^T E = G."

8. **Clause (i) and (viii): "belong to the field".**
   - What is wrong: "ratios of rho along a generator belong to the field" (i), and "the field fixes lambda ... and rho ..." (viii). A generator lies on many null hypersurfaces, and rho depends on the hypersurface (on phi), not on the field alone.
   - Change (i) to "belong to the field and the hypersurface", and (viii) to "Along a generator of a given null hypersurface the field fixes ...".

9. **Clause (iii), and "closed form" in the technical and lay levels.**
   - What is wrong: s is defined from rho (ds = d lambda / rho), and in (beta) rho itself is the parameter. Given the shape as a function of lambda, the formulas are integral equations, not closed-form solutions. Lambda is recovered by a further quadrature; in my Gaussian example it is an error function.
   - Add to (iii) after form (alpha): "The datum enters as a function of s (or of rho), parameters built from the solution; given the shape as a function of lambda, the formulas determine rho only implicitly, and lambda is recovered by the stated quadrature."
   - In the technical level, change "integrates in closed form" to "integrates explicitly once the shape is given as a function of s or of the area".
   - In the lay level, change "can be solved outright" to "can be integrated explicitly".

10. **Wording about the paper.**
    - Formal (iii): "(its equations (3.26), as extracted: ...); no difference from it was found". Keep "as extracted". Add: "a second, independent extraction of the PDF made for review gave the same equations (3.25d), (3.25f), (3.26a) to (3.26d), with varrho the square root of the area density and u affine; the typeset PDF was not read directly".
    - Mark the quotation with upper indices in formal (iii) as "(in the paper's component notation, quoted)", as the proof does.
    - One-liner: change "(the formula of the paper that prompted it)" to "(agreeing, as far as a text extraction shows, with the paper that prompted it)".

11. **check.py does not test the shape-shear relation.**
    - What is wrong: no function computes G_ij = -X_i.X_j from the gauge fields and tests G^{-1}G' = 2 S_X, nor (1/4) tr((qbar^{-1} qbar')^2) = <sigma, sigma>. Yet form (beta), the clock and (v) are stated through qbar. The power-law check asserts "the shape is diag(rho^a, rho^-a)" without computing the shape from hb.
    - Required change: in check_area_density_and_the_linear_focusing_equation_on_strong_waves, compute G from wave.phys(x) for the two connecting vectors, take d/d lambda with wave.along, and pin that (1/4) tr((G^{-1}G' - theta id)^2) equals wave.shear2().v on all five waves. Use an E(lambda_0) that is not the identity, so G is not trivially id at the point; see my wave_gtg.py for a working version.

12. **Labels of the power-law check.**
    - check_exact_power_law_waves_and_the_area_as_a_clock is evaluated at the single point lambda_1 = 3. There, theta and <sigma, sigma> are fixed by the input S0 through (vi)(b).
    - Change its GA.check label from "d rho/d lam is proportional to rho^(-a^2/4) and lam to rho^(1 + a^2/4)" to "d ln p / d ln rho = -a^2/4 and d ln lam / d ln rho = 1 + a^2/4 at the sample point". Optionally sample a second lambda.

13. **Index notation in formal (i).** "The matrix G_ij = -X_i . X_j".
    - Introduce it as a linear map: "the matrix, in the basis X_1, X_2 of the screen, of minus the product (the Gram map)". Likewise, say that sigma's matrix is that of the screen map sigma in that basis. The rules allow 2 by 2 matrices only as matrices of linear maps of the screen plane.

## Optional suggestions

- (vii) needs w smooth only on [lambda_0, lambda_1 + 2/|theta(lambda_1)|], not for all lambda. Weaken the hypothesis.
- The vacuum null-plane case of (vii) is exhibited by no check. Here is an exact example I worked out:
  - Take t = 1 - lambda, w = diag(6/(3 - t^2), -6/(3 - t^2)): trace-free, smooth for |t| < sqrt 3.
  - The second column of E is b = (t - t^3/3)/(2/3), with b(lambda=0) = 1 and b'(0) = 0, so S(0) = 0 is a null plane at lambda_0 = 0. b vanishes at lambda = 1, where the field is smooth.
  - The first column has f'' = w11 f > 0, so f >= 1.
  - It could be added to check_focusing_bound_and_exact_caustics, sampled at points with the S0 given by the series.
- Terminology: "area density" is used both for rho (clause (i) title, (vi)(c) "is the area density") and for rho^2 ((ii), (iii)(alpha)). Pick one, for example "root area density" for rho, as the paper's varrho.
- (viii): mark "(a null plane where the field vanishes; a stationary horizon)" as examples ("for example").
- The credit "the parameter with alpha = 1 is the dressing time of CFL" holds in the affine frame and up to a constant factor (their eq. (142), V_aff = A integral of sqrt(Omega) d lambda in four dimensions; the constraint (157) is linear in Omega). Say "in an affine frame, up to a constant factor".
- The tests in check_integrated_forms of form (beta) with matter are (ii) multiplied by 2p. They are true but add little beyond (ii). A test in the rho variable itself, as in my forms2.py, would add something.

## Settled points (from the brief)

1. **(i).**
   - rho^2 is the physical area of the parallelogram spanned by the separations: physical vectors are hb^{-1} of background vectors, and the derived metric is their product.
   - "Carried" is defined precisely (vanishing bracket along the generator), and positivity is proved.
   - Rescaling by |det c| is proved. The sentence about ratios needs fix 8.
   - d rho / d lambda = theta rho / 2 is proved from (L2) and R1 (iii)(a); it is not assumed.
   - qbar' = 2 qbar sigma and the factor 1/4 are correct. I verified both from gauge fields (see below).
2. **(ii) and the sign of the curvature term.**
   - The sign matches R1 (iii) (+K.R(K)).
   - (P) K.R(K) <= 0 is the null energy condition in the store sign: the Definition says the literature's Ricci on null k is -k.R(k), and R2 (vii) gives K.R(K) = -8 pi G K.T(K).
   - K.G(K) = K.R(K) for null K, for any Lambda, is correct. I verified it on my waves (K.G(K) = K.R(K) = 0 and = 5).
3. **(iii).**
   - Both forms are verified on my own examples. The condition p != 0 is stated in (iii)(beta), (v) and (viii).
   - "Closed form" needs fix 9.
4. **(iv).** The bound and the equality case are correct. The disjunction needs fix 2.
5. **(v).**
   - It is correctly stated as one component of the field equation on one generator. The characteristic initial value theorem is explicitly disclaimed in the formal and technical levels and in the extraction note.
   - The lay level says it does not show that the data determine gravity everywhere, but its "what the free data are" overclaims (fix 1).
   - The title is a name and acceptable. It could be read as a claim about full data; fix 1 removes the support for that reading in the text.
6. **(vi).** All verified (see below). The limit "the same history on every generator" is stated in the formal level; the lower levels need fix 4. The pinned value -61/48 is reproduced.
7. **(vii).**
   - The proof is complete for the vacuum null-plane case: E'' = wE is linear with smooth coefficients, the hypersurface and phi are smooth while det E != 0, the trace inequality holds, and the step from a zero integrand to w = 0 is valid.
   - Non-triviality ("w does not vanish identically on [lambda_0, lambda_1]") and smoothness are stated. No support condition is needed.
   - The field is smooth at the caustic: det hb = 1 and w is smooth there.
8. **(viii).**
   - The proved relations are correct: the invariance of v and t, the integral formula, and the two inequalities.
   - The formal level keeps the reading apart ("the reading argued") and disclaims flows and states. The lay level needs fix 6.
9. **The paper.**
   - I fetched https://arxiv.org/abs/2611.34924: "An algebraic quantization of gravity from the null cone", V. Chandrasekaran, submitted 25 Nov 2026.
   - I also fetched the PDF through a summarising extraction tool, so this is again not a direct reading. It reports: (3.25c) Theta = 2 L varrho / varrho; (3.25d) sigma_AB = (varrho^2/2) L qbar_AB; (3.25f) d^2 varrho/du^2 + (varrho/8)(d_u qbar)^AB d_u qbar_AB = 0; (3.26a) d_v log(d_u varrho) = -(v/8)(d_v qbar)^AB d_v qbar_AB; (3.26b) d_u varrho = p exp(-Xi); (3.26c) Xi = (1/8) integral_eps^v s (d_s qbar)^AB d_s qbar_AB ds; (3.26d) p[u(v) - u(eps)] = varrho_S integral_eps^v e^Xi ds.
   - It also reports that varrho is the square root of the area density, u is affine, v = varrho/varrho_S, and that the paper states Xi >= 0.
   - All of this agrees with the entry's (ii) and (iii)(beta) and with rho, sigma and qbar, including the factors. The entry's wording ("as extracted ... not checked against the PDF") is appropriately limited; fix 10 records the second extraction.
10. **Checks.**
    - All seven test their clauses. None is vacuous.
    - The closed forms of hb and Omega used at order eight are tested in the same series function (closed_form_holds: inverse and torsion to full jet order). Because the torsion equation fixes Omega, this is not circular. They are also tested against the solved Omega in check 1.
    - The `!= 0` mutation survivor in check_null_gradient is a non-degeneracy guard. The function is still a real test: K null as a jet, B(m_i) = S m_i as jets, the parallel frame, and the curvature form.
    - Premises are called where they are used.
    - Weak points: the shape-shear relation is untested (fix 11), and the labels of the power-law check claim more than is tested (fix 12).
11. **Rules.**
    - No em dashes, no "honest", no "load-bearing", no "curved spacetime", and no bare imaginary unit.
    - The run and credit names appear only in the front matter, as required.
    - The title is 72 characters.
    - Theorem/Proof is not used for the argued reading.
    - No literature is used as a premise.
    - Index notation: see fixes 10 and 13.
12. **Citations (verified 27 Nov 2026).**
    - Sachs1962: R. K. Sachs, "On the characteristic initial value problem in gravitational theory", J. Math. Phys. 3 (1962), 908-914, DOI 10.1063/1.1724305. Title, journal, volume, pages, year and DOI verified (scilit); author verified (reference [37] of arXiv:1203.4534).
    - Penrose1965: R. Penrose, "A remarkable property of plane waves in general relativity", Rev. Mod. Phys. 37 (1965), 215-220, DOI 10.1103/RevModPhys.37.215. All fields verified (scilit).
    - Rendall1990: A. D. Rendall, "Reduction of the characteristic initial value problem to the Cauchy problem and its applications to the Einstein equations", Proc. R. Soc. Lond. A 427 (1990), 221-239, DOI 10.1098/rspa.1990.0009. All fields verified (scilit and INIS; author from reference [36] of arXiv:1203.4534; issue 1872 not given in the entry, which is fine).
    - CiambelliFreidelLeigh2024: L. Ciambelli, L. Freidel, R. G. Leigh, "Null Raychaudhuri: canonical structure and the dressing time", JHEP 01 (2024) 166, arXiv:2309.03932, DOI 10.1007/JHEP01(2024)166. All fields verified (Springer page).
    - The classical credits are fair as worded. The dressing-time credit needs the qualifier in the suggestions.
13. **Open problem.**
    - Filing against op.gravitational-field-at-null-momentum is defensible: its statement lists "anything beyond first order" as open, and R1 is filed there.
    - The problem is about quantum commutation, and the note says plainly that nothing quantum and nothing about the light-cone requirement is settled. Decision (1) for the maintainer is the right place for this.
    - Fix 1 is needed in the note.
14. **Levels.** The formal level is accurate. The technical, lay and one-liner levels each drop a hypothesis or a limit (fixes 3 to 6, 9, 10).

## Independent verification (scripts in /home/claude/scratch/referee-shear/)

- **wave_gtg.py** (lib/gtg.py jets, Fractions)
  - Setup:
    - Cartesian labels, not the entry's light-cone labels.
    - Point (3/7, -5/3, 2/5, -1/9).
    - My own profile at amplitude 9: w11 = 9(2 + d - 3d^2), w12 = 9(-1 + 4d^2 + d^3), w22 = -w11 (vacuum), or -w11 + 5 (matter, violating (P)).
    - My own S0 = [[-3/5, 7/4], [7/4, 2/9]] and E(lambda_0) = [[2, 1], [-1, 3]], which is not the identity.
    - Omega solved from the torsion equation, at jet order 4.
  - Results:
    - The field is torsion-free, and the solved Omega equals (a.l) l ^ w(y) as jets.
    - On all six planes, R(B) = -l ^ w(B.l) exactly.
    - Ricci = (tr w)(a.l) l; ricci_flat exactly when tr w = 0.
    - K is null as a jet, and l.hb(K) = 1.
    - The screen frame is orthogonal and parallel, and B(m_i) = S_ji m_j as jets.
    - theta = tr S, and <sigma, sigma> = tr(trace-free S)^2.
    - (K^m_j).R(K^m_i) = w_ij, and K.R(K) = K.G(K) = tr w.
    - The separations m(E e_i) are carried and tangent.
    - rho^4 = -(hb^{-1}(x1^x2))^2 = det G = (det E)^2 = 49.
    - d rho^4 / d lambda = 2 theta rho^4 as jets.
    - rho''/rho = -1/2(<sigma, sigma> - K.R(K)) exactly: -104701/32400 in vacuum, -23701/32400 with matter.
    - tr G^{-1}G' = 2 theta, and (1/4) tr((qbar^{-1}qbar')^2) = <sigma, sigma> = 104701/16200, from the gauge-field G.
- **pinned_series.py** (sympy, exact; Riccati and Jacobi with S(0) = 0 on the entry's W_BOTH)
  - The coefficient of d^4 in rho is -61/48 eps^2. The coefficient of d^8 is -1/504 eps^2 - 40931/53760 eps^4.
  - Odd powers of eps vanish through d^9.
  - These match the entry's pinned values. With wave_gtg.py's identity rho^4 = (det E)^2 from gauge fields, this confirms the series test.
- **forms2.py** (sympy, exact)
  - On a shape with rotating axes, (1/4) tr((qbar^{-1}qbar')^2) = 2 sinh^2(u) phi'^2.
  - (iii)(alpha) holds in vacuum on phi = omega s^2/2 (<sigma, sigma>_s = C omega^2 s^2, a quartic exponent). The residual of rho'' + <sigma, sigma> rho / 2 in lambda is 0, and so is the residual of the formula for e. The wrong kernel (s + t) gives a nonzero residual.
  - (iii)(beta) holds on phi = k ln rho, with lambda(rho) inverted exactly and the ODE checked in lambda (residual 0).
- **forms3.py** (sympy)
  - (vi)(c) first statement on a rotating trace-free shear: S' = w - S^2, and tr w = 0.
  - (vi)(c) second statement on a concrete rho, qbar with rotating axes: the construction E = O A gives a symmetric S with tr S = 2 rho'/rho.
- **Matter form of (iii)(alpha), on generic symbolic rho(s), qbar(s)**: de/ds = -<sigma, sigma>_s + rho^2 K.R(K). This was verified in a first run (forms_sympy.py) that was stopped before it could print, so the result is unconfirmed. The algebra is the same chain rule as the vacuum case, which did pass.
- **Entry gate**: python -m tp.checkone run once, all 7 checks passed (10.6 s). I did not run the mutation test or the full-store check.
