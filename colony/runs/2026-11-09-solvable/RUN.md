# Run 2026-11-09-solvable: what is specific to this run

LAB = /home/claude/phys-graph. Run folder: colony/runs/2026-11-09-solvable/ (findings/, work/<name>/, verify/).
Read colony/BRIEF.md and colony/POLICIES.md; this file overrides them. Baseline: baseline.log.

## Goal
Leon asked for the open problems that can actually be solved, attacked with new routes. A triage of all 32 open problems
picked the targets below: finite, checkable questions, or free numbers that an independence proof can close. Most
success clauses accept a no-go or an independence proof; that is a full result here, not a consolation. Several targets
are single attack items of a larger problem: solve the item and say plainly that the problem stays partial.

## Clusters, targets and leads (each lead is a suggestion from the triage; test it, do not assume it)

### C1 topology and horizon modes (attackers C1A, C1B)
- op.wall-class-invariant. Lead: the stored lens-space result (synthesis.lens-space-wall-rung-count-sees-the-integral-twist)
  shows the definite-side count turns on whether L + L is trivial, a K-theory question. Adams' theorem: mL over RP^n is
  stably trivial iff 2^phi(n) divides m (phi(n) = number of i in 1..n with i = 0,1,2,4 mod 8); the mod-2 condition
  (1+x)^m = 1 only needs 2^ceil(log2(n+1)). They first differ at n = 9 (16 against 32). Test whether walls RP^n
  (dim Sigma >= 4) separate ht(w1 L), e(L) and k(Sigma) on definite and indefinite sides, after checking exactly how
  the store defines k and e (synthesis.wall-rung-count-is-height-of-dying-line-class). Also the dim <= 3 table (attack
  item 2). Adams' theorem would be a literature input: name it as a decision for Leon (import as a Fact) rather than
  filing it as a premise yourself.
- op.helicity-per-boundary-mode (J3 at the horizon). Lead: derive the partial-wave reduction in GA instead of importing
  Regge-Wheeler/Teukolsky/Chandrasekhar: Doran, Lasenby and Gull separated the Dirac equation in the Schwarzschild field in
  Gauge Theory Gravity (PG gauge) in the 1990s (prior art, cited from memory). Show, for the massless scalar and Dirac
  fields (spin 1 and 2 if feasible), that each (omega, l, m, s) channel obeys a 2D wave equation in the tortoise
  coordinate with a potential proportional to 1 - 2M/r, decaying as exp(2 kappa r_*) at the horizon, so each channel is a
  two-dimensional mode there. Exact checks on the radial operator (rational M, polynomial identities).
- op.odd-towers, attack item 1 only: the Fock ideals and mass formulas of the odd towers' representatives (dimensions 3
  and 5 under P3), checked against the stored gauge algebras.
C1A constructive; C1B adversarial (find where each lead fails: Adams irrelevant to the store's k, J3 failing for spin 1
or 2 or for massive fields, the odd ideals' mass formulas not matching).

### C2 algebra and gauge loose ends (attackers C2A, C2B)
- op.qft-non-abelian-gauge-fields: (a) the Virasoro relations of the gauge factors' Sugawara parts on the band domain,
  so that the central values 32/7, 2, 1, 1 and remainder 52/7 are central charges in the full sense (stored:
  synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split,
  synthesis.window-energy-of-one-generation-is-exactly-the-so10-sugawara-energy,
  synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves); (b) the Higgs-sector BRST:
  the field-level differential with the Goldstone and doublet terms (s phi), extending
  synthesis.field-level-brst-differential-of-the-derived-gauge-fields-is-nilpotent (nilpotency on all fields, the
  gauge-fixing term exact, the 't Hooft-Feynman gauge with the series' two doublets).
- op.hypothesis-s, last attack item: whether the joint Clifford clause is exactly an instance of the foundation
  postulates (synthesis.signed-directions-and-the-integer-clifford-algebra: directions sharing one central sign bit,
  distinct directions not commuting, generate a Clifford algebra), or asks more (adjoint, signature).
- op.gram-square-and-face-space, attack item 1: decide whether quark brackets satisfy Koide at all (the remaining class
  D2 > D3 > D1); a data check with masses imported or cited (say which), exact where possible.
C2A constructive; C2B adversarial (Virasoro failing on windows (edge terms, the anomaly of the remainder), s phi
nilpotency needing a condition on the vacuum, the sign-bit reduction missing the adjoint, Koide closed negatively).

### C3 the mod-24 lead: generations and the light-ray sea (attackers C3A, C3B)
- op.counted-mode-energy, the open question "which fields form the light-ray sea", and op.qft-structural-inputs (three
  generations). Stored and argued (op.counted-mode-energy known, 31 October): a one-period recurrence of fermion parity
  with the zeta ordering needs the sea's chiral central charge to be a multiple of 24; spin-1/2 content alone gives
  16 n_g, a multiple of 24 iff n_g = 0 mod 3; with the integer-weight fields it is 78 at n_g = 3 and fails. Questions:
  (1) state exactly, with a proof on windows, what the recurrence condition is and that it needs c = 0 mod 24 (the
  -kappa/24 per component, synthesis.null-ordering-of-counted-units-is-zeta-symmetric,
  synthesis.counted-unit-energy-at-half-offset); (2) is the recurrence condition derived from a stored premise (the window
  reading, KMS at period 2 pi / kappa, (N+)), or is it a new choice? If a choice, say so and cost it as a candidate
  premise for Leon; (3) which fields form the sea (decide from the stored light-ray content, J3, and the boson results);
  (4) the consequence for n_g: n_g = 0 mod 3, not n_g = 3; say what would fix 3 rather than 6, 9, ...; (5) the
  right-handed neutrino: the 16 includes it; what changes without it (15 n_g).
  Prior art, check on the web and cite: arguments that link a gravitational anomaly or modular invariance mod 24 (or 16)
  to the number of generations exist in the literature (for example Garcia-Etxebarria and Montero on Dai-Freed anomalies,
  and work on chiral central charges and the 24); find and cite what exists, and say what is new here.
C3A constructive; C3B adversarial (the condition is a choice, the zeta ordering is a convention, bosons must be in the
sea, the test is arithmetic coincidence; look for a counter-model with n_g = 3 failing or n_g = 2 passing).

### C4 independence sweep (attackers C4A, C4B)
Targets (each asks the series to fix a number; the success clauses accept a proof that it cannot):
- op.window-p3: the lowest causal member of each residue (selectors periodic mod 8 argued; make it a proof: a second
  model of every premise with the representative shifted by 8, or a theorem).
- op.pair-sector-current: the 126 coefficient relative to the 10 (attack item 3: independent of every stored relation,
  making the second family's factor 3 an input).
- op.rung-unit: xi G (equivalently v/M_P): a rescaling symmetry of the premise set, or a second model.
- op.thickness-deposit-rule: no rule P2 licenses gives R3 (attack item 1, second half).
- op.residue-killing-weights: the count unit (whether the residue requires the two-array unit given the stored content).
Method: an independence proof exhibits two models of the full premise set (at pinned versions, use cone to list it) that
differ in the number, or a symmetry of every premise that moves it. Exact checks of each premise in both models.
C4A takes window-p3, thickness and the residue; C4B takes pair-sector-current and rung-unit. Each first makes a genuine
attempt to derive the number (the constructive kill test: pre-register what a derivation would need), then proves
independence. Read each other's findings; one strong proposal per problem at most.

## Bridges
One bridge-hunter starts midway: links across clusters (for example J3 and the sea content of C3; the odd towers' ideals
and the window; Sugawara central values and the c = 0 mod 24 test).

## Gate and rules
As BRIEF.md and the previous runs: check4.py exits 0 with no warnings (no W413); validate_one ok
(colony/runs/2026-11-06-edge-normality/verify/final/validate_one.py <dir> colony/runs/2026-11-09-solvable/verify/final);
register with `python3 colony/labcli.py propose_claim @<abs draft json>` (move aside first; copy coverage.yaml back; quote
YAML strings containing ": "); a proposal cannot cite another proposal (E201). Copy the format of a recent accepted
synthesis.* entity (for example synthesis.colour-centre-flux-bounds-polyakov-lines-and-the-leading-glueball-tube).
Everything in GA (no imaginary unit where a GA unit stands; declare outside_ga otherwise); results derived, not imported,
with literature as prior art; a result that truly rests on a literature theorem lists it as a decision for Leon (new
imported Facts and new postulates are maintainer-only). House style: no em dashes; never "honest"/"honestly"/
"load-bearing"; Q(v) for squares; no agent or run names in store text. Credit {name: Claude Opus 5.5, role: proposal and
drafting, source: run 2026-11-09-solvable}. Up to 3 proposals per attacker, one per target preferred. Run checks with
PYTHONDONTWRITEBYTECODE=1. One gate process at a time per agent; 2 CPUs shared by 8 attackers: keep exploration scripts
light, never kill other processes; do not edit store/, commit, push or spawn agents. Findings:
findings/attack-<name>.md (names C1A, C1B, C2A, C2B, C3A, C3B, C4A, C4B).
