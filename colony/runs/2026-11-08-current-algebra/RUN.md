# Run 2026-11-08-current-algebra: what is specific to this run

LAB = /home/claude/phys-graph. Run folder: colony/runs/2026-11-08-current-algebra/ (findings/, work/<name>/, verify/).
Read colony/BRIEF.md and colony/POLICIES.md; this file overrides them. Baseline: baseline.log (0 errors, 0 warnings).

## Target
op.qft-non-abelian-gauge-fields, the attack item "The current algebra along generators" (store/open_problems.yaml; read
its statement, known including the 8 November paragraph, and attack items). On a finite window of a null generator the
channels' pair currents satisfy exactly the level-one u(n) current algebra
(synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators (i)), with energy quadratic in the currents
(synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves); per light ray and generation
there are sixteen channels, the Weyl components (synthesis.slot-module-light-ray-arrays-are-weyl-components). Questions:
(1) the exact embedding of the Standard Model gauge algebra (and the series' gauge algebra of the minimal massive
composite: synthesis.gauge-algebra-by-tower, standard-model.gauge-algebra-minimal-massive-composite) in these u(16)
currents: which channel-unitary matrices realise it, on which channels, and the level of each simple factor and of the
abelian factors (the Dynkin index of the embedding times the level one of u(16)), exactly, on finite windows (the
window form of the central term, edge-clean vectors, as the stored entities state it);
(2) the Sugawara decomposition: the energy along a generator as the sum of the gauge-factor Sugawara parts and a coset
part, exact on windows, with the central charges counted (c = 16 for sixteen complex chiral fermions, split among the
factors and the coset); whether the decomposition is exact on finite windows or only on edge-clean vectors;
(3) what this does and does not give for the four-dimensional Yang-Mills field: say precisely (it is a current algebra
along each generator, kinematics and a 1+1 dynamics, not the gauge field; anomalies: the level and the anomaly
cancellation per generation may be related; check exactly, do not assert).
Success: an exact finite statement of the embedding and the levels, or of an obstruction (for example a factor that does
not act by channel-unitary matrices because a gauge generator mixes chiralities across the light ray's two arrays).

## Pairs
Attacker A (constructive): build the embedding and compute the levels and the Sugawara split exactly.
Attacker B (adversarial): find what fails: chirality mixing, hypercharge normalisation, the abelian factor's level depending
on the chosen normalisation, edge terms that spoil the window form, anomalies; and test whether the u(16)_1 current algebra
is the right object at all (the store's channels may be real or complex with the unit J: settle which, and whether the
currents are u(16) or so(32)).
Both: everything in GA (unit J for the boson-like currents, I4 where the unit principle says; no imaginary unit), derived
not imported (Kac-Moody, Sugawara, Frenkel-Kac, conformal embeddings, Goddard-Kent-Olive cosets as prior art in the
extraction note only), exact checks (Fractions, lib/GA.py). Up to 2 proposals each; read your sibling's findings midway and
at the end.

## Gate and rules
As BRIEF.md and the previous runs: check4.py exits 0 with no warnings (no W413); validate_one ok
(colony/runs/2026-11-06-edge-normality/verify/final/validate_one.py <dir> colony/runs/2026-11-08-current-algebra/verify/final);
register with `python3 colony/labcli.py propose_claim @<abs draft json>` (move aside first; copy coverage.yaml back; quote
YAML strings containing ": "); a proposal cannot cite another proposal (E201). House style: no em dashes; never
"honest"/"honestly"/"load-bearing"; Q(v) for squares; no agent or run names in store text. Credit {name: Claude Opus 5.5,
role: proposal and drafting, source: run 2026-11-08-current-algebra}. Run checks with PYTHONDONTWRITEBYTECODE=1. One gate
process at a time; 2 CPUs shared; never kill other processes; do not edit store/, commit, push or spawn agents. Findings:
findings/attack-A.md, findings/attack-B.md.
