# Synthesis: open problems and gaps (21 October 2026)

**Status (21 October 2026).** A, B1, B2, C and D accepted into the store after an
independent review. D was held until its Step 3 was proved over the whole branch
(exact bounds; the least |U_tau3|^2 is 0.7688) and now cites the measured window
from the global fit rather than through the conjectured Observation. B1 settles
the open question `q.tower.odd-charge`.


Angle: close the store's open items (the open question, conjectures, results
tagged open-problem or undetermined-input, setting notes naming open
directions) and the gaps the "Every premise cited" pass recorded in
BUILD_REPORT.md (clauses with no argument of their own; premises that may sit
on the wrong result). No seed/CONTRADICTIONS_*.md existed at the time of this
pass.

Five candidates, all classified **proved** and filed as proposals (ids under
`synthesis.`, `proposed_by: {kind: ai}`, `ai_involved: yes`). Every finite
computation was checked in exact rational arithmetic with GA.py; each
proposal's check.py also passes the store's sandboxed runner
(`tp.evidence.run_check`). Scratch scripts are in
`/tmp/claude-0/-home-claude/f5c21aa3-33bd-54d7-a8e9-4d9b5d6a3726/scratchpad/synth-2/`.

| # | Proposal id | Open item addressed | How far | Class |
|---|---|---|---|---|
| A | `synthesis.colour-light-content-proton-ceiling` | clause (e) of `standard-model.table-exact` (no argument of its own) | fully, and generalised | proved |
| B1 | `synthesis.tower-limit-forgets-residue` | `q.tower.odd-charge` (the store's one open question) | fully | proved |
| B2 | `synthesis.plane-commutant-even-ground` | `q.tower.odd-charge`, second half (which invariant separates the cases) | partly | proved |
| C | `synthesis.mirror-asymmetry-route-one` | clause (v) of `dark-matter.mirror-tower-copy-one` (first route unargued) | partly; shows a stated claim does not survive | proved |
| D | `synthesis.theta23-at-s3-s2-direction` | the open number of `neutrino.mixing-none-leading-order` (near-maximal theta_23 from the breaking) | settled at the S3 to S2 direction | proved |

---

## A. Content no heavier in colour than in hypercharge cannot meet the proton condition

**Open item.** Clause (e) of `standard-model.table-exact` ("none of the three
admissible spectra meets the proton condition") is argued only by pointing to
`standard-model.proton-condition-candidates`(1), which reports floating-point
lifetimes. BUILD_REPORT lists it among the clauses with no argument of their
own.

**Statement.** One loop, normalisation of
`standard-model.imported-one-loop-running-trace-ratio`(a), t = ln(mu/M_Z)/2pi,
b = (41/10, -19/6, -7) below every threshold, record values of
`standard-model.spectrum-run`; content Delta^(k) switched on at t_k >= 0. Let
t_13 = (a_1 - a_3)/(b_1 - b_3) (the desert crossing of a_1 and a_3,
M_13 = 2.5 x 10^14 GeV). If every threshold has Delta_3 >= 0 and
Delta_1 >= Delta_3, then
(i) every point with a_1 = a_3, in particular any meeting, has t <= t_13 and
a_3(t) <= a_3 + 7 t_13, with t = t_13 exactly when Delta_1 = Delta_3 at every
threshold below the crossing (the wino attains both bounds);
(ii) hence M_U <= M_13, alpha_U^{-1} <= 40.4, and the proton figure
(alpha_U^{-1}/45)(M_U/10^15 GeV)^2 < 1/10, against the condition's
5.2 sqrt(15) > 20: no such content meets the proton condition, at any number
of thresholds (short by a factor above 200 in the figure, about 10^5 in
lifetime);
(iii) the three admissible rows, Delta = (0, 4/3, 0), (2/5, 2, 0),
(5/2, 25/6, 2), satisfy the hypothesis, so clause (e) follows with an argument
of its own.
Colour singlets and complete multiplets always satisfy the hypothesis; a
colour triplet does iff |Y| >= sqrt(5/18); the gluino (Delta_1 - Delta_3 = -2)
and Q- or d^c-type triplets do not. A proton-safe one-loop spectrum needs
content with Delta_3 > Delta_1 at some threshold.

**Premises.** `standard-model.imported-one-loop-running-trace-ratio@1`,
`standard-model.spectrum-run@2`, `standard-model.one-threshold-exact-criterion@2`,
`standard-model.table-exact@4`, `standard-model.imported-proton-condition@1`.

**Novelty.** Searched "gluino needed to meet proton condition", "upper bound
on the unification scale", "colour-neutral content", find_text `L_{13}`.
Closest: `standard-model.direction-demanded-content-doublet-heavy` (the
content must be SU(2)-heavy for f > 0) and `standard-model.proton-condition-candidates`
(numerical lifetimes of the three rows). Neither states a bound on M_U from
the a_1, a_3 pair or a structural reason for clause (e).

**Derivation.** (a_1 - a_3)(t) = D_13 - b_13 t - sum (Delta_1 - Delta_3)(t - t_k)_+
<= D_13 - b_13 t with b_13 = 111/10 > 0, so a crossing has t <= t_13;
a_3(t) = a_3 + 7t - sum Delta_3 (t - t_k)_+ <= a_3 + 7 t_13; the proton figure
is increasing in both. The wino's closed-form solution from the one-threshold
criterion gives x = t_13 exactly. Field contributions:
Delta_1 - Delta_3 = k d_2 ((3/5) Y^2 d_3 - T_3).

**Check.** `check_proton_ceiling.py` (scratch) and the proposal's check.py:
the three rows' exact solutions obey the bounds and the wino saturates them;
1500 pseudo-random exact multi-threshold contents obey (i); controls (a gluino
at M_Z, the full supersymmetric content from M_Z) cross above t_13; the proton
figure at the ceiling is bounded above by 1/10 with rational bounds
(pi < 355/113, exp by (1 - x/2^m)^{-2^m} with upward rounding). Record:
M_13 = 2.46 x 10^14 GeV, alpha_U^{-1} = 40.37, figure <= 0.054,
tau_p ~ 1.8 x 10^29 yr. All pass.

**Classification.** Proved. Note for BUILD_REPORT item 3: the general part
(i) and (ii) uses only the imported running and b_3 < 0; Hypothesis (S) enters
only through the table's identification of the content.

---

## B1. The limit of every tower is the same algebra

**Open item.** `q.tower.odd-charge` (T03 Question 5.8): identify the limit for
odd p - q; decide whether it is again a plain tensor product with Mat_{2^inf};
which real K-theoretic invariant separates the cases if not. Also noted open
in `one-relation.imported-completion-ladder` and `note.tower.setting-scope`.

**Statement.** For any (p,q), odd charge included:
(i) lim T_k = Cl(R^{p,q} + H_inf) is isomorphic, as a Z_2-graded algebra with
the frame *-structure, to Cl(H_inf) = Mat_{2^inf}, by the isomorphism induced
from a bijection of orthogonal frames matching squares (Q(x) = 1 generators
placed before the e_j, Q(x) = -1 before the f_j); the filtrations interleave,
Cl(m,m) in phi(T_k) in Cl(M,M), m = min(p,q)+k, M = max(p,q)+k;
(ii) for odd charge lim T_k is not Cl(p,q) (x) Mat_{2^inf}: the limit has
centre R, the latter Z(Cl(p,q)) = R + R or C; it is Cl^0(p,q) (x) Mat_{2^inf};
(iii) the completed complexified limit is CAR for every (p,q); for odd charge
not Cl(p,q)_C (x) CAR = CAR + CAR;
(iv) no invariant of the limit algebra (real K-theory included) separates the
eight towers; even Cl(p,q) (x) Mat_{2^inf} for even charge is Mat_{2^inf}. The
residue survives only in the filtration.

**Premises.** `tower.algebraic-limit-even-charge@2`, `tower.car-limit-even-charge@2`,
`tower.structure-tower-c-norms@3`, `tower.grade-twist-when-it-inner@2`.

**Novelty.** Searched "limit of the tower for odd charge", "Clifford algebra
of the union", "centre of the direct limit", find_text "odd charge" and
"K-theor". The store has only the even-charge theorems and the open question;
`note.tower.setting-introduction` says the paper declined to "assert the
unproved standard expectation", which (ii) shows is false.

**Derivation.** The limit is Cl(U) by the universal property (parity-free).
U and H_inf both have countable orthogonal frames with infinitely many vectors
of each square, so matching them in order is an isometry, inducing a graded
*-isomorphism. Centre: blades are eigenvectors of conjugation by generators;
the odd floor's centre is span{1, omega_k}; omega_k anticommutes with
e_{k+1}, f_{k+1}; so the limit's centre is R. For n odd,
Cl(p,q) = Cl^0 (x) Z, and Cl^0 has even charge. C*-norms correspond under the
*-isomorphism; completion is that of the (0,0) tower, CAR.

**Check.** `check_tower_limit.py` and the proposal's check.py: centres of odd
floors (six signatures, k <= 2) are span{1, omega_k}; omega_k anticommutes with
the next plane; Z(T_{k+1}) meets T_k in R; the frame bijection's images obey
the Clifford relations of the target, are compatible along the tower and
interleave (twelve signatures). All pass.

**Classification.** Proved. Answers the question: the odd-charge limit is a
plain matrix algebra, but not the ground algebra tensored with one; the
separating invariant does not exist for the bare limit.

---

## B2. At the top of the tower the planes' commutant is the even ground algebra

**Open item.** The second half of `q.tower.odd-charge` (what separates the
cases), once B1 shows the bare limit cannot.

**Statement.** (i) The relative commutant of the plane algebra B_inf in
lim T_k is exactly Cl^0(p,q); on a single floor the commutant of B_k is the
twisted copy A_k = Cl(p,q) of `tower.commuting-copies` (dimension 2^n), and
the next plane cuts it to its even half, since x Omega_k anticommutes with
e_{k+1}, f_{k+1}. (ii) So the pair (lim, B_inf) determines Cl^0(p,q): n, the
parity of r, for n even whether r = 0 or 2 mod 4 (omega^2 = (-1)^{r/2}), and
with the classification the class {r, -r}. (iii) It sees no more than that
class: Cl^0(p,q) = Cl^0(q,p) (one presentation on a frame with all squares
reversed). The residue survives at the top exactly up to the reversal, the
orbit along which P2 equates towers. Whether the pair distinguishes r from -r
is left open.

**Premises.** `tower.algebraic-limit-even-charge@2`, `tower.commuting-copies@2`,
`tower.volume-elements-planes@2`, `tower.rigidity-clock-frozen@2`.

**Novelty.** No store result computes a relative commutant in the limit; the
closest is `tower.commuting-copies` (finite floors).

**Derivation.** Blade argument: a blade commutes with every plane generator
iff it contains none and has even length. Omega_k is a product of bivectors of
the first k planes, so commutes with the new plane while x anticommutes.
Reversal: u_i = e_i e_n have squares -Q(e_i)Q(e_n), unchanged.

**Check.** `check_tower_limit.py` and the proposal's check.py: on eleven
signatures, the commutant of all planes of T_{k+1} restricted to T_k is the
span of even ground blades; on T_k alone it has dimension 2^n; common
presentation of Cl^0(p,q) and Cl^0(q,p) on eight signatures; centre and
omega^2 of Cl^0 on eighteen. All pass.

**Classification.** Proved (the open remainder is stated in the claim).
Filing note: the filed check.py does not call `premise()` on
`tower.algebraic-limit-even-charge`, which it lists; the corrected file (one
added line) is `.../scratchpad/synth-2/B2/check.py`. The proposal tool refuses
a second filing while one is waiting.

---

## C. The mirror's asymmetry by the audit route, and what that route needs

**Open item.** Clause (v) of `dark-matter.mirror-tower-copy-one`: the first
route ("by the audit, as in (iv)") has no argument; the proof argues only the
second route. Bears on BUILD_REPORT item 3 (P4 in
`dark-matter.mirror-share-assembled` "discharged by the copy theorem").

**Statement.** Let Phi: (sigma, mu, rho) -> (sigma, mu, -rho) be the canonical
anti-isometry of tractor fibres (`odd-extensions.two-towers-one-curved-universe`).
(i) Phi carries Witt pairs to Witt pairs (Phi W = W for W spanned by the
sigma-direction and mu_C vectors); on Fock modules it intertwines creation,
intertwines annihilation up to -1, and intertwines every mode number
operator exactly (the two signs cancel), so it carries grade k to grade k and
the asymmetry per mode with sign +1; Phi o C (C the flag conjugate) carries W
to Phi W' and the asymmetry with sign -1.
(ii) So route one gives epsilon_2 = +epsilon_6 iff the mirror is oriented by
Phi W. That assignment is a discrete datum exchanged by conjugating the
mirror's kinematic data alone, an automorphism under the seventeenth
refutation's first premise; it is fixed by P1's orientation clause or by P2
applied to that bit, so route one already contains route two's input.
(iii) Route one applies P2 to a continuous descent datum along the orbit, the
reach at which `dark-tower-matter.mirrors-temperature-p2` gets xi = 1 and
Delta N_eff = 7.45, excluded. It stands only under a scoping of P2 that the
store does not state.
Consequence: clause (v) rests, on present premises, on route two, and the P1
attack note's "withdraw the clause and (v) stands by the audit" does not
survive `dark-tower-matter.mirrors-temperature-p2`. Offered, not proved: a
scoping of P2 to superselected charges (the stored asymmetry Q = epsilon N,
`dark-matter.stored-asymmetry-charge-not-number`(i), is one; the temperature
ratio is not) would restore route one.

**Premises.** `odd-extensions.two-towers-one-curved-universe@2`,
`dark-matter.orientation-arrow-seventeenth-refutation@4`,
`dark-matter.flag-bit-exists-exactly-tower-dimension@2`,
`dark-matter.mirror-tower-copy-one@4`, `dark-tower-matter.mirrors-temperature-p2@3`.

**Novelty.** Searched "reversal carries the Witt flag", "relative orientation
of the mirror", "sign of the mirror asymmetry". Closest:
`note.dark-matter.setting-p1-attacked-could-there-have` (asserts route one
survives withdrawal of P1's clause) and `dark-tower-matter.mirrors-temperature-p2`
(the cold mirror as an unstated exception to P2). No store result states the
flag and grading behaviour of Phi or connects the two.

**Derivation.** Witt basis n_a, p_1, p_2 | n_b, q_1, q_2 of V_C, where
Phi = diag(1,1,1,-1,1,1) and h'(Phi w, Phi v) = -h(w, v); the Fock relations
follow; the conjugation argument parallels the seventeenth refutation; (iii)
reads off `dark-tower-matter.mirrors-temperature-p2` step 1.

**Check.** `check_mirror_flag.py` and the proposal's check.py: Phi^T h' Phi = -h;
real signatures (2,4) and (4,2); W, W' maximal isotropic for both forms; on the
8-dimensional Fock module the intertwining of creation, annihilation (sign -1)
and all number operators, the grade operator; C an isometry, Phi o C an
anti-isometry carrying W onto W'. All pass.

**Classification.** Proved: (i) exactly; (ii) at the level of the seventeenth
refutation's covariance argument, on its premise; (iii) an assembly of store
results. It closes the missing step of route one (the sign) and shows the
route is not independent of P1's orientation clause.

---

## D. Near-maximal theta_23 at the S3 to S2 direction

**Open item.** `neutrino.mixing-none-leading-order` (conjectured, tagged
open): "whether a breaking of the size that remark fixes can supply a
near-maximal theta_23 is open"; its tilts of 13 and 3 degrees are
"unscripted estimates" and the degree conversion "is not scripted".

**Statement.** Textures of `neutrino.breaking-relation` at E = e_3 e_3^T in both
sectors: charged c(J + delta_c E), delta_c = 0.286; m_D = d(J + delta E);
M_R = alpha Pi + M_3 J/3.
(i) m_nu = lambda_D E + lambda_M w^ w^T exactly, w = (3, 3, 3 + delta),
lambda_D = 2 d^2 delta^2/(3 alpha), lambda_M = d^2 |w|^2/(3 M_3); (1,-1,0) is in
both kernels (m_1 = m_e = 0), so the heavy eigenvectors share a plane.
(ii) The heavy neutrino eigenvector is nearer w than e_3 iff
lambda_M > lambda_D; m_2/m_3 peaks at lambda_M = lambda_D with value
tan^2(phi/2) (at delta = 0.286: M_3/alpha = 176.0, ratio in (0.240, 0.241),
which explains the remark's "near 0.24 at about 176"); the two roots are
exchanged by lambda_M -> lambda_D^2/lambda_M and their heavy eigenvectors are
mirror images across the bisector.
(iii) On the perturbative branch (lambda_M >= lambda_D), any |delta| <= 1,
|U_tau3|^2 > 0.76; at the remark's instance (delta = 0.286, M_3/alpha = 66)
|U_tau3|^2 > 0.96 (about 11 degrees apart; tilts about 13 and 3 degrees,
confirming the unscripted estimates).
(iv) Past the peak at |delta| = 0.286 and m_2/m_3 in (0.168, 0.172): delta =
+delta_c (M_3/alpha = 469.5) gives |U_tau3|^2 in (0.55, 0.58), just outside;
delta = -delta_c (M_3/alpha = 530.7) gives |U_tau3|^2 in (0.50, 0.55), inside
the window (0.39, 0.55).
So a breaking of the remark's size supplies near-maximal theta_23, but only on
the root past the peak (alpha/M_3 about 1.9 x 10^-3) and with the Dirac
neutrino breaking opposite in sign to the charged lepton's; never on the
perturbative branch the paper takes.

**Premises.** `neutrino.breaking-relation@1`. The window is cited from
`neutrino.mixing-none-leading-order` in the text, not used as a premise (it is
conjectured).

**Novelty.** No store result computes the eigenvectors or the angle; the
target Observation records the question as open and the tilts as unscripted.

**Derivation.** Rank-one decomposition from Pi J = 0 and e_3^T Pi e_3 = 2/3;
the family-exchange symmetry puts both heavy eigenvectors in the plane
spanned by (1,1,0), e_3; for a sum of two rank-one pieces,
m_2 m_3/(m_2 + m_3)^2 = s sin^2(phi)/(1+s)^2 (symmetric under s -> 1/s),
tan 2psi = s sin 2phi/(1 + s cos 2phi), psi(1/s) = phi - psi(s);
|U_tau3|^2 = 1/2 + tr(C_e C_nu)/sqrt(D_e D_nu) with rational ingredients.

**Check.** `check_theta23.py` and the proposal's check.py, exact throughout
(square roots handled by squaring with signs): the decomposition and kernels;
the charged calibration m_mu/m_tau in (0.0594, 0.0596); the instance ratio and
|U|^2 > 0.96; the mirror pairing (equal ratios, mirrored overlaps) on four
instances; the "nearer w iff lambda_M > lambda_D" test on 400 instances; both
second roots; 600 perturbative-branch instances with |U|^2 > 0.76; the peak
value and location. Cross-checked against floating-point diagonalisation.
All pass.

**Classification.** Proved. It settles the open number at this direction; it
does not address other breaking directions or the PMNS angles beyond
|U_tau3|^2, and whether the far root is acceptable is now the question.

---

## Examined and not pursued

- Clause (i) of `dark-matter.asymmetry-arrow-counted-fifteenth-refutation`
  (the Sakharov matching): a correspondence of names, explicitly "none is a
  mechanism producing a number"; nothing finite to supply beyond what the
  orientation-arrow proposition already proves.
- The closing clause of `odd-extensions.two-towers-one-curved-universe` ("an
  element no derived quantity of the series uses"): the algebraic content is
  already (ii) and (iii) of that theorem (A = A^0 + A^0 omega; the
  doubled-or-complexified bit is the sign of omega^2 = -Q(e_5) given the common
  Lorentzian omega_4); what remains is a census claim over the series, not a
  computation.
- Premise placement items in BUILD_REPORT item 3 for (S) and (U): bookkeeping;
  A records that its general part needs no (S).
- `transport.obstructions-are-moved-never-destroyed`, `sheaf.wall-class`,
  `interior.duality-monodromy-fibration-over-ring`,
  `correspondence.googly-localisation-quartic-order`: no reduction to a finite
  computation found within store results.
