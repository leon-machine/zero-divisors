# Referee report: run 2026-11-11-contradictions (REPORT.md A1 to A6, B, C; CONSEQUENCES.md)

Referee: independent, adversarial. Nothing under `store/`, REPORT.md or CONSEQUENCES.md was edited.
Scripts written here (all exact unless labelled decimal), run from this folder:

- `ref_a1_fs_uniqueness.py`: 53 checks, 0 failures. Pointwise algebra of $A_\rho$ in $\Cl(2,4)$; field
  strength of $A_\rho$ computed from jets (lib/gtg.py) on de Sitter, six FLRW fluids and Schwarzschild; kernel
  ranks; the mirror in $\Cl(4,2)$ under two renormalisations of the null pair; a torsion counterexample.
- `ref_a3_signatures.py`: 12 checks, 0 failures. Signature bookkeeping of clauses (1) to (3) of the wall-class
  theorem on a transversal model (GA.congruence_signature).
- `ref_a5_a6_numbers.py`: A5 totals exact (as $a + b/\pi$, $a, b \in \mathbb{Q}$), 10 checks, 0 failures; A6
  numbers in decimal arithmetic (order of magnitude only, labelled).
- `perturb/`: four perturbed copies of the author's two scripts (see A1).

Labels: **computed** (exact script), **read** (from the store, quoted), **argued**, **could not check**.

---

## A1. The frozen point and two connections

### (1) Is the contradiction real? Partly.

The report's central factual sentence is wrong as worded: "in a universe with matter the normal tractor
connection has no parallel tractor on the matter regions". The store itself says otherwise.
`synthesis.parallel-frozen-point-on-matter-regions-is-the-field-space-premise` v3, clause (iii) (**read**):
"Off the Einstein region transport can still carry parallel tractors whose own scale is not the physical one.
For the dust field ... the functions $\sigma = c\,\tau^{2} + h\,\tau^{3}$ are the first slots $\ip{X}{I}$ of
$D^{T}$-parallel tractors". More generally every FLRW field is conformally flat, so its normal tractor
connection is flat with a six-dimensional space of parallel tractors (**argued**, and consistent with my
computation that the stored Weyl kernel condition fails identically on FLRW). The correct statement is
clause (ii) of the same entity: "transport keeps no frozen point parallel in the physical scale wherever
$T \neq 0$".

With that correction there is a real tension, not a logical contradiction. P1a (**read**): "a theorem up to a
common normalisation wherever the Weyl tensor has no kernel vector, given that every tower's frozen point is
parallel for one tractor connection". The cited theorems are about $\Omega_T$
(`synthesis.frozen-point-unique-where-weyl-has-no-kernel` v6: "$\nabla$ is the $\Cl(2,4)$ gauge field
$\Omega_{T}$"). (FS) says (**read**): "for the normal tractor connection, preserving a tractor in the physical
scale is the Einstein condition". So under (FS) the frozen point (unit pairing with $X$ in the physical scale)
is not $\Omega_T$-parallel on matter regions, and P1a's conditional status sentence, read with $\Omega_T$, has a
hypothesis that (FS) denies there. P1a never names the connection, so the defect is one of omission. I
confirmed by reading that P1, the uniqueness theorem and the two-frozen-points theorem do not mention (FS).

### (2) Verdict on the proposal: SOUND WITH FIXES (new theorem); consequences 2, 3 and 6 OVERSTATED.

The new theorem is correct (**computed**, independent route):

- $(u\wedge A)\times(u\wedge B) = 2\rho\,A\wedge B$; $A_\rho\times I_\rho = 0$ for any Lorentz $\Omega$ and any
  frame; $A_\rho\times(\sigma\nInf + \tau\nO) = (\tau - \rho\sigma)E(a)$; $A_\rho\times\mu = \Omega\times\mu -
  (E\cdot\mu)\,u$ (checked at $\rho = 0, 1/3, -5/2, 7$).
- Field strength from jets, not assumed: on de Sitter, six FLRW fluids and Schwarzschild in Kerr-Schild form,
  $F(\hb(X)) = -(\mathcal{R} - \tfrac{\Lambda}{3})X$ with $\Lambda = 6\rho$ in the store's sign (gtg.py C5/C6),
  Lorentz block only. This matches the stored formula of
  `synthesis.frozen-point-field-space-is-the-gtg-pair-...` (ii): "the Lorentz block is
  $-(\mathcal{R}(B) - \tfrac{\Lambda}{3}B)$ in the store's sign".
- Derivative step: with $\mu = 0$ on a neighbourhood, $D_aV = (a\cdot\nabla\sigma)\nInf + (a\cdot\nabla\tau)\nO
  + (\tau - \rho\sigma)E(a)$, so $\sigma$ and $\tau$ are constant and $\tau = \rho\sigma$: $V = \sigma I_\rho$
  with $\sigma$ constant. Nothing uses $\rho \neq 0$; the restriction "for $\rho \neq 0$" in REPORT.md is
  unnecessary (at $\rho = 0$, $V = \sigma\nInf$).
- On Schwarzschild ($\Lambda = 0 = 6\rho$) $F = -\mathcal{W}$ exactly and the kernel is zero: on Einstein fields
  at the same $\Lambda$ the condition is the stored Weyl condition (confirmed).
- Perfect fluids (FLRW instants built from the Friedmann equations, a different route from the author's
  hand-entered eigenvalues): kernel dimension 0 for $w = 0, 1/3, 1, -1, -2/3$; 1 at $w = -1/3$; de Sitter at the
  same $\Lambda$: $F = 0$, all six tractor directions in the curvature kernel. The table is right.

Fixes and overstatements:

1. **REPORT.md**: replace "the normal tractor connection has no parallel tractor on the matter regions" by "...
   no parallel tractor in the physical scale (unit pairing with $X$)". Drop "for $\rho \neq 0$".
2. **Consequence 2 (normalisation stops being a premise): OVERSTATED.** $\ip{X}{cI} = c$ is trivial
   (**computed**), but it forces $c = 1$ only if one requires every tower's frozen point to have unit pairing
   with the one $X$ of the physical scale. $\ip{X}{I_r} = 1$ says that tower $r$'s scale is the physical metric
   $g$; that is the metric clause itself, in normalised form. (FS) as stored normalises one tractor ("admits a
   tractor field $I$ with $D_{a}I = 0$ ... and $\ip{X}{I} = 1$"); it says nothing about a second tower. Without
   the added requirement, one varied connection and the kernel condition give $I_r = c_r I$, metrics
   $c_r^{-2}g$ and norms $c_r^2\Lambda/3$, exactly the stored theorem's conclusion transposed. True weaker
   statement: under (FS), "one varied connection" and the kernel condition, P1a holds up to constants $c_r$;
   P1a plus P1c together are equivalent to "(FS) holds for every tower's frozen point with the one $X$".
3. **Consequence 3 (P1c becomes a consequence): OVERSTATED** for the same reason: common $N$ is equivalent to
   $c_r = \pm 1$, which is not derived. A tower with $I_r = cI$, $c \neq \pm1$, shares the connection and has a
   homothetic metric with $\Lambda_r = c^2\Lambda$, which is self-consistent.
4. **Consequence 4 (one point of matter anywhere suffices)**: correct on a connected region of the invertible
   region of $\hb$ (the parallel transport argument). Hidden hypothesis: the series' universes have walls
   (the descent wall, stretched singularities) where $\hb$ is not invertible, so "connected universe" must be
   "connected component of the invertible region". State it.
5. **Consequence 6 (the mirror): right in substance, wrong in detail** (**computed**, `Part 4`). A bivector acts
   with the opposite sign in $\Cl(4,2)$, so "the same connection" must be read as the same covariant derivative,
   not the same bivector-valued form. Two renormalisations of the null pair:
   - Keep $X = \nO$, flip $\nInf$ (my convention (ii)): the reversed tower's (FS) form with $\Omega' = -\Omega$,
     $\rho' = -\rho$ is $A' = -A_\rho$ as an element and is the same operator; its frozen point is
     $I' = -I_\rho$ with $\ip{X}{I'}' = 1$ and $Q'(I') = -2\rho$.
   - The author's (flip $\nO$, keep $\nInf$): $u$ and $I_\rho$ are unchanged as vectors, as claimed, but the
     reversed (FS) form is NOT the same operator: it is $A_\rho$ with the frame reversed, $E \mapsto -E$, i.e.
     $\mathrm{Ad}(I_4)A_\rho$. $I_4$ acts as $-1$ on spacetime vectors and fixes the added plane; it lies in
     $SO(2,4)$ outside the identity component and reverses both time and space orientation.
   So the claim holds up to a sign of $I$ or a discrete gauge element. The discrete element matters for P1b
   (the one Witt flag on the reversal orbit), which REPORT and CONSEQUENCES do not discuss. Also, in the
   reversed tower's own labels $\Lambda' = 6\rho' = -\Lambda$ and (FS)'s sentence "of de Sitter type for
   $\rho > 0$, anti-de Sitter type for $\rho < 0$" flips its label although the stabiliser group is the same;
   $N = M_P/H$ must be read with $\Lambda = 3\varepsilon H^2$ (conventions, "the frozen point's datum") so that
   it stays common. Whether the reversed tower varies the same connection at all is not given by (FS): it is
   the "one connection" hypothesis, as for $[-g]$ in the stored theorem.
6. **Consequence 7 (torsion)**: the gap is real and the author's check does not probe it (see below). With
   torsion $F = L - u\wedge T$ and $F\times V = L(X)\cdot\mu - u\,(T(X)\cdot\mu) + T(X)\,(u\cdot V)$. Counterexample
   (**computed**, `Part 5`): on a dust instant where $L$ has no kernel vector, choose $T(X) = -(L(X)\cdot\mu_0)/c$;
   then $V_0 = \mu_0 + \sigma\nInf + \tau\nO$ with $\tau - \rho\sigma = c$ and $\mu_0 \neq 0$ is in the pointwise
   curvature kernel. A sufficient condition (**argued**): the map $(\mu, c) \mapsto (X \mapsto L(X)\cdot\mu -
   c\,T(X),\ X \mapsto T(X)\cdot\mu)$ is injective at some point; then $\mu = 0$, $c = 0$ there and the
   derivative step goes through as before. $I_\rho$ itself stays parallel with torsion (it is kinematic).

### (3) Recomputed

All of the above in `ref_a1_fs_uniqueness.py` (exact). Author's scripts read after mine. Perturbations of
the author's scripts (`perturb/`):

- `cc_wrong_factor.py`: FLRW eigenvalues changed to $5(\rho+3p)$ and $9\rho$ (wrong factors and wrong sign of
  the space-space block): every FLRW check still passes. The author's table checks only which eigenvalues are
  zero; the eigenvalues are typed in, not derived.
- `cc_torsion.py`: the torsion "identity" check is `A or B` with both signs; with the first coefficient changed
  to $-7$ it still passes. It is a tautology, not a check.
- `fs_wrong_sign.py`: $(u\wedge a)\times(u\wedge b) = -2\rho\,a\wedge b$ is caught (3 failures). Good.
- `fs_k1zero.py`: setting the time-space eigenvalue to zero is caught. Good.
The author's FS script never computes a field strength from a field and never checks the derivative step; my
script supplies both.

### (4) Hidden hypotheses and risks

The kernel table needs Einstein's equations to turn matter into curvature; under (FS) these come from the
action, so the uniqueness theorem's matter clause rests on (FS) twice. "Generic matter" means no kernel of
the full $\mathcal{R} - \tfrac{\Lambda}{3}\mathrm{id}$; anisotropic or Ricci-null configurations can have
kernels. Moving P1a onto (FS) puts P1's 108-result future cone (**read**, `future_cone_size` 108) behind a
premise whose refutation clause (a) is the $w = -1$ rule.

---

## A2. The no-echo prediction

### (1) Real? Yes.

**Read.** The prediction's formal level: "The framework's quantum structure lies at the stretched singularity,
$r_c = (2M)^{1/3}$ ... by Postulate (C1): deep inside the hole, at Planck curvature, and nowhere near the horizon
... A single statistically confirmed echo train would refute the framework's localisation of quantum
structure." Holds given exactly `singularity.c1-curvature-cutoff` (graph, confirmed). (C1) v5 scope:
"read as a calibration of the count on the Schwarzschild family only ... Away from the Schwarzschild family the
count is read through the horizon placement, the modes on the horizon". (C$_{\mathrm{loc}}$) v6: "On a hole's
horizon the modes on each light ray and the modes premises (C1) and (C2) place at the curvature cutoff are one
set described twice". The prediction concerns Kerr remnants, so its stated basis is out of its own scope there.
The report understates one point: through (C$_{\mathrm{loc}}$) the same modes are on the horizon even for
Schwarzschild, so "nowhere near the horizon" is in tension with the store everywhere, not only on Kerr.

### (2) Verdict on the revised proposal: SOUND WITH FIXES.

1. The kept basis edge, `interior.imported-equivalence-einstein-equations`, says only (**read**): "the GTG field
   equations for $(\hb, \Omega)$ are equivalent to the Einstein field equations". It asserts no field equation.
   What makes Einstein's equations hold at and across the horizon is (FS) with the action, or
   (C$_{\mathrm{loc}}$) plus the Clausius relation, which (C$_{\mathrm{loc}}$) calls "a separate hypothesis and
   not a clause of this premise". CONSEQUENCES A2.3 counts (FS)'s 19 results as exposed but the revised basis
   does not add (FS). Fix: add the assumes edge for whichever route supplies the field equations ((FS), or
   (C$_{\mathrm{loc}}$) with Clausius as a stated hypothesis).
2. "The field equations holding up to the horizon" should be "at and across the future horizon": the Kerr
   quasinormal spectrum uses the ingoing (regularity) condition there.
3. Absence of echoes also needs the horizon modes to impose no reflecting boundary condition. The
   (C$_{\mathrm{loc}}$) identification ("identified with the matter field on those light rays (the horizon modes
   and the matter crossing the patch are one field)") supports that reading (**argued**), but its clause
   (R$_{\mathrm{loc}}$) makes the horizon modes KMS before the crossing, and some published echo models derive a
   frequency-dependent reflectivity from exactly a thermal horizon state (the "Boltzmann reflectivity"
   proposal of Oshita, Wang and Afshordi, cited from memory). Fix: state in the prediction that the horizon
   modes impose no reflection on classical perturbations, as a reading of the identification clause, and add
   the state's regularity across the horizon (Premise (HD), whose one-liner gives "Hadamard states on every
   later field, the local form of (N$_{+}$)") if the state is part of the basis.
4. **The claim that (N$_{+}$) cannot serve on Kerr is overstated.** (N$_{+}$) v12 cases (a) to (c) are the
   eternal Schwarzschild, de Sitter and Minkowski local horizons, and Kerr has no stationary Hadamard state
   ("on Kerr the corresponding result is argued, from superradiance"). But its "Local form" covers "a local
   Rindler horizon $\mathcal{H}_{p,\ell}$ of a gravitational field ... with nonvanishing field strength", argued
   at leading order, and a Kerr horizon patch is such a horizon at leading order
   (`synthesis.c-loc-is-a-second-placement-of-the-count` (ii)). That is the same argued strength at which
   (C$_{\mathrm{loc}}$)'s own (R$_{\mathrm{loc}}$) holds for nonzero field strength ("it follows from the local form
   of (N$_{+}$), argued at leading order"). REPORT.md's first proposal already used the local form, so
   CONSEQUENCES A2.1 rebuts a stronger proposal than the one made.
5. Counts **verified by the store** (`future_cone_size`): (FS) 19, (C$_{\mathrm{loc}}$) 30, (C1) 57.
6. Delays (**decimal**): $8M\ln(M/m_P)$ gives 35 ms at $10\,M_\odot$, 0.107 s at 30 and 0.25 s at
   $70\,M_\odot$, as stored.

### (4) Risks

As CONSEQUENCES says, after the change the prediction is GR's own (ledger "absent") and discriminates nothing.
Point 3 above is the one way a series premise could predict echoes.

---

## A3. "Obstructions are moved, never destroyed"

### (1) Real? Partly: under one reading of "completion" only.

**Read and computed.** Clause (3) of `synthesis.wall-class-one-rung-obstruction` v3 gives, when
$w_1(\shL) = 0$, a form "nondegenerate at every point of $M$, equal to $G \perp H$ outside $C$ on the physical
side and to $G \perp K_-$ outside $C$ on the far side with $K_-$ positive definite". Signatures: physical
$(p,q) + (1,1)$, far $(p-1,q+1) + (2,0)$, both $(p+1,q+1)$; on the wall the block of $(k,a,b)$ has determinant
$-2\mu^2$ and total signature $(p+1,q+1)$ (`ref_a3_signatures.py`). Clause (2): signature $(n,n)$ everywhere,
including $\beta = 1$ at the wall. The bookkeeping is right, and under a loose reading of "completion" the
conjecture's "no completion is nondegenerate globally" fails.

But the conjecture fixes its own reading: "The one-sided completion theorem and shadow wall of that paper
prove exactly this for tame corank-one degenerations". That is true only of standard completions, the reading
of `sheaf.conservation-degeneracy-absolute-form` v4: "$h = G \perp K$ for a nondegenerate form $K$ on a
complement, with $\operatorname{sig}(K)$ the same on both exterior regions ... Degeneracy can be displaced, never
destroyed." Clause (3) changes the model ($H$ against a definite $K_-$), and on the far side it does not even
adjoin a hyperbolic plane, so it is not a "completion" in the series' usage. On the strict reading there is no
contradiction, and the tame case is a theorem. The entity has no `source_formal`; the locator (T01 Conj 7.9)
could not be checked against the deposited paper here.

### (2) Verdict: SOUND WITH FIXES.

- Restating to the strict reading is right. Record it as removing an ambiguity ("on the loose reading, the
  statement would be refuted by clauses (2) and (3)"), not as refuting the conjecture as worded.
- **Missed by the author:** the conjecture is internally inconsistent about scope. Its hypothesis is "degenerating
  tamely along a locus (in the sense of the series' sheaf-theoretic paper)", and `sheaf.tameness` defines
  exactly the tame corank-one case, yet it then says "the conjecture asserts the pattern is not an artefact of
  the tame case". The restatement must replace the hypothesis, not add to it.
- CONSEQUENCES A3.1 "the lens walls need two to five rungs" is wrong as a summary (**read**): the store has
  $k \ge 4$ on every side of $L^{2n+1}(4)$, $n \ge 2$; $k = 5$ on the definite side of $L^5(4)$; $5 \le k \le 6$
  on $L^7(4)$; and $k \ge 1 + \lfloor n/2 \rfloor$ in general, unbounded in dimension. "$k$ planes need
  $w_1(\shL)^k = 0$" is right (`synthesis.wall-rung-count-...` (1): "$x^{j} = 0$ for every $j \geq k$").

---

## A4. Kasner premises against the dating

### (1) Real? No contradiction in the store: a recorded tension between two postulates and a conjecture.

**Graph, verified.** Both premises have empty future cones and no `uses`/`assumes` from anything; they are
named in text by five claims, (HD), `store/conventions.md` and `store/open_problems.yaml`. Both premises say
(**read**): "The two cannot both hold; which one gives way is not decided here." `dark-energy.gravity-pre-metric-
forces-degenerate-exactly` (2): gravity's action is "defined across the singular locus", which denies neither
side. I found no proved result deciding it (**read**, limited to the entities listed).

### (2) Verdict: SOUND WITH FIXES.

- **Missed:** `store/open_problems.yaml` (line 5417 on) records "By Leon's decision of 1 November both are
  postulated". Lowering them reverses a recorded decision of Leon's, which the report does not say. It cites
  only the 10 November "no mechanism" decision.
- The open-problem entry must be updated with the change.
- "the conventions line goes" is not right: the Kasner texts still write (P1), (P2), which collide with T14's
  P1, P2, so the "Same names" entry (or a renaming to, say, (K1), (K2)) is still needed.
- Keep the refutation conditions as a remark, as CONSEQUENCES A4.4 says.

---

## A5. Premise D's note and the reduction theorem

### (1) Real? Yes, as a textual contradiction.

**Read.** D's note: "no stored statement of the fitted total with the cell radius as unit has D in its past
cone". **Graph, verified by a full scan:** exactly one entity holds given both D and R2,
`synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball`. Its holds-given contains D (by its
use of `dark-matter.democracy-de-sitter-radius-unit-ball`), R1, R2 and R3, and its clause (i) states
$T = (11\pi + 16)/3\pi$ in the length $d$, which under R2 is the cell radius. The theorem contradicts itself:
clause (i) says "the stored wording does not choose between them", while its own closing paragraph says "This
reading is not adopted: by Premise R3 as now stated the unit of thickness is each tower's own cell radius".
It still lists P4 among the premises its model satisfies ("a model of P1, P2, P3, P4, ...").

### (2) Verdict: OVERSTATED (the split is optional).

The numbers are right (**computed**, exact): $T = 11/3 + 16/3\pi = (11\pi + 16)/3\pi \approx 5.364$;
counter-filling $s_3 = s_5 = 16$ under the own-radius reading gives $a_r = 2d$ and $T = 11/3 + 32/3\pi \approx
7.06$; $T(\lambda,\mu) = 1 + 8/3\mu + 16\lambda/3\pi$, with values $(2,1)$ and $(1,2)$ as stored; cubic cells
give 5; one $D = 2$ tower read at $D = 4$ gives $7/3 + 8/\pi$. The formula $f_r = (m_r/m_6)(V_3/V_{D_r})
(a_6/a_r)^3$ follows from $\nu_r = 1/(V_{D_r}a_r^{D_r})$ with thickness $a_r$ (**computed** on rationals): R1
enters through $m_r/m_6$ and R2 through $a_r = d$, separately. Strictly, R2 enters once in the formula (the
density and the unit merge into $a_r$); "used twice" is a reading.

A split is not needed for consistency. Holding D and R2 together is not inconsistent (D's own note argues that it
forces cell radius equal to de Sitter radius, a strong but consistent conjunction), and the theorem has an empty
future cone. The minimal fix: name this theorem as the exception in D's note (it states both readings side by
side as an audit), delete "the stored wording does not choose between them", and drop P4. The split is a
reasonable optional tidy-up and also makes D's note true as written.

---

## A6. $Q = \epsilon N$

### (1) Real? Partly.

**Decimal arithmetic, order of magnitude, matches the author:** $N = M_P/H = 1.03 \times 10^{61}$ ($H^2 =
\Lambda/3$, $H = H_0\sqrt{\Omega_\Lambda}$); baryons inside $1/H$: $4.8 \times 10^{78}$ today, $3.8 \times 10^{79}$ at
$z = 1$, $6.2 \times 10^{87}$ at $z = 1090$; $n_B/s = 8.7 \times 10^{-11}$; thermal entropy in the ball
$5.5 \times 10^{88}$; $\epsilon N = 8.9 \times 10^{50}$ at $\epsilon = 8.7 \times 10^{-11}$; $\pi N^2/\ln 2 = 4.8 \times
10^{122}$, times $\epsilon$: $4.2 \times 10^{112}$; $Q/N = 4.7 \times 10^{17}$; per registered unit $1.0 \times
10^{-44}$.

The stored texts mostly guard against the conflict. `dark-matter.stored-asymmetry-charge-not-number` v10
(**read**): "$N = M_{P}/H$, which fixes a count of registered units, about $\pi N^{2}/\ln 2$, without being it ...
the argument uses only that $N$ is common". The conflict is confined to two places: the label "the asymmetry
per mode" next to $Q = \epsilon N$ (with $N = M_P/H$ no per-mode reading gives a number at most one), and the
registered premise's valuation sentence, "Its value is taken from the record: in this tower it is fixed by the
measured baryon density, ..., equivalently the $8.7 \times 10^{-11}$ baryons per unit entropy". Read as "fixed by
the datum" it is consistent; read as $\epsilon = 8.7 \times 10^{-11}$ it conflicts with $Q = \epsilon N$, and
$n_B/s$ uses the thermal entropy, the quantity of the reading clause (iv) rejects. "Per mode" refers to
boundary modes (the stored "the asymmetry per mode depending on the tower's own charge structure" in
`dark-matter.asymmetry-arrow-counted-fifteenth-refutation`), so conventions Known limit 5 (two meanings of
$N$) does not rescue the per-mode label: neither $N$ nor $N^2$ makes $8.7 \times 10^{-11}$ the right factor.

### (2) Verdict on the revised proposal: SOUND WITH FIXES.

- The numbers are unchanged, as claimed (**argued**, using the stored relations): equal charge per comoving
  volume and equal mass per baryon give $f_2 = 1$; the mirror's own $n_B'/n_\gamma' = \eta/\xi^3$ is the stored
  $\eta'$. It does not smuggle the thermal reading back in provided the equality is stated as $n_B' = n_B$ per
  comoving volume, with this tower's $s$ only as the unit of comoving volume. It must not be stated as
  $n_B'/s' = n_B/s$, which is the thermal reading. Note that the value 8.7e-11 is today's ruler, not the
  descent's datum, unless no entropy is produced in this tower after the descent.
- **Hidden hypothesis in restated route one.** `synthesis.tower-charge-sector-label-temperature-not` v5 (i) is a
  theorem about boundary-mode windows, "On every window $\mathfrak{A}_{F} \otimes \mathfrak{A}'_{F'}$", under
  Hypothesis (B'), "the CAR algebra over $\ell^{2}(J) \oplus \ell^{2}(J')$". Its windows are finite sets of
  boundary modes, not comoving spatial regions, and (iii) adds that a thermal state over infinitely many modes
  has no finite total charge. "P1's one metric gives the two towers the same comoving regions, so P2 equates the
  labels of corresponding regions" therefore needs an identification of boundary-mode windows with comoving
  regions of the two towers. That is a new premise and should be stated.
- **Consequence 5 (P1c loses its only use) is overstated.** In the original route the common $N$ is what matches
  the two towers' mode sets so that equal $\epsilon$ gives equal $Q$. The restated route needs a matching of
  windows by some other means. P1c is freed only if that identification is supplied without it.
- Minor stored-number note (**decimal**): (iii) says $\eta'$ "runs from 19 to 26 at the floor". With the quoted
  $\xi \in [2.8, 3.2] \times 10^{-4}$ and $\eta = 6.1 \times 10^{-10}$ I get 18.6 to 27.8, and 0.0095 (not "about
  0.008") at $\xi = 4 \times 10^{-3}$. This is consistent if the floor is about $2.85 \times 10^{-4}$, and does not
  bear on A6.

---

## B and C

- B1: right (**read**/argued). In a $\Lambda$-dominated epoch $1/H$ is constant and the age grows; `standard-model.what`
  says "the coincidence is epochal".
- B2: partly. The trichotomy text already says "under the action as written ... $N$ is a parameter of the laws;
  the conditional clause holds only if the norm is promoted", so the fix is cosmetic.
- B3: right. `dark-matter.odd-towers-populated` is a postulate and the prediction says "If the four odd towers
  hold matter".
- B4: right. The neutrino entity says "conditional only on the frozen point's definition off the vacuum region,
  which the dark-energy paper names, does not use"; (FS) now adopts it.
- C, (U) against (EW): **graph verified.** There is a pinned `contradicts`, and no entity holds given both (37 hold
  (U), 16 hold (EW), 0 hold both). **Missed:** the link's own rationale says "consistent in the eigenvalue reading,
  which is what the formal level states". The store pins a contradiction between two formal levels that its own
  rationale calls consistent. Either the link should name the entry reading, or the formal level of (U) should.
- C, Sakharov zero against $\xi = 0$: the attachment-module result is scoped (the one-liner names "the attachment's
  helicity modules"). $B = 8$ was not recomputed (could not check in the time).
- C, univalence against parity-odd CHSH: **read**. `synthesis.chsh-with-parity-even-...` says "the two settings
  are recorded side by side". Settled as stated.
- Not checked: (L$_E$), Premises C/S2, the "mystery of largeness" item, and the 1,391-claim status agreement.

## Missed by the author (summary)

1. A1: the normal tractor connection does carry parallel tractors on matter regions (stored dust example; flat
   on FLRW). Only the physical-scale one is absent.
2. A1: $c = 1$ and P1c are not derived (normalisation circularity). The mirror is the same operator only up to a
   sign of $I$ or $\mathrm{Ad}(I_4)$, a discrete element relevant to P1b. The type label and the sign of
   $\Lambda$ flip in the reversed tower's convention.
3. A1: the author's torsion check is a tautology, and the FLRW check is blind to the eigenvalue factors.
4. A2: the kept basis edge asserts no field equation. The revised basis must name (FS) or Clausius. Horizon
   reflectivity is not excluded by (C$_{\mathrm{loc}}$) as written. The local form of (N$_{+}$) is dismissed
   unfairly.
5. A3: the conjecture's hypothesis ("tamely", which is corank one) contradicts its "not an artefact of the tame
   case". The lens-wall rung counts are misreported.
6. A4: lowering reverses Leon's 1 November decision; open_problems.yaml must change; the namesake entry stays.
7. A5: the theorem contradicts itself (clause (i) against its Status paragraph). An edit suffices.
8. A6: the sector-label theorem is about boundary-mode windows, so restated route one needs a window-to-region
   identification, and P1c is not freed by A6 alone.
9. C: the (U)/(EW) `contradicts` link's rationale says the stored formal levels are consistent.

## Summary table

| Item | Contradiction real? | Verdict (latest form) | Main reason |
|---|---|---|---|
| A1 | Partly (tension by omission; report's key sentence false) | SOUND WITH FIXES (theorem); consequences 2, 3, 6 OVERSTATED | Theorem verified exactly incl. derivative step, signs, Weyl reduction, fluid table; $c=1$/P1c circular; mirror only up to sign or $\mathrm{Ad}(I_4)$; torsion needs extended condition; $\rho \neq 0$ unnecessary |
| A2 | Yes | SOUND WITH FIXES | Basis must name what gives the field equations ((FS) or Clausius) across the horizon, and a no-reflection/regular-state clause; (N$_{+}$) dismissal overstated; counts 19/30/57 verified |
| A3 | Partly (loose reading only) | SOUND WITH FIXES | Signatures verified; conjecture's own sentence fixes the strict reading, where tame case is proved; hypothesis self-inconsistent; rung counts misreported |
| A4 | No (recorded tension) | SOUND WITH FIXES | Graph claims verified; reverses Leon's 1 Nov decision; update open_problems.yaml; keep namesake line |
| A5 | Yes (textual) | OVERSTATED | All totals verified exactly; an edit of D's note and two stale sentences suffices; split optional |
| A6 | Partly | SOUND WITH FIXES | All numbers verified (decimal); revision keeps $f_2 = 1$, $\eta' = \eta/\xi^3$; restated route one needs a boundary-window to comoving-region identification, so P1c not freed |
