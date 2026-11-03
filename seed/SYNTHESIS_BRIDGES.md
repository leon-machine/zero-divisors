# Synthesis: cross-subject bridges

**Status (21 October 2026).** Bridges 1, 3 and 4 accepted into the store after an
independent review and its wording fixes; bridge 2 (the de Sitter temperature)
was then proved at Leon's request (21 October, late): the cosmological horizon's
completed pair and boundary-mode algebra were built, (R) transplanted as the
premise (R_Lambda), and the temperature follows under (P) and (R_Lambda); the
mirror and status clauses are a separate corollary.


Session synthesis-bridges-2026-10-21. Angle: pairs or small sets of results in
different subjects that share structure, combined into a statement the store
does not contain. Four candidates are filed as proposals (three proved, one
conjectured); four further candidates were killed, all on novelty. Every
proved candidate has a `check.py` (exact arithmetic, imports GA.py, reaches its
premises only through `premise()`), run in this workspace, in the evidence
sandbox, and under the evidence layer's mutation test. Scratch scripts and
drafts are in
`/tmp/claude-0/-home-claude/f5c21aa3-33bd-54d7-a8e9-4d9b5d6a3726/scratchpad/synth-1/`.

| # | proposal id | subjects bridged | classification | check |
|---|---|---|---|---|
| 1 | `synthesis.de-sitter-static-boost-frozen-point` | dark-energy, mass, thermality | proved | pass (mutants: 2 of 8 survive) |
| 2 | `synthesis.de-sitter-temperature-frozen-point-norm` | thermality, dark-energy | conjectured | none (no finite reduction) |
| 3 | `synthesis.oriented-causal-towers-mirror-pair-every-window` | dark-matter, clifford-structure, zero-divisors, quantum-fields | proved | pass (2 of 8) |
| 4 | `synthesis.wick-rotor-chiral-angular-rotor` | thermality, quantum-fields, conformal-spacetime | proved | pass (1 of 8) |

All four pass `validate_draft` (layers 1, 2, 3 and 5) with no error or warning
on the new entity; the only findings are information notes (I213, a bridging
result's neighbours sit in other subjects, which is the point; I305, the
store-wide re-confirmation count).

---

## 1. The cosmological horizon's boost is the frozen point's time translation

**Bridge.** The frozen point of the mass and dark-energy papers (its norm is
$\Lambda/3$) and the plane-and-rate of the singularity paper (the boost plane
and its surface gravity are the one conversion factor the Hawking temperature
needs).

**Statement** (proposal `synthesis.de-sitter-static-boost-frozen-point`,
subject dark-energy). In T11's conventions ($\ip{\nO}{\nInf} = 1$,
$X(x) = \nO + x - \tfrac12 Q(x)\nInf$), let $I_\Lambda = \nInf + \tfrac{\Lambda}{6}\nO$
and $W = \nInf - \tfrac{\Lambda}{6}\nO$ (T10's $W = V/\ip{V}{V}$, so
$\ip{W}{I_\Lambda} = 0$, $Q(W) = -\Lambda/3$). Put $B_\Lambda = e_0\wedge W$. For
every real $\Lambda$:

1. $B_\Lambda$ lies in the stabiliser of $I_\Lambda$ and
   $B_\Lambda^2 = \ip{I_\Lambda}{I_\Lambda} = \Lambda/3$.
2. Its Killing field $\xi = X\cdot B_\Lambda$ is tangent to the cone, has
   $Q(\xi) = (1 + \tfrac{\Lambda}{12}Q(x))^2 - \tfrac{\Lambda}{3}x_0^2$, and on the
   static slice has physical norm $1 - \tfrac{\Lambda}{3}R^2$ ($R$ areal): it is
   the static time of the observer at the origin.
3. For $\Lambda > 0$: horizon at $R_h = \sqrt{3/\Lambda}$, surface gravity
   $\kappa_\Lambda = \sqrt{\Lambda/3}$, so $\kappa_\Lambda^2 = B_\Lambda^2 = \ip{I_\Lambda}{I_\Lambda}$;
   $B_\Lambda = H u$ with $u = e_0 e_W$ a unit ambient boost in the plane of
   $e_0$ and the unit Stelle-West direction. The flow's fixed set is the
   bifurcation sphere $\{x_0 = 0,\ Q(x) = -12/\Lambda\}$, where its linearisation is
   $H$ times the unit boost of the normal plane. The Euclidean static patch is
   smooth iff imaginary time has period $2\pi/\sqrt{\ip{I_\Lambda}{I_\Lambda}}$
   (the counterpart of the $8\pi M$ of T05 Prop 7.18).
4. The sign of the norm sorts the flow: boost with horizon ($\Lambda > 0$), null
   rotation $B_0 = e_0\nInf$, $B_0^2 = 0$, no horizon ($\Lambda = 0$), rotation with
   closed static time ($\Lambda < 0$).
5. Under $Q \mapsto -Q$ (the mirror's $(4,2)$ tractor metric) $\ip{I}{I}$ flips
   sign and $B_\Lambda^2$ does not: the convention-free identity is
   $\kappa^2 = B_\Lambda^2$.

**Premises.** `mass.de-sitter-scale-frozen-point@2`,
`dark-energy.stelle-west-vector-frozen-point@2`,
`singularity.imported-surface-gravity-redshifted-acceleration@1`,
`singularity.euclidean-section-period@2`. Holds given: nothing (none of the
four has postulates in its past cone). Lineage: motivated by
`singularity.plane-rate`, `odd-extensions.translation-bivectors-frozen-point`,
`odd-extensions.two-towers-one-curved-universe`.

**Novelty.** `find_text` finds no "Gibbons", "static patch", "cosmological
horizon" surface gravity or "de Sitter temperature" result. Closest:
`dark-energy.stelle-west-vector-frozen-point`(iv) has the commutators
$[e_a\wedge W, e_b\wedge W] = (\Lambda/3)e_a\wedge e_b$ but not the square of
$e_0\wedge W$ or its reading as the static boost;
`odd-extensions.exceptional-algebra-residue-completion-both-sides`(ii) and
`dark-energy.under-action-written-norm-parameter-laws`(i) state
$H^2 = \ip{I}{I}$ as the Hubble rate; `standard-model.what`(i) says no paper
applies the boundary-mode method to the cosmological horizon. The
identification of the horizon's boost, its fixed set and its surface gravity
with the frozen point's stabiliser and norm is not in the store.

**Derivation sketch.** $e_0 \perp W$ and both are orthogonal to $I_\Lambda$, so
$B_\Lambda$ is a 2-blade commuting with $I_\Lambda$ and
$B_\Lambda^2 = -Q(e_0)Q(W) = \Lambda/3$. With $\ip{X}{e_0} = x_0$ and
$\ip{X}{W} = 1 + \lambda Q(x)/2$ ($\lambda = \Lambda/6$),
$\xi = x_0 W - (1 + \lambda Q/2)e_0$, giving $Q(\xi)$; $g = \sigma^{-2}\eta$ with
$\sigma = \ip{X}{I_\Lambda}$ gives the static norm $1 - 2\lambda R^2$. The surface
gravity is $|f'(R_h)|/2$ (the imported Fact), and the Euclidean-period argument
of T05 Prop 7.18 uses only $f(R_h) = 0$, $f'(R_h) \neq 0$.

**Check.** `check.py::check_static_boost` (and the 90-check scratch script
`check_ds_boost.py`), in $\Cl(2,4)$ over Fraction: (1) and (5) at eight values of $\Lambda$ of both
signs and zero, in both forms; (2) on a $3 \times 5^4$ product grid, which proves
the polynomial identity (degree at most 2 in $\lambda$, 4 in each coordinate);
the static-slice norm at six radii and four $\Lambda$; the horizon data at three
rational $H$; the vanishing and exact Jacobian at three bifurcation spheres.
**Pass.**

**Classification.** Proved here.

## 2. The cosmological horizon's descent temperature (conjectured)

**Statement** (proposal `synthesis.de-sitter-temperature-frozen-point-norm`,
subject thermality, status conjectured). If the boundary modes of the
cosmological horizon carry a completed pair satisfying hypotheses (i) to (iii)
of `singularity.modular-descent`, and premise (R)
(`singularity.r-regularity-fixed-locus`) is transplanted to that horizon, then
the descended state is thermal at
$T_\Lambda = \kappa_\Lambda/2\pi = \sqrt{\ip{I_\Lambda}{I_\Lambda}}/2\pi = \sqrt{\Lambda/3}/2\pi$
(Gibbons-Hawking), with three consequences: $\beta H = 2\pi$ in Hubble time,
against $\beta_{\mathrm H} = 6\pi$ at the Schwarzschild exceptional set
(`singularity.modular-flow-boundary-modes-holonomy-universal`(ii)); the same
temperature for this world and the mirror (candidate 1, clause 5); and the
conversion factor that `singularity.rate-rigidity-temperature-not-algebra-intrinsic`
says the algebra cannot supply is here the frozen point's norm, a parameter of
the laws under the action as written
(`dark-energy.under-action-written-norm-parameter-laws`), so $T_\Lambda$ is
undetermined within the series exactly as $\Lambda$ is.

**Premises / lineage.** Motivated by `singularity.modular-descent`,
`singularity.r-regularity-fixed-locus`,
`singularity.rate-rigidity-temperature-not-algebra-intrinsic`,
`singularity.euclidean-section-period`, `mass.de-sitter-scale-frozen-point`,
`dark-energy.under-action-written-norm-parameter-laws`, `standard-model.what`,
and candidate 1 (named in the text; lineage cannot point at an unaccepted
proposal).

**Novelty.** As for candidate 1; the store has no temperature for any horizon
other than Schwarzschild's.

**Why not proved.** The series constructs no boundary-mode algebra for the
cosmological horizon, and (R) is stated for the Schwarzschild boundary modes
only. The rate is proved (candidate 1); the thermality is the unproved step.
No finite exact computation decides it, so no check is attached.

**Classification.** Conjectured.

## 3. In every dimension the oriented causal towers are the mirror pair {2, 6}

**Bridge.** The flag/family structure of the dark-matter paper (T14 Prop 3.9,
Thm 3.10), the sign of $\omega^2$ (T01 Lem 2.7), the type-C residues of the
Rule 2 note, and the field theory's pseudoscalar unit.

**Statement** (proposal
`synthesis.oriented-causal-towers-mirror-pair-every-window`, subject
dark-matter). Call a tower of signature $(p,q)$, $n = p + q$, *oriented* if a
Witt pair of its complexified conformal ambient $(p+1, q+1)$ lies in opposite
families (by `dark-matter.two-families-are-two-chiralities`, iff
$n \equiv 0 \pmod 4$), and *causal* if $\min(p,q) = 1$. Then in every dimension,
with no choice of representatives or window:

1. oriented and causal forces residue $2$ or $6$; in each $n \equiv 0 \pmod 4$
   exactly $(1, n-1)$ and $(n-1, 1)$ qualify, with residues $\{2, 6\}$, a
   mirror pair;
2. the self-mirror residues $0, 4$ never host an oriented causal tower, and
   every signature of residue $0$ or $4$ has $\omega^2 = +1$ (no pseudoscalar
   unit; chirality a real splitting of the even subalgebra);
3. every oriented causal tower has $\omega_n^2 = \omega_{n+2}^2 = -1$, $\omega_n$
   commutes with the ascended plane and is central in the even subalgebra (the
   properties of $I_4$), and its spacelike extension $\Cl(p, q+1)$ is type C.

So the conclusion of `dark-matter.which-towers-can-carry-arrow` (holds given
P2, P3) that the oriented causal towers are this one and the mirror holds, as
a statement about residues, without P3.

**Premises.** `dark-matter.two-families-are-two-chiralities@2`,
`transport.sign@2`, `odd-extensions.imported-conformal-completion@3`,
`rule2.where-obstruction-sits-commuting-square@3`,
`field-theory.where-each-lives@2`. Holds given: nothing.

**Novelty.** `which-towers-can-carry-arrow` and
`flag-bit-exists-exactly-tower-dimension` reach the oriented-and-causal sort
only at the P3 representatives, and `towers-are-residues-single-clock-filter`(iii)
shows the sterile set moves with the window; no result states that the
oriented causal pair is window-independent, and `find_text` finds no
treatment of $(1,7)$, $(7,1)$ or "every window". The coincidences
"self-mirror even residue iff $\omega^2 = +1$" and "oriented causal iff
spacelike extension type C" are not stated either.

**Derivation sketch.** Orientation depends on $n$ alone (Step 1). Causal
signatures have $p - q = \mp(n-2)$, and $n \equiv 0 \pmod 4$ gives
$n - 2 \equiv 2 \pmod 4$, hence residues $\{2, 6\}$ (Step 2). $\omega^2$ by T01
Lem 2.7; type C by the Rule 2 note's Thm 2.2(a).

**Check.** `check.py::check_oriented_causal`: the family bit computed
*directly* on every conformal ambient for $n = 2, 4, 6, 8$ (all signatures,
ambients up to dimension 10) from a complex Witt basis over the Gaussian
rationals (`GA.QI`), whose canonical relations it verifies, as the ratio of the
pseudoscalar's eigenvalues on the null blade and the top state; the oriented
causal signatures found are exactly $(1,3), (3,1)$ and $(1,7), (7,1)$;
$\omega^2$ for every signature with $n \le 12$; the residue arithmetic for every
$n \equiv 0 \pmod 4$ up to 64; clause 3 on the four signatures. This extends
T14's own check (split forms of dimension 4, 6, 8) to the Lorentzian-type
ambients and to $m = 5$. **Pass.**

**Classification.** Proved here.

## 4. With the conformal spinors' unit, the Wick-rotated boost is the angular rotor on each chiral half

**Bridge.** The Euclidean rotor of T05 (Prop 7.21: no real rotor of
$\Cl(1,3)$ realises the Euclidean rotation; the angular member $I\sigma_r$ rotates
along the sphere, not around it), the state-selection note (Prop 5.2: the
Euclidean rotation is the angular member $\exp(\theta I\sigma_r/2)$), and the field
theory's units ($I_6 = I_4E$, $\CS = L_0 \oplus L_\infty$ with $I_6 = \pm I_4$).
The two thermality texts read differently; this bridge locates where each is
right.

**Statement** (proposal `synthesis.wick-rotor-chiral-angular-rotor`, subject
thermality). With $i = I_6$ (the complex unit of $\CS$):

1. $I_6\sigma = E\,(I_4\sigma) = E\,e_2e_3$, a real 4-blade of $\Cl^+(2,4)$ of
   square $-1$, so $R^W_\theta = \exp(\theta I_6\sigma/2) = \cos(\theta/2) + \sin(\theta/2)E\,e_2e_3$
   is a real even element, period $4\pi$;
2. $R^W_\theta = \tfrac12(1+E)R_\theta + \tfrac12(1-E)R_{-\theta}$ with
   $R_\theta = \exp(\theta e_2e_3/2)$ the angular rotor: on $L_0$ the continued
   boost is the real angular rotor, on $L_\infty$ its inverse, the sense set by
   the chirality (the relative sign of $I_6$ and $I_4$);
3. $R^W_\theta$ is not a rotor ($R\tilde R = \cos\theta + \sin\theta\,E e_2e_3$) and for
   $\theta \notin \pi\Z$ does not map vectors to vectors: T05's clause (3) stands
   for vectors and every real holonomy (so kill condition K1.3 of the pairing
   note is unaffected), while state-selection's identification holds on each
   chiral half of the conformal spinors, up to the orientation sign.

**Premises.** `singularity.euclidean-rotor-where-it-lies@2`,
`state-selection.euclidean-partner-curvature-selected@2`,
`field-theory.where-each-lives@2`, `odd-extensions.imported-conformal-completion@3`.
Holds given: nothing. Lineage: motivated by
`note.pairing.setting-two-claims-kill-conditions-fixed-3` (K1.3).

**Novelty.** No `I_6\sigma`, `E e_2e_3` or chiral reading of $R_{i\theta}$ in the
store. The I4 pass deliberately kept a bare $i$ in Prop 7.21 because $i = I_4$
would contradict its clause (3); this candidate uses $I_6$, not $I_4$, and is
consistent with clause (3).

**Derivation sketch.** $E$ commutes with $\sigma$ and $e_2e_3$, $I_4\sigma = e_2e_3$,
so $I_6\sigma = E e_2e_3$ and $(E e_2e_3)^2 = -1$; multiply by the idempotents
$\tfrac12(1\pm E)$; the reverse of a 4-blade is itself, and the cross term of the
conjugate of $e_2$ is $\sin\theta\,E e_3$, of grade 3.

**Check.** `check.py::check_wick_rotor`: every identity in $\Cl(2,4)$ over
Fraction at four rational points of the circle, the idempotents, the inverse,
the failures of $R\tilde R = 1$ and of vector preservation, the rotor property
of $R_\theta$ and its fixing of $e_0, e_1$, and the periods at $\pi, 2\pi, 4\pi$.
**Pass.**

**Classification.** Proved here.

---

## Killed candidates

All killed on novelty: each combination turned out to be in the store
already. None was killed by a failed check.

- **Rule 2 reading of the de Sitter ascent.** For $\Lambda > 0$,
  $\Cl(I^\perp) \cong \Cl(1,4)$ is the spacelike type-C obstruction of residue 6,
  $e_I$ its opposite-sign Rule 2 repair, and the Rule 2 ladder pair
  $\tfrac12(e_I \pm e_V)$ is the chart's $(\nInf, \nO)$ rescaled. Already
  carried by `odd-extensions.four-extensions-oriented-pair` (doubled
  $= \Cl(1,3)\oplus\Cl(1,3)$), `odd-extensions.two-towers-one-curved-universe`(iii)
  ($e_5 = \pm\omega'$ on the summands), `odd-extensions.line-tame-wall`
  (canonical null frame $I = aI_0 + b\varphi$, $2ab = \Lambda/3$) and
  `note.odd-extensions.two-bits-compared`; the Rule 2 name adds no content. Not
  checked.
- **Capacity deficit as a tower invariant.** $r_\C - r_\R = \lfloor |p-q|/2 \rfloor$
  is constant along every tower, generalising the "third pair needs a unit" of
  `dark-tower-matter.pairs`. Immediate from
  `one-relation.two-capacities-three-consequences`(2) (both capacities rise by
  one per rung).
- **Pair count meets flag bit.** $(n+2)/2$ odd iff the flag bit exists is
  already the "$m$ odd" clause of `dark-matter.flag-bit-exists-exactly-tower-dimension`.
- **The two ordering shifts.** The families' light-pair floor
  (`families.skeleton-rank-one-plus-ordering-shift`(2)) and the twistor
  homogeneity offset (`hawking.homogeneity-ordering-shift`) share the
  half-commutator per mode; the families paper already marks the identification
  as a reading, and combining them yields no new statement.

## Notes for the maintainer

- Candidates 1, 3 and 4 hold given nothing; all their premises have empty
  "holds given". Candidate 3's main value is removing P3 from the
  oriented-and-causal sort.
- Candidate 1 ledger: it uses `mass.de-sitter-scale-frozen-point`, which the
  build classes essential.
- Candidate 4 changes no stored result; it suggests a remark on
  `singularity.euclidean-rotor-where-it-lies` and
  `state-selection.euclidean-partner-curvature-selected` noting that the two
  readings agree on each chiral half of $\CS$ when $i = I_6$.
