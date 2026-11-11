# Revised proposals (after the referee's report)

This file supersedes the proposals of REPORT.md and CONSEQUENCES.md. It takes every finding of
`verify/referee.md` (independent referee, Claude Opus 5.5). Nothing in `store/` is changed. Evidence for the
algebra is the referee's exact scripts in `verify/`; the author's two scripts in `work/` are weaker (the torsion
check there is vacuous and the fluid check does not test the eigenvalue factors) and are not to be reused.

## 1. The frozen point under (FS)

What is wrong in the store. P1a gives its metric clause the status of a theorem "given that every tower's frozen
point is parallel for one tractor connection" and cites two theorems about the normal tractor connection. Under
(FS) the frozen point (unit pairing with $X$ in the physical scale) is not parallel for that connection on
matter regions. P1a does not name the connection, and none of the three entities mentions (FS). It is an
omission, not a logical contradiction. (Correction to REPORT.md: the normal tractor connection does carry
parallel tractors on matter regions; it carries none in the physical scale.)

Proposed changes.
1. *A new theorem*, the (FS) form of the uniqueness result. For a torsion-free field on a connected component
   $U$ of the invertible region of $\hb$, and any $\rho$ (zero allowed), the field strength of
   $A_{\rho} = \Omega - (\nInf - \rho\nO)\wedge\hb^{-1}$ is the Lorentz block
   $-(\mathcal{R} - \tfrac{\Lambda}{3}\mathrm{id})$, $\Lambda = 6\rho$, in the store's sign. If at one point of
   $U$ that operator has no kernel vector, every tractor parallel for $A_{\rho}$ on $U$ is $c\,I_{\rho}$ with
   $c$ constant. Clauses: (i) on Einstein fields at the same $\Lambda$ the condition is the stored Weyl
   condition; (ii) for perfect fluids on isotropic fields there is no kernel vector at $w = 0, \tfrac13, 1, -1,
   -\tfrac23$, one at $w = -\tfrac13$, and on de Sitter at the same $\Lambda$ the field strength vanishes;
   (iii) with torsion $T$ the condition is not sufficient (counterexample on a dust instant) and is replaced by
   injectivity of $(\mu, c) \mapsto (X \mapsto L(X)\cdot\mu - c\,T(X),\ X \mapsto T(X)\cdot\mu)$ at one point.
   Stated hypothesis: clause (ii) uses Einstein's equations to turn matter into field strength. Check: from
   `verify/ref_a1_fs_uniqueness.py`.
2. *P1's status paragraph* names the connection: with every tower's frozen point parallel for the one varied
   connection of (FS), P1a is a theorem up to constants $c_{r}$ on any component containing one point of the
   kind in 1. What stays postulated is unchanged in number: the one connection, and the normalisation
   $c_{r} = \pm 1$. P1c stays a postulate; it is equivalent to that normalisation, given one $G$.
3. *The two stored theorems* keep their statements; their "Applied to towers" sentences are scoped to the
   normal tractor connection, that is to Einstein regions. For the (FS) connection the independent choice of
   `synthesis.two-frozen-points-conformally-flat` exists only on a component that is exactly de Sitter at that
   $\Lambda$.
4. *A remark on the mirror, not a theorem.* The reversed tower reads the same covariant derivative with
   $I' = -I_{\rho}$ (keeping $X$), or the same $I_{\rho}$ after the discrete element $\mathrm{Ad}(I_{4})$,
   which reverses time and space orientation. In its own labels $\Lambda' = -\Lambda$, so $N$ is read with
   $\Lambda = 3\varepsilon H^{2}$. Whether that discrete element bears on P1b (the one Witt flag) is a new
   attack item.

Withdrawn: that the normalisation and the common $N$ follow. Requiring unit pairing with the one $X$ for every
tower's frozen point is the metric clause itself.

Decision for Leon: an optional restatement of P1a and P1c together as one sentence, "(FS) holds for every
tower's frozen point with the one $X$", to which they are equivalent. It changes no content. It would put (FS)
in the holds-given of P1's 108 results, so it ties them to the $w = -1$ rule.

## 2. The no-echo prediction

What is wrong in the store. The prediction rests on (C1) alone and says the quantum structure is "nowhere near
the horizon". Through (C$_{\mathrm{loc}}$) the same modes are on the horizon ("one set described twice"), on
Schwarzschild as well as Kerr, and (C1) is scoped to a Schwarzschild calibration.

Proposed restatement of the prediction's basis, four parts.
1. *The field equations at and across the future horizon*, with an assumes edge to what supplies them: (FS)
   with the stored action, or (C$_{\mathrm{loc}}$) with the Clausius relation as a stated hypothesis. The
   imported Einstein equivalence, the present basis edge, asserts no field equation and is not enough.
2. *The identification clause of (C$_{\mathrm{loc}}$)*: the horizon modes are the matter field on the light
   rays.
3. *A stated reading*: the horizon modes impose no reflecting condition on classical perturbations. This is
   not a consequence of (C$_{\mathrm{loc}}$) as written: its clause (R$_{\mathrm{loc}}$) makes the modes thermal
   before a crossing, and some published echo models obtain a reflectivity from a thermal horizon state (the
   referee cites Oshita, Wang and Afshordi from memory; to be verified before anything is stored).
4. *Regularity of the state across the horizon*: the local form of (N$_{+}$) at the horizon's points, argued at
   leading order, with (HD) if the state is to be part of the basis.

(C1) leaves the basis and stays where it is used, the Schwarzschild count. The sentence "nowhere near the
horizon" goes. The kill consequence becomes: an echo train refutes the field equations at the horizon or the
no-reflection reading, not a localisation.

Withdrawn: that (N$_{+}$) cannot serve on Kerr. Its local form applies there at the same argued strength as
(R$_{\mathrm{loc}}$).

Consequences that stand: the prediction is then general relativity's own (ledger already "absent") and should
be described so; the deposited T8 and T17 wording would be marked as substantively changed.

Decision for Leon: which route supplies the field equations in 1. Recommended: (FS), which is the adopted
action, with (C$_{\mathrm{loc}}$) for 2.

## 3. "Obstructions are moved, never destroyed"

What is wrong in the store. An ambiguity, and a scope error. The conjecture's own sentence ("prove exactly this
for tame corank-one degenerations") fixes the strict reading of "completion", under which there is no conflict
with the wall-class theorem; on a loose reading clauses (2) and (3) of that theorem would be counterexamples.
Separately, its hypothesis is "degenerating tamely", which is the corank-one case that is already proved, while
it says the pattern "is not an artefact of the tame case".

Proposed restatement.
1. "Completion" means a standard completion, $h = G \perp K$ with one signature of $K$ on both exterior regions
   (the wording of `sheaf.conservation-degeneracy-absolute-form`).
2. The hypothesis is replaced, not extended: the conjecture is for degenerations beyond the tame corank-one
   case, where the theorem does not reach.
3. A note records that with the exterior model allowed to change, nondegenerate forms exist and the
   obstruction is paid for in rungs: $k$ planes need $w_{1}(\shL)^{k} = 0$, the class is conserved along the
   wall sequence, and on the lens walls $L^{2n+1}(4)$ the stored counts are $k \ge 4$ on every side for
   $n \ge 2$, $k = 5$ on the definite side of $L^{5}(4)$, $5 \le k \le 6$ on $L^{7}(4)$, and
   $k \ge 1 + \lfloor n/2\rfloor$ in general.
4. A link to `sheaf.wall-class`, which asks the same question at sheaf level.

Before storing: check the wording of T1 Conjecture 7.9 in the deposited paper; the entity has no source text.

## 4. The Kasner premises: withdrawn

There is no contradiction in the store, only the tension both premises already record. Lowering them would
reverse Leon's decision of 1 November to postulate them (`store/open_problems.yaml`). Nothing is proposed. If
that decision is revisited, the changes are: the two premises become stated hypotheses, the open-problem entry
is updated, their refutation conditions move to a remark, and the "Same names" line of the conventions stays.

## 5. Premise D's note and the reduction theorem

What is wrong in the store. D's note says no stored statement of the fitted total has D in its past cone;
`synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball` states the total and holds given D
and R2. That theorem also contradicts itself: clause (i) says "the stored wording does not choose between"
the readings of R3, and its closing paragraph says the fixed-length reading "is not adopted".

Proposed changes (edits, no split).
1. D's note names this theorem as the one exception: an audit that sets the two readings side by side.
2. In the theorem, the sentence "the stored wording does not choose between them" is replaced by R3's present
   choice (each tower's own cell radius), and P4 is dropped from the list of premises its model satisfies.

Optional, for Leon: the split into two entities, which would also make D's note true without the exception.

## 6. $Q = \epsilon N$

What is wrong in the store. Two wordings. The label "the asymmetry per mode" stands beside $Q = \epsilon N$ with
$N = M_{P}/H$, for which no per-mode reading gives a number of at most one ($Q/N$ is about $5 \times 10^{17}$
for the de Sitter ball today). And the registered premise's valuation sentence can be read as
$\epsilon = 8.7 \times 10^{-11}$, which is a yield per unit of thermal entropy, the quantity of the reading that
clause (iv) of the charge result rejects. The stored argument itself is guarded ("the argument uses only that
$N$ is common") and is not touched.

Proposed changes (wording only).
1. In the registered premise: $\epsilon$ is fixed by the measured baryon density; $8.7 \times 10^{-11}$ is this
   tower's yield $n_{B}/s$ today, used as a unit of comoving volume, and is not the value of $\epsilon$. It
   equals the descent's datum only if no entropy is produced in this tower after the descent.
2. Where the equality across the reversal orbit is stated in numbers, it is stated as equal charge per comoving
   volume, $n_{B}' = n_{B}$, never as $n_{B}'/s' = n_{B}/s$.
3. The label "per mode" beside $Q = \epsilon N$ is removed or qualified in the three entities that carry it.

Withdrawn: the restatement of route one through sector labels on comoving regions, and the claim that P1c
loses its use. The sector-label theorem is about boundary-mode windows; identifying them with comoving regions
would be a new premise. It is recorded as an open item, not proposed.

## Smaller items

- `standard-model.dating-descent` (i): "in any $\Lambda$-dominated epoch the age is automatically of order $N$
  Planck times" holds only near the onset of that epoch; reword to the epochal form of `standard-model.what`.
- `pred.dimmed-evaporation-bursts`: "if the four odd towers hold matter" is now the adopted premise.
- `neutrino.double-prediction-sum-predicted-floor`: the $w = -1$ condition it calls unused is now (FS).
- The pinned `contradicts` between Hypothesis (U) and Premise (EW) carries a rationale saying the two formal
  levels are consistent in the eigenvalue reading. Either the link or (U)'s formal level should name the entry
  reading in which they conflict. (Found by the referee.)
- `dark-matter.stored-asymmetry-charge-not-number` (iii): $\eta'$ "from 19 to 26" recomputes to 18.6 to 27.8
  from the quoted $\xi$, and "about 0.008" to 0.0095 (decimal; consistent if the floor is near
  $2.85 \times 10^{-4}$). (Found by the referee.)
- Dropped: the trichotomy item of REPORT.md B2, which the stored text already covers.

## What the revised set amounts to

One new theorem (1), one prediction rebased (2), one conjecture restated (3), and wording edits to about a dozen
entities (1, 5, 6 and the smaller items). No postulate is added, retired or re-typed; no status changes; no
prediction or fitted number changes value.
