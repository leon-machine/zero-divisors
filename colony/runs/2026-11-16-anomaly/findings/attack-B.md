# attack-B (angle B, adversarial), run 2026-11-16-anomaly

Status: FINAL (attack round). Labels: proved / computed / argued / conjectured. Every kill condition below was
written before the computation it governs (the first version of this file, 11:04, holds them unchanged).
Scripts and gate logs: work/attack-B/ (s3_explore.py, s2_test.py, p1.check4.log, p2.check4.log, the two drafts and
the working copies of the two proposal folders).

Proposals filed (2 of at most 3):
- P1 synthesis.colour-angle-fixed-by-no-stored-conjugation-and-relaxed-by-no-stored-field (op.strong-cp; also
  answers the last attack item of op.matter-asymmetry-origin). check4: exit 0, 0 errors, 0 other findings
  (first pass had three W413 weak-check warnings, removed by pinning exact values). validate_draft ok.
- P2 synthesis.order-four-structure-on-real-projective-walls-and-the-signed-count-modulo-sixteen
  (op.order-four-anomaly-and-sixteen). check4: exit 0, 0 errors, 0 other findings. validate_draft ok.
Nothing of attack-A's is refiled (A: the mass phase, the B - L inheritance with the coefficient, the spectral
asymmetry on RP^5).

---------------------------------------------------------------------------------------------------------------
## S1. The colour angle term under the three conjugations (op.strong-cp, first attack item)

Routes:
- R1 (the problem's): the term as the grade-four part of the colour field square, its sign under (a) the flag
  reversal, (b) the stored CPT conjugation C = Ad(I_6) kappa in the field-action convention, (c) the signature
  reversal to the mirror.
- R2 (another subject, dark energy): the frozen point's action epsilon(I, V, F, F) and clause (5) of the stored
  CPT-conjugation result already hold the sign rule for a form built from a field square; transport it.
- R3 (own): a counter-model to "CPT covariance forces theta = 0": a real-linear flag conjugate (det -1) against kappa.
Chosen: R1 with R2 as template and R3 as the control.
Kill condition (pre-registered): "a stored premise forces the bare angle to zero" dies if the stored conjugation,
in its own convention, leaves the term invariant; it survives only if some stored premise both reverses the term
and is premised as a symmetry of the action with its parameters fixed.

Established:
- proved (exact, Cl(1,3)): <F^2>_4 = F ^ F = 2 (E.B) I_4 for F = E + I_4 B; reversal and the grade involution fix
  it; an isometry g of the vectors, acting by outermorphism, multiplies it by det g.
- proved (exact, Cl(2,4), on the stored clauses): C has vector part -1 on R^{2,4} (det +1, outermorphism = grade
  involution = Ad(I_6)), so it fixes every bivector field and every four-form built from two of them; on the
  colour index it acts by an automorphism, and every automorphism of su(3) keeps the trace form (checked for the
  outer one and an inner one). So the term is INVARIANT under the stored conjugation. KILL CONDITION FIRED: the
  CPT premise holds for every value of the angle and says nothing about it.
- proved: a real-linear flag conjugate (det -1, stored clause (3)) reverses I_6 and reverses the term when it
  preserves and reorients the four-space carrying F. It also reverses the frozen point's action (stored clause
  (5)), so it is a symmetry of nothing stored. Convention caveat (stored, clause (5)): if the conjugation is
  applied to the Clifford integrand as a whole in the six-dimensional ambient, every top-degree sign inverts,
  the gravitational action's included, so that convention cannot single out the angle either.
- proved (exact): signature reversal. e_mu e_nu -> -e'_mu e'_nu is an isomorphism Cl+(1,3) -> Cl+(3,1) with
  I_4 -> I'_4 (the unsigned identification is not multiplicative but gives the same four-form). The mirror's
  term is the copy WITH THE SAME SIGN. So the reversal does not send theta to -theta; and even if it did it would
  relate two towers, not act within one.
- argued (from the above): what each premise says. CPT covariance: nothing. Flag as datum: the two flag signs are
  configurations of one functional with one angle, C exchanges them and fixes the term: nothing, and the term is
  no refutation of that premise. Copy theorem with the common-ceiling-coupling premise ("every other coupling of
  the copied theory at M"): theta_mirror = theta_ours at the ceiling; relates, fixes neither. Real breaking: lepton
  matrices only. On the mass phase: the adjoint reading of C on the family terms (the premised one) fixes it;
  the entrywise reading (not premised) would force mass phase in {0, half turn} together with J = 0, already
  closed by the stored J.
- argued, angle (c) of my brief: "the flag is the one CP-violating datum" (the "why" of op.strong-cp) does NOT
  survive the stored quark-stage phase. The flag is configuration data; the up-down phase selected from the data
  is a parameter of the family terms, which C in the adjoint reading does not move. The laws carry a parity- and
  time-odd parameter of their own (J), and the angle would be another.
Transport-absent (textbook: CPT fixes the angle term). New for the store: done for the stored conjugation, which is
not the CPT operator of field theory, in its own convention.
Proposal: P1, clauses (i) to (iii) and Reading (a), (b).
Next step: none on S1; the sentence in op.strong-cp "a flag that is its one CP-violating datum" should be reworded
(maintainer).

---------------------------------------------------------------------------------------------------------------
## S3. A Peccei-Quinn charge on the stored couplings (op.strong-cp third item; op.matter-asymmetry-origin last item)

Routes:
- R1 (the problem's): extend the stored charge list with the colour coefficient; add the two doublet phases.
- R2 (another subject, generations): family-dependent charges and textures of Y, Y~; the one-type stages.
- R3 (own, adversarial): hunt an overlooked charge: family-dependent phases, doublet mixing (the whole U(2) that
  commutes with the gauge group), rank-deficient Y~, the per-sector reading, the scalar potential alone.
Chosen: all three as one linear-algebra statement over family matrices.
Kill conditions (pre-registered): "no Peccei-Quinn charge on the stored couplings" dies if there is a pair (Y, Y~)
allowed by a stored reading, with no massless quark, and a phase symmetry of the Yukawa terms with nonzero colour
coefficient. "The neutral odd scalar is an axion" dies if invertible Y, Y~ force the coefficient to vanish.

Established:
- proved (trace argument, four lines; exact kernels for n = 2, 3, symmetric and non-symmetric pairs): with
  Phi = (alpha, conj beta) the two doublets of one kind, M_u = Phi_1 Y + Phi_2 Y~, M_d = conj(Phi_2) Y +
  conj(Phi_1) Y~, anti-Hermitian generators K_Q, K_u, K_d on the families and K_Phi in u(2): if det Y != 0 then
  a_3 := (2 tr K_Q + tr K_u + tr K_d)/I_4 = -n (q_1 - q_2); if also det Y~ != 0 then q_1 = q_2 and a_3 = 0.
  "THE NEUTRAL ODD SCALAR IS AN AXION" IS DEAD (its kill condition fired); "no Peccei-Quinn charge" stands.
- proved: the hypothesis is the physical one. At the cone's family point det M_d = beta^n det Y,
  det M_u = conj(beta)^n det Y~: both invertible iff no quark is massless. On the lift family
  (|beta|^2 - |alpha|^2) Y~ = beta M_u - alpha M_d, so Y~ is invertible when |alpha/beta| (= e^{-2 eta}, of order
  10^-88) is below sigma_min(M_u)/sigma_max(M_d).
- proved (general case, determinant-weight argument): a nonzero colour coefficient needs K_Phi diagonal and
  det(aY + bY~) = c a^j b^(n-j), 2j != n; then a_3 = -(2j - n)(q_1 - q_2), a quark is massless on the cone, and on
  the lift locus the product of the 2n quark masses is |c|^2 H^(2n). So the hidden charge my brief asked me to
  look for exists only at couplings that the masses exclude.
- computed (counter-models, the hypothesis is needed): Y~ = 0 (a_3 = -n(q_1 - q_2): the stored fourth charge);
  Y = 1 with Y~ nilpotent (family-dependent charges, a_3 = -n (q_1 - q_2)); the family split Y = diag(1,1,0),
  Y~ = diag(0,0,1) (a_3 = -(q_1 - q_2)). A singular Y~ whose determinant form is not a monomial gives 0.
- proved (five-mode module, one family): the rows of the coupling to c* force h_v + h_w = 0, which the stored
  clause (ii) took as a hypothesis ("one doublet and its conjugate"): it is now a consequence of the covariant
  coupling. Kernel: span{Y, n_B, n_L}, A_3 = 0.
- proved: the charge removed is, modulo Y, n_B, n_L, the unit of the module with slot charges -2 (stored, A_3 =
  A_2 = 8). It has charge 0 on the coupling to c and 4 on the coupling to c*: the conjugate coupling cuts the
  group it generates to its quarter turns, and the quarter turn (the unit on the sixteen, -1 on slot vectors) is
  the pseudoscalar omega of the ten Majoranas, up to inverse. With the imported shift rule, omega moves the
  angle by (A_3/2)(pi/2) = 2 pi per family: no constraint.
- proved (scalar sector): the axial phase alpha, beta -> e^{I_4 phi} alpha, e^{I_4 phi} beta fixes N, m, |Q|, the
  D-term, W(N) for EVERY W, k_10 |Q|^2 and the cone; it turns Q by e^{2 I_4 phi}, so it is broken by k_4..k_9,
  by the lift constraint Q = -H^2 and (above) by the Yukawa terms. At the cone's family point it is unbroken in
  combination with hypercharge; the normal pair is the complex field it turns (hence m_H = m_A at k_8 = k_9 = 0,
  the stored formula); no massless direction but the gauge orbit. On the lift locus the phase of Q is fixed by
  the constraint, so there is no neutral odd scalar there at all.
- proved: the normal pair does couple linearly to the angle term through the mass phase:
  delta log det M_u = (alpha_1/conj beta_1) tr(Y~^-1 Y), delta log det M_d = (conj alpha_1/beta_1) tr(Y^-1 Y~).
- argued (order of magnitude, literature inputs): that coupling relaxes nothing; a 3 TeV pair lowers the angle by
  a relative part chi |t|^2/(v^2 M^2) of order 10^-13 (chi near (75 MeV)^4, |t| of order m_t/m_b).
- consequence for op.rung-unit: the strong CP question puts NO condition on the second invariant W(N). The lead
  "W(N) is constrained by whichever way the doublets' neutral phase is decided" (LEADS.md) is closed negatively.
- counterfactual, literature checked: had Y~ been absent the axial phase would be a Peccei-Quinn symmetry broken
  at the weak scale; such an axion is excluded (Review of Particle Physics, Axions and other similar particles,
  Ringwald, Rosenberg, Rybka, 2021 revision, read at pdg.lbl.gov: "the associated standard and variant axions were
  quickly excluded", limits in the Listings; the measurements, from memory: K+ -> pi+ + nothing, J/psi and
  Upsilon -> gamma + nothing, beam dumps). Not needed for the result, since no axion exists.
Transport-absent (a two-doublet model in which both doublets couple to both quark types has no Peccei-Quinn
symmetry: textbook). New for the store: proved for the stored coupling with family matrices and doublet mixing,
with the exact condition and the counter-models; the identification of the fourth charge with the unit and of its
remnant with omega.
Proposal: P1, clauses (iv) to (viii) and Reading (c), (d), (e).
Not proved: completeness of the list of stored scalar fields (argued: the rung field's eight components).

---------------------------------------------------------------------------------------------------------------
## S4. The decision (drafted for Leon; nothing filed)

From S1, S3 and attack-A's S2: no stored premise fixes the bare angle (S1, proved signs, argued reading); the mass
phase is not fixed by the stored coupling and is real on exactly one open texture (A); nothing relaxes the
angle (S3). So THE SERIES DOES NOT FIX THE PHYSICAL ANGLE: it is a free input, and by the neutron bound an input
tuned to ten decimal places. Draft registration, in the format of synthesis.matter-asymmetry-registered-free-input
(a new postulate: maintainer-only, not filed):

  id (suggested): synthesis.colour-angle-registered-free-input
  title: Premise: the physical colour angle is a registered free input
  status: postulate; subject: standard-model; tags: [gauge-fields, undetermined-input]
  Premise (theta-bar). Let Theta(F) be the grade-four part of the colour field square and theta its coefficient
  (in the normalisation in which the integral of the term over a closed four-manifold is theta times an integer),
  and let theta_M be the I_4 phase of det(M_u M_d) on the covariant coupling. The premise: the physical angle
  theta-bar = theta + theta_M is a free number of the series; it is not computed from the transport structure,
  from another premise of the register, or from a dynamics of the series, and it is not a function of N, of
  xi G, of the level, or of epsilon. Its value is constrained by the record: |theta-bar| below about 2 x 10^-10.
  Scope. It registers one number for this tower; its equality in the mirror is the common-ceiling-coupling
  premise read for the angle and the family matrices, not this premise. It is a parameter of the laws, not
  configuration data: the stored conjugation fixes the term, so the angle is not exchanged with the flag.
  What it does not give: why it is small; the bare angle and the mass phase separately (only the sum is
  physical); the weak field's angle.
  Refutation condition. False if a stored result fixes theta-bar from the series' premises (at zero or at any
  value) with the mass phase included; if a stored field is shown to relax it (a phase symmetry of the stored
  couplings with nonzero colour coefficient, which needs det(aY + bY~) to be a single monomial); or if it is
  shown to be a function of another registered number. A measured neutron dipole moment that fixes a nonzero
  value does not refute it; it measures it.
  Imports the registration needs (maintainer): (1) the neutron bound, Abel et al., Phys. Rev. Lett. 124, 081803
  (2020): d_n = (0.0 +- 1.1 stat +- 0.2 sys) x 10^-26 e cm (abstract read at source; the 90 percent limit
  1.8 x 10^-26 e cm is the stored figure, not re-read in the paper's body); (2) the conversion, Dragos, Luu,
  Shindler, de Vries, Yousif, Phys. Rev. C 103, 015202 (2021): d_n = -0.00152(71) theta-bar e fm and
  |theta-bar| < 1.98 x 10^-10 at 90 percent (read at source), with the caveat of Bhattacharya, Cirigliano,
  Gupta, Mereghetti, Yoon, Phys. Rev. D 103, 114507 (2021) that lattice values are not yet reliable
  (|d_n| below about 0.01 theta-bar e fm; read at source), so the bound on the angle is good to a factor of a few;
  (3) theta-bar = theta + arg det and the shift under a rotation with colour coefficient ('t Hooft 1976,
  Fujikawa 1979; from memory, not checked at source).
  Alternative that Leon may prefer (a different, stronger postulate; see decision 2): register only the bare
  coefficient and adopt the pure-grade stage texture of attack-A's result, which makes theta_M zero or a half
  turn at tree level and turns the Cabibbo phase into an exact quarter turn.

---------------------------------------------------------------------------------------------------------------
## G2 / G3. The count on real projective five-space and the wall theory (op.order-four-anomaly-and-sixteen)

Routes:
- R1 (the problem's): take the count 1/16 per component (attack-A's G1) and say what it requires of the content.
- R2 (another subject, walls): find the order-four structure inside the stored wall theory: the Clifford jump
  Cl(L x R^{0,2}) of the rung-count theorem, the classes (w(Sigma), x) of the wall class.
- R3 (own, adversarial): test whether the count constrains anything: is omega's signed count well defined on its
  class modulo the Standard Model group; is omega a symmetry at any stored stage; is RP^5 the space; is L^5(4).
Chosen: R2 and R3; R1 only as a conditional reading (the anomaly statement is literature, not imported).
Kill condition (pre-registered): "the count forces sixteen" dies if (1) with the store's omega the structure on
RP^5 is not the one the literature's generator carries, or (2) the stored premise (Majorana element present) makes
omega a non-symmetry so the count constrains nothing, or (3) no stored wall result ties RP^5 as cross-section to
four-dimensional content.

Established:
- (1) did not fire. proved: in Cl(p,q), p + q = 2m, the pseudoscalar lifts -1 and squares to (-1)^(m+q); for the
  definite six-space it is -1, and with omega (square -1) the pair is an involution. Literature read at source
  (Garcia-Etxebarria and Montero, arXiv:1808.00009, section 4.3 and appendix C.4, eq. (C.21)): the bordism group
  of five-manifolds with this structure is Z_16, its generator is RP^5, eta(RP^5) = 1/16; the element is the
  order-four one inside X = -2Y + 5(B - L) (their hypercharge normalisation), the centre of Spin(10). Same
  structure, same space, same element as the store's omega. (The open problem cites this from memory; it is now
  checked. Hsieh's formula was checked at source by attack-A. Tachikawa and Yonekura: not re-read.)
- (2) FIRED, as stored: with the Majorana element omega is broken to the grading. The same source says so itself
  (the right-handed neutrino mass term breaks the Z_4).
- (3) FIRED in the form stated, with a positive part. proved (given the stored Whitney import; one clause given
  the classical (L2)/(K)): on a wall with cross-section RP^(2m-1) and tautological dying line the restricted
  cotangent bundle is 2m copies of the line with monodromy -1; on a side of signature (p,q) the lift is the
  pseudoscalar, of square (-1)^(m+q), and the class w_2(E+) + w_2(E-) is (m + q) x^2: the same exponent.
  Across a wall with definite physical side exactly one side needs an order-four twist: the definite side for
  RP^5 (far side (5,1): square +1, spin), the Lorentzian far side (3,1) for RP^3. In the stored Clifford jump
  the twist element is the pseudoscalar j of the jump plane L x R^{0,2} (a global section, square -1): checked
  in Cl(6,2), J_{6,0} j = -J_{5,1} E. So THE WALL THEORY DOES CARRY THE ORDER-FOUR STRUCTURE on RP^5 walls. What it
  does not carry: an identification of j with omega (omega acts on the slot module, j on the jump); fields of the
  slot module on a six-dimensional M (the tower is four-dimensional; its walls have three-dimensional
  cross-sections, where the literature's group is 0, appendix C.4 as returned by the fetch tool's reading of
  the paper, not seen by me line by line, and no count arises); the anomaly statement.
- proved (given (L2) and the stored lens-space classes): RP^n has the order-four structure with its tautological
  line exactly for n = 1 mod 4 (n >= 5) and is spin exactly for n = 3 mod 4. L^5(4): w_2 = u != 0 and every class
  of H^1 has square 0, so NO order-four structure with either flat line: it is not a space on which the count can
  be made. Same fact as the stored "order-eight structure" remark.
- proved (exact enumeration): every involution of the Standard Model torus on the sixteen reverses 0 or 8 states
  (sixteen of them, one trivial) and fixes the neutral singlet. So the signed count of omega g is 0 mod 16 on
  sixteen components and 1 mod 16 on fifteen, for every g: the count modulo 16 is a function of the class of omega
  modulo the Standard Model group, which is what "omega modulo the Standard Model group is unbroken" needs.
  Fifteen-component generations: n_g mod 16, zero only for 16 | n_g; 3 for three generations.
- argued, conditional on (H1) the count (attack-A's proposal, not yet stored) and (H2) the anomaly statement
  (literature: Dai and Freed 1994 and Witten 2016, Rev. Mod. Phys. 88, 035001, for the phase as the exponentiated
  eta invariant, from memory; Garcia-Etxebarria and Montero, read at source): sixteen per generation pass for any
  number of generations, fifteen fail for three. But, angle (d) of my brief: the count is a condition on the
  content ONLY FOR A GAUGED omega. The source's own section 2.1: an anomaly in a global symmetry is not an
  inconsistency, it means the symmetry cannot be gauged. In the stored chain: Majorana element present: omega
  broken; a stage whose group contains omega (Pati-Salam, so(10), u(5) with the abelian factor gauged): the
  singlet is already forced by the multiplet or by the local conditions (the source: when the Z_4 sits in a
  U(1) the condition follows from the local ones); a stage whose group does not contain it, without the
  Majorana element: a global symmetry, no inconsistency. So the count adds no constraint at any stored stage.
  This is the second branch of the problem's success clause ("it does not constrain the content"), at the
  level argued-on-proved-algebra, conditional on (H2) for what an anomaly is.
Transport-absent mathematics (Spin-Z_4 structures, Stiefel-Whitney classes). New for the store: the structure
located in the wall theory, the modulo-16 well-definedness, the negative on L^5(4) from stored classes.
Proposal: P2.
Next step: the open problem can be closed as "does not constrain the content in the stored chain" if Leon
accepts (H2) as the meaning of the anomaly (decision 4), or kept reformulated. The only route left to a real
constraint is a premise that omega is gauged where the continuous group does not contain it.

---------------------------------------------------------------------------------------------------------------
## Testing attack-A's claims (read at 11:15, 12:20, 13:05)

- S2, "the mass phase is not fixed": CONFIRMED. A's inverse map agrees with my (iv) (the same two identities).
  Consistent with my S3: the common phase moves Theta, hypercharge does not.
- S2, registered claim K-S2b ("every stored reading with a real determinant is closed by stored data"): I built
  the counter-model independently (work/attack-B/s2_test.py, exact): symmetric one-type stages, real first
  stages, down stage real, up stage a pure I_4 multiple: det M_u = 4/33275, det M_d = -1/1372 (both real),
  D = -I_4 12525896188/2110276598401125 != 0, spectra unequal; at an eighth turn the determinant is not real; with
  both real D = 0. A found the same at 12:45 and withdrew K-S2b. The filed statement survives my tests:
  (a) sign: checked, half turn for c_u c_d > 0 in my instance; A states the sign rule. A half turn is not a
  solution (meson spectrum; literature from memory): A says "zero angle or half turn, the sign nothing fixes".
  (b) hidden hypotheses, all stated by A: real first stages; one sector real; bare coefficient zero.
  (c) not a symmetry: any conjugation common to both sectors gives D = 0 (stored); so nothing protects it beyond
  tree level. I add (argued, not computed): in this coupling the heavy doublet couples with the two family
  matrices exchanged, so a one-loop correction to the mass phase is not obviously below 10^-10; a computation
  is the natural next item.
  (d) circularity (cone of the stored Cabibbo result, 123 entities): no entity on the angle, the neutron bound or
  the rung field in its past cone; using its selected phase to locate the real determinant is not circular.
  The selection does use |V_us|; on the texture |V_us| becomes a prediction (0.22257 at the stored 2+1+1 central
  ratios, inside the window; 0.22055 at the 2+1 ratios, just below it), so the texture is testable.
- A2, doublet count: CONFIRMED, with a supporting premise from S3. At the cone's family point alpha = 0: the
  light doublet is beta (vev, h, the eaten modes), the heavy one is alpha (normal pair, charged pair), with
  exactly zero vev: one light doublet. A's conserved space span{Y, B - L} needs that no further charge exists
  on the covariant coupling; my (iv) proves it (q_1 = q_2, a_3 = 0), and the charge that would appear with
  independent slot charges is colour-anomalous, as A's kill condition required. No wrong doublet count found.
- G1, structure group: CONFIRMED. A's space is the definite six-space with pseudoscalar of square -1; by my
  (i), (iii) that is exactly the side of the RP^5 wall that needs the twist ((6,0), (4,2), (2,4), (0,6)); on
  (5,1), (3,3), (1,5) the lift squares to +1 and no omega enters. "No spin structure on RP^5" also follows from
  w_2 = x^2 (my (v)). The count's sign convention (omega against its inverse) only exchanges +1/16 and -1/16; my
  modulo-16 clause is insensitive to it. Hidden hypothesis to state in A's proposal if not there: the count is
  on the round (definite) structure; the anomaly reading is literature.
- A3: not attacked beyond reading; the two forms with nonzero B - L (Majorana element, weak triplet) agree with
  the stored charge list.

---------------------------------------------------------------------------------------------------------------
## Unexpected links

1. One charge, three anomalies (proved pieces, argued whole). The stored fourth Dirac charge is the unit of the
   module (charge 1 on all sixteen, slot charge -2). Its colour coefficient (A_3 = 8) is the Peccei-Quinn
   coefficient; its weak coefficient (A_2 = 8) is that of a fermion number; and the conjugate coupling Y~ on c*,
   the same coupling that m_t != m_b requires, cuts it down to its quarter turn, which is omega, the element of
   op.order-four-anomaly-and-sixteen. So the continuous symmetry whose colour anomaly would relax the angle and
   the discrete symmetry whose global anomaly counts to sixteen are one object, and the second doublet coupling
   is what separates them. Entities: synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them (ii),
   synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element (ii), P1 (vi).
2. The pseudoscalar as the lift of -1, in four places (proved, one formula J^2 = (-1)^(m+q)): omega of the ten
   Majoranas; the antipodal lift on the six-space; the pseudoscalar j of the wall's jump plane; I_6 of the
   conformal ambient, which is the Ad-part of the stored CPT conjugation. RP^5 is the space of lines of the
   ambient R^{2,4}, and the stored C acts on it trivially on points and by I_6 (square -1) on spinors.
   conjectured, first computation not done: fields of the slot module that are functions on lines (not rays) of
   the ambient must be twisted by an internal element of square -1 on every component, that is by omega modulo
   the gauge group; if the series' conformal fields are functions on lines, this is where omega would enter the
   store's own geometry. Nothing stored says which. Entities: P2 (i),
   synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation (1).
3. Walls flip the existence of spinors (proved given (K)): the class w_2(E+) + w_2(E-) changes by x^2 across a
   tame wall with dying line class x. On real projective walls exactly one side carries untwisted spinors. This
   bears on op.wall-class-invariant: x^2 is a function of the stored wall class, and it is the obstruction to
   a spin structure on the doubled dying line already used in
   synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial (2).
4. The stored D-term is PQ-symmetric for the same reason the supersymmetric two-doublet potential is, and the
   stored lift constraint Q = -H^2 plays the part of the soft term that breaks it; on the cone the symmetry is
   unbroken at the vacuum and the second doublet is inert in the potential but not in the Yukawa terms (it
   couples with the family matrices exchanged: the stored B-meson exclusion). argued; no new result.
5. op.second-order-breaking: A's texture ties the up-down phase to the mass phase (2 phi), so the neutron bound
   is a bound on the stage phase at the 10^-10 level on that texture. Belongs to A; noted for the bridge-hunter.

---------------------------------------------------------------------------------------------------------------
## Decisions for Leon

1. Register the colour angle as a free input (new postulate; draft in S4). Recommendation: yes, the physical
   angle theta-bar, with the refutation conditions as drafted. This needs the imports of decision 3.
2. Whether to adopt instead, or in addition, the pure-grade stage texture of attack-A's mass-phase result as a
   premise (stage coefficients real in one sector and a real multiple of I_4 in the other, real first stages).
   It would make the mass phase 0 or a half turn at tree level and predict |V_us| from the mass ratios. Against:
   it is not a symmetry, the sign is free, loops are not computed, and the bare coefficient stays free.
   Recommendation: do not adopt now; record it as the open reading and ask for the one-loop mass phase first.
3. Imports (each used by P1's Reading or by the registration; none filed): (a) theta-bar = theta + arg det and
   the shift of the angle under a rotation with colour coefficient ('t Hooft 1976; Fujikawa 1979; from memory);
   (b) the neutron dipole measurement and the conversion to the angle (Abel et al. 2020; Dragos et al. 2021;
   Bhattacharya et al. 2021; all read at source, abstracts); (c) the topological susceptibility (from memory;
   the 2021 lattice paper read gives (66(9)(4) MeV)^4); (d) the exclusion of the weak-scale axion (PDG review,
   read; the individual measurements from memory). Recommendation: import (a) and (b) with the registration;
   (c) and (d) are used only in an order-of-magnitude remark and a counterfactual and need not be imported.
4. op.order-four-anomaly-and-sixteen: whether to import the anomaly statement (H2) after all. My recommendation
   is unchanged from the earlier run's and now has a reason: no. With it the count is conditional on a gauged
   omega, which no stored stage has without already forcing the singlet; the problem can be closed on its second
   success branch (the count does not constrain the content in the stored chain), keeping as the one live
   question whether omega is gauged where the continuous group does not contain it (a premise, not a result).
   The classical facts P2 leans on, (L2) and (K) (Karoubi 1968, from memory), are of the kind already carried
   as "(L2), cited from memory" by a stored result; importing them as one Fact would make P2's clauses (iii) and
   (v) unconditional.
5. Rewording (maintainer, no decision of substance): the "why" of op.strong-cp says the flag is the vacuum's one
   CP-violating datum; with the stored quark-stage phase that is not so (S1). The "known" of
   op.order-four-anomaly-and-sixteen cites the bordism generator from memory; it is now checked at source and
   stands. LEADS.md's line that op.rung-unit's W(N) is constrained by the neutral phase is closed negatively.
6. Whether the conformal fields of the series live on lines or on rays of the ambient (link 2). If on lines,
   omega has a geometric origin and a short computation would show it; if on rays, nothing follows.
