# Referee brief, run 2026-11-10-phase3

You are an independent referee for proposals filed against the Transport Lab store (a claim graph of a research
programme on Clifford-algebra zero divisors as a bridge between GR and quantum theory, written in geometric algebra).
LAB = /home/claude/phys-graph. Work only there and in `colony/runs/2026-11-10-phase3/verify/work-<your-name>/`.
Never spawn agents, never commit or push, never edit store/ or proposals/.

Blindness: do NOT read `colony/runs/*/findings/`, `colony/runs/*/work/`, RUN.md, or the other referee's report. Judge each
proposal on its own text, its premises in the store and its check.

Tools: `python3 colony/labcli.py get_claim|get_proof|search_claims|find_text|cone|neighbourhood|conventions|notation|get_open_problem '<json>'`;
`PYTHONDONTWRITEBYTECODE=1 python3 colony/runcheck.py proposals/<id>/check.py`; `lib/GA.py` (exact Clifford algebra over
Fractions). check4 has been run centrally on every proposal; logs are `colony/runs/2026-11-10-phase3/verify/final/check4-<id>.log`;
do not rerun check4. WebSearch/WebFetch are allowed to check literature; say what you verified and what you could not. One
heavy process at a time (2 CPUs shared with the other referee).

For each proposal: (1) check every proof step; confirm each cited store entity says what is needed at the pinned version;
(2) run and read the check, make at least two targeted perturbations and confirm it fails, recompute one key number by your
own route; (3) hunt hidden hypotheses, overclaiming at title/one-liner/lay level, "proved" where only argued, literature
misquoted or cited from memory, circularity (use `cone`), classical results presented as new, duplicates of stored entities
and of each other; for an independence proof: are both models models of the FULL premise set at the pinned versions (list
it with `cone`; a premise missing from the audit is a defect), and does the moved quantity really differ; (4) verdict:
SOUND; SOUND WITH FIXES (exact fixes); OVERSTATED (the true weaker statement at every level); WRONG (counterexample or
failing step); UNCLEAR (what decides it).

House style: no em dashes; never "honest"/"honestly"; never "load-bearing"; Q(v) for the square of a vector; macros only
from store/notation.yaml. Leon's rules (check as fixes): everything in geometric algebra; results derived, not imported
(literature as prior art only); no imaginary unit where a GA unit can stand (store/conventions.md, unit principle).

Write your report to colony/runs/2026-11-10-phase3/verify/<your-name>.md with a summary table (id, verdict, one-line
reason), then per proposal the exact fixes. Also rule on duplicates and overlaps within your set.

Lessons of the previous round, apply them as tests: a sampled check supports "computed", not "proved", unless the
proof carries a degree bound or a basis argument; an independence or "no stored premise" claim is "argued" unless audited
over the full joint cone; scope (frame, range of n or l, hypotheses, conditional inputs) must appear in title, one-liner,
statement and lay level alike; literature cited from memory must be flagged and, where you can, checked on the web.

Do not delete files with shell removal commands. If you install a Python package, install it outside the repository.
Both topics draw headlines: be strict on overclaiming. Every result here is classical mathematics or a clarification
placed in the series' algebra; a title, one-liner or lay level that reads as a derivation of quantum correlations from
the bit, or as a passed test of the entropy count, is OVERSTATED.

Three referees; 2 CPUs are shared by all three, so keep computations light and guard any large power. This run is
consolidation: statements of exposure, no-gos, premise audits and textbook results placed in the series' algebra. A
level that reads as a mechanism for the spectrum, a derivation of the dark-matter ratio, a test passed by dark
energy, or new quantum field theory is OVERSTATED unless the proof carries it. Leon's position, to apply as a rule on
wording: the graviton does not exist in the series; no proposal may present quantisation of the gravitational gauge
fields as a goal or a gap, or extend a stored counting of a graviton.

## Referee R1: dark energy and the primordial spectrum (three proposals)
- synthesis.norm-released-locally-on-isotropic-fields-tracks-dust-and-never-accelerates
- synthesis.red-tilt-criterion-on-power-law-stages-and-the-index-ledger-of-the-stored-sources (base of the spectrum topic)
- synthesis.scalar-sector-at-the-isotropic-scalar-kasner-point-obeys-the-spectator-equation

Specific points to settle.
Released norm: the frozen-point MacDowell-Mansouri functional with the norm u = 3/Lambda released as a local field on
homogeneous isotropic reflection-invariant GTG fields with flat slices: rederive the four equations and the
elimination Lambda(rho - 3p) = rho(rho + 3p) by your own route; "dust: Lambda = 8 pi G rho, deceleration 1/2; radiation:
no solution; vacuum: u(t) free" each verified; the hypothesis (Mat) on how matter couples (read the stored statement):
is every conclusion labelled as under (Mat), flat slices, no axial torsion, bare functional (c_3 = c_5 = 0), one fluid,
at title, one-liner and lay level; "never accelerates" in the title against that scope; the relation to
synthesis.promoted-norm-weyl-clock-flat-weight clause (v) (the same equation with the clock density set to zero): new
content or a corollary; clause (vii) on the promoted norm keeping w = -1: cited from synthesis.promoted-norm-one-global-pair
at its version or re-proved; does any level say or imply the series "has no fallback" as a theorem (that is an argued
audit, a search of the store, and must be labelled so). Prior art on a dynamical Stelle-West norm (Westman and
Zlosnik) checked on the web.
Red-tilt criterion: every stored mode equation of the form chi'' + (1+f) chi'/T + (k^2 T^(-2P) - kappa/T^2) chi = 0 is
red exactly when f^2 + 4 kappa > 9(1-P)^2, given the stored index 3 - 2 nu: verify the Bessel reduction and the
inequality by your own route, including sign conventions for "red" and the stored definition of the index; "every
stored wall has unit trace of exponents so stored wall geometry never reddens": which stored statement gives unit
trace, at what version, and is "every" audited or sampled; the 24-row ledger: spot-check at least six rows against
the stored entities they quote (index, equation, premises) and say which you checked; the windows (p in [0.66791,
0.66930], fluid w = -0.0029 as 12w/(1+3w), p in [42.9, 89.9]) recomputed, with the data value they rest on named and
its stored Fact pinned; the conditional clause on dust plus the constant run as a contraction: labelled conditional
on a stage the store does not hold, at every level; the running relation (running = -6 x index, +0.21) and the
"32 sigma" against a Planck running quoted from memory: a number from memory may not appear above the proof text or
carry a significance in a statement level unless a stored Fact holds it; Cai and Wilson-Ewing (arXiv 1412.2914)
checked on the web; "no other stored structure" is a pattern search (241 matched, about forty read): labelled argued
at title, one-liner, technical and lay. Does the title or lay level read as a no-go theorem over the series when it is
a criterion plus an argued ledger.
Kasner scalar sector: at the isotropic point of the scalar Kasner disk, in the gauge with unperturbed spatial metric,
the linearised field equations force f = u, b = tau^(2/3) u'/k and reduce to u'' + u'/tau + k^2 tau^(-2/3) u = 0: verify
the linearisation in the store's GTG setting (which stored background, which stored field equations, at what
versions), the gauge choice and residual gauge freedom, and that the reduced equation is equivalent to the
linearised equations (not only implied by them); "the gauge-invariant curvature perturbation is u/3": which
definition, verified; the consequence "blue index, so the stored Kasner kill is not a gauge or spectator artefact"
is given the stored adiabatic vacuum and a k-independent normalisation assumed, not rederived: labelled at every
level; scope "isotropic point only" in title and one-liner.
Overlaps: the base and the Kasner result (rows 23, 24 of the ledger point to it); with stored Kasner and spectrum
entities (search before accepting novelty).

## Referee R2: dark-matter premises (two proposals)
- synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball (base of the topic)
- synthesis.constituent-momentum-is-the-unique-spin-covariant-quadratic-vector-on-the-spinor-ideal

Specific points to settle.
Mass per unit ball: read dark-matter.unit-ball-rule, dark-matter.total-function-thickness and the postulates R1, R2,
R3, D, P2, P3 at their stored versions. Clause (i): every share depends on R1 and R2 only through (E), equal mass per
unit ball: verify by your own computation, and decide the point raised against it: the store ties R3's thickness
unit to "the cell radius R2 chose"; under the reading in which each tower's thickness is in its own cell radius the
total moves with the density law intact (a claimed exact example 11/3 + 32/(3 pi) = 7.06): recompute it and say
exactly which reading of R3's unit the clause needs, and whether that reading is stated at title, one-liner,
technical and lay level; the model "both R1 and R2 violated, every share kept": is it a model of the rest of the
premise set of the total (list the past cone of the closed form with `cone`; a premise missing from the audit is a
defect); "D is (E) in the unit of the de Sitter radius, given the stored sphere reading" and "D and R1+R2 do not
imply each other ((ell/d)^D)": verify; "the mirror's share of one is obtained twice" and the 1/200 difference on the
burning branch: verify from the stored population count; "cubic cells give exactly 5": verify; the count "5 of 23 (8
with the population count)": recompute the past cone yourself and list the postulates. Does any level read as a
derivation or a confirmation of 5.364; the true statement is a reduction of which premises the fit uses. Statements
about what was chosen with the number known must quote the store, not outside notes.
Constituent momentum: in the six causal towers of dimension 3, 4, 5 the spin-covariant quadratic maps from the
spinor ideal to vectors form one real line spanned by H1's momentum: verify the rank computation over Q by your own
route for at least dimension 3 and one tower of dimension 4 (what "spin-covariant" means exactly: which group, which
action on the ideal, left or two-sided; real or complex line); "psi e_t rev(psi) is a pure vector in dimensions 3 and
4; in dimension 5 it is j + s I": verify; m^2 = s^2 against dark-tower-matter.where-mass-begins at its version; the
two-constituent cross terms (dimensions 3 and 4; dimension 5 not computed: said at every level); the reading "H1 is
weakened, not retired" labelled argued; the conjecture was formed after a first probe: is the check a real test
(complete rank, not a sample); classical representation theory: prior art named, flagged if from memory; H1 is not
in the result's past cone: confirm with `cone`.
Overlaps and structure: the two do not overlap; rule on whether either duplicates stored dark-matter results.

## Referee R3: quantum field theory (three proposals)
- synthesis.protraction-identity-of-the-curvature-operator-from-vanishing-torsion (cite-first: the curved-field proposal will cite it)
- synthesis.curved-field-vacuum-polarisation-freedom-is-five-local-covariant-constants-of-which-one-is-transverse
- synthesis.one-loop-self-energy-and-vertex-extend-with-the-ward-identity-holding-at-a-common-cut-off-length

Specific points to settle.
Protraction identity: vanishing torsion gives d_a ^ calR(a ^ b) = 0: check every proof step from the stored definition
object (which clauses), the grade count, and the general formula with torsion C(g^mu)/2 = D ^ Theta^mu - Theta^nu ^
D_nu g^mu with signs, by your own exact computation on one torsion-free and one torsion field; the inversion
P(c) = C(c)/2 - c.(d_e ^ C(e))/4 "in every dimension and signature": proved or computed for d = 3, 4, 5; the converse
fails (Omega = 0 with a non-holonomic coframe: zero curvature, nonzero torsion): is that sentence in the statement;
the kernel dimension d^2(d^2-1)/12; it is the classical first Bianchi identity and the route is Lasenby, Doran and
Gull 1998 section 5: check on the web and make sure the levels say classical; is it already stored (search the
dictionary Fact and pairing.loop-classes-are-weyl-components).
Curved-field freedom: read the stored synthesis.vacuum-polarisation-kernel-on-a-gravitational-field-has-the-flat-leading-part-and-no-weyl-term-of-degree-four
clause (iv) and the imported local-covariance Fact at their versions. The difference of two local covariant
extensions is c1 Lap + c2 D(D.) + c3 m^2 + c4 (scalar curvature) + c5 (Ricci map): verify the invariant count (exact
ranks under the Lorentz algebra; 2 curvature terms under the protraction identity, 3 without, 6 for general maps) by
your own route; transversality leaves c (1, -1, 0, 0, 1): verify with the store's sign of the Ricci term; decisive on
overclaiming: the Fact classifies DIFFERENCES of extensions; existence of a transverse (Ward-preserving) local
covariant extension is not in it; the Fact's sources are for a scalar field (check gr-qc/0103074 and gr-qc/0111108
on the web; Zahn arXiv 1210.4031 and 1311.7661 for the Dirac field) and concern the time-ordered product; the
scaling degree omega = 2 on the field is argued; torsion is outside. So every level must say "if a transverse local
covariant extension exists" and "given the imported Fact, sourced for scalar fields", and the title's "is five
constants of which one is transverse" must not read as closing the stored argued clause. The protraction identity
is stated as a hypothesis (a proposal cannot cite a proposal): fine for now; say what the citation should be.
One-loop self-energy and vertex: on the Euclidean section in Cl(4,0), self-energy extended by first-order Taylor
subtraction on the ball |x - y| < l, vertex by subtracting the value at the origin on the cylinder: the
Ward-Takahashi identity holds exactly on the extended kernels for every gauge parameter and mass. The checks test
ingredients and constants, not the identity: so referee the proof, Steps 3 to 5, line by line (integration by parts
on the cut-off regions, boundary terms at |x - y| = l, the cylinder against the ball: why a common length is needed
and the failure term (xi e^2/(8 pi^2)) ln(l_V/l_Sigma)); recompute the kernel constants (-xi e^2/(4 pi^4), (3 + xi) e^2
m/(16 pi^4)) and ln(M_Sigma^2/M_V^2) = 1/2 by your own route and check the literature value in arXiv hep-th/9709067
on the web; "derived, not imposed": the identity is built in by the choice of subtraction regions: is that said;
scope: Euclidean section only (the cylinder does not transfer to Lorentzian signature), massive case given standard
propagator properties not checked, F2(0) and on-shell conditions untreated: at title, one-liner, technical and lay;
"the Scharf import is not needed" must read "on the Euclidean section"; it is textbook physics (Freedman, Johnson,
Latorre; differential renormalisation): the levels must say so and claim nothing beyond existence of one
Ward-preserving pair at one loop; the stored regulator-free vacuum-polarisation result: what exactly it imported and
whether this discharges it; GA: no Dirac matrices where the store uses GA.
Overlaps: the curved-field result and the protraction identity as a structure; any of the three against stored
field-theory.* entities.
