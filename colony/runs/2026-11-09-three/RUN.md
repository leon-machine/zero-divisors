# Run 2026-11-09-three: what is specific to this run

LAB = /home/claude/phys-graph (branch run/2026-11-09-three). Run folder: colony/runs/2026-11-09-three/
(findings/, work/<name>/, verify/). Read colony/BRIEF.md and colony/POLICIES.md; this file overrides them.
Baseline: baseline.log (0 errors, 0 warnings).

## Goal
Leon asked for a look over the physics graph, a choice of three problems where an advance can be made, and an
attack on them; and, separately, cross-pollination: links between areas and new areas worth investigating.
The earlier run of today (colony/runs/2026-11-09-solvable, read its REPORT.md, findings/ and bridges.md) triaged
all 32 open problems. The three targets below are the strongest leads it left unexecuted. Do not redo what it
settled. A no-go or an independence proof is a full result.

## One cluster, three targets (attackers A constructive, B cross-pollinating and adversarial)

### T1. op.wall-class-invariant, attack item 4 (and item 1's remainder if reached)
Leon decided (9 November) that the lens-space inputs are derived in the store, not imported. The two results
synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial and
synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height are conditional on them. Derive, with exact
checks: the integral and mod-2 cohomology rings of L^{2n+1}(4) (cellular chain complex of the Z4 action on the
sphere, cup products from the equivariant diagonal or from the Gysin sequence of the circle fibration over CP^n);
the stable class of T Sigma + R; the spin class q1 with 2 q1 = p1 and p1 = e^2 for oriented plane bundles;
Sq^1 = 0 on classes lifting to Z4; the complex K-ring Z[chi]/(chi^4 - 1, (chi - 1)^{n+1}) with its
lambda-operations (at least the part the K-theory result uses: the order of 2^{k-1}(1 - xi)). Prefer the
algebra-core style (docs/ALGEBRA_CORE.md): own proofs, exact checks, long classical proofs flagged honestly as
what is derived and what is still cited. State exactly which hypotheses of the two conditional results each
derived fact discharges, so the maintainer can lift the conditions. If a fact cannot be derived at reasonable
length (the K-ring in full is the likely one), say what weaker derived statement suffices for the stored use
(for example a faithful character/representation-ring computation on a finite skeleton, or the Atiyah-Hirzebruch
filtration bound) and derive that. Then, if reached: the exact rung count on L^5(4) between the lower bound 3 and e(L).
B: hunt for where the stored conditional results use more than what A derives (hidden use of the full K-ring,
of real K-theory, of orientation conventions); try to find a wall on which k is not determined by
(W, beta w1, signature), which would settle the problem's success clause negatively.

### T2. op.helicity-per-boundary-mode, attack item 1: spin 2
synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional derives J3's channel-reduction
clause in the static GTG gauge for spins 0, 1/2, 1. Do spin 2: the linearised gravitational field about the
Schwarzschild solution, in GA / Gauge Theory Gravity (flat background, gauge fields; linearise the field
strength, or work with the Weyl bivector map's perturbation, whichever gives a closed radial equation). Target:
each (omega, l, m, parity) channel obeys a 2D wave equation in the tortoise coordinate with potential
V = f(r) W(r), f = 1 - 2M/r, W regular at r = 2M (Regge-Wheeler: W = l(l+1)/r^2 - 6M/r^3; Zerilli: the rational
potential with lambda = (l-1)(l+2)/2), so V decays as e^{2 kappa r_*} and each channel is two-dimensional at the
horizon. Exact checks: rational M, polynomial/rational-function identities for the radial operator, the
Chandrasekhar intertwiner between the two parities, and at least one check that the reduced equation is
equivalent to the linearised vacuum equations on that channel (not only quoted). State what is derived and what
is cited (the literature results are prior art; cite from memory with a flag). If the full derivation of the
even-parity reduction is too long, derive the odd parity in full and reach even parity through the intertwiner
(Chandrasekhar's transformation maps solutions to solutions and preserves the horizon behaviour), and say so.
Then state what remains of J3 as premise (current-boson identification, partial-wave lift).
B: test where it fails: l = 0, 1 (no radiative channel; gauge and mass/spin perturbations), the algebraically
special frequencies where the intertwiner degenerates, gauge dependence of "two-dimensional at the horizon",
non-uniformity in l (as for the lower spins), and whether the horizon-regular gauge (PG chart) changes the rate.
Also: does the stored use of J3 for the graviton (hawking.helicity-lift-joints-itemised, J1 homogeneities -6, +2)
match the derived channel count (two parities = two helicities per (l, m))?

### T3. op.qft-structural-inputs, attack item 1: the generation number
Two untested leads from the earlier run. (a) Bridge L1(c): if every massless helicity channel on a light ray
must be registered by its own array (J3 read per light ray, with synthesis.array-ln2-is-zero-mode-doublet-one-tower
clause (iv): one array's current sector is one oscillator tower), then 2 n_V + n_s + 2 eps <= 16 n_g; on the
store's content (12 vectors, 8 real rung components, graviton) 34 <= 16 n_g, so n_g >= 3, independent of the
recurrence choice. The stored tension: synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins.
(b) The Sakharov lead: synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations
(N_V - N_W/4 = 0 exactly at N_g = 3 on 12 vectors and 16 Weyl per generation); C3B called it the stronger lead.
Questions: is either condition derived from stored premises, or a choice? What exactly is the status of the
Sakharov cancellation (is a vanishing induced quadratic coefficient required by a stored premise, for example
the field-space postulate with the frozen point fixing Lambda, or the induced-gravity item of
op.einstein-from-the-field-theory)? Does (a) + asymptotic freedom (n_g <= 5, stored) + the recurrence test
(3 | n_g) pin 3, and under which named premises? Deliver either a theorem "n_g = 3 under premises X, Y, Z"
with each premise's status stated and the fitting risk assessed (the answer 3 is known in advance: say what
would have counted as failure, and whether the counting rule was fixed before the count), or an independence
proof (two models of the full premise set). Take the more defensible of the two; do not inflate.
B: adversarial: counter-models (content with n_g = 2 passing the capacity bound, for example fewer scalars; one
doublet: 2*12 + 4 + 2 = 30 <= 32 passes n_g = 2), whether the bound is a choice of counting rule, whether the
Sakharov weight changes with the scalar content or regulator (gauge dependence of the quadratic coefficient is
noted in op.einstein-from-the-field-theory), look-elsewhere accounting across the store's several "threes".

## Cross-pollination (agent X, separate brief)
A graph-wide read for links between subjects and for new areas to investigate; writes findings/bridges.md and
sends leads on T1-T3 to the attackers through the orchestrator.

## Gate and rules
As BRIEF.md and the previous runs: check4.py exits 0 with no warnings; validate_one ok
(python3 colony/runs/2026-11-06-edge-normality/verify/final/validate_one.py <dir> colony/runs/2026-11-09-three/verify/final);
register with `python3 colony/labcli.py propose_claim @<abs draft json>` (move aside first; copy coverage.yaml back;
quote YAML strings containing ": "); a proposal cannot cite another proposal (E201). Copy the format of a recently
accepted synthesis.* entity of the earlier run (for example
synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional). Everything in GA (no imaginary
unit where a GA unit stands; declare outside_ga otherwise, for example for topology: kind other); results derived,
not imported, with literature as prior art; a result that truly rests on a literature theorem lists it as a
decision for Leon (new imported Facts and new postulates are maintainer-only). House style: no em dashes; never
"honest"/"honestly"/"load-bearing"; Q(v) for squares; no agent or run names in store text. Credit
{name: Claude Fable 5.2, role: proposal and drafting, source: run 2026-11-09-three}. Up to 3 proposals per attacker,
one per target preferred; A and B read each other's findings midway and never file the same result. Run checks
with PYTHONDONTWRITEBYTECODE=1. One gate process at a time per agent (2 CPUs shared); never kill other processes;
do not edit store/, commit, push, switch branch or spawn agents. sympy is not available: Fractions, GA.py and
your own polynomial/rational-function arithmetic. Findings: findings/attack-A.md, findings/attack-B.md, written
early and kept current, ending with "Unexpected links" and "Decisions for Leon".
