# Run 2026-11-06-edge-normality: what is specific to this run

LAB = /home/claude/phys-graph (run every tool from there). Run name: 2026-11-06-edge-normality.
`export TP_COLONY_RUN=2026-11-06-edge-normality`.
Run folder: colony/runs/2026-11-06-edge-normality/ (findings/, work/<your-name>/, verify/).
Read colony/BRIEF.md and colony/POLICIES.md first. This file overrides them where they differ.

## Target (one problem, one cluster)
`op.r-premises-external` (read it in full with `labcli.py get_open_problem`), together with its
sibling `op.null-positivity-curved-horizons` item (ii) where the same result settles both.

What is still open after the earlier runs (do NOT redo the settled parts):
- Settled and in store: the local form of (N+) at every point (local normality, Hadamard route,
  (HS) a theorem); within stationary gauge-invariant quasi-free states, (N+) is equivalent to local
  normality to the null vacuum at the edge; the folium form on the Moebius-closed generator (global
  quasi-equivalence) with the slope-jump counter-model; affine-KMS states pass every pointwise
  condition; half-sided modular inclusions give positivity only from KMS data for the boost about
  two cuts (thermal input); point-spectrum boosts admit no half-sided translations.
- Open: the GROUND-STATE CLAUSE without stationarity, from a principle of the series with no
  thermal input; or a proof that no principle expressible in the series' algebra can supply it
  (which records (N+) as a permanent import). Either outcome is a success; a sharp partial result
  (a principle that gives the ground state up to an explicitly named residual datum) is valuable.

## Leads from the 6 November scalars session (context, not store results)
1. Condition of geometric modular action (CGMA). Buchholz and Summers (CMP 155 (1993) 449, "An
   algebraic characterization of vacuum states in Minkowski space") and Buchholz, Dreyer, Florig,
   Summers (Rev. Math. Phys. 12 (2000) 475) characterise vacuum states by requiring only that the
   modular CONJUGATIONS of wedge algebras act geometrically (as wedge reflections); no modular group,
   no temperature appears in the hypothesis. Cited from memory: verify the statements (WebSearch /
   WebFetch are allowed) before relying on them, and record exactly what they assume (in particular
   whether the spectrum condition is derived or assumed, and any modular stability condition).
   Generator analogue to test: for gauge-invariant quasi-free states on the CAR algebra of one
   generator, the modular conjugation of the half-line algebra of [a, infinity) acts as the
   reflection about a, for every cut a. Products of two such reflections are affine translations
   fixing the state vector, so translation invariance (stationarity) might come OUT rather than go
   in. Candidate theorem: CGMA at every cut gives (N+) up to the time-orientation sign (ground state
   or its reflection, the filled positive-energy sea), and the orientation is fixed by the direction
   of the half-line inclusions. Whether CGMA counts as "no thermal input" must be argued explicitly
   (J alone, versus S = J Delta^{1/2}).
2. In Cl(1,3), with B = gamma_0 gamma_3 the boost bivector and J = gamma_1 gamma_2 the transverse
   (anisotropic kernel) bivector, I_4 B = J exactly (check with GA.py). So the boost continued to
   imaginary rapidity with I_4 as the imaginary unit is the transverse rotation, and the wedge
   reflection is I_4 (total reflection, the PCT element) composed with the pi-rotation in the
   transverse plane: the Bisognano-Wichmann form of the wedge modular conjugation is an element of
   the series' algebra. This is how CGMA could be "a principle stated in the series' algebra".
3. A pure gauge-invariant quasi-free state is the Fock state of a basis projection (a complex
   structure on the one-particle space). The ground-state clause is the statement that this
   projection is the spectral projection of the translation generator (the Hardy-space
   polarisation). The Witt pair of a transport increment (n null, partner m, {n, m} = 1, with
   n m n = n: m is the generalised inverse of n) is a polarisation; whether the transport principle
   fixes which member annihilates the state is a possible principle.
4. Completion context: half-sidedness (with unique vacuum) forces type III_1 (Longo, Wiesbrock),
   and the hyperfinite III_1 factor is unique (Connes, Haagerup). So the open question is the
   existence of the state with the right property, not which continuum.

## Arms
- A (constructive): aim to prove. Start from lead 1 (CGMA on the generator), but give three routes
  as BRIEF.md requires and choose explicitly. Use `find_text` for "geometric modular action",
  "Buchholz", "Summers", "modular conjugation" first, so you do not redo stored work.
- B (adversarial and cross-pollinating): aim to break or bound. Test lead 1 hardest: is CGMA thermal
  input in disguise (does geometric J at every cut force Delta geometric, hence KMS at 2 pi)? Do
  stored counter-models (slope-jump vacuum, affine-KMS states, half-thermal products, the Hawking
  state of a collapsing hole) satisfy CGMA at every cut? Then attempt the independence statement:
  make "principle expressible in the series' algebra" precise and give a model where every such
  principle holds and the ground-state clause fails, or show why no such model exists.
Read your sibling's findings file midway and at the end; never file what they filed. With one
cluster there is no bridge-hunter: put cross-links you find in "Unexpected links".

## Filing gate and rules
As BRIEF.md: check4.py exits 0 (environmental E401 acceptable) and validate_draft ok; exact
arithmetic, `import GA`, premise() per premise, mutation-sensitive checks. At most 3 proposals per
arm; one strong one is better. Literature used from memory is flagged in findings and listed as a
Fact to import (decision for Leon); do not create imported or postulate entities or `assumes` edges.
Credit: `{name: Claude Opus 5.5, role: proposal and drafting, source: run 2026-11-06-edge-normality}`.
House style: no em dashes; never "honest"/"honestly"; never "load-bearing"; declared macros only.
The machine has 2 CPUs: one gate process at a time each; never kill other processes.
