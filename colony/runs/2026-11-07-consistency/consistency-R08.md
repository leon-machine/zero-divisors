# Consistency read R08: entropy and generations

Reader R08, 7 November 2026. 191 entities (entropy 116, generations 75: 143 claims, objects and
predictions, 48 notes). Read in full, line by line, in dependency-ordered batches: the formal level
and one-liner of all 143 claims, objects and predictions; every proof of every derivation (all 335 KB,
with its uses, assumes and pins); the full text of all 48 notes. Technical and lay levels were read for the entities below
and otherwise scanned for stale or overclaiming phrases (saturation, curved spacetime, convention
words, house style), not read line by line. Exact computations are in
`/tmp/claude-0/-home-claude/23cbb9be-73ca-5537-8211-47496476158a/scratchpad/r08/work/` (`qf_phase.py`,
`rs_face_action.py`, both on `lib/GA.py`, exact arithmetic).

## Fixed (maintainer bookkeeping: credit, `maintainer_pass_consistency` note)

- synthesis.real-structure-breaks-source-stabiliser-to-z2: v3 -> v4. Proof (ii): the intermediate
  expression for the face action of $I_4R_n$ read $\overline{(-I_4)}\cdot I_4R_n\cdot(-1)\cdot(-1)$, which
  equals $-R_n$; replaced by $\overline{I_4^3\det R_n}\,I_4R_n = \overline{I_4}\,I_4R_n = R_n$. Exact check
  (Cl(1,3), $a = 1, \tfrac23$): $\det(I_4R_n) = I_4$, $N(I_4R_n) = R_n$, old intermediate $= -R_n$.
  Formal statement right and unchanged.
- synthesis.counted-unit-energy-at-half-offset: v2 -> v3. Proof (i): bare unit `(iy/2\pi)` written
  $(I_4y/2\pi)$ with the theta functions' numbers in span{1, I_4} (missed by the unit pass and by the
  detector).
- synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase: v3 -> v4. Proof (i):
  the Pauli-matrix reading $\tfrac{a+d}{2}\mathbb{1} + \mathbf{h}\cdot\boldsymbol{\sigma}$ written as the
  Cl(3,0) paravector $\tfrac{a+d}{2} + h$, $h = \operatorname{Re}b\,e_1 - \operatorname{Im}b\,e_2 +
  \tfrac{a-d}{2}e_3$, trace $2\langle\cdot\rangle_0$ (pure notation).
- note.families.setting-gaussian-theorems: v2 -> v3. Cross products $[p\times q]_\times$,
  $f_+\times f_-$, $u'\times f_+$ written as duals $-I_f(p\wedge q)$ etc., the notation of the
  rigidity proof (pure notation).
- synthesis.sds-clausius-fixes-area-constant: v4 -> v5. Proof (iv): states that $Q(I_\Lambda) =
  \Lambda/3$ holds in the normalisation $n_0\cdot n_\infty = +1$ the check uses, and is $-\Lambda/3$ in
  T01's $-1$ (the two normalisations of conventions.md).
- synthesis.de-sitter-entropy-pi-n-squared (v6, one-liner only): $Q(I)$ -> $Q(I_\Lambda)$ (bare $I$
  read as the pseudoscalar).
- synthesis.de-sitter-mode-count (v3, one-liner only): same.

tp check (layers 1-3) after the edits: no error or warning on these entities (one E111 from the
Cabibbo edit, `\cdoth`, fixed in place).

## Known open items settled

- synthesis.quadratic-flows-cannot-thermalise-descent (ii), coherence-phase sign: the proof is right,
  the formal is not. With $\alpha_t = \operatorname{Ad}(e^{JtH})$, $H = \sum_j\omega_jN_j$, exact check in
  Cl(4,2) ($J = g_1g_2$ commuting with the modes, Cayley phases): $\alpha_t(a_j) = e^{-J\omega_jt}a_j$,
  $\alpha_t(a_j^*a_i) = e^{-J(\omega_i-\omega_j)t}a_j^*a_i$, $\alpha_t(a_ia_j) = e^{-J(\omega_i+\omega_j)t}a_ia_j$.
  So for the proof's $C_{ij} = \omega(a_j^*a_i)$ (and $C \mapsto UCU^*$, $U = e^{-Jtk}$) the coherence
  acquires $e^{-J(\omega_i-\omega_j)t}$; the formal's $e^{+J(\omega_i-\omega_j)t}$ holds only for
  $C_{ij} = \omega(a_i^*a_j)$, under which $C \mapsto UCU^*$ with that $U$ is false. The pairing sign
  agrees. Formal mathematics: listed for Leon (item 1).
- synthesis.real-structure-breaks-source-stabiliser-to-z2 (ii), intermediate expression: wrong sign
  (gives $-R_n$), fixed above.

## For Leon

1. synthesis.quadratic-flows-cannot-thermalise-descent, formal (ii). Evidence: above. Proposed fix:
   replace "multiplies the coherence $C_{ij}$ by $e^{J(\omega_{i} - \omega_{j})t}$" by "multiplies the
   coherence $C_{ij} = \omega(a_{j}^{*}a_{i})$ by $e^{-J(\omega_{i} - \omega_{j})t}$" (version 3). Also:
   its `maintainer_pass_ga_units` note says the $i$'s were kept and declared, which the later
   `maintainer_pass_resolve_units` reversed; propose prefixing that note "Superseded by
   maintainer_pass_resolve_units:".
2. scrambling.spreading-law-chaos-bound-saturated and scrambling.return-delay-scrambling-log-recovered:
   status `proved`, but the content is an order-of-magnitude estimate ($\sim$, $\approx$, "Tier,
   declared", "the standard doubling estimate") and both proofs are only "Follows from ..., as the
   source states". Further, return-delay gives a real-time return delay from pairwise operations
   spreading over the window, which the rate model's own premise (L$_E$) excludes:
   singularity.l-boundary-mode-locality says the real-time spreading law is not realised under it and
   the scrambling time is a modular-time statement, and synthesis.number-diagonal-dynamics-spreads-nothing
   proves it. Proposed: status `conjectured` (or an argued level) for both, and in return-delay's
   formal add "Under (L$_E$) this is a modular-time (rotor-flow) estimate, not a real-time delay
   (\claimref{singularity.l-boundary-mode-locality})", with a `flow_note` (rotor) like spreading-law's.
3. scrambling.area-law-test, formal: "the count reproduces the Bekenstein-Hawking entropy, coefficient
   included" is the 1-nat reading, which scrambling.residue-each-convention (iii) says credits each
   mode with more entropy than it can hold. Proposed: append "(in the 1-nat convention; with each mode
   credited its $\ln 2$ the condition is $\nu\Delta t = M/(2\ln 2)$, Proposition
   \claimref{singularity.area-law-test})", as the one-liner already says. Near-duplicate of
   singularity.area-law-test in the other convention; the singularity one is the one with physical
   content.
4. synthesis.kerr-ring-count-misses-area-law: formal written in metric and coordinate language
   ($g = \eta + 2H\,k\otimes k$, signature $(-,+,+,+)$, coordinate forms); and $z = r - Iau$ uses an
   unnamed unit $I$. Proposed: state the field as the Kerr-Schild gauge field $\hb(a) = a + H(a\cdot k)k$
   (gtg-dictionary C2), keep the metric as a parenthetical reading, and name the unit of $z$ as
   synthesis.kerr-ring-double-cover-data does. Not a pure notation change, so not done.
5. Unit statements on abstract Hilbert spaces: $\C^{m}\otimes\C^{n}$ appears without "numbers read in
   span{1, I_4}" in synthesis.eviction-deficit-against-page-deficit (formal),
   synthesis.imported-haar-average-purity, synthesis.imported-haar-moments-of-random-pure-state,
   synthesis.eviction-keeps-one-replica-saddle (iii); singularity.l-stabiliser-tangent reads its scalars
   in span{1, J} but writes $\mathfrak{so}(2\nu)\oplus\C$ and $\mathrm{Spin}(2\nu,\C)$. Proposed: add the
   U1 sentence (or span{1, J} for the radial-atom modes) once per entity; the imports keep their
   source's form under U4.
6. synthesis.slot-module-light-ray-arrays-are-weyl-components (GA-owned): see ga-issues-R08.md.

## Duplicates

None exact. Near-duplicates kept for good reason: scrambling.area-law-test and
singularity.area-law-test (two conventions; prefer the singularity one, item 3);
synthesis.eviction-keeps-one-replica-saddle and its generalisation
synthesis.eviction-keeps-one-of-catalan-many-replica-saddles (the first carries the weight and Haar
clauses); synthesis.imported-haar-average-purity is the $n = 2$ case of
synthesis.imported-haar-moments-of-random-pure-state. The `families.imported-*` proved entities and
neutrino.imported-indifference-faces-democratic-alignment-rank are restatements (marked by the tools).

## Checked and found consistent (selection)

Causal-epoch integral and expansion; slice volumes and $\kappa_s = \nu\lambda^{-1/2}$; Kasner and
Schwarzschild frame curvatures $(2,-1,-1,-1,-1,2)$ in the store sign; Euler-term numbers (0, $-4$, $-1$,
$-4$, Euclidean actions); SdS Clausius bounds; Page-deficit bounds; Catalan gap and its $n \to 1$
limit $\tfrac12$; envelope witness $\rho_{L_2} = \mathrm{diag}(5968, 9657)/15625$; pairing-sector
adjoint spectrum $\pm\sqrt{cd}$; number-diagonal evolution $v_je^{-2JtH_1}$; Koide crossing, $K$,
$x^*$; Koide angle, nullity, Fourier form; skeleton spectrum and trace; cumulant bounds;
$\varepsilon$-form of the particle-hole map; channel-phase orbit and denominator bounds; QED shift
$\kappa = 3\alpha/2\pi$; asymptotic-freedom bounds; Kerr volume rate and examples. Boost-bivector,
phase-flow and KMS signs agree with conventions.md in every entity that uses them.

## Counts

Entities read 191; fixed 7 (5 with a version bump, 2 one-liner only); For Leon 6 items (5 entities
with proposed formal or status changes); duplicates 0 exact (3 near pairs noted); known open items
in this subject settled 2 of 2; cross-subject items 1 (xsubject-R08.md); GA issues on GA-owned
entities 2 (ga-issues-R08.md). tp check runs used: 1.
