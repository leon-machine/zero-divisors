# Referee brief, run 2026-11-10-phase1

You are an independent referee for proposals filed against the Transport Lab store (a claim graph of a research
programme on Clifford-algebra zero divisors as a bridge between GR and quantum theory, written in geometric algebra).
LAB = /home/claude/phys-graph. Work only there and in `colony/runs/2026-11-10-phase1/verify/work-<your-name>/`.
Never spawn agents, never commit or push, never edit store/ or proposals/.

Blindness: do NOT read `colony/runs/*/findings/`, `colony/runs/*/work/`, RUN.md, or the other referee's report. Judge each
proposal on its own text, its premises in the store and its check.

Tools: `python3 colony/labcli.py get_claim|get_proof|search_claims|find_text|cone|neighbourhood|conventions|notation|get_open_problem '<json>'`;
`PYTHONDONTWRITEBYTECODE=1 python3 colony/runcheck.py proposals/<id>/check.py`; `lib/GA.py` (exact Clifford algebra over
Fractions). check4 has been run centrally on every proposal; logs are `colony/runs/2026-11-10-phase1/verify/final/check4-<id>.log`;
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

Write your report to colony/runs/2026-11-10-phase1/verify/<your-name>.md with a summary table (id, verdict, one-line
reason), then per proposal the exact fixes. Also rule on duplicates and overlaps within your set.

Lessons of the previous round, apply them as tests: a sampled check supports "computed", not "proved", unless the
proof carries a degree bound or a basis argument; an independence or "no stored premise" claim is "argued" unless audited
over the full joint cone; scope (frame, range of n or l, hypotheses, conditional inputs) must appear in title, one-liner,
statement and lay level alike; literature cited from memory must be flagged and, where you can, checked on the web.

Do not delete files with shell removal commands. If you install a Python package, install it outside the repository.
Both topics draw headlines: be strict on overclaiming. Every result here is classical mathematics or a clarification
placed in the series' algebra; a title, one-liner or lay level that reads as a derivation of quantum correlations from
the bit, or as a passed test of the entropy count, is OVERSTATED.

## Referee R1: entanglement (six proposals)
- synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate
- synthesis.chsh-over-the-rationals-pure-states-on-a-circle-and-the-pell-records
- synthesis.three-party-trade-off-of-chsh-values-and-the-local-value-two
- synthesis.signatures-in-which-commuting-observables-exceed-the-chsh-value-two
- synthesis.chsh-with-parity-even-observables-needs-two-modes-per-party-and-no-klein-twist
- synthesis.chsh-bound-needs-positivity-across-settings-and-anticommutation-holds-only-on-the-state

Specific points to settle.
Hypothesis (P) (values are a linear, normalised functional non-negative on x x-dagger, dagger the blade inverse): is it
stated as a hypothesis, with the same wording, at every level of every proposal that uses it; is it exactly what each
proof uses (does any proof also use omega(x-dagger) = omega(x), or positivity on elements not of the form x x-dagger);
is "dagger = blade inverse" well defined and an anti-automorphism in every signature used, and is positivity
frame-dependent in indefinite signature as one proposal says (then which elements count as observables must be stated).
The certificate 8 - C^2 = (1/2)(Z-dagger Z + {A1,A2}^2 + {B1,B2}^2), Z = [A1,A2] - [B1,B2]: verify by your own
computation with noncommuting symbols or exact matrices over Q, including the hypotheses (self-adjoint, square one,
the parties commute) and the sign conventions; the example A = (17/8)e1 + (15/8)f1 with CHSH value 17/4.
The signature list: recompute by your own enumeration that every CHSH configuration has C^2 = 4 in exactly the fourteen
signatures listed and that the others admit C^2 = 4 + 4K; is "matrix size at most 2" the right reading against the
stored classification of real Clifford algebras; is the statement about Cl(1,3) against Cl(3,1) worded so that nobody
reads it as "no Bell violation in spacetime signature" (it concerns two commuting pairs inside ONE copy of the algebra).
The parity result: even observables of disjoint mode sets commute without a twist; one mode per party gives at most 2;
two modes per party reach every rational value below 2 sqrt 2; the twisted one-mode violation uses parity-odd elements.
A decisive check on notation: the values 14/5, 82/29, 478/169 are reported as 2(c + s); on the stored pair state with
AMPLITUDES c, s the maximum is 2 sqrt(1 + 4 c^2 s^2), which is smaller unless c = s. Establish exactly which state and
which directions give 14/5 (it should be the equal-weight state with (c, s) the rational point of one party's
directions) and require the text to say so unambiguously wherever c, s appear.
The positivity counter-model: the functional lambda(x) = <(1 + C) x>_0 on the integer algebra: normalised, non-negative
no-signalling probabilities at every setting pair, CHSH value 4, failing only lambda((C - t)^2) >= 0: verify each
property yourself; is "the bound uses positivity on exactly (C-t)^2 and (1-K)^2" proved; is "no stored premise supplies
positivity" labelled argued.
The rational proposal: the circle X^2 + Y^2 = 8 of pure states of the sector; the orbit under the stored rational rotor;
the denominator law 8 - (P/Q)^2 >= 4/Q^2 with equality on x^2 - 2 Q^2 = -1 (prove or refute; recompute the first records
2, 14/5, 82/29, 478/169); what is and is not decided; is anything presented as new that is elementary number theory.
The three-party trade-off: omega(C_AB)^2 + omega(C_AD)^2 <= 8 under (P): check the proof line by line; nested twists
as instances of the stored twist clause; the remark on a horizon mode and a third party must be labelled as a remark
resting on the stored pair-state reading.
Overlaps: six proposals on one topic. Rule on a structure: which is the base statement, which cite it, what is
duplicated (the identity C^2 = 4 - [A1,A2][B1,B2] appears in several), and whether any two should be merged.
Literature: check on the web what you can of Tsirelson 1980, Landau 1987, Toner-Verstraete 2006, Kurzynski et al. 2011,
Popescu-Rohrlich 1994, and the fermionic-mode Bell literature cited (Dasenbrook et al. 2016; Debarba et al. 2020).

## Referee R2: the Kerr count (two proposals)
- synthesis.stretched-horizon-count-on-kerr-gives-the-area-law-at-every-spin
- synthesis.no-spin-independent-curvature-level-set-carries-the-count-to-slow-kerr

Specific points to settle.
Stretched horizon: the title reads as a passed test while the result's own clause says it cannot fail: rule on title,
one-liner and lay wording so the tautology is plain; the placement (SH) is a hypothesis: is that plain, and does the
text say it is to be IDENTIFIED with the stored (Loc) placement, not added to it (the stored
synthesis.c-loc-is-a-second-placement-of-the-count records that adding a second placement doubles the coupling);
"same nu": only the product nu rho_0 enters: require that wording. Recompute by your own route: the Gram determinant
-Delta Sigma on r = const for every Killing flow; the rate per area per proper distance tending to kappa_+; the count
2 pi nu rho_0 A_+ per modular period at leading order and the claim that the second-order slow-rotation coefficient
vanishes; the three inequivalent carries of the Schwarzschild formula with ratios M/s, M r_+/(2 s^2) and 1; the Smarr
form 8 pi nu (M - 2 Omega_H J); the extremal limit; the inner-horizon clause (is it uniform as a -> 0). The proof file
was edited after the gate (a coefficient 6x^2 -> 5x^2): check that line. Is the Kerr-Schild Fact and the Kerr
surface-gravity Fact quoted correctly at the pinned versions, and are signs tested against the stored conventions.
Everything in Gauge Theory Gravity: is any step metric or coordinate language that should be a labelled reading.
Curvature level set: the determinant det h = rho^2 [R(2M - R) - a^2 - (1 - u^2) a^4 u^2 / R^2] is "proved in the text
and sampled at 25 points": is there a degree argument making the sample decisive, or should it be "computed"; the
two-sided bounds and the range rho <= M/3, 0 < a <= 4 rho/5; the conclusion "no spin-independent (nu, rho(M)) gives
A_+/4 at zero and nonzero spin": is it proved for the stated class only (modulus level sets) and is the untreated
window stated at every level; the proved deficit is a few per cent: is the argument that it does not vanish at large M
sound. Consistency of the two proposals with each other and with the stored synthesis.kerr-ring-count-misses-area-law
and synthesis.c1-c2-forms-forced-one-number at their current versions.
