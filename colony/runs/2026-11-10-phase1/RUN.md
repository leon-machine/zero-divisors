# Run 2026-11-10-phase1: what is specific to this run

LAB = /home/claude/phys-graph (branch run/2026-11-10-phase1, from main at 2371f35). Run folder:
colony/runs/2026-11-10-phase1/ (findings/, work/<name>/, verify/). Read colony/BRIEF.md and colony/POLICIES.md; this
file overrides them. Baseline: baseline.log (0 errors, 0 warnings).

## Goal
Leon approved phase 1 of the theory action plan of 10 November: two targets chosen from a read of the whole graph, not
from the open-problem list. A negative result established with exact checks is a full result. Both targets are
headline topics, so the standard on overclaiming is strict: say exactly what is classical mathematics rooted in the
series' postulates and what is new.

## Cluster E: entanglement from the foundation (attackers EA constructive, EB adversarial)
The graph has no Bell, CHSH or Tsirelson result. The foundation layer says directions sharing one central sign bit,
with distinct directions not commuting, generate a Clifford algebra: synthesis.premise-the-bit (F1),
synthesis.premise-minimal-non-commutativity (F2), synthesis.premise-superposition-over-the-integers (F3),
synthesis.continuum-completion-premise (F4), synthesis.signed-directions-and-the-integer-clifford-algebra,
synthesis.composition-cycles-counting-needs-addition, synthesis.division-gives-the-rationals,
synthesis.the-sign-is-the-rotor-at-infinity (rational rotors of the plane). Subsystems in geometric algebra:
synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product (sub-Clifford algebras, blade
projection, Klein twist). Also read synthesis.quarter-turn-rotors-of-the-even-subalgebra-form-a-state-design-of-order-three
and the measurement results under one-relation.* (record-chain votes; the imported envariance Born rule).
- E1. The CHSH bound. State the CHSH combination for two subsystems of one Clifford algebra (settle the role of the
  Klein twist: observables of the two parties must commute, so say which elements are the parties' observables), and
  prove: for observables of square one, the square of the CHSH element is 4 minus the product of the two commutators
  (fix the sign convention), so its extreme value is 2 sqrt 2, attained exactly when each party's two directions
  anticommute. Say exactly which premises are used: F1 to F3 for the algebra; and what notion of "value" or
  "state" is needed to turn an operator identity into a bound on correlations (a positive scalar-part functional, the
  stored Hermitian structure, or something else): if a positivity or state-space premise beyond F1 to F4 is needed,
  NAME it exactly; it is then a decision for Leon, not a hidden hypothesis. Exhibit the saturating state in GA.
- E2. Attainment before the continuum. Over the integers and the rationals (F1 to F3, before F4): is 2 sqrt 2 attained
  or only approached? Use the rational rotors of the plane. Decide exactly: the supremum over rational directions and
  rational states, whether it is attained, and the best value at small denominators (a sequence with a proved limit,
  for example through Pell-type approximants of sqrt 2, would be the result). State what "state with rational
  coefficients" means and whether normalisation needs a square root.
- E3. If it follows from the same anticommutation: a monogamy statement for three parties (for example the
  Toner-Verstraete quadratic trade-off for CHSH values, or the weaker statement that two pairs cannot both exceed 2),
  proved in the algebra; and the local bound 2 for commuting directions (the "classical" case as the commutative
  subalgebra), so the three values 2, 2 sqrt 2 and the algebraic maximum 4 are all placed.
- E4 (findings unless a result drops out): what this adds to the stored measurement account and what it does not;
  whether the Born weights (squared norm as scalar part of a product with a projector) can be derived in the store
  from a named premise in place of the imported envariance argument. Do not file a Born-rule claim in this run; it is
  phase 2.
Prior art, to check on the web and cite: Tsirelson (Cirel'son) 1980 for the bound and its Clifford-algebra proof;
Landau 1987 for the operator identity; Toner and Verstraete for monogamy; Doran and Lasenby (multiparticle spacetime
algebra, the singlet state) and Hestenes for GA treatments; the reconstruction literature on why not more than 2 sqrt 2
(Popescu-Rohrlich boxes; information causality). Say plainly that the bound is classical mathematics and that what is
new, if anything, is its rooting in F1 to F3, the subsystem split in GA, and E2.
EB adversarial: is the Klein-twisted split the right notion of "two parties" (do fermionic parity superselection and
the graded tensor product change the bound: there is a literature on CHSH with fermionic modes and superselection;
check it); does the bound need positivity not in the foundation; is "anticommuting" forced or one of several
maximisers; does E2 collapse (is 2 sqrt 2 attained with rational data after all, for example with unnormalised states
or because only ratios matter); is anything here more than Tsirelson restated.

## Cluster K: the Kerr entropy test (attackers KA constructive, KB adversarial)
The boundary-mode count is calibrated on the Schwarzschild field (pred.boundary-mode-density, scrambling.mode-count,
singularity.c1-curvature-cutoff, singularity.c2-cell-density, singularity.c3-counted-epoch,
scrambling.residue-each-convention, synthesis.de-sitter-mode-count). Stored for Kerr:
synthesis.kerr-ring-count-misses-area-law (the counting rule read literally on the Planck-curvature locus gives
N/(A_+/4) of order M^{-1/3}, not 1), synthesis.imported-kerr-surface-gravity-entropy,
synthesis.kerr-ring-connection-limit-null-rotation-winding-three, interior.imported-kerr-schild-form-kerr-gauge,
hawking.i-state-continuum; op.kerr-ring attack items 2 and 3 (get_open_problem; read its `known` in full: it records
that superradiance leaves no global KMS state at fixed angular velocity). Everything in Gauge Theory Gravity (flat
background, gauge fields; the Kerr gauge field in Kerr-Schild form).
- K1. Decide what the Schwarzschild count actually counts, in a form that can be carried to Kerr: restate the stored
  count (rate nu/T_H per Killing time, one modular period as the counted epoch, N_epoch ln 2 = S_BH) as a statement
  about the horizon's modular data (surface gravity, cross-section area, the Killing flow), and say which step used
  the curvature cutoff (C1) and which used only the horizon.
- K2. Carry that to Kerr on the co-rotating Killing flow chi = d_t + Omega_H d_phi: compute the count per modular
  period 2 pi / kappa_+ as a function of (M, a), exactly, and compare with A_+/4 = pi (r_+^2 + a^2). First computation:
  the slow-rotation expansion to second order in a/M; then the exact expression; then the extremal limit kappa_+ -> 0.
  Exact checks with rational M and a chosen so that sqrt(M^2 - a^2) is rational.
- K3. Verdict, pre-registered: (a) the horizon reading reproduces A_+/4 identically, in which case say whether that is
  a test or a tautology (if the count is defined from kappa and A it cannot fail: then the content is that the ring
  reading is wrong and C1 must be restated as a horizon statement; say what C1 becomes and whether Schwarzschild is
  unchanged); (b) it mismatches by a function of a/M: then name the premise that carries the blame (C1, C2, C3, the
  residue, or (N+) whose scope does not include Kerr) and whether pred.boundary-mode-density's kill condition is met.
  State the rotating analogue of the I-state: which channels fail to have a KMS state (superradiant modes,
  omega < m Omega_H) and what the count does with them.
- K4 (findings unless a result drops out): the angular-momentum ledger: does the count per period carry the hole's
  spin (Smarr: M = 2 T S + 2 Omega J), and does the two-array unit of the residue see it (op.residue-killing-weights
  item 2 names a spinning-hole test).
KB adversarial: show the horizon reading is circular if it is (the count calibrated to reproduce A/4 on Schwarzschild
by choice of nu: then Kerr adds one free function unless nu is spin independent: test exactly that: is the SAME nu,
with no new input, enough); look for a spin-dependent ingredient the rule lacks (the frame-dragged cell density, the
proper length of the generators' period, the superradiant sector); test the extremal limit (zero temperature, finite
area: a count per modular period with infinite period); check the stored ring result's hypothesis a >= 2(2M)^{2/3}
against the horizon reading; say whether the test discriminates anything.

## Bridge
One bridge-hunter midway (for example: the mode count per light ray against the CHSH setting; the Klein twist in both
clusters; the two-array unit and entangled pairs across the horizon; monogamy against the stored monogamy/firewall
note note.singularity.monogamy-firewalls-small-corrections-theorem).

## Gate and rules
As BRIEF.md and the previous runs: check4.py exits 0 with no warnings (pin literals so no W413); validate_one ok
(python3 colony/runs/2026-11-06-edge-normality/verify/final/validate_one.py <dir> colony/runs/2026-11-10-phase1/verify/final);
register with `python3 colony/labcli.py propose_claim @<abs draft json>` (move aside first; copy coverage.yaml back;
quote YAML strings containing ": "); coverage kinds are only exact, complete, sampled, partial; a proposal cannot cite
another proposal (name siblings in the extraction note as intended citations). Copy the format of a recently accepted
synthesis.* entity (for example synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product).
Everything in GA: no imaginary unit where a GA unit stands, no Pauli or Dirac matrices (declare outside_ga otherwise);
gravity in GTG. Results derived, not imported, with literature as prior art; a result that truly rests on a literature
theorem lists it as a decision for Leon (new imported Facts and new postulates are maintainer-only). Lessons of the
last referees, apply before filing: a sampled check supports "computed", not "proved", unless the proof carries a
degree bound or basis argument; "no stored premise" and independence claims are "argued" unless audited over the full
joint cone; scope and conditions go in title, one-liner, technical and lay levels alike (W503); test signs against the
stored conventions, not against your own gauge. House style: no em dashes; never "honest"/"honestly"/"load-bearing";
Q(v) for squares; no agent or run names in store text. Credit {name: Claude Fable 5.2, role: proposal and drafting,
source: run 2026-11-10-phase1}. Up to 3 proposals per attacker, one per target preferred; siblings read each other's
findings midway and never file the same result. labcli is slow (each call loads the store): prefer reading entity
files directly under store/claims/<id>/ for content and use labcli for cone, validate and propose. Run checks with
PYTHONDONTWRITEBYTECODE=1. One gate process at a time per agent (2 CPUs shared by four attackers); never kill other
processes; do not delete files with shell removal commands; do not edit store/, commit, push, switch branch or spawn
agents. sympy is not available: Fractions, GA.py and your own exact arithmetic. Findings:
findings/attack-<name>.md (EA, EB, KA, KB), kill conditions pre-registered before computing, kept current, ending with
"Unexpected links" and "Decisions for Leon".
