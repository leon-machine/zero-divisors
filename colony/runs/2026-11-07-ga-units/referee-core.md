# Referee report: the two core unit results (blind)

Referee: referee-core, 2026-11-07. Read: colony/BRIEF.md (store model, Role: referee),
store/conventions.md ("The language: geometric algebra", "The imaginary units"), the two entities
(entity.md, proof-main.tex, check.py, coverage.yaml), every cited premise at its pinned version, and
the stored results named for duplication. Nothing under colony/runs/2026-11-07-ga-units/ was read.
No store file was edited. Scratch (independent recomputation, mutation harness):
/tmp/claude-0/-home-claude/23cbb9be-73ca-5537-8211-47496476158a/scratchpad/{indep1.py, indep2.py,
centralizer.py, mutate.py}.

Kill conditions, written before computing: (1) is WRONG if any sign in (i)-(v) fails in exact
arithmetic for some even-dimensional signature, or if Cl(V) (x) span{1, I_W} -> Cl(W) fails to be
multiplicative or bijective; (2) is WRONG if any of J sigma = +I_4, tau_t(v) = e^{-Jt} v, the
continuation at t = -J lambda, KMS at tau_{J beta} = Ad(e^{-beta K}), omega(v* v) = 1/(1 + e^beta)
or Ad(rho^{Jt}) = tau_{-beta t} has the opposite sign against the store's v, v*, sigma and KMS
convention. None was triggered.

---

## 1. std-algebra.complexification-is-the-odd-extension (v1)

**Verdict: SOUND WITH FIXES** (fixes are attribution and wording; no mathematical error found).

### Premises at pinned versions
All four pins are current and say what is used:
- odd-extensions.volume-element-odd-dimension@3: odd n, omega central, omega^2 = (-1)^{n(n-1)/2+q}. Used in (i). OK.
- primer.centre@2: centre R + R omega for odd n. Used in (i). OK.
- odd-extensions.doubling-or-complexification@5 (ii): omega^2 = -1 gives Cl = Cl^0 (x) C with omega the unit. Used for Cl(W) = Cl^0(W) + Cl^0(W) I_W. OK.
- std-algebra.complexification@2 (i): Cl(V) (x) C = Mat_{2^{n/2}}(C) for n even. Used in (ii). OK.
- Cone: holds given nothing (no postulate); derived ledger absent, matching the note's "Transport-absent".

### Proof steps
Setting, (i), (ii), (iii), (iv), (v) each checked by hand; every step is correct. In particular:
- (i) e commutes with I_V because n is even; e_k I_V = -I_V e_k; I_W^2 = eps_V Q(e). The side computation with q' agrees: (n+1)n/2 and n(n-1)/2 differ by n (even), so (-1)^{(n+1)n/2+q'} = eps_V (-1)^{[Q(e)=-1]} = -1 in both cases.
- (ii) Cl(V)e = Cl(V)I_W since I_V is invertible; the multiplication map is bijective by the blade split and multiplicative by centrality; the presentation argument is right.
- (iii) (a + I_W b)^2 = Q(a) - Q(b) + 2<a,b> I_W is the complex-bilinear extension; nullity criterion correct.
- (iv) P_+- idempotent, commuting with I_V; e P_+- = +-P_+-, so Cl(W)P_+- = Cl(V)P_+-; (xP_+-)I_W = +-(xI_V)P_+-; even and vector forms correct.
- (v) eps for Cl(1,3) = (-1)^{6+3} = -1, for Cl(2,4) = (-1)^{15+4} = -1; Q(e) = +1, giving Cl(2,3), Cl(3,4); I_6 = I_4 e_+ e_- in this order.

### Is the isomorphism statement exactly right?
Yes. Cl(W) is an algebra over the field span{1, I_W} because I_W is central; every element of
Cl(V), in particular every vector of V, commutes with I_W (checked on all 16 blades of Cl(1,3) in
Cl(2,3)); Cl(V) is a real subalgebra and a real form; Cl(W) = Cl(V) + Cl(V)I_W is a direct sum of
real subspaces (the second summand is not a subalgebra), and as a span{1, I_W}-algebra Cl(W) is
Cl(V) (x)_R span{1, I_W}. Complex conjugation x + yI_W -> x - yI_W is the automorphism e -> -e
fixing V (checked on all 32 x 32 blade pairs of Cl(2,3)). The even-subalgebra form Cl^0(W) +
Cl^0(W)I_W is correctly called a second real form (for W = Cl(2,3), Cl^0 = Cl(3,1) = Mat_4(R),
not Cl(1,3) = Mat_2(H)).

### Independent recomputation (indep1.py, 100 exact checks, all pass)
- eps_V formula, I_W^2 = -1 with Q(e) = -eps_V and +1 with the other sign, I_W central, centre exactly {1, I_W} (by blade count, which is exact since conjugation by generators permutes blades up to sign): every signature of n = 2, 4, 6 (the check does n = 6 only for (1,5)-type and the commutant only for n <= 4).
- Multiplicativity and bijectivity of a + bu -> a + bI_W on all basis pairs for V = (1,3), (3,1), (4,0) (eps_V = +1, Q(e) = -1), (2,2), (1,1) and (2,4) (the check does all pairs only for (1,3)).
- (a + I_W b)^2 for rational vectors in Cl(2,3), Cl(3,4), Cl(4,1); e_2 + I_5 e_3 null; e_0 + I_5 e_1 squares to 2 (not null, as the criterion says); (e_2 + I_4 e_3)^2 = -2 + 2e_0e_1; (y -+ eps I_5 e_0)^2 = Q(y) - eps^2 -+ 2 eps y_0 I_5, the standard x^0 - i eps sign under i -> I_5.
- (iv) for both idempotents on every blade, every signature with eps_V = -1 in n = 2, 4, 6.

### Check and perturbations
runcheck: 4/4 PASS. Mutations (each caught by the intended function): Q(e) = +eps_V (fails (i));
P_+ and P_- swapped (fails (iv)); I_4 for I_5 in the complex vectors (fails (iii)); u^2 = +1 in the
abstract product (fails (ii)); left unit I_V x in place of right unit x I_V on all blades (fails (iv)).
The check is not vacuous.

### Duplicates, overclaiming, hidden hypotheses
- **Partial duplicate (spacetime instance already stored).** odd-extensions.four-extensions-oriented-pair (table row "this world + time": Cl(2,3), omega^2 = -1, Cl(1,3) (x) C = Mat(4,C)) and odd-extensions.mirror-inside-complexified-extension-absent-doubled (iii) (Cl(2,3) = Cl(1,3) + omega Cl(1,3)) already state clause (ii) for V = Cl(1,3). The new entity is the general even-n theorem plus (iii), (iv) and the conformal instance, so it is not a duplicate as a whole, but it does not mention these.
- Not a duplicate of std-algebra.complexification (ii) or odd-extensions.doubling-or-complexification (ii): those complexify Cl^0(W), this complexifies Cl(V) with V's vectors kept as vectors. It correctly cites both for the Cl^0 form.
- No overclaim found. (iii)'s "may be read as the complex unit of any such scalar computation" is limited to functions of the square computed in the field; nothing about limits eps -> 0+ or distributions is claimed. (i)'s "only sign" is within Q(e) = +-1, as stated.
- Observed elsewhere (not a defect of this entity): rule2.odd-lorentzian-dimension-exactly-one-real and synthesis.phase-flow-is-time-rotor-flow-kms-continuation cite this entity by \claimref, but the build lists used_by = [] for it, so neither has it in `uses`. rule2 applies it to an odd-dimensional V via V + Rf, a step this entity (even n only) does not state.

### Fixes
1. extraction.note: add "The spacetime instance of (ii) is stored as odd-extensions.four-extensions-oriented-pair (row this world + time) and odd-extensions.mirror-inside-complexified-extension-absent-doubled (iii); this result is its general even-dimensional form." Decision for Leon: a pinned `specialises` link from those two to this entity.
2. formal (ii), first sentence after the map: "equivalently $\Cl(W) = \Cl(V) \oplus \Cl(V)I_{W}$ as real vector spaces, with $\Cl(V)$ a real subalgebra commuting with $I_{W}$". This is precision only; the current text is not wrong.
3. (Optional, for the users) a one-line remark that for odd n one complexifies through V + Rf, which is how rule2 uses it; or rule2 should state that step itself.

---

## 2. synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom (v1)

**Verdict: SOUND WITH FIXES.** Every sign is right. One hidden choice: J is not the only unit
that commutes with the atom. Some wording needs to be more exact ("state", "not at -beta", "the source"),
and the ledger label is wrong.

### Premises at pinned versions
All pins current: singularity.modular-structure-completed-pair@5 (sigma = v*v - vv* = e_0e_1, rotor
flow v -> e^{-lambda} v, v* -> e^{lambda} v*, projectors, K = sigma/2 = N - 1/2), singularity.pseudo-inverse-identities-hyperbolic-atom@4 (v, v* = (e_0 +- e_1)/2 satisfy CAR in Cl(1,1)), std-algebra.bivector-exponential@2 (series collapse; the proof correctly notes only A^2 scalar is used, since 2JK = I_4 is a 4-vector, not a bivector), tower.structure-tower-c-norms@8 (frame *; the entity uses its real restriction e_0 rev(x) e_0, which I confirmed blade by blade by my own construction), singularity.kms-uniqueness-factor@5 (KMS in the form omega(ab) = omega(b alpha_{i beta}(a)) on a complex matrix factor; transferred to A by the *-isomorphism A = Mat_2(span{1, J}), J -> i). Cone: holds given nothing; derived ledger **absent**.

Uncited but used: primer.centre (centre of Cl(1,1) is R, in (ii)); the anticommutation of I_4 with vectors in (iii) is standard (std-algebra.orthogonal-anticommute). Minor.

### Signs recomputed independently (indep2.py, 54 exact checks, all pass; centralizer.py)
Against the store's v = (e_0 + e_1)/2, v* = (e_0 - e_1)/2, sigma = v*v - vv* = e_0e_1:
- J = e_2e_3: J^2 = -1; commutes with e_0, e_1, v, v*, sigma; J sigma = sigma J = +I_4; J* = -J; v* is the frame * of v; sigma* = sigma; JK = I_4/2.
- A = Cl(1,1) + Cl(1,1)J is exactly the commutant of J in Cl(1,3) (8 blades), a fact the entity does not state but that confirms (ii).
- Fock matrices over span{1, J} on the left ideal A P_+ (my own route): v and v* are the two off-diagonal matrix units, J is J times the identity, I_4 = diag(J, -J) in the basis (P_+, v), so I_4 P_+- = +-J P_+-; T(x) = 2<x>_0 - 2J<Jx>_0 equals the Fock trace on all 8 basis elements.
- Phase flow U = cos(t/2) + I_4 sin(t/2) = e^{JtK} at rational circle points: U* = U^{-1}, U v U^{-1} = e^{-Jt} v, U v* U^{-1} = e^{+Jt} v*; image of a radial vector has a trivector part.
- Complex parameter z = t + J theta (not only the pure-imaginary point): e^{JzK} = e^{JtK} e^{-theta K}, tau_z(v) = e^{-Jz} v = e^{theta} e^{-Jt} v, tau_z(v*) = e^{Jz} v*. Rotor flow e^{lambda K}: v -> e^{-lambda} v, v* -> e^{lambda} v*; z = -J lambda gives Jz = lambda, i.e. lambda = Jt.
- KMS: with the store's convention of singularity.two-kms-functionals-sign / kms-uniqueness-factor, phi(ab) = phi(b alpha_{i beta}(a)), alpha_{i beta}(a) = e^{-beta K} a e^{beta K}, read with i -> J: omega_beta(x tau_{J beta}(y)) = omega_beta(yx) holds on all 64 basis pairs with tau_{J beta} = Ad(e^{-beta K}) computed from e^{-beta K} = cosh(beta/2) - sigma sinh(beta/2); it fails with Ad(e^{+beta K}); omega_beta(v*v) = 1/(1 + e^beta) (Fermi-Dirac with weight 1, as two-kms (1)); omega_beta(x*x) real positive on samples.
- Modular flow: rho^{Jt} = e^{-J beta t K} exactly equals cos(beta t/2) - I_4 sin(beta t/2) = e^{J(-beta t)K}, and Ad(rho^{Jt}) v = e^{J beta t} v = tau_{-beta t}(v). This is the standard Tomita-Takesaki sign (sigma_t = Ad(rho^{it}), KMS at -1), so Ad(rho^{Jt}) = tau_{-beta t} is right; it is independent of which of +-i J is sent to.
- (I_4 a)(I_4 b) = +ab and (Ja)(Jb) = -ab for all pairs of five radial vectors.

### Is "one-mode CAR algebra over span{1, J}" exact?
Yes, as a *-algebra: A is Mat_2(span{1, J}), with v, v* the matrix units and the frame * the
conjugate transpose (conjugate-linear since J* = -J); the proof's quotient-by-dimension argument is
correct. It is exact only for the radial plane: J anticommutes with e_2, e_3 ((Je_2)(Je_2) = +e_2e_2),
so J is a scalar only on A, which the entity says.

### Check and perturbations
runcheck: 5/5 PASS. Mutations, all caught: J = e_1e_2 (fails all five); trace sign
2<x>_0 + 2J<Jx>_0 (fails (vi)); phase e^{+Jt} on v (fails (iv)); * = plain reversion (fails
(ii), (iv), (vi)); Gibbs density e^{+beta K} (fails (vi), via omega(v*v)); modular flow on the wrong
projector (fails (vi)); continuation at t = +J lambda (fails (iv)-(v)). Weak spot: clause (v) is
checked only through the separate rotor computation and the scalar identity -J(-J lambda) = -lambda;
tau_z at a genuinely mixed z = t + J theta is not checked (my indep2.py does it; it holds).

### Hidden hypothesis: J is a choice, not the unique unit
The centraliser of the atom (of e_0, e_1) in Cl(1,3) is four-dimensional, span{1, e_2e_3, e_0e_1e_2,
e_0e_1e_3}, a quaternion algebra. u = sigma e_2 = e_0e_1e_2 also squares to -1, commutes with v, v*,
sigma, satisfies u* = -u, and gives the same structure (uK = e_2/2, Ad(e^{utK}) v = e^{-ut} v,
checked exactly); u and J anticommute. J is distinguished, up to sign, as the only such unit in the
even subalgebra, equivalently the only one fixed by rotations of the transverse plane, and its sign is
fixed by J sigma = +I_4. The formal does not claim uniqueness, but the title ("the complex unit") and
the lay text ("supplies one that does") read as if it were unique. Note: u is exactly the odd-extension
unit I_V e of convention U3 for the atom window V = span{e_0, e_1} realised with e = e_2 (I_V^2 = +1,
so Q(e) = -1), the unit that synthesis.phase-flow-is-time-rotor-flow-kms-continuation (v) uses for
windows including K = sigma/2.

### Duplicates and overlap
- (iv)-(vi) restate stored results with the formal i replaced by J: singularity.euclidean-rotor-where-it-lies (1)-(2) (R_{i theta} = exp(i theta sigma/2), diag(e^{-i theta/2}, e^{i theta/2}) on the module; with i = J this is e^{theta I_4/2} = cos + I_4 sin, which matches the J-reading and diag(J, -J) above); singularity.kms-uniqueness-factor and singularity.two-kms-functionals-sign (1) (KMS state, occupancy); and synthesis.phase-flow-is-time-rotor-flow-kms-continuation (v) (Ad(e^{lambda K}) = tau_{-I lambda}, KMS swap omega_beta(A Ad(e^{-beta K})(B)) = omega_beta(BA)) with that entity's unit hat I in place of J. Signs agree throughout. New content: (i)-(iii), JK = I_4/2, and the fact that the unit lies in Cl(1,3). The entity cites none of euclidean-rotor-where-it-lies, two-kms-functionals-sign or phase-flow-is-time.
- Store consistency (decision for Leon, not a defect of this proof): for the same atom phase flow the store now has two units, J here (U2) and hat I = I_V e in phase-flow-is-time (v) (U3). Inside Cl(1,3) they are different, anticommuting elements of the quaternionic centraliser (J vs sigma e_2) and give different automorphisms of Cl(1,3) that agree as abstract flows. The conventions forbid identifying them; one of the two entities should say how they relate.
- The 2026-11-01 note on singularity.euclidean-rotor-where-it-lies (U1 reading, i = I_4 on values: i sigma = e_2e_3, the dual-plane rotor) gives exp(theta J/2), whose conjugation is trivial on A (J is central there). Under U2 the continued rotor on the atom is exp(theta I_4/2). The two readings are about different objects (values vs mode operators), so they do not contradict each other. This entity is the place to say so in one sentence.

### Fixes
1. **Non-uniqueness (formal (i) or a new clause, and title/lay).** Add: "The centraliser of $e_{0}, e_{1}$ in $\Cl(1,3)$ is $\mathrm{span}\{1, J, e_{0}e_{1}e_{2}, e_{0}e_{1}e_{3}\}$, a quaternion algebra; $J$ is, up to sign, its only unit of square $-1$ in the even subalgebra (equivalently, fixed by the rotations of the transverse plane), and its sign is fixed by $J\sigma = +I_{4}$. Odd units such as $\sigma e_{2}$ (the odd-extension unit of the atom window with $e = e_{2}$) also commute with the atom and are not identified with $J$." Title: "The transverse bivector is the even complex unit of the radial atom" (or keep the title and add the clause). Lay: "supplies one that does, the only one built from the even part of the algebra".
2. **"State" in (vi).** Replace "it is the only state of $\Aa$ that does" by "it is the only $\mathrm{span}\{1, J\}$-linear state of $\Aa$ that does". Real-linear normalised positive functionals are not unique: phi_b(x) = real part of (1 + bJ) omega_beta(x) is positive, normalised and KMS for every real b, and differs from omega_beta at x = J. Only b = 0 is hermitian (phi(x*) = phi(x)).
3. **"Not at -beta".** Formal (vi) is stated "for real beta"; at beta = 0 the "not at -beta" is false. Write "and, for $\beta \neq 0$, not at $-\beta$". Uniqueness is fine at beta = 0 (tracial state of a factor).
4. **Proof (vi) notation.** The symbol y stands for both e^beta and the KMS argument ("for $x = v$, $y = v^{*}$ unless $y^{2} = 1$"). Rename e^beta (for example $q = e^{\beta}$) in the proof and the check docstring.
5. **"The source's phase flow" (formal (iv)).** Name it: "the phase flow $\operatorname{Ad}(e^{itK})$ of Theorem \claimref{singularity.kms-uniqueness-factor} (and $\operatorname{Ad}(e^{it\sigma/2})$, $v \mapsto e^{-i\omega t}v$, of T05 Thm 7.16 / T07 Def 2.7), with $i$ written as $J$". Its sign agrees: v -> e^{-it} v.
6. **Ledger label.** extraction.note says "Transport-convenient"; the derived ledger is absent (no transport completion in the cone). Change to "Transport-absent".
7. **Links.** Add to extraction.note that (iv)-(vi) are euclidean-rotor-where-it-lies (1)-(2), kms-uniqueness-factor and two-kms-functionals-sign (1) written with J, and the atom case of phase-flow-is-time-rotor-flow-kms-continuation (v) with J in place of hat I. Decision for Leon: pinned `supports`/`specialises` links, and which unit the atom's phase flow uses in phase-flow-is-time (v).
8. **Premises (minor).** Add primer.centre@2 to `uses` (centre of Cl(1,1) in (ii)).
9. **Check (optional tightening).** In check_phase_flow_with_unit_J, test tau_z(v) = e^{-Jz} v at a mixed z = t + J theta (U at a circle point times cosh(theta/2) - sigma sinh(theta/2)), not only the scalar identity -J(-J lambda) = -lambda.

---

## Summary
| entity | verdict | blocking? |
|---|---|---|
| std-algebra.complexification-is-the-odd-extension | SOUND WITH FIXES (cite the stored spacetime instance; one wording precision) | no |
| synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom | SOUND WITH FIXES (J is the even unit, not the only one; F-linear "state"; beta != 0; name the source; ledger absent) | no |

Every sign named in the brief was recomputed independently and agrees with both entities and with
the store's conventions (U2, U3) and KMS sign convention. No postulate is in either cone.
