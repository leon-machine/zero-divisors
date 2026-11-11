# Consequences of the six proposals of REPORT.md

Leon (11 November 2026, 09:14): "explore the consequences of your proposals further and report back".
Nothing in `store/` is changed. For each proposal: what depends on the entities involved (**graph**), what
the change forces elsewhere, and whether the proposal stands as first written. Exact checks are in
`work/consequences_checks.py` and `work/fs_parallel_tractors.py` (**computed**); the rest is **read**, argued.

Two proposals change after this pass: A2 (a smaller change than first proposed) and A6 (the first proposal
was wrong).

## A1. Uniqueness of the frozen point for the (FS) connection

Blast radius (**graph**). `synthesis.frozen-point-unique-where-weyl-has-no-kernel` and
`synthesis.two-frozen-points-conformally-flat` have empty future cones. P1 is in the holds-given of 108
results, but none of them cites the Weyl condition, so the edit is: one new theorem, P1's status paragraph,
and the "Applied to towers" sentences of the two theorems.

Consequences.
1. *The new theorem contains the stored one.* On an Einstein field at the same $\Lambda$,
   $\mathcal{R} - \tfrac{\Lambda}{3}\mathrm{id}$ is the Weyl part, so the kernel condition is the stored one.
   Nothing proved is lost.
2. *The normalisation stops being a premise.* (FS) asks $\ip{X}{I} = 1$. A second parallel tractor is $cI$,
   and $\ip{X}{cI} = c$, so $c = 1$ (**computed**). P1a today lists three things as still postulated: the one
   connection, the normalisation, the conformally flat regions. Under (FS) only the first remains.
3. *P1c (the common N) becomes a consequence* (**read**). If every tower's frozen point is parallel for the
   one varied connection with unit pairing, the frozen points are equal, so their norms are equal, so
   $\Lambda$ and $N = M_{P}/H$ are common (given one $G$). P1c is recorded today as "postulated, with no
   derivation found", and its remark that a second tower might carry its own norm would go.
4. *Where uniqueness holds.* For a perfect fluid on an isotropic field the de Sitter-subtracted field strength
   has eigenvalues proportional to $\rho + 3p$ (time-space bivectors) and $\rho$ (space-space). No kernel
   vector for dust, radiation or stiff matter; one kernel vector (the time direction) at $w = -\tfrac13$; all
   four at $\rho = 0$ (**computed**). A parallel tractor on a connected region is fixed by its value at one
   point, so one point of ordinary matter anywhere in a connected universe gives uniqueness everywhere. The
   stored theorem needs a point of the Einstein region with a kernel-free Weyl part (a black hole exterior);
   the new one needs any matter at all.
5. *What becomes false.* "The metric clause of P1 is an independent choice on conformally flat regions":
   under (FS) this holds only on a universe that is exactly de Sitter everywhere. The two-frozen-points
   theorem stays true of the normal tractor connection and loses its application to P1.
6. *The mirror* (**read**, to be proved in the theorem). Reversing the sign of the form sends $\rho$ to
   $-\rho$ and $\nO$ to $-\nO$, so $I_{\rho}$ and $u = \nInf - \rho\nO$ are unchanged: the reversed tower
   reads the same connection and the same frozen point. This is the step most worth a referee.
7. *Scope.* Torsion-free fields. With spin torsion the field strength gains a part $u \wedge \tau$, acting as
   $(u \wedge t)\times v = (t\cdot v)u$ (**computed**); the kernel argument then needs a second line and is
   not done here.
8. *Cost.* P1 leans on (FS) where it leaned on nothing. (FS) is exposed to the $w = -1$ rule, so a refuted
   (FS) would return P1a and P1c to bare premises. The 108 results would gain (FS) in their holds-given only
   if you choose to retire P1a/P1c as premises rather than keep them and note the derivation.

Verdict: stands, and is larger than first stated: it can retire two of P1's three clauses to consequences of
"one varied connection" plus (FS).

## A2. The basis of the no-echo prediction

Blast radius (**graph**). The prediction has no dependants. It rests on (C1) and on
`interior.imported-equivalence-einstein-equations`. (C1) stays in the holds-given of 57 results (the
Schwarzschild count), untouched.

Consequences.
1. *The first proposal (rebase on (N$_{+}$)) does not work for the holes that are observed.* (N$_{+}$)'s own
   scope notes say that on Kerr no stationary Hadamard state exists (argued, from superradiance), and that its
   collapse form is proved for the spherical null shell only. A merger remnant is neither.
2. *A smaller change does work.* Under (C$_{\mathrm{loc}}$) the horizon's modes are "the matter field on
   those light rays": no structure beyond the matter fields is placed at the horizon. An echo needs a
   reflecting structure there. So the prediction follows from what is already in its basis, the field
   equations holding up to the horizon, with (C$_{\mathrm{loc}}$)'s identification in place of (C1). Revised
   proposal: drop (C1) from the basis, keep the Einstein equivalence, add (C$_{\mathrm{loc}}$).
3. *What an echo would then refute.* Not a localisation at the cutoff, but the field equations at the horizon
   or (C$_{\mathrm{loc}}$)'s identification: refutation condition (b) of (FS) and (c) of (C$_{\mathrm{loc}}$).
   That exposes 19 and 30 results in place of (C1)'s 57.
4. *The prediction becomes general relativity's own.* Its ledger entry is already "absent". The principles
   file names no-echo among the predictions that make the series defensible; after the change it should be
   described as "no departure from general relativity at the horizon", which the series shares with it.
5. *Deposited text.* T8 and the T17 stance table give the cutoff as the reason; a generated paper would mark
   this as a substantive change from the deposited version.

Verdict: revised as in 2.

## A3. "Obstructions are moved, never destroyed"

Blast radius (**graph**). Empty future cone. Named by `sheaf.wall-class` (lineage and clause (c)) and
`obj.transport.obstruction-types`.

Consequences.
1. *The stored rung-count results already say what survives.* A completion that keeps one exterior model
   moves the degeneracy to a shadow wall (theorem). A completion allowed to change the exterior model exists
   and is paid for in rungs: $k$ planes need $w_{1}(\shL)^{k} = 0$
   (`synthesis.wall-rung-count-is-height-of-dying-line-class`), the class of the dying line is conserved along
   the wall sequence (`synthesis.twisted-wall-induction-conserves-dying-line-class`), and the lens walls need
   two to five rungs. So "never destroyed" survives as "conserved as a class and paid in rungs", not as "no
   completion is nondegenerate".
2. *Part of the conjecture is then answered.* It "asks for the cohomological invariant ... presumably a class
   built from the mod-8 residues". On tame walls the stored pair $W(\Sig) = (w(\Sig), w_{1}(\shL))$ is that
   invariant on one rung: the coarse part is the clock mismatch $2 \in \Z_{8}$. The open part is beyond the
   tame corank-one case and beyond one rung, which is `sheaf.wall-class` (b), (c).
3. *Two conjectures become one question.* After restating, this conjecture and `sheaf.wall-class` ask the
   same thing at fibre and sheaf level; a merge, or a `specialises` link, would say so.
4. *Deposited text.* T1 Conjecture 7.9 carries the unrestricted wording; the generated T1 would mark a
   substantive change.

Verdict: stands; the restatement should use the rung count, as in 1.

## A4. The Kasner exit premises against the dating

Blast radius (**graph**). No assumes edge to either premise; five results and (HD) name them in text;
`store/conventions.md` lists them under "Same names".

Consequences.
1. *Lowering them is bookkeeping.* Postulates 71 to 69, no holds-given list changes, six texts say
   "hypothesis" for "Premise", and the conventions line goes. The stored Kasner results already state (P1)
   as a hypothesis in their formal levels.
2. *It agrees with the decision of 10 November* ("no mechanism" for the primordial spectrum): the Kasner
   results all end blue, so the premises carry no adopted result.
3. *The other direction costs more.* Dropping the dating's reading (iii) would leave
   `synthesis.finite-range-descent-deposit-cannot-seed-cmb` ("initial data of the pre-metric sector") without
   its reading and reopen the stance decided on 10 November.
4. *What is lost.* The premises' refutation conditions would have no entity. They can be kept as a remark on
   `synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching`.
5. *No proved result is involved either way*: `dark-energy.gravity-pre-metric-forces-degenerate-exactly` says
   only gravity and the $\theta$-terms cross a wall, which denies neither side.

Verdict: stands.

## A5. Splitting the dark-to-baryon reduction theorem

Blast radius (**graph**). Empty future cone; cited in the notes of R3, the single-ideal premise and the
population premise. D is in the holds-given of three results; after the split, two.

Consequences.
1. *On the adopted reading the three rules do not reduce.* With R3's unit each tower's own cell radius, the
   shares are $f_{r} = (m_{r}/m_{6})(V_{3}/V_{D_{r}})(a_{6}/a_{r})^{3}$: R1 enters through the mass ratio and R2
   through the radii, separately, and R2 is used twice. So the count in `dark-matter.status-rule` (iv), "rests
   on R1, R2 and R3", is right as it stands, and clause (i) of the theorem becomes a statement about a reading
   the store declines. It is worth keeping as that, labelled.
2. *The other total results already use the adopted reading.* `dark-matter.total-function-thickness` measures
   the thickness in each tower's own cell radius. No other entity needs rewording.
3. *The id.* The id says "r1-r2-and-d". Clause (ii), under D alone, needs its own id; the old id stays with
   clause (i) or is retired through `tombstones.yaml`.
4. *D's note becomes true as written*, and no entity holds given D and R2 together.

Verdict: stands.

## A6. $Q = \epsilon N$

Blast radius (**graph**). `dark-matter.stored-asymmetry-charge-not-number` is used by 11 results, the copy
theorem by 20; the registered premise by none.

Consequences.
1. *The first proposal was wrong.* I proposed $\epsilon = Q/N$ with $Q$ the charge of the de Sitter ball. That
   charge is not constant: inside the fixed radius $1/H$ there are $4.8 \times 10^{78}$ baryons today,
   $3.8 \times 10^{79}$ at $z = 1$ and $6.2 \times 10^{87}$ at recombination (decimal arithmetic, in the
   script). A "temperature-independent charge fixed by the descent's data" cannot be that.
2. *Nor is it a number per mode.* $Q/N = 4.7 \times 10^{17}$ today, above one, which no asymmetry per
   fermionic mode can be; per registered unit it is $10^{-44}$.
3. *What is conserved is the charge per comoving volume.* The record's $8.7 \times 10^{-11}$ is that, measured
   against this tower's entropy as a comoving ruler. Revised proposal: define $\epsilon$ as the charge per
   comoving volume, quoted as $n_{B}/s$ with $s$ this tower's entropy for both towers. The mirror's yield
   against its own entropy is then $\epsilon/\xi^{3}$, which is the stored $\eta' = \eta/\xi^{3}$, so the
   stored numbers are unchanged.
4. *Route one of the copy theorem needs restating.* It argues: $N$ common, so $Q = \epsilon N$ is one label,
   so a difference would be an uncaused distinction. Restated: the tower charge is a sector label on every
   finite window (`synthesis.tower-charge-sector-label-temperature-not` (i), proved), and P1's one metric
   gives the two towers the same comoving regions, so P2 equates the labels of corresponding regions. This
   uses P1a, not P1c.
5. *P1c loses its only use.* Its text says it is used by the charge reading alone. With A1 it would be both a
   consequence and unused, so it could be dropped from P1 rather than rederived.
6. *Unaffected.* The seeding comparisons and the gravitational floor use $8.7 \times 10^{-11}$ as a yield,
   which is what it is. The mirror's share of one, the registered premise's refutation condition and "the
   unexplained numbers are $N$ and $\epsilon$" stand.

Verdict: revised as in 3 and 4.

## Interactions and order

- A1 and A6 both act on P1c: A6 removes its use, A1 derives it. Do A1 first, then decide whether P1 keeps a
  clause (c) at all.
- A1 and A2 both move weight onto (FS). After both, (FS) carries the Einstein equations of the action route,
  the $w = -1$ registration, the uniqueness of the frozen point and part of the no-echo basis, and its
  refutation by the $w = -1$ rule would reach further than today.
- A3, A4 and A5 are independent of the others and of each other.
- No proposal changes the value of any prediction or of any fitted number. Net change to the register: two
  postulates fewer (A4), P1 reduced to one clause plus (FS) (A1, A6), one new theorem (A1), one theorem split
  (A5), one prediction rebased (A2), one conjecture restated (A3).
