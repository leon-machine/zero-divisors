# Run 2026-11-11-contradictions: contradictions in theory across the graph

Leon (11 November 2026): "go through all of the physics graph and identify/resolve any contradictions in
theory that you find". He chose the scope "changes plus premises" and "report only": nothing in `store/` is
changed by this run. Each item below has a proposed resolution for his decision.

## What was read, and what was not

- Structure, whole graph (2,361 entities): declared against effective status, every `uses`/`assumes` edge,
  every pinned `contradicts`, joint occurrence of mutually exclusive premises in "holds given".
  `tp check --layers 1,2,3`: 0 errors, 0 warnings.
- Read in full (formal level): all 71 postulates, 15 refuted claims, 31 conjectured claims, 14 predictions,
  and `store/conventions.md`.
- Entities changed since the consistency run of 7 November (about 200): every one-liner, and the formal
  level of those a candidate touched.
- Not read: the formal levels and proofs of the roughly 1,000 proved claims unchanged since 7 November
  (they had a full read then). A contradiction lying wholly inside those is outside this run.

Labels: **graph** = shown by a query of the store; **computed** = exact check in `work/`; **read** = from the
stored texts, argued.

## A. Contradictions that need a decision

### A1. The frozen point is parallel for two different connections (FS against P1a)
- `synthesis.field-space-premise-parallel-frozen-point` (FS, adopted): the frozen point is parallel for the
  varied connection $A_{\rho} = \Omega - (\nInf - \rho\nO)\wedge\hb^{-1}$, on every configuration, matter
  included. It says itself that the series' transport (the normal tractor connection) preserves a tractor in
  the physical scale only on Einstein fields and differs from $A_{\rho}$ on shell with matter.
- `dark-matter.p1-single-frozen-point` (P1a) gives its metric clause the status "a theorem up to a common
  normalisation wherever the Weyl tensor has no kernel vector, given that every tower's frozen point is
  parallel for one tractor connection", citing `synthesis.frozen-point-unique-where-weyl-has-no-kernel` and
  `synthesis.two-frozen-points-conformally-flat`. Both are theorems about the normal tractor connection
  $\Omega_{T}$. Neither entity, nor P1, mentions (FS) (**graph**: no reference).
- The conflict (**read**): in a universe with matter the normal tractor connection has no parallel tractor
  on the matter regions, so the hypothesis of P1a's theorem fails there; and under (FS) the connection that
  does carry the frozen point is not the one the theorem is about.
- What holds for the (FS) connection (**computed**, `work/fs_parallel_tractors.py`, exact): the soldering
  bivectors stabilise $I_{\rho}$; $(u\wedge a)\times(u\wedge b) = 2\rho\,a\wedge b$ with
  $u = \nInf - \rho\nO$, so on torsion-free fields the field strength is the Lorentz block
  $L = \mathcal{R} + 2\rho\,E\wedge E$ up to the store's sign; Lorentz bivectors kill $I_{\rho}$ and $u$; and
  $(u\wedge a)\times u = 2\rho\,a$. Hence (argued from these) a tractor parallel for $A_{\rho}$ is a constant
  multiple of $I_{\rho}$ wherever $L$ has no kernel vector, for $\rho \neq 0$. That condition is on the de
  Sitter-subtracted field strength, not on the Weyl part: it holds on generic matter regions, conformally
  flat ones included, and fails where the field is exactly de Sitter at the same $\Lambda$ ($L = 0$).
- So two stored statements change under (FS): "an independent choice on conformally flat regions" shrinks to
  "on regions that are exactly de Sitter at that $\Lambda$", and the no-kernel condition is no longer Weyl's.
- **Proposed resolution.** Add one theorem, the (FS) analogue of the uniqueness result (statement above,
  with the degenerate cases: $L$ vanishing on a subspace of bivectors), and restate P1a's status paragraph to
  name which connection: the varied connection of (FS), with the two normal-tractor theorems kept as the
  vacuum case. Alternative: keep P1a on the normal tractor connection and say it is a statement about
  Einstein regions only.

### A2. The no-echo prediction rests on a placement the store no longer holds for spinning holes
- `scrambling.no-echo-prediction-registered` (live, v2): the quantum structure is "at the stretched
  singularity ... and nowhere near the horizon", by (C1); it predicts the unmodified Kerr spectrum, and says
  an echo "would refute the framework's localisation of quantum structure". Its basis is (C1) alone
  (**graph**: holds given `singularity.c1-curvature-cutoff`).
- `singularity.c1-curvature-cutoff` v5, `singularity.c2-cell-density` v4 and (IC) v3: the cutoff placement is
  "a calibration of the count on the Schwarzschild family only"; away from it "the count is read through the
  horizon placement, the modes on the horizon". `synthesis.c-loc-local-horizon-premise`: on a hole's horizon
  the modes on each light ray and the modes at the cutoff "are one set described twice".
- The conflict (**read**): every merger remnant is a Kerr hole, the case in which the store places the modes
  on the horizon; the prediction's stated reason (no structure near the horizon) is the opposite of that
  placement, and its basis premise is out of its own scope there.
- The conclusion probably survives on other grounds: under (N$_{+}$) and its local form the horizon modes are
  in the null vacuum, which is the smooth horizon. That is not what the entity says or rests on.
- **Proposed resolution.** Restate the prediction's basis as the horizon state (local form of (N$_{+}$), with
  (C$_{\mathrm{loc}}$)), keep (C1) for Schwarzschild only, add the assumes edges, and reword the kill
  consequence: an echo train would refute the null-vacuum state of the horizon modes, not a localisation.

### A3. A conjecture contradicted as worded by a stored theorem
- `transport.obstructions-are-moved-never-destroyed` (conjectured, v2): "any completion of the family that is
  nondegenerate of constant signature on one side of the locus degenerates on a displaced locus on the other
  side; no completion is nondegenerate globally", and "the one-sided completion theorem and shadow wall ...
  prove exactly this for tame corank-one degenerations".
- `synthesis.wall-class-one-rung-obstruction` (proved, v3), for tame corank-one walls: clause (2) gives a form
  on $T^{*}M \oplus T^{*}M$ nondegenerate of signature $(n,n)$ at every point; clause (3) gives a one-rung
  form nondegenerate at every point of $M$, equal to $G \perp H$ on the physical side, whenever
  $w_{1}(\shL) = 0$. Signatures agree on both sides ($(p{+}1, q{+}1)$), so these are globally nondegenerate
  completions of constant signature (**read**).
- Only the strict reading (one exterior model $K$ on both sides) is obstructed, and that is already a theorem
  (`sheaf.conservation-degeneracy-absolute-form`; clause (1) of the wall-class result).
- **Proposed resolution.** Restate the conjecture to the strict reading and to walls beyond the tame
  corank-one case (where it is still open), and record that the unrestricted wording is refuted on tame walls
  by clauses (2) and (3). The conjecture has no note of the wall-class result at present.

### A4. Kasner exit premises against the dating: recorded as contradictory, not resolved
- `synthesis.pre-descent-contracting-kasner-stage-premise` and
  `synthesis.pre-descent-state-carried-into-descended-phase-premise` (postulates) need a metric stage before
  the descent; `standard-model.dating-descent` (iii) (conjectured) reads pre-descent physics as pre-metric.
  Both premises say "the two cannot both hold; which one gives way is not decided here".
- No result has an assumes edge to either premise (**graph**), so nothing proved is exposed.
- **Proposed resolution.** Since the series keeps "no mechanism for the primordial spectrum" (decision of
  10 November), the lighter change is to lower the two Kasner premises from postulate to stated hypotheses of
  the Kasner results (as the radiation-type descent is), leaving the dating as it is. The other way round
  needs the dating's reading (iii) dropped.

### A5. Premise D's note is contradicted by the graph, and one theorem stands on a reading R3 now declines
- `dark-matter.d-democracy-total-mass` (note of 10 November): D and the unit-ball reading are alternatives,
  and "no stored statement of the fitted total with the cell radius as unit has D in its past cone".
- `synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball` (proved, v1) states the fitted
  total $(11\pi + 16)/3\pi$ in clause (i) and holds given both D and R2 (**graph**; D enters through its use
  of `dark-matter.democracy-de-sitter-radius-unit-ball`). It is the only entity resting on both.
- The same theorem reads R3 "in the fixed length $d$" and says "the stored wording does not choose between"
  the readings; `dark-matter.r3-one-cell-per-unshared-direction` v2 now chooses the other one (each tower's
  own cell radius) and says the reduction "holds only in that reading", the one not adopted. The theorem
  also lists the retired P4 among the premises its model satisfies.
- Nothing is false as a conditional statement; the contradiction is between the theorem's text, D's note and
  R3 v2.
- **Proposed resolution.** Split the theorem: clause (i) (under R1 to R3, fixed-length reading, marked as the
  reading not adopted) and clause (ii) (under D alone), so that no entity holds given D and R2 together; fix
  the two stale sentences and the P4 mention; then D's note is true as written.

### A6. The asymmetry: $Q = \epsilon N$ against the value quoted for $\epsilon$
- `dark-matter.stored-asymmetry-charge-not-number` (v10) and `dark-matter.mirror-tower-copy-one` (v):
  $Q = \epsilon N$ with $N = M_{P}/H$, $\epsilon$ "the asymmetry per mode". The registered premise
  `synthesis.matter-asymmetry-registered-free-input` values $\epsilon$ by the baryon density, "equivalently
  the $8.7 \times 10^{-11}$ baryons per unit entropy".
- Arithmetic (not a stored check): $N \approx 1.0 \times 10^{61}$; the baryon number inside the de Sitter
  radius $1/H$ is about $5 \times 10^{78}$. With $\epsilon = 8.7 \times 10^{-11}$, $\epsilon N \approx 10^{51}$,
  and with the registered units $\pi N^{2}/\ln 2$ it is about $4 \times 10^{112}$. The count that makes
  $8.7 \times 10^{-11}$ the right factor is the thermal entropy, about $5 \times 10^{88}$, which is not common
  to the towers: the mirror's is smaller by $\xi^{3}$. Baryons per unit entropy is the quantity of the
  thermal reading that clause (iv) of the first result rejects.
- So the premise's valuation sentence, read as a value of $\epsilon$, contradicts the charge reading on which
  the mirror's share of one stands (**read**). Read only as "fixed by the same datum" it is consistent, but
  then $\epsilon$ has no stated number and $Q$ no stated region.
- **Proposed resolution.** In the premise and the two results: say that $\epsilon$ is $Q/N$ for a stated
  region (the de Sitter ball), give that number, and call $8.7 \times 10^{-11}$ the record's yield $n_{B}/s$
  in this tower from which $Q$ is read, not $\epsilon$.

## B. Smaller inconsistencies of wording

1. `standard-model.dating-descent` (i): "in any $\Lambda$-dominated epoch the age of the universe is
   automatically of order $N$ Planck times". In a $\Lambda$-dominated epoch $1/H$ is constant and the age
   grows without bound; the statement holds only near the onset of that epoch.
   `standard-model.what` (iii) says the coincidence is epochal, which is the correct form. Fix (i).
2. `standard-model.trichotomy-what-kind-number`: $N$ is initial data "only if the norm is promoted";
   `synthesis.einstein-route-makes-n-initial-data` (i): initial data on the Clausius route "with no
   promotion". Add "under the action" to the first.
3. `pred.dimmed-evaporation-bursts`: "if the four odd towers hold matter"; that is now the adopted premise
   `dark-matter.odd-towers-populated`, so on the store's premises $o > 0$.
4. `neutrino.double-prediction-sum-predicted-floor` (v1): $w = -1$ "conditional only on the frozen point's
   definition off the vacuum region, which the dark-energy paper names, does not use"; the store now adopts
   that condition as (FS). It also calls the two stances "one joint prediction", where
   `pred.neutrino-mass-sum-floor` now says they are exposed in opposite senses.

## C. Candidates checked and found already settled in the store

- Hypothesis (U) against Premise (EW): pinned `contradicts`; no entity holds given both (**graph**).
- (L$_{E}$) against the real-time spreading law: the premise is kept, both scrambling estimates are
  conjectured, and no proved result uses either (**graph**).
- Premises C and S2 of the simulations: exclusive readings; only the two conjectured simulation results list
  both, each reporting both readings.
- The Sakharov zero at three generations against the doublets' $\xi = 0$: scoped on 9 November to the
  attachment modules; the content's coefficient is $B = 8$.
- Univalence against the parity-odd CHSH settings: recorded side by side by decision, with an attack item.
- "The number N is a mystery of largeness": status conjectured under a `refuted.` id, by the decision of
  10 November.
- No proved claim uses a refuted or conjectured claim; declared and effective status agree on all 1,391
  claims (**graph**).
