# Run 2026-11-07-consistency: decisions draft (reconciler)

Sources read in full: consistency-R01.md to R12.md, xsubject-R01.md to R12.md, ga-issues-R01.md to R12.md,
ga-tensor.md, ga-matrices.md, CONSISTENCY.md, GA_REWRITE.md, GA_ROUND2.md, colony/POLICIES.md section 4.
ga-forms.md is not present (see H4); no ga2-*.md report exists yet (round 2 is running). Entities were looked up in
store/ read-only where a claim needed confirming. Exact checks by the reconciler (lib/GA.py, Fractions, 27 checks,
all pass): /tmp/claude-0/-home-claude/23cbb9be-73ca-5537-8211-47496476158a/scratchpad/recon/verify_recon.py
(quadratic-flow phase, rule2 null pair, Kerr-Schild chart, Q(I_Lambda) under both n0.ninf normalisations,
sigma_r^2 = +1 for the Weyl sign, i_6 = I_4E, de Sitter scale Box phi, ln 9/8). Items marked "checked here" rest on
that script or on a hand derivation written out below; the others rest on the reader's own exact script, named.

Routine means: no change of a premise, a status, an assumes edge, or a retirement; apply without asking under
POLICIES section 4. Uses edges, links (equivalent_to, restates, about, comments_on), wording, sign and constant
corrections backed by an exact computation, and applying a decision Leon has already made are routine.

## Summary

| Category | Items | Routine | Need Leon |
|---|---|---|---|
| A. Formal corrections backed by exact computation | 16 | 16 | 0 |
| B. Status stronger than its proof | 6 | 2 | 4 |
| C. Premise gaps and premise scope | 6 | 4 | 2 |
| D. Citations and links | 13 | 13 | 0 |
| E. Duplicates | 12 | 12 | 0 |
| F. Conventions additions | 15 | 15 | 0 |
| G. Stale wording depending on A to C | 13 | 13 (2 wait for C1, 1 for B1) | 0 |
| H. Anything else | 15 | 15 | 0 |
| Total | 96 | 90 | 6 |

Already applied in this run by the GA rewriters (checked in store/, not counted above): the Hadamard Step 7 sign and
regulator, its stale lay level and "(HS) premise" label (synthesis.hadamard-dirac-..., v6 proof now has
$-\tfrac12\epsilon^2$); the attachment cone unit read as $-I_7$ (R10 L5, verified by the tensor rewriter); the
operator-join unit sentence (R10 L3); the residues scalar-curvature remark and its $J$; the two-dimensional anomaly
sign sentence; the duality entity's formal $j$ as $I_7$; note.interior's field-equation sign; the GTG dictionary (iv);
the equivalence Fact's dangling eqrefs; the Kasner and radical-normal signatures declared; the Schrodinger cross
product and unit sentence; the slot-module unit sentence; the twisted-wall clock wording; the descent unit_note;
casimir-form-join's factor 1/2; the Kaluza-Klein sign epsilon; $\mathbb{Q}(i)$ in the loop proofs; the two-loop "Step 0".
All six known open items of the brief are settled: quadratic-flow sign (A1), boost-evolution Hamiltonian (A2), the
real-structure intermediate expression (fixed by R08), Hadamard Step 7 (fixed), the sign of $I_6$ on $\CS$
(orientation-dependent, fixed in the chart by R10; F4), operator-join $I_6$ against $I_4$ (fixed).

Five most consequential:
1. C1. Under P2 version 2 the mirror's common ceiling coupling, and with it the share of one, has no premise behind it.
2. A3. synthesis.positive-structure-and-natural-scale-actions-... has the wrong sign of $\Lambda$ in its Euler-Lagrange
   equation and contradicts synthesis.twistor-flat-fields-give-nordstrom-not-einstein (i).
3. C2. pred.leptonic-cp-trivial needs a real charged-lepton matrix that its premise does not state; the store's own
   circulant result gives maximal CP violation without it.
4. B1. Two scrambling estimates are filed as proved, and one of them asserts a real-time delay that (L_E) excludes.
5. A5 with A6. The Schwarzschild horizon-translation result is stated in the outgoing chart (past horizon) while it
   says ingoing, and the Killing-horizon value factor needs $\beta = +\sqrt{1-f}$ for its sign of $\kappa$.

## A. Corrections to a formal statement backed by an exact computation (all routine)

A1. synthesis.quadratic-flows-cannot-thermalise-descent (ii), v2. Readers: R08 (known open item).
- Evidence: $\operatorname{Ad}(e^{J\theta N})a = e^{-J\theta}a$ (checked here; R08 qf_phase.py in Cl(4,2)). With the proof's
  $C_{ij} = \omega(a_j^*a_i)$ and $U = e^{-Jtk}$ the coherence gets $e^{-J(\omega_i-\omega_j)t}$; the formal writes
  $e^{+J(\ldots)}$ and leaves $C_{ij}$ undefined. The pairing sign is right; the proof is right.
- Fix: "multiplies the coherence $C_{ij} = \omega(a_j^*a_i)$ by $e^{-J(\omega_i-\omega_j)t}$"; prefix the
  maintainer_pass_ga_units note "Superseded by maintainer_pass_resolve_units:". Version 2 -> 3.
- Recommendation: apply.

A2. synthesis.boost-evolution-on-generators-is-one-unitary-group (ii), (iii). Readers: R01 (known open item).
- Evidence: with $a(f) = \int \bar f\,\psi\,du$ and $\alpha_l(\psi(u)) = e^{-l/2}\psi(e^{-l}u)$, the substitution
  $v = e^{-l}u$ gives $\alpha_l(a(f)) = a(g)$, $g(v) = e^{l/2}f(e^lv) = (D_{-l}f)(v)$ (checked here by hand; R01
  boost_sign.py). The proof of (iii) pulls the phase out of the antilinear $a$ without conjugating: two compensating
  slips. Clause (iii)'s Hamiltonian $+\kappa w$ is right; (v), (vi) unaffected.
- Fix: R01's text for formal (ii), proof (ii), (iii).
- Recommendation: apply.

A3. synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale (ii). Reader: R03.
- Evidence: the store-sign scalar of $\varphi^2\eta$ is $6\Box\varphi/\varphi^3$ (as
  synthesis.twistor-flat-fields-give-nordstrom-not-einstein (i) states); the stored de Sitter scale
  $\sigma = 1 - \Lambda Q/12$, $\varphi = 1/\sigma$, gives $\Box\varphi = -\Box\sigma/\sigma^2 + 2(\partial\sigma)^2/\sigma^3
  = +\tfrac23\Lambda\varphi^3$ with $\Box\sigma = -\tfrac23\Lambda$, $(\partial\sigma)^2 = \Lambda^2Q/36$ (checked here;
  R03 v/r03_checks.py). The entity writes $\Box\varphi = -\tfrac23\Lambda\varphi^3$; its "the flip changes nothing"
  is false for $\Lambda \ne 0$. Two proved entities contradict on the sign.
- Fix: R03's text (formal (ii), proof (ii)); check.py docstring and label to match, then runcheck.
- Recommendation: apply. The entity is on ga2_gravity.txt: give the fix to the round-2 gravity rewriter, or apply after
  it finishes, so two writers do not touch it.

A4. rule2.where-obstruction-sits-commuting-square (c). Reader: R11.
- Evidence: $f = \tfrac12(\nu + e)$, $f^* = \tfrac12(\nu - e)$ with $\nu^2 = -1$, $e^2 = +1$ gives $ff^* + f^*f = -1$;
  with $e$ first it is $+1$ (checked here). Leon corrected exactly this in the twin
  transport.where-obstruction-lies-commuting-square on 2026-10-23.
- Fix: copy the twin's text (formal, technical), version 5 -> 6.
- Recommendation: apply (an existing decision).

A5. synthesis.schwarzschild-horizon-translations-are-no-conformal-symmetry. Reader: R02.
- Evidence: for $\hb^{-1}(a) = a - (M/r)(a\cdot k)k$, $k = e_0 + \hat x$, at $r = 2M$: $Q_g(e_0 + \hat x) = 0$,
  $Q_g(e_0 - \hat x) = -4$ ($M = \tfrac12$; checked here, R02 ks.py). This is the outgoing chart (past horizon), which
  is why (v) and the check find $(K\cdot D)K = -\kappa K$. Proof (iv) uses $v = t + r$, which this field does not have;
  proof (v) writes $e^{+\kappa v}$ against its own $-\kappa$. The conclusion is time-reflection symmetric and stands.
- Fix: R02's wording route (keeps check.py): "outgoing (Kerr-Schild) gauge, which covers the exterior, the past horizon
  and the white-hole interior"; (v) $\lambda \mapsto e^{-\kappa\tau}\lambda$ on the past horizon; proof (iv) in
  $u = t - r$; proof (v) $d\lambda/du = c\,e^{-\kappa u}$; one sentence that the future horizon follows by time
  reflection; add the "Beyond one flat chart" sentence its flag requires. Repoint in D1.
- Recommendation: apply the wording route, not the alternative $k = e_0 - \hat x$ (that one needs a check.py change).

A6. synthesis.killing-horizon-value-factor-is-the-generator-boost (iii), (iv). Reader: R02 (and xsubject-R02 1).
- Evidence: $(K\cdot D)K = \beta(r_h)f'(r_h)/2\,K$ (R02 pg.py); $\kappa = f'/2$ needs $\beta(r_h) = +1$, which the
  proof assumes and the formal ($\beta^2 = 1 - f$) does not say. For de Sitter that is the contracting chart (past
  horizon, $-H$); the dictionary's expanding chart gives $+H$ on the future horizon.
- Fix: "$\beta = +\sqrt{1-f}$" in (iv); "$-H$ for de Sitter in this chart, which contains the past cosmological
  horizon (the expanding chart gives $+H$ on the future one)"; (iii) "for either sign of $\kappa$ (future and past
  horizons)". Repoint in D2.
- Recommendation: apply; on ga2_gravity.txt, so coordinate as in A3.

A7. synthesis.local-normality-at-the-edge-gives-the-null-ground-state (v). Reader: R02.
- Evidence: $\int_s^{2s}\int_s^{2s}(u + w)^{-2} = \ln\tfrac32 - \ln\tfrac43 = \ln\tfrac98$ (checked here); for
  $R = (I_4/2\pi)(u - v)^{-1}$ the integral of $|R|^2$ is $(2\pi)^{-2}\ln\tfrac98$.
- Fix: "the integral of $|2\pi R/I_4|^2$ over every square $[s, 2s]^2$ is $\ln\tfrac98$".
- Recommendation: apply.

A8. odd-extensions.transport-constrains-frozen-point-only-through (i). Reader: R07.
- Evidence: $I$ spans the radical of $W = I_0^\perp$, so $\{I\}^\perp \cap W = W \ni I$, and
  "$\varphi \perp \{I\}^\perp\cap W$" contradicts $Q(I,\varphi) = 1$ (read in store: formal (i) as quoted by R07).
  The proof uses only the isometry fixing $W$; (ii) already says "orthogonal to the Lorentz frame".
- Fix: "$\varphi$ orthogonal to the Lorentz frame of $W$" (formal (i), technical).
- Recommendation: apply.

A9. synthesis.frozen-point-geometry-reads-descent-as-vacuum (ii), technical; standard-model.dating-descent (iii). R07.
- Evidence: the bound $k/(a_dH_\Lambda) > 7\times10^9$ at 1 MeV is derived for $k \ge a_0H_0$; the observed range
  starts at $k = 2/\eta_0$ ($k/a_0H_0 \in (0.627, 0.631)$), where the ratio is below $4.6\times10^9$ (R07 v3.py).
- Fix: "$> 4\times10^9$ at 1 MeV ($> 7\times10^9$ for $k \ge a_0H_0$)". Conclusion unaffected.
- Recommendation: apply.

A10. sheaf.wall-class (b) and note.sheaf.wall-class-posed. Reader: R09 (xsubject-R09 1).
- Evidence: the rung $(+1,+1)$ leaves $d = p - q \bmod 8$ unchanged ($(p+1) - (q+1) = p - q$);
  tower.rigidity-clock-frozen and synthesis.wall-class-one-rung-obstruction say the same.
- Fix: (b) "... transferring it to the next shadow wall, the rung shifting both signatures by (1,1) and leaving both
  clock positions unchanged"; a dated bracket in the note (paper text).
- Recommendation: apply. Clause (a) is a separate question (B4).

A11. synthesis.macdowell-mansouri-is-the-frozen-point-reduction-of-five-dimensional-chern-simons (iii) (forms-owned).
Reader: R03 (ga-issues-R03 3).
- Evidence: $\sigma_r^2 = +1$ (checked here), so $W(B) = m(B + 3\sigma B\sigma)$, $m = -M/(2r^3)$, gives
  $W(\sigma_r) = -2M/r^3\,\sigma_r$, while the store-sign Weyl map has $\mathcal{W}(\sigma_r) = +2M/r^3\,\sigma_r$.
  $48m^2$ is sign-free.
- Fix: "$F = -\mathcal{W}$, $\mathcal{W}$ the Weyl map in the store's sign". Not yet applied (no forms report).
- Recommendation: apply.

A12. synthesis.electron-positron-to-muon-pairs-...-one-loop-unitarity formal (1). Reader: R06 (ga-issues-R06 3).
- Evidence: the formal gives spin sums for an outgoing particle and an incoming antiparticle only; the tree trace
  uses the incoming electron $p_1 + m_e$ and the outgoing antimuon $p_4 - m_\mu$ (proof Step 1 has the full rule).
- Fix: "the spin sums of a particle, incoming or outgoing, and of an antiparticle are the multivectors $p + m$ and
  $p - m$". Still open in store.
- Recommendation: apply.

A13. note.programme.setting-series-paper-paper-2 (GA-owned, T17 status table), T15 row. Reader: R04.
- Evidence: the grade-three state $(1)_{-1}$ is $e_R$; $e^c$ has $Y = +1$
  (standard-model.hypercharge-global-form-pair-counting-consistency (2)). Still open in store.
- Fix: "(the filled twistor, at $Y = -1$, is $e_R$, the conjugate of $e^c$)".
- Recommendation: apply.

A14. dark-matter.open-channels-their-costs. Reader: R05 (not rechecked here).
- Evidence: with $3.044/3$ per neutrino the coefficient for the heaviest neutrino non-relativistic is 6.43, not 6.40;
  the 0.47 threshold is unchanged.
- Fix: 6.40 -> 6.43.
- Recommendation: apply after one line of arithmetic in the maintainer pass.

A15. scrambling.area-law-test, formal. Reader: R08.
- Evidence: "reproduces the Bekenstein-Hawking entropy, coefficient included" holds in the 1-nat convention only;
  scrambling.residue-each-convention (iii) says that convention over-credits each mode; with $\ln 2$ per mode the
  condition is $\nu\Delta t = M/(2\ln 2)$ (singularity.area-law-test).
- Fix: append "(in the 1-nat convention; with each mode credited its $\ln 2$ the condition is $\nu\Delta t = M/(2\ln 2)$,
  Proposition \claimref{singularity.area-law-test})", as its one-liner already says.
- Recommendation: apply.

A16. dark-energy.wall-counterterm. Reader: R09 3.
- Evidence: the formal identifies $\omega^{ab}$ with $\Omega$; the conventions (GTG) say Cartan-form values are $-\Omega$
  on vectors. $\mathrm{CS}(\omega)$'s cubic term is odd under $\omega \to -\omega$, so the sign of the value
  $8p_1p_2p_3$ depends on the identification.
- Fix: state that $\omega^{ab}$ are the Cartan connection forms (curvature $d\omega + \omega\wedge\omega$), minus
  $\Omega$ on vectors; recompute the value against T10 Prop 4.11 before stating it.
- Recommendation: apply after that one computation; if the sign of the value changes, it is still an A correction.
  Not on any GA list (see H3).

## B. Status stronger than its proof

B1. scrambling.spreading-law-chaos-bound-saturated (v5) and scrambling.return-delay-scrambling-log-recovered (v2):
NEEDS LEON. Reader: R08 2.
- Evidence: both are order-of-magnitude estimates ($\sim$, $\approx$, "Tier, declared", "the standard doubling
  estimate"); both proofs are "Follows from ..., as the source states". return-delay states a real-time delay from
  pairwise spreading, which singularity.l-boundary-mode-locality excludes under (L$_E$) and
  synthesis.number-diagonal-dynamics-spreads-nothing proves.
- Proposed fix: status conjectured for both; in return-delay's formal add "Under (L$_E$) this is a modular-time
  (rotor-flow) estimate, not a real-time delay (\claimref{singularity.l-boundary-mode-locality})" with
  `flow_note: rotor`.
- Recommendation: conjectured for both, with the return-delay sentence.

B2. dark-matter.no-coupling-rule-odd-towers-follows (v5, GA-owned forms): NEEDS LEON. Reader: R05 5.
- Evidence: status proved, while its formal ends "The result is at structural level, not proved in the series'
  strict sense", and its lay and one-liner say the same.
- Proposed fix (either): (a) restate the formal as the three facts it does establish, (a) the coupling is dimensionful
  for $d \ne 4$ and the comparison length is not fixed, (b) no gauge coupling value is derived in the store, (c) P2
  equates only along the reversal orbit, with "so any such rule is a further premise" as the reading, and drop the
  disclaimer; or (b) lower to conjectured.
- Recommendation: (a), status stays proved.

B3. one-relation.record-chain-votes-measurement-without-collapse, one-relation.character-experience-three-record-chain-
theorems, one-relation.overlap-table-sorted: NEEDS LEON. Reader: R12 2.
- Evidence: the first two rest on "Remark rem:recording", which is not a store entity (it is under unresolved_refs);
  overlap-table's proof says clauses (ii), (iii) and the constants clause are "proved to no standard beyond its own
  statement".
- Proposed fix: enter rem:recording as a postulate (the recording premise) with assumes edges from the two
  record-chain results (status stays proved, given it); move overlap-table's (ii), (iii) and the constants clause
  from the formal into a Reading in the technical level, leaving (i) as the proved formal.
- Recommendation: as proposed. (Alternative: lower the three to conjectured.)

B4. sheaf.wall-class (conjecture), clause (a): NEEDS LEON. Reader: R09 1.
- Evidence: synthesis.wall-class-one-rung-obstruction proves that clause (a) cannot see torsion in either reading of
  "standard"; the conjecture as posed cannot hold in (a).
- Proposed fix: restate the conjecture with (a) replaced by the one-rung (or k-rung) completion, cite the
  obstruction, keep status conjectured; the wording fix of (b) is A10.
- Recommendation: restate with the one-rung completion, status conjectured.

B5. one-relation.measure-indifference-borns-rule-located (routine). Reader: R12 2.
- Evidence: the fine-graining and continuity steps are Zurek's envariance argument "imported with its critique", but no
  imported entity carries it.
- Fix: import Zurek (2005) as a Fact and add the uses edge (POLICIES section 4: importing literature cited from
  memory is routine).
- Recommendation: apply.

B6. mass.imported-unitary-representations-de-sitter-group (routine). Reader: R10 L6.
- Evidence: the imported Fact (Dixmier) asserts in its formal that mass.casimir-form-join's $C_2(I_\perp)$ is "in this
  same normalisation, with no shift"; synthesis.operator-join-casimir-shifts (iii) calls that hypothesis not proved;
  synthesis.operator-join-point-spectrum-on-positive-energy-modules uses it for sharpness.
- Fix: move the sentence out of the Fact (into casimir-shifts as its stated hypothesis), and state the hypothesis in
  point-spectrum's sharpness clause.
- Recommendation: apply; no status, premise or assumes change (a hypothesis made explicit).

## C. Premise gaps and premise-scope questions

C1. P2 version 2 and the mirror's common ceiling coupling: NEEDS LEON. Reader: R05 1 (also ga-issues-R05 1).
- Entities: dark-matter.p2-indifference@2; dark-matter.mirror-tower-copy-one (iv) (assumes P1@1, P2@2), and through it
  dark-matter.mirror-share-assembled (ii), dark-matter.mirror-share-one-how-fragile (ii) ("P2-protected"),
  dark-matter.population-count-one-share-half-percent (proof), dark-matter.which-towers-can-carry-arrow,
  dark-matter.no-coupling-rule-odd-towers-follows (c), standard-model.under-s-mirror-inherits-desert (mention).
- Evidence (read in store): P2@2's scope is "labels, not states"; synthesis.tower-charge-sector-label-temperature-not's
  Reading ends "The scoping reaches the stored charge $Q = \epsilon N$ ..., but not the ceiling coupling, which is not
  a charge." mirror-tower-copy-one (iv) applies P2 to exactly that coupling, which gives $\Lambda_2 = \Lambda_6$,
  $c_2 = c_6$ and the share of one.
- Proposed fix (either): (a) P2 version 3, adding to the scope paragraph "and the parameters of the deposited dynamics
  along the orbit (the couplings at the ceiling), which are neither labels nor states"; or (b) mark (iv) and the share
  of one as resting on a further premise.
- Recommendation: (a). P2 at version 1 reached the couplings, the scoping was written to release the temperature, and
  (a) keeps that. Then reword the tower-charge Reading's last sentence to match. The $f_1 = f_7$, $f_3 = f_5$ citations
  of P2 (dark-matter.total-function-thickness, note.dark-matter.setting-dark-matter-ratio-unit-ball) can say that the
  equalities also follow from R2's reversal-invariant measures (routine).

C2. neutrino.real-breaking-assumption and pred.leptonic-cp-trivial: NEEDS LEON. Reader: R10 L1, xsubject-R10 X1.
- Evidence: synthesis.circulant-charged-leptons-excluded-with-real-neutrino-sectors (iv)(c): the complex Koide
  circulant as charged-lepton matrix (synthesis.koide-channel-phase-is-no-symmetry-angle), the electron on the
  democratic line and a real $P_{12}$-breaking $m_\nu$ give $\cos\delta_{CP} = 0$. The assumption makes only the Dirac
  and Majorana neutrino matrices real; $\delta_{CP} \in \{0, \pi\}$ also needs the charged-lepton matrix real in the
  same basis.
- Proposed fix (either): (a) add to the assumption's formal "and the charged-lepton matrix is real in the same basis
  (the textures of neutrino.breaking-relation)", and "with a real charged-lepton matrix" to the prediction's technical
  level and one-liner; or (b) record the circulant branch as a namesake tension.
- Recommendation: (a). It states what the prediction already uses; the stored tau placement is excluded by (iv)(b),
  so no stored result changes.

C3. Which unit acts on the five-mode module (routine). Reader: R04 2, xsubject-R04 1.
- Entities: rungs.generators-outside-gauge-algebra, standard-model.left-right-parity-what-breaks-it (against
  obj.standard-model.two-rung-module-sectors-slot-components, standard-model.ten-transported-ambient-space-doublets-are,
  std-algebra.complexification-is-the-odd-extension).
- Evidence: "$I_4$ commutes with every mode operator" holds on the abstract Fock module (U1), but the ten are identified
  with $V_\mathbb{C} + R_2 + \bar R_2$, and as Clifford elements $I_4$ anticommutes with the spacetime pair vectors,
  whose complexification is $I_7$.
- Fix: R04's sentence in both proofs ("on the five-mode Fock module numbers, $I_4$ among them, act as scalars; as Clifford
  elements $I_4$ commutes with the rung vectors, and the pair vectors of $V_\mathbb{C}$ are complexified by $I_7$, which is
  not used here").
- Recommendation: apply (a which-unit sentence; it identifies nothing).

C4. synthesis.attachment-conformal-energy-is-generated-by-z: orientation of $I_6$ in its frame (routine). Reader:
R10 (ga-issues-R10 2; the tensor rewriter left it).
- Evidence: on $\CS$ left $I_6$ is $-I_7$ or $+I_7$ by orientation (R10 work-R10/i6_on_cs.py); the z-adapted result's
  "$+R_{I_6}$, a convention" should be a stated consequence of the frame used.
- Fix: one sentence naming the orientation of $I_6$ in the frame $(e_0, \ldots, e_3, \nu, e_-)$ and the resulting sign,
  after extending i6_on_cs.py to that frame.
- Recommendation: apply after the check.

C5. ruling R3 in note.dark-tower-matter.neutral-row (routine, no action). Reader: R05 10.
- Evidence: R05 added the which-unit sentence ($u$ on the five-dimensional pairs, $I_4$ on the multiplicity spaces, not
  identified).
- Recommendation: keep as written; reading the note over span{1, u} would identify two units.

C6. Normality, modular-data and the attachment edge: premise hygiene through a non-premise citation (routine; edges in
D4). Reader: R02 4, xsubject-R02 3.
- Evidence: J3 and (Q) enter synthesis.normality-on-the-closed-generator-... and synthesis.modular-data-on-a-generator-...
  only through the rotor realisation of the Moebius closing, which the check computes itself.
- Recommendation: cite a premise-free statement of the rotor realisation if one exists; otherwise keep the edge.

## D. Citations and links (all routine)

D1. synthesis.schwarzschild-horizon-...: repoint positive-null-energy@7 (cited only for the dilation of its setup) to
synthesis.null-vacuum-on-a-horizon-generator@1 (i); drops (N+) from holds_given. R02 1.
D2. synthesis.killing-horizon-value-factor-...: holds_given (c1, c2, L, P, R, N+) arrives through boost-evolution,
affine-cell and positive-null-energy for a geometric statement; repoint to null-vacuum-on-a-horizon-generator. R02 2,
xsubject-R02 2.
D3. synthesis.thermality-of-every-future-half-generator-fixes-the-period-and-the-null-ground-state: repoint to
null-vacuum-on-a-horizon-generator@1 (ii), (iii) and stationary-generator-states-and-the-edge-scaling@1 (iii), and the
formal's claimref; this also removes (N+) from synthesis.geometric-modular-conjugations-... R02 3.
D4. synthesis.normality-on-the-closed-generator-... (GA-owned): stationary-horizon-state@4 -> stationary-generator-
states-and-the-edge-scaling@1 (i), (iii); synthesis.modular-data-on-a-generator-...: wedge-reflections (cited only for
$I_4B = J$) -> a premise-free source of that identity; the attachment edge as C6. R02 4, ga-issues-R02 1.
D5. synthesis.imported-null-plane-modular-hamiltonian-first-law, technical: positive-null-energy (ii) ->
null-vacuum-on-a-horizon-generator (iii) (text citation). xsubject-R02 4.
D6. pairing.two-frames-share-vacuum-selected-transport (ii): it cites pairing.regular-frame-class-vanishes-horizon-changes
with no uses edge, and that result uses this one (a cycle). Write it as a mention ("computed in the regular frame by
..., which builds on (i) here"), no edge. R01 3.
D7. scrambling.pair-mode-qubit-one-object (formal, technical) and scrambling.epoch-modular-period-two-unknowns-become:
"one ladder pair per point of the exceptional set" is T04 Thm 8.7 (sheaf.schwarzschild-degeneration-boundary-tame), not
tower.witt-index-quantum-capacity (which states only $\min(p,q)$); cite it and add the uses edge in the first. R12 1,
xsubject-R12 2.
D8. dark-matter.imported-gravity-only-coupling: "only contact" is the sector decomposition; cite the Definition
obj.dark-matter.frozen-phase-operators; keep the assumes edge to P1. R05 4.
D9. synthesis.matter-asymmetry-registered-free-input: dark-matter.stored-asymmetry-charge-not-number is a Proposition,
not a Theorem. R05 11.
D10. interior.gauge-trajectory-unipotent-ray: add uses singularity.unipotent-ray@4 and singularity.cones-fold@4 for
clauses (1), (2), (4) (restatement); it keeps the group law as its own content. R06 3.
D11. note.conformal.abstract: comments_on conformal.minimal-nondegenerate-completion (the abstract's subject). R11 6.
D12. references.yaml: WeinbergQFT1 and WeinbergQFT2 both cite Vol. 2 (1996) (read in store); merge the key into
WeinbergQFT2 and repoint lepton.imported-free-sector-anomaly-conditions and its -external entry. R04 5.
D13. one-relation.imported-square-roots-real-clifford-algebras: "conjugate to one of a short list" -> "conjugate to the
pseudoscalar (one class; std-algebra.square-roots-of-minus-one)". R11 5.

## E. Duplicates (all routine: links now; no retirement proposed)

E1. synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator... (vii) and Step 8 = synthesis.floor-regulator-
keeps-the-charge-and-the-central-term-below-the-cut-off (v). Leon merged them on 2 November; drop (vii) and Step 8 with a
pointer. Keep floor-regulator. R06 2.
E2. interior.gauge-trajectory-unipotent-ray (1), (2), (4) = singularity.unipotent-ray, singularity.cones-fold (and (3) the
cometric of sheaf.gauge-field-cometric). Keep the singularity originals; link by D10. R06 3.
E3. field-theory.imported-standard-field-theory names the Adler-Bell-Jackiw anomaly;
synthesis.imported-adler-bell-jackiw-axial-anomaly imports it with citations. Keep the latter; a marked pointer in the
former. R06 4, xsubject-R06 4.
E4. sheaf.kasner-data-interior (imported, Kasner 1921) states what interior.kasner-form-interior proves with rates. Keep
both (sheaf's users pin it, and making it proved would be a status change); a restates link to the proved one. R07 5.
E5. interior.imported-equivalence-einstein-equations (T06) and singularity.imported-equivalence-einstein-equations (T05,
adds the curvature clause). Keep both for their paper locators; equivalent_to, T05 the better one. R03.
E6. Sheaf against three-routes and twins (R09): sheaf.base-unipotents-wall = three-routes.base-unipotents-their-action-
candidates (equivalent_to; keep sheaf); sheaf.transversal-independence-wall > three-routes.change-transversal-canonical-
isomorphism-completions and sheaf.no-equivariant-value-wall > three-routes.no-equivariant-value-boundary (specialises
links; keep sheaf); singularity.modular-structure-completed-pair > hawking.modular-structure-completed-pair (equivalent_to;
keep singularity, it has the rotor-group caveat); singularity.purity-output-partner-commutant =
state-selection.partner-purification-are-canonical (equivalent_to; keep singularity); singularity.net-assembly-net-it-
everything ~ three-routes.join-disqualified-wrong-stalks and singularity.sheaf-assembly-sheaf ~ three-routes.it-sheaf-risk-
resolves-into-standing + three-routes.stalks-are-pointwise-metric-levels (links; the three-routes ones carry the 23 October
correction).
E7. Clifford core (R11): conformal.witt-extension-theorem equivalent_to std-algebra.witt-extension (keep std);
std-algebra.complexification (ii) ~ odd-extensions.doubling-or-complexification (i), (ii); odd-extensions.doubling-or-
complexification (iii) ~ std-algebra.even-subalgebra-isomorphism (join the existing chain);
odd-extensions.volume-element-odd-dimension restates primer.centre and primer.sign for odd n; std-algebra.zero-divisors-
annihilated (d), (e) ~ transport.exhaustiveness-every-zero-divisor-annihilated-idempotent (1) and the consequence clause
of transport.regularity-localises-zero-divisors-idempotents (keep std as the general statement).
E8. tower.morita-equivalence-algebra-amplification (imported, Lam) = std-algebra.morita-amplification (iii) (proved):
equivalent_to; keep the status imported (a derivation would be a status change, not needed). R11 4.
E9. Tower and Fock imports (R12): odd-extensions.imported-towers-clock restates dark-matter.imported-eight-towers-mod-8-
clock (keep dark-matter); standard-model.imported-tower-commuting-copies-fock-module is a subset of
rungs.imported-tower-one-qubit-per-rung (keep rungs); pairing.imported-stabiliser-tangent-external lists the sources of
one-relation.imported-cartans-purity-theorem-thouless-form (keep Cartan); rungs.imported-fock-representation-bogoliubov-
group-external = standard-model.imported-fock-representation-clifford-algebra-bogoliubov (keep standard-model). Links now;
the last pair is an exact duplicate that a later dedupe pass may retire under POLICIES section 4.
E10. dark-matter.imported-composition-simulated-external is a citation list of Randall 2008 and Clowe 2006, which
simulations.imported-bullet-cluster imports with content: link, keep the bullet-cluster entity. R05.
E11. Restatements after the 7 November splits (R02): synthesis.positive-null-energy-gives-r-premises (i), (ii) restate
synthesis.null-vacuum-on-a-horizon-generator (ii), (iii); synthesis.stationary-horizon-state (i) to (iii) restate
synthesis.stationary-generator-states-and-the-edge-scaling (i) to (iii). Mark restates so counts take each once; the
premise-free entities are the homes.
E12. three-routes.imported-collar-data-coupling (proved, empty derivation, no about link) restates the definition
obj.sheaf.collar-data-coupling verbatim: add `about: obj.sheaf.collar-data-coupling`. R09 4.
No action (reported as near-duplicates kept by design): the two area-law tests (A15), the eviction pair, the Haar pair
(R08); the s-wave current restatements and the cost-r notes (R01); the unit-ball triple, the cluster pair, the towers
types pair (R05); the acknowledged standard-model overlaps (R04); the T09 Thm 5.3 and mass-bracket restatements (R10).

## F. Conventions additions (store/conventions.md; one line each; all routine)

F1. Frozen-point norm (R08, xsubject-R08): "For $I_\Lambda = n_\infty + \tfrac{\Lambda}{6}n_0$,
$Q(I_\Lambda) = \tfrac{\Lambda}{3}\,n_0\cdot n_\infty$: $+\Lambda/3$ in the $n_0\cdot n_\infty = +1$ normalisation, $-\Lambda/3$ in
T01's." (checked here). Also add "in the normalisation $n_0\cdot n_\infty = +1$" to standard-model.imported-frozen-point-
dictionary's statement.
F2. $\Cl^0$ against $\Cl^+$ (R11 2): "The T01-derived regions write $\Cl^0(p,q)$ for the even subalgebra $\Cl^+(p,q)$;
$\Cl^0$ for grade zero is the standard-algebra objects' usage." (a line, not 25 renames).
F3. P1/P2 (R07 6, xsubject-R07 2), under Same names: "P1, P2 are T14's single frozen point and indifference
(dark-matter.p1-single-frozen-point, dark-matter.p2-indifference); (P1), (P2) in the Kasner-exit results are
synthesis.pre-descent-contracting-kasner-stage-premise and synthesis.pre-descent-state-carried-into-descended-phase-premise."
No rename.
F4. $I_6$ against $I_7$ (R10 L2, xsubject-R10 X2): "In the T09 Fock model ($w_3 = b_3 + I_7b_4$, $I_7 = I_6e$),
$I_6 = I_4E$ acts on $\CS$ as $+I_7$; the opposite orientation $a_1a_2b_1b_2b_3b_4$ acts as $-I_7$. A result using the
mass-chart $I_6$ and the T09 scalar $I_7$ together names the orientation."
F5. The tower complexification scalar (R12 4, xsubject-R12 5): "In the tower limit the scalars are span{1, $1\otimes I_4$},
a formal unit in a tensor factor (the floors' odd extensions do not pass to the limit); for the physical ground it is not
the ground's volume element $\gamma_0\gamma_1\gamma_2\gamma_3$." Keep the symbol, written $1\otimes I_4$.
F6. The letter $J$ (xsubject-R03 1, R11 9, ga-issues-R03 1, ga-issues-R05 7): "$J$ is $e_2e_3$ (U2) unless the entity says
otherwise at its first use; other uses: the Schouten trace (tractor and mass entities), the Hodge star (the duality
result), a complex structure on a vector space (CPT, positive-energy, the Hermitian $J = I_7e_1e_+$), a map
(transport.totality); $J_a$ are modular conjugations."
F7. Boost-bivector signs ($B = n\gamma_0$ against $B_k = \gamma_0 n$): already recorded (conventions lines 101 to 104);
nothing to add.
F8. Massive Dirac unit (xsubject-R12 1): "On a massive Dirac line the field theory's unit is the right unit $xI_4$;
Hestenes' unit is the right factor $I\sigma_3 = \gamma_2\gamma_1$. They are not identified; the store relates them only on
massless modes, $L_{I_4} = -\Gamma R_{I\sigma_3}$ (synthesis.massless-frequency-sign-relative-to-i4-is-not-the-chirality (ii))."
F9. Ladder labelling (xsubject-R12 3, R11 dark-matter.two-families): "On the radial atom $v$ annihilates ($N = v^*v$);
on tower planes $v = \tfrac12(e + f)$ creates, so there $N_j - \tfrac12 = -K_j$." Plus a sentence in
synthesis.phase-flow-is-time-rotor-flow-kms-continuation (iii) saying which labelling its $N_j$ uses.
F10. Total parity (R09 7): "Singularity entities write $\Gamma = \prod_k\sigma_k$, $\sigma_k = 2N_k - 1$; descent-lift
entities $\Gamma_k = (-1)^{N_k} = -\sigma_k$; the totals differ by $(-1)^N$ and only $\operatorname{Ad}(\Gamma)$ is used."
F11. $Q$ on non-vectors (R05 11): "$Q(v)$ is for vectors; for other elements of scalar square write $\omega^2$." (fix the
three dark-tower-matter entities at their next revision).
F12. T06 triples (xsubject-R03 2): "T06's flat-model triples list the ($n_0$, $W$, $n_\infty$) components; the tractor
splitting $\sigma n_\infty + \mu + \rho n_0$ has $(1,0,0) = n_\infty$."
F13. Curvature letters in the MacDowell-Mansouri blocks (xsubject-R03 3): "$R$ is the background field strength (literature
sign, $-\mathcal{R}$), $\mathcal{R}$ the store sign; an entity writing $F_W$ names which." Check
dark-energy.imported-macdowell-mansouri-theorem-stelle-west's letter in round 2.
F14. Reduced Planck mass (xsubject-R09 3): "$\bar M_P = M_P/\sqrt{8\pi}$ (quantity.reduced-planck-mass); $M_P$ is the
non-reduced mass." Then fix dark-matter.imported-massless-graviton-production-rate's letter.
F15. Naming the unit (R06 1): "The unit is named ('the unit $I_4$'), never equated with a bare $i$ ('$i = I_4$')." See H1.
Optional, not counted: the two rung-mode labellings and the Majorana sign (known limit 3, R04 10, already recorded); the
seesaw transposition conventions (R10; transpose-invariant bounds).

## G. Stale wording that depends on a decision (all routine once the decision is in)

G1. "The cold mirror is an exception to P2" (R05 2; waits for C1): dark-matter.mirror-tower-copy-one (GA-owned),
dark-matter.open-channels-their-costs, dark-matter.radiation-audit-what-theorem-closes-what, dark-matter.stored-asymmetry-
charge-not-number, dark-tower-matter.mirror-against-record, dark-tower-matter.mirrors-temperature-p2 (correct about T14's
own P2), dark-tower-matter.towers-built, simulations.imported-mirror, pred.no-dark-radiation, note.dark-tower-matter.abstract,
...setting-contribution, ...setting-what-note-depends-what-would. Sentence: R05's ("an exception to P2 at its version-1
reach; P2 as scoped leaves $\xi$ free (synthesis.tower-charge-sector-label-temperature-not), and the cold mirror then needs a
non-equilibrium descent (synthesis.cold-mirror-needs-non-equilibrium-descent)"). Under C1 (a) it stays true.
G2. synthesis.mirror-asymmetry-route-one (iii) and close (R05 3; waits for C1): P2@2 states the scoping it says "no premise
states"; "(iii) ... Premise P2 (version 2) states one, so route one stands at that scope", and the close says clause (v)
has both routes. No assumes edge needed: route two carries (v) without P2.
G3. Hypothesis (S) "not proved / declared and open" (R04 1, 8): families.imported-one-derived-generation-hypothesis-s,
neutrino.imported-derived-content-singlets; dated "Status now" lines in note.standard-model.setting-content-charges-
chirality-2 (also its thirteenth-generator sentence, against standard-model.under-s-composites-state-space-spinor@6 (3)(b)),
note.standard-model.setting-introduction, note.standard-model.setting-successor-problems, note.neutrino.setting-position-series.
G4. The adopted Henneaux-Teitelboim promotion (R07 3; decided 2026-10-23): add "which the store adopts
(programme.n-parameter-of-the-laws)" in standard-model.trichotomy-what-kind-number (4) and standard-model.what (ii); the T10
notes stay as dated paper text.
G5. singularity.sheaf-assembly-sheaf last sentence (R09 2; the 2026-10-23 correction): R09's text ("... its even part,
span{1, sigma}, is untwisted, so M is defined there as well and does not see the twist"); the same in
note.three-routes.setting-metric-level-sheaf.
G6. synthesis.series-wald-entropy-changes-without-flux-on-local-horizons proof (i) (R03 B; the dictionary's bifurcation
rule): "on a cross-section $\{t = t_0, r = r_b\}$ of the horizon locus in the Painleve-Gullstrand chart". On ga2_gravity.txt.
G7. Premise (Q) version labels (R01 2, xsubject-R02 5; Leon's 23 October "note only"): label "$\kappa k$" as "(Q) version 2"
in angle.imported-singularity-papers-state-selection (formal, technical, proof), singularity.bosonisation-bridge-s-wave-sector
((2), (3), technical, proof), synthesis.array-ln2-is-zero-mode-doublet-one-tower (formal, technical),
synthesis.boundary-mode-premises-finite-models, obj.hawking.boundary-mode-algebra-windows-boost-dynamics,
singularity.universality-temperature-under-g (proof); the Planck value holds at both offsets (R01 planck_offset.py). Search
the other subjects for "(Q)'s weights $\kappa k$" in the same pass.
G8. scrambling.return-delay-scrambling-log-recovered: the modular-time sentence (waits for B1).
G9. T03's odd-charge "open" (R12 3): note.tower.abstract, ...setting-scope, ...setting-introduction, ...setting-contribution,
note.tower.what-completion-means-here-why-it: leave the paper text; add a remark note commenting on q.tower.odd-charge that
points to synthesis.tower-limit-forgets-residue.
G10. families.imported-dictionary-exact-join (R10 L4): "$B_\Lambda = 0$ and scalar Gram matrix" -> "$B_\Lambda = 0$ and
$h = 0$", the current mass.exact-join (5).
G11. Setting notes with a superseded step (R05 6, 8; R10 obs.): note.dark-matter.setting-levels-results (the trichotomy
exhaustiveness bracket), note.dark-matter.setting-predictions-collected row 12 ($D = 2 - g/(1+g)$, just below 2),
note.mass.setting-successor-problems (5) (many-twistor now proved): dated brackets only.
G12. synthesis.hadamard-scaling-limit-premise: "Version 4 (this one)" while at version 6 -> "statement version 4". R02 11.
G13. Contradictory or stale extraction notes: standard-model.pair-count-dimension (two 7 November notes, R04 6: annotate the
ga_units one as superseded), singularity.pseudo-inverse-identities-hyperbolic-atom unit_note (R11 9), note.dark-energy.
setting-machine-verification's Chern-Simons letter $Q$ -> CS (xsubject-R09 2; forms-owned, not yet rewritten);
q.tower.odd-charge's typing note stays as history.

## H. Anything else (all routine)

H1. "with $i = I_4$" in about fifteen field-theory entities and two titles (field-theory.mass "Mass with $i = I_4$"; the
unit-i4 title) (R06 1): treat as a bare unit under the unit principle; mechanical fix "with the unit $I_4$". Recommendation:
apply (the unit-i4 entity is widely pinned; a title change needs no content repin).
H2. Overclaims in a formal level: dark-energy.acoustic-no-go-one-way-grip "no other channel" -> "no channel outside the
C-even neutral sector" (R07 4); singularity.non-removability-invariant-argument (a) "invariant under every gauge
transformation" -> R06's scalar wording, (b) $K$ in GA eigenvalue form (R06 5); synthesis.euler-entropy-first-order-rate-
on-local-patches' sign sentence about $\Ric^\circ$ (ga-issues-R03 5; forms-owned, still open).
H3. GA language on entities named by readers but on no rewriter list (GA_OWNED, ga2_gravity, ga2_matrices, ga2.txt):
standard-model.connection-forced (connection forms; R04 gives the GA form), dark-energy.wall-counterterm (forms; with A16),
pairing.two-frames-share-vacuum-selected-transport (Lorentz matrix; R01 4), three-routes.support-preserving-families
(Pauli-string labels; R09 6). Recommendation: add the first three to the gravity round-2 list and the last to the matrices
list. Every other reader-named GA item is on a list.
H4. Forms rewriter: ga-forms.md is absent. 21 of the 26 ga_forms.txt entities carry a maintainer_pass_ga_rewrite note; five
do not (note.dark-energy.setting-machine-verification, pairing.displacement-pairs-point-mode-vacuum-parallel,
synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling,
synthesis.loc-independent-of-clausius-and-killing-data, synthesis.pre-descent-contracting-kasner-stage-premise). Reader issues
on forms-owned entities still open in store: A11, B2, G1 (mirror-tower-copy-one caveat), G13 (CS letter), H2 (Ric° sentence),
synthesis.parallel-frozen-point-on-matter-regions-is-the-field-space-premise (letter $A$ for connection and vector; the
dilation slot $\beta\,n_0\wedge n_\infty$ against $\beta\,n_\infty\wedge n_0$ in two siblings; ga-issues-R03 4),
synthesis.collar-kms-extension-completion-locus (GTG form of proof (i), ga-issues-R01), the W222 index false positives
(ga-issues-R07). Recommendation: get the forms report, or treat these in the maintainer pass.
H5. Notation clashes, one batch at next revision (no content change): $H_+$ label in restricted-dirac against hadamard-dirac
(i) (R02 6; add R02's sentence); $\kappa$ for an operator in n-plus-null-ground-state (R02 8; rename to $\mu$ at the
postulate's next revision, pure notation); $B$, $D$, $Q_k$, $R$ double uses (R02 10); $U$, $\rho$ normalisations and "up to a
phase" (R01 5); $A$ matrix against the pseudoscalar component $A$ (R04 3, rename $\mathcal{A}$); $N$ Hermitian norm against
$N = M_P/H$ (R04 4); $\epsilon$ double in families.rigidity-pairing-sector-one-event; $\gamma$ for the pseudoscalar in
rule2.rule-2-kaluza-klein-algebra; Mat(2, \mathbb{H}) -> \Mat_2(\HH); $e_\mu$ against $e_0..e_3$ in
interior.exact-parallelism-convergence-rate (ga-tensor); the rotor $J$ and vector $\nu$ in normality-on-the-closed-generator
(ga-issues-R02 2); $d\Omega^2$ beside the gauge field $\Omega$ (R03 C); $E$ wording in mass.casimir-form-join (ga-issues-R10 6);
the duality proof's lowercase $i_4$, $i_6$ -> $I_4$, $I_6$ (checked here: $i_6 = e_0\cdots e_5 = I_4E = I_6$ with
$e_4 = e_+$, $e_5 = e_-$, so the rename is sign-safe; this answers ga-matrices "possible error" 4).
H6. Complex-field stand-ins without a named unit ($\C$, $\C^m\otimes\C^n$, $\Mat_n(\C)$, $\mathfrak{so}(2\nu)\oplus\C$):
R02 9, R03 C, R08 5. Add the U1 sentence (or span{1, J} for the radial-atom modes) once per entity; imports keep the source
form under U4.
H7. outside_ga declarations (R11 8): rule2.imported-gamma-matrices-odd-dimension, rule2.imported-graphenes-two-valleys-doubling
(imported); note.rule2.what-planar-obstruction-physically, note.rule2.setting-machine-verification, note.rule2.setting-setting-
what-imported, note.rule2.three-dimensions-matter-below, note.transport.three-dimensions (bridge). All are on round-2 lists.
H8. one-relation.dirac-current-conserved-density (R12, ga-tensor): keep the bridge declaration. A real-bilinear GA statement
changes the class of currents, which U6 forbids; no question for Leon.
H9. GTG proofs for the coordinate curvature computations (ga-tensor "For Leon"): new derivations, not decisions; the
outside_ga declarations stand. Heat-kernel and Sakharov Facts stay declared imported (no store sign for Euclidean curvature
is needed for them).
H10. mass.chart-form-spin-isomorphism has two `source_formal:` keys, the first empty (ga-matrices 1): delete the empty one.
H11. Repins: every reader and rewriter bump with an unchanged statement can be repinned after review (lists in consistency-R01,
R02, R04, R09, R11 and ga-matrices). For A1 to A16, check the dependants' content before repinning.
H12. I213 subject placement (xsubject-R02 6): synthesis.incidence-vacua-entanglement-light-cones-of-unit-diamond ->
conformal-spacetime; synthesis.state-selection-r-and-le-against-t05 -> descent.
H13. note.simulations.setting-introduction-5: empty YouTube links "()" (R05 7): drop the parentheses until URLs are supplied.
H14. R02's incident: seven credit lines differ from the checkpoint commit in quoting only (same YAML value); expect them in the
diff, no action.
H15. Optional postulate wording: singularity.q-joint-quasi-freeness-s-wave "weights symmetric under $k \to -1-k$" means
$\omega_{-1-k} = -\omega_k$ (R01 2); defer to the postulate's next revision (a bump of a widely pinned postulate for no
content change).

## Needing Leon (six; one recommended answer each)

1. C1. P2@2 and the mirror's ceiling coupling: restate P2 as version 3, with the couplings at the ceiling inside its scope.
2. C2. neutrino.real-breaking-assumption: add "the charged-lepton matrix is real in the same basis"; carry it into
   pred.leptonic-cp-trivial.
3. B1. scrambling.spreading-law-chaos-bound-saturated and scrambling.return-delay-scrambling-log-recovered: lower both to
   conjectured; return-delay gets the modular-time sentence.
4. B2. dark-matter.no-coupling-rule-odd-towers-follows: restate the formal to its three established facts and keep it proved.
5. B3. one-relation record chain: enter rem:recording as a postulate with assumes edges from the two record-chain results;
   move overlap-table-sorted's (ii), (iii) and the constants clause into a Reading.
6. B4. sheaf.wall-class: restate clause (a) as the one-rung completion; it stays conjectured.
