# Run 2026-11-24-three-routes: what is specific to this run

LAB = /home/claude/leon-machine/zero-divisors (branch run/2026-11-24-three-routes, from main at 58338e0).
Session name for proposals: 2026-11-24-three-routes. Model for credit entries: Claude Fable 5.2.
Referees: Claude Opus 5.5, blind.

## Request
Leon, 23 and 24 November: which open problems are most consequential; three attack routes for each of
six; then "go ahead and run these" on the three routes recommended first. The eighteen routes are to be
filed as attack items on their problems in the maintainer pass (ROUTES.md in this folder holds them).

## Method
The standing method (BRIEF.md), with one problem per cluster: each target has an attacker A
(constructive: execute the named route) and an attacker B (adversarial and cross-pollinating: try to kill
the route, build counter-models and independence models, look in other subjects). Because each target
arrives with a route already chosen, step 2 of the attacker role (three routes) is shortened: A states
two alternatives to the named route in a paragraph and then executes the named one; B is free to choose.
One bridge-hunter after the attack round (not midway: the orchestrator cannot relay while the attackers
run); its links go to the attackers in the fix round. Blind referees, one fix round, one close-out.

## Targets and named routes

### P. op.positivity-of-values, route "records"
Read every self-adjoint projector with rational coefficients as a possible label of a record
(Hypothesis (RP); a reading, Leon's to adopt or not, so it is a named hypothesis of anything filed, never
a premise). Then: weights of records are non-negative frequencies, they add on orthogonal projectors,
and by the stored theorem (synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear)
they are the restriction of one state of (P) on two modes. To do:
1. Extend the additivity theorem past two modes: Cl_Q(l,l), l >= 3. The record names a first step: any two
   rational vectors of Q^(2^l) lie in a four-dimensional rational subspace similar to the standard one,
   which needs the representation of positive rationals by positive definite rational forms of dimension
   at least four (a consequence of Hasse-Minkowski; derive what is needed in the store if it is short,
   otherwise list it as a Fact to import, a decision for Leon).
2. Say exactly what of (P) is then left assumed: the sign; the value of elements whose spectral
   projectors are not rational (the CHSH element); additivity of values across summands that do not
   commute. Test whether the CHSH element is a rational combination of rational self-adjoint projectors
   and what that gives.
3. Read the prior art before calling anything new: Mushtari, Lobachevskii J. Math. 9 (2001) 47, and
   Mushtari 1995, 1998 (so far read through abstracts only; if you cannot read them, say so and keep the
   flag).
Attacker B: the independence side. Try to extend the stored functional of value 4 (or another
non-positive functional) to a model of every other stored premise, the recording premises included; test
whether the recording premises imply that coarse counts over many records are classical (macroscopic
locality, Navascues and Wunderlich, prior art from memory) and whether that gives the bound 2 sqrt 2
without (P); look for a three-mode counterexample to additivity implying linearity.

### G. op.gravitational-field-at-null-momentum, route "palatial pair"
Give the two transverse trace-free directions at null momentum a canonical pair on polynomials, as the
stored photon has (field-theory.fock-space-maxwell-modes), one mode over span{1, I_4} per null momentum,
and test whether that meets the series' requirement of no signal outside the light cone. To do:
1. Build an exact lattice model with the constraint structure of the first-order gravitational field
   (spin two: transverse trace-free variables, the four constraints), in the manner of the stored
   lattice Maxwell model, and repeat its three tests: the slaved field, the field with canonical
   transverse trace-free variables, dressed detection. If spin two in two space dimensions has no
   transverse trace-free part, say so and choose the smallest model that has one.
2. State the palatial construction for the two directions in the store's terms and what it costs: the
   conventions' sentence on the graviton, the burst ratio (2 + g + o)/(1 + g), the ontology readings.
   Adopting it is Leon's decision: file results as conditional on a named hypothesis, never as a premise.
Attacker B: try to meet the requirement WITHOUT states on the two directions (a composite of the
light-ray fermions with the commutator as a Schwinger term; the recording premises making the source a
number; any other stored structure), and try to break the palatial route (a dressing that cannot exist
with the gravitational constraints; a conflict with field-theory.no-canonical-commutation-relations-tower
or with the Krein premise). The published trilemma (Galley, Giacomini and Selby 2022, from memory) is
prior art: say what of it the stored results already reproduce.

### H. op.deposit-state-is-hadamard, route "CPT-symmetric wall"
Take the mirror as the far side of the radical-normal tame wall
(synthesis.radical-normal-tame-wall-is-a-regular-initial-surface-whose-smoothness-selects-no-state)
instead of the Riemannian continuation of attack item 5, and require the state to be invariant under the
stored CPT conjugation across the wall (prior art: Boyle, Finn and Turok 2018, from memory). On a
radiation-type descent M = m a is linear in conformal time. To do:
1. Decide existence and uniqueness of the invariant quasi-free state for the Dirac field, massless and
   massive, in the store's GA form; note that the stored CPT conjugation reverses energy and is not the
   field-theory CPT operator (Leon's ruling of 7 November), and say which conjugation the route needs.
2. Compute the occupation profile over an admissible reference (conformal vacuum; adiabatic of infinite
   order) exactly where possible, and decide the Hadamard property by the stored moment criterion.
3. Check it against the cold-mirror result, the far-side attack item, obstructions (O1) to (O5) of the
   problem record, and the mirror's deposit law.
Attacker B: the adversarial side. The trace anomaly of Hadamard states on a radiation-type field (the
Euler term goes as t^-4 against t^-2 for the density) against the tame conformal bracket, which the store
has only for w = 1/3; the necessity route (Fewster and Verch 2013, from memory: finite fluctuations of
Wick polynomials force the Hadamard form); and any stored result that the CPT-symmetric state
contradicts.

## Kill conditions, registered before computing
- P1. For three modes there is a function on the rational self-adjoint idempotents that adds on
  orthogonal ones and is not the restriction of a linear functional (then the extension fails).
- P2. Two rational vectors of Q^8 exist that lie in no four-dimensional rational subspace similar to the
  standard one (then the named first step fails and another is needed).
- P3. The CHSH element at the stored settings is not a rational combination of rational self-adjoint
  projectors, or its value is not fixed by weights on projectors without additivity across summands
  that do not commute (then (RP) leaves the Tsirelson bound assumed).
- P4. A functional that violates positivity satisfies every other stored premise, the recording
  premises included (then (P) is independent, and that is the result).
- G1. In the spin-two lattice model with canonical transverse trace-free variables no dressed detection
  commutes with the field at every spacelike event (then the palatial pair does not meet the
  requirement).
- G2. The first-order signal of the stored device result does not vanish with the free part in the
  spin-two model.
- G3. A structure already stored meets the requirement with no states on the two directions (then the
  palatial pair is not forced, and that is the result).
- H1. No quasi-free state of the Dirac field on the doubled field is invariant under the conjugation, or
  a continuum of them is (no selection).
- H2. The invariant state's occupation over an admissible reference has a power-law tail (not Hadamard).
- H3. The invariant state contradicts a stored result (the cold mirror, the deposit law, (O1)).
- H4. For the massless field the invariant state is not the conformal vacuum.

## Run-specific rules
- At most two gate processes on the machine at once: wrap every check4.py and validate_draft call as
  `flock /tmp/gate-<0 or 1>.lock <command>` (attackers of P and half of H use lock 0, G and the rest
  lock 1; the orchestrator says which).
- Results that would otherwise be imported are derived in geometric algebra inside the entity where the
  proof is short; the literature is then prior art (Leon's preference of 7 November). Declared exceptions
  use `outside_ga`.
- No imaginary unit where a pseudoscalar does the work; I_4 for the field theory.
- Every proposal states its named hypotheses in its title or one-liner when it is conditional.
- A negative result (a kill condition firing) is filed as a result.
