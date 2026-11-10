# Referee brief, run 2026-11-08-colour-lattice

You are an independent referee for proposals filed against the Transport Lab store (a claim graph of a research
programme on Clifford-algebra zero divisors as a bridge between GR and quantum theory, written in geometric algebra).
LAB = /home/claude/phys-graph. Work only there and in `colony/runs/2026-11-08-colour-lattice/verify/work-<your-name>/`.
Never spawn agents, never commit or push, never edit store/ or proposals/.

Blindness: do NOT read `colony/runs/*/findings/`, `colony/runs/*/work/`, RUN.md, or any other referee's report. Judge
each proposal on its own text, its premises in the store and its check.

Tools: `python3 colony/labcli.py get_claim|get_proof|search_claims|find_text|cone|neighbourhood|conventions|notation '<json>'`;
`PYTHONDONTWRITEBYTECODE=1 python3 colony/runcheck.py proposals/<id>/check.py`; `lib/GA.py` (exact Clifford algebra over
Fractions). check4 and validate_one have been run on every proposal; logs are in
`colony/runs/2026-11-08-colour-lattice/verify/` and `verify/final/`; do not rerun check4. WebSearch/WebFetch are allowed
to check literature; say what you verified and what you could not. One heavy process at a time (2 CPUs shared).

For each proposal: (1) check every proof step; confirm each cited store entity says what is needed at the pinned
version; (2) run and read the check, make at least two targeted perturbations and confirm it fails, recompute one key
number by your own route; (3) hunt hidden hypotheses, overclaiming at title/one-liner/lay level, "proved" where only
argued, literature misquoted or cited from memory, circularity, classical results presented as new, duplicates of
stored entities and of each other; (4) verdict: SOUND; SOUND WITH FIXES (exact fixes); OVERSTATED (the true weaker
statement at every level); WRONG (counterexample or failing step); UNCLEAR (what decides it).

House style: no em dashes; never "honest"/"honestly"; never "load-bearing"; Q(v) for the square of a vector; macros only
from store/notation.yaml. Leon's rules (check as fixes): everything in geometric algebra; results derived, not imported
(literature as prior art only); no imaginary unit where a GA unit can stand (store/conventions.md, unit principle).

Context: these proposals attack the store's open problem op.qft-non-abelian-gauge-fields, attack item "Colour: a colour
rotor lattice (none is stored) and its continuum limit; pure-colour confinement is the Yang-Mills mass-gap problem and is
not addressed" (read it in store/open_problems.yaml). Stored results to check against:
synthesis.weak-factor-rotor-lattice-strong-coupling-area-law,
synthesis.non-abelian-gauge-fixing-has-gribov-copies-and-the-weak-rotor-lattice-with-doublets-has-a-perimeter-law,
synthesis.imported-wilson-lattice-gauge-theory-and-strong-coupling-confinement,
synthesis.imported-singer-gauge-slice-neuberger-lattice-brst-and-fradkin-shenker-complementarity,
synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces,
synthesis.field-level-brst-differential-of-the-derived-gauge-fields-is-nilpotent (colour block).
A standing point for every proposal: nothing at title, one-liner or lay level may suggest progress on the Yang-Mills
mass-gap (Clay) problem beyond what is proved; strong-coupling lattice statements are classical (Wilson 1974,
Osterwalder-Seiler 1978, Drouffe-Zuber 1983) and the new content is at most their exact GA form.

## Referee C: the proposals
- synthesis.colour-centre-flux-bounds-polyakov-lines-and-the-leading-glueball-tube (called A below)
- synthesis.a-finite-subgroup-of-colour-shares-its-strong-coupling-expansion-through-link-degree-three (B1)
- synthesis.colour-triplets-give-the-fundamental-colour-loop-a-perimeter-law-at-strong-coupling (B2)

## Points to settle
B1 (finite subgroup). Re-derive the order 96 of the J-commuting signed permutations of e3..e8 fixing Re Omega, that they
lie in SU(3) (det = 1 in GA terms), the trivial centre, and the invariant dimensions 0, 2, 2 in degrees 1-3 and 20 vs 12
in degree 4 (by your own count, e.g. character inner products). Is "G average = Haar average to degree 3" proved without
importing a Haar moment (the projector argument: what guarantees that the SU(3)-invariants are exactly the
su(3)-annihilated tensors, and is the Haar average's projector property derived or assumed)? The plaquette series
beta/18 + beta^2/216 + 0 beta^3 versus beta^3/972: recompute. The reading "strong coupling cannot separate SU(3) from a
group that freezes at weak coupling": which parts are proved, which argued, and is the weak-coupling freezing of finite
groups (cited from memory) clearly marked? The "first closed surface is the cube" step: labelled standard? Is the
lattice-spacing / stored-gaps survey (premises F4, P2, C1/C2, R2, floors) accurate against those entities, and does it
belong in this entity?
B2 (triplets). Re-derive c(kappa) = kappa/6 - kappa^3/288 + O(kappa^5) and the rank-one mean link (one J-complex colour
line); the Haar moment E[x^4] = 1/16 by your own route; the Wilson-quark spin trace -2^(P-1) round a rectangle with hop
factors 1 -+ d_mu in Cl(4,0); the leading term (n_f/6)(2 kappa)^P. Is the outside_ga declaration (Grassmann integral)
justified and minimal? Is "the series' physical question is QCD's, not the Clay problem" stated as a reading?
A (centre flux, Polyakov, glueball tube). Re-derive: colour rotors = rotors of the e3..e8 block fixing the pure-spinor
idempotent E = prod_k (1 + I P_k)/2, and that this gives both J-commutation and det = 1 (fixing Re Omega); the character
chi = 4(<R>_0 + <R>_6) - 1 and the action (4 beta/3)(1 - <U_p>_0), beta = 6/g^2 (consistent with the imported Fact (i)'s
beta = 2N/g^2 and the stored SU(2) normalisation?); the centre rotor z = -prod_k(1/2 - (sqrt3/2) P_k) (is it central and
of order 3, and is sqrt3 handled exactly in the check?). The centre-flux argument: does a single-link change by z really
force a Z3 flux two-chain on every surviving term, so that no R x T fundamental loop has a term below order A? Is this a
proof at all orders of the strong-coupling (character) expansion on a finite lattice, and is the expansion's convergence
assumed or not needed? N-ality-zero lines "not bound": exactly 1 for three coincident lines joined by the volume form;
is the adjoint perimeter law claimed or only argued? Polyakov lines: <P> = <PP> = 0 at every beta (centre symmetry on a
periodic lattice: exact, finite volume); line-antiline (1/9)(beta/18)^(N_t r) and the baryonic junction
(1/27)(beta/18)^(3 N_t) with int chi^3 = 1: recompute; is the off-axis case excluded from the claim? The glueball tube:
leading connected plaquette correlator (1/18)(beta/18)^(4t), no lower term (the per-slab deformation argument: check
it); the decay rate 4 ln(18/beta) per step is a leading-order statement at fixed t, not a uniform-in-t gap in infinite
volume: is that stated at every level? Imported Fact (ii) (Osterwalder-Seiler) covers analyticity and the area law, not
exponential clustering: confirm the proposal does not lean on it for a gap.
Overlap: A and B1 both use the degree-3 moments of the same group; say whether either duplicates the other and what
each should keep.
Write your report to colony/runs/2026-11-08-colour-lattice/verify/C.md (summary table: id, verdict, one-line reason).
