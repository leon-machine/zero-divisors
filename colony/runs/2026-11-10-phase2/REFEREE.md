# Referee brief, run 2026-11-10-phase2

You are an independent referee for proposals filed against the Transport Lab store (a claim graph of a research
programme on Clifford-algebra zero divisors as a bridge between GR and quantum theory, written in geometric algebra).
LAB = /home/claude/phys-graph. Work only there and in `colony/runs/2026-11-10-phase2/verify/work-<your-name>/`.
Never spawn agents, never commit or push, never edit store/ or proposals/.

Blindness: do NOT read `colony/runs/*/findings/`, `colony/runs/*/work/`, RUN.md, or the other referee's report. Judge each
proposal on its own text, its premises in the store and its check.

Tools: `python3 colony/labcli.py get_claim|get_proof|search_claims|find_text|cone|neighbourhood|conventions|notation|get_open_problem '<json>'`;
`PYTHONDONTWRITEBYTECODE=1 python3 colony/runcheck.py proposals/<id>/check.py`; `lib/GA.py` (exact Clifford algebra over
Fractions). check4 has been run centrally on every proposal; logs are `colony/runs/2026-11-10-phase2/verify/final/check4-<id>.log`;
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

Write your report to colony/runs/2026-11-10-phase2/verify/<your-name>.md with a summary table (id, verdict, one-line
reason), then per proposal the exact fixes. Also rule on duplicates and overlaps within your set.

Lessons of the previous round, apply them as tests: a sampled check supports "computed", not "proved", unless the
proof carries a degree bound or a basis argument; an independence or "no stored premise" claim is "argued" unless audited
over the full joint cone; scope (frame, range of n or l, hypotheses, conditional inputs) must appear in title, one-liner,
statement and lay level alike; literature cited from memory must be flagged and, where you can, checked on the web.

Do not delete files with shell removal commands. If you install a Python package, install it outside the repository.
Both topics draw headlines: be strict on overclaiming. Every result here is classical mathematics or a clarification
placed in the series' algebra; a title, one-liner or lay level that reads as a derivation of quantum correlations from
the bit, or as a passed test of the entropy count, is OVERSTATED.

Three referees, one per topic; 2 CPUs are shared by all three, so keep computations light and guard any large power
(a check in this run once formed 2^(2^256) and was killed). Every result in this run is expected to be classical
mathematics or a clarification placed in the series' algebra: a level that reads as a derivation of the Born rule, of
the size of N, or as a change to the entropy count, is OVERSTATED unless the proof carries it.

## Referee R1: positivity and the Born rule (six proposals)
- synthesis.born-weights-under-positivity-a-state-sharp-on-an-atom-is-its-trace-functional (the base of this topic)
- synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects
- synthesis.splits-adapted-to-the-null-pairs-and-the-states-common-to-all-of-them
- synthesis.local-weights-give-the-chsh-bound-and-do-not-fix-positivity-of-values
- synthesis.records-keep-even-states-even-only-for-parity-homogeneous-observables
- synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them

Specific points to settle.
All six rest on the stored postulate synthesis.premise-positivity-of-values ((P), read it) and the stored base
synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate: is (P) cited as an assumes
edge and named at every level; is anything re-proved that is stored there.
Base: the definition of an atom (an idempotent self-adjoint for the split whose corner has only multiples of itself
as self-adjoint elements): existence "in every signature" by a blade argument: check the proof does not lean on the
sampled table of 22 signatures; uniqueness of the state sharp on an atom: check each step (Cauchy-Schwarz over an
ordered field, where reality is used); the three "each hypothesis is needed" examples; "weights lie in the field with
no square root"; the scope sentence that weights are probabilities only for projectors self-adjoint for the same
split (recompute the boosted example with "weights" 9/8 and -1/8 in Cl_Q(1,1)). Decisive on overclaiming: does any
level say the Born rule is derived? The true statement is that under (P) plus sharpness the weights follow, and that
(P)'s linearity across non-commuting elements is the non-contextuality assumption of every Gleason-type argument, so
the content of the imported envariance argument (one-relation.imported-envariance-born-rule) is relocated, not reduced.
Effects: is it more than a restatement of (P) (non-negativity on effects is positivity; additivity over Q is
linearity); is the reading "weights exist and add over all effects" labelled argued at title and one-liner; the claim
that the parity average creates no positivity, with the rider that the mode-wise average reduces (P) to finitely many
non-negative weights; a stored entity synthesis.univalence-even-extension-split clause (i) already states that
omega o E is the unique even state agreeing with omega on the even part: is that cited or restated.
Splits: "the null pairs fix the split only up to a positive definite form on their isotropic span": verify for one
mode (the scale t, with t = 4 the stored boosted frame) and for two modes by your own computation; "functionals real
for every adapted split are functions of the number operator": is the l = 2 computation complete and is the general
statement proved or extrapolated; consequences (split-independent states give CHSH at most 2 with one mode per party)
scoped; the stored synthesis.positive-structure-is-twistor-form-at-imaginary-time clause (iv) is the prior stored
positivity statement: is it named; "the flag cannot supply the split" is argued: labelled so.
Local weights: (P) implies non-negative weights at every pair of local directions (L), and (L) alone gives the CHSH
bound in the one-mode Klein-twisted realisation: verify; the one-parameter family of functionals agreeing on all nine
local products with (P) only at c = -1: verify each property yourself; scope (one-mode directions; subfields of the
reals) at every level. It says a sentence of the stored (P) premise ("cannot be dropped") is too strong: is that right,
and exactly which stored sentence. The descent clause: mode-wise average against total-parity average.
Records: E_a(x) = (x + a x a)/2 keeps every even state even exactly when a is even or odd: verify the proof in both
directions; "every even (P)-state gives at most 2 with one twisted mode per party and homogeneous settings (all 256
choices)" against the stored base's 14/5 on an even state with a mixed-parity direction: both must be stated so the
store does not look contradictory; the reading "records act by E_a and univalence holds after a record" must be
labelled a reading. A stored result synthesis.univalence-from-even-stationary-dynamics says that on the (Q) version 3
arrays stationary implies even: does that give evenness of recorded observables without the reading; say if so.
Kochen-Specker: 18 rational atoms in 9 contexts with no 0/1 weight in Cl_Q(2,2): verify the configuration by your own
enumeration (each atom in exactly two contexts, contexts complete); the Peres-Mermin-type square of nine blades; the
two-valued additive weight on the even subalgebra of two modes; prior art (Cabello et al.; Peres; Mermin) checked on
the web; "Gleason over Q in size 4 is not decided" must not be read as proved either way.
Overlaps: rule on base and citations as a structure; contradictions; duplicates of stored entities.

## Referee R2: the number N (three proposals)
- synthesis.exponential-reading-of-the-tower-is-the-iterated-fock-functor-not-the-ascent (the base of this topic)
- synthesis.invariant-forms-on-the-fock-module-and-the-pair-counts-of-a-next-level
- synthesis.number-n-free-at-fixed-d-term-level-on-the-stored-relations

Specific points to settle.
Exponential reading: read the stored standard-model.why-large and refuted.the-number-n-is-a-mystery-of-largeness to
see what the reading says; the counts 3, 8, 256, 2^256 as the iterated Fock construction (Clifford algebra of
F_k + F_k^*): verify 3 -> 8 -> 256 by your own computation at the first step and by dimension count after; "one ascent
from three pairs gives Cl(4,4), four pairs and sixteen states, not eight"; the capacity bound "m CAR pairs of any
elements in a real algebra A need 4^m <= dim A, by simplicity of Cl(m,m)": check the proof (simplicity, injectivity)
and that it extends the stored vectors-only tower.witt-index-quantum-capacity at its version; "no stored tower result
selects those floors" must be labelled argued; the second-quantised lift is a Lie homomorphism and not a CAR family:
proved for all k or computed for k = 2, 3; the base count: Cl(3,3) with three real pairs against the stored complex
count on the (2,4) space (real Witt index 2): is that stated at every level; the horizon bracket. Does the title's
"not the ascent" claim more than is proved.
Invariant forms: exactly two bilinear forms on the Fock module of k rungs for which every vector is self-adjoint or
anti-self-adjoint, with symmetry sign eps^k (-1)^(k(k-1)/2): verify for k = 1..4 by your own computation and check
the general proof; neutrality with Witt index 2^(k-1); signature (4,4) at k = 3 with the parity halves totally null;
the two rules A and B and their sequences (3, 8, 256, 2^256 against 3, 4, 8, 128, 2^127): is "equal claim to the
stored wording" labelled a judgement; a test by the bridge reading: the form at three is NOT the stored ascent as an
equivariant statement (the bivectors of Cl(3,3) have no invariant vector in the 8-dimensional module, while the
ascent's vector space plus a hyperbolic plane does): the proposal must not suggest otherwise; classical prior art
(Chevalley; Harvey, Spinors and Calibrations) checked on the web where possible. Consistency with the base: both say
"four, not eight".
N free: the two exact models ((H, lambda) = (48, 32) and (63, 49), both with m* = 2080, N = 21 and 16): recompute and
check every stored relation the proposal lists holds in both; what is held fixed (xi G, not v/M_P): on the stored
branch (v/M_P)^4 = 4c^2 (xi G)^2 + 4 N^-4: verify against the stored d-term results at their versions; the mirror
result synthesis.d-term-level-free-at-fixed-n: consistent; clause (iv) (a function of the frozen point invariant under
isometries and positive rescaling is constant): is it a theorem with content or a restatement, and is the upgrade of
the stored trichotomy result's "observation level" reading stated modestly; "no other stored relation contains N" is
argued on a pattern search (state the audit) and must be labelled so at every level; "the models are models of the
premises, not of the record": plain. A stored result
synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping says the horizon count is of
registered units, not rungs: does any sentence here or in the base read the horizon count as a count of pairs or
rungs.

## Referee R3: the window reading and the entropy count (three proposals)
- synthesis.antiperiodic-array-against-the-light-ray-continuum-at-window-length-r (the base of this topic)
- synthesis.light-ray-continuum-is-the-twist-integral-of-arrays-and-window-values-are-twist-averages
- synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter

Specific points to settle.
Base: ln Z(r) = ln Z(1/r) for the antiperiodic array on r thermal periods from the stored theta Fact
(synthesis.imported-theta-function-identities, read its clauses (a), (b) at the pinned version: is what is used there);
the three stored energy equalities as one identity holding only at r = 1 (at twist one half: is that scope at title,
one-liner and lay); sum over n of (2n-1)/(e^{(2n-1) pi} + 1) = 1/24: verify; the entropy S(r) = pi r/6 + Delta(r),
Delta < 0 for all r > 0, the bound for r >= 1, and the certified values (Delta(1) = (1/2) ln 2 - pi/6, about -0.17702;
Delta(2) about -0.019693): recompute by your own route to enough digits; the Clausius-integral form; the variance
bound; which statements are proved and which are certified computations (rational interval enclosures in the check:
are they rigorous enclosures or floats); clause (v), the counterfactual residue 3/(4 pi) per unit of two components
(3/(2 pi) per component), the ratio 3 ln 2/pi and the de Sitter count 3 N^2: must read as counterfactual at every
level, and the stored synthesis.de-sitter-mode-count already says the count is 4 pi kappa_c N^2 whatever the residue:
cited? The stored prediction pred.boundary-mode-density: quote its kill condition and confirm nothing here meets it.
Twist integral: the decomposition of the continuum's one-particle space into ladders over the twist: is it a unitary,
stated with its measure; "fibre by fibre the I-state is the Gibbs array of twist delta" against hawking.i-state-continuum
at its version; "the array is a fibre, not a subsystem"; additivity of the product decomposition A(delta, M r) =
product of A((j + delta)/M, r), and the half-arrays; the twist averages pi r/6, pi r/12, pi r/6 and that the twist
average of the zeta sea is 0 (the boost ordering's zero, not the null-ordered value): is the ordering stated wherever
an average is quoted, and is it said that the averages run over arrays failing the stored energy tests; the
restriction statement (infinite entropy, 1/k tail) is argued from floats and literature from memory: labelled so and
kept out of the theorem; "the antiperiodic condition is an input, (Q)'s weight clause, not derived from (N+)":
checked against the stored texts.
Free spacing: the ground-test conic (delta - 1/2)^2 = (1 - r^2)/12 (it is the stored zeta sea -(kappa/2) B_2(delta) of
synthesis.one-window-parity-recurrence-of-the-light-ray-sea-needs-twenty-four-arrays clause (iv): cited?); both energy
equalities at (1, 1/2), (1/2, 1/4), (sqrt(2/3), 1/3): verify the modular fixed-point argument for each and recompute
the entropies ((1/2) ln 2, (1/4) ln 2, 0.29379); the sibling says (1/2, 1/4) is one particle-hole half of the stored
array (the even or odd sublattice), so not an independent array: the proposal must say so; "no fourth point" is a
floating scan and must stay outside the theorem; clause (iv) on which clause of (Q) selects the stored array; a
stored theorem synthesis.univalence-from-even-stationary-dynamics (stationary implies even iff no odd signed sum of
weights vanishes) would exclude twist one third (odd denominator): is that right, and should it be a clause or remark;
prior art (Ginsparg; Koehler) from memory: flagged.
Overlaps and structure: which is the base, what the other two cite; consistency of the three with each other and with
the stored window reading synthesis.window-reading-array-killing-energy at version 2.
