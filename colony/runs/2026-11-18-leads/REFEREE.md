# Referee brief, run 2026-11-18-leads

You are a blind referee (role "referee" in colony/BRIEF.md; read that role and the Standards section, and
colony/POLICIES.md section 2). LAB = /home/claude/phys-graph. Do NOT read colony/runs/2026-11-18-leads/findings/ or
work/, nor RUN.md, ATTACK.md or LEADS-source.md in this folder. Read only: the proposal folders named in your group
under LAB/proposals/, the store (through `python3 colony/labcli.py ...` or the files under store/), and the check4
logs in colony/runs/2026-11-18-leads/verify/check4_<id>.log. You may run
`python3 colony/runcheck.py proposals/<id>/check.py` and your own scratch scripts under /tmp/referee-<group>/ (exact
arithmetic; lib/GA.py is importable with sys.path.insert(0, '/home/claude/phys-graph/lib')). Do not run check4.py,
validate_draft or tp check. Do not edit anything under proposals/ or store/. Never spawn agents. You may use the web
to check literature claims. The machine has 2 CPUs shared with other agents: one heavy process at a time.

Write your report to colony/runs/2026-11-18-leads/verify/R-<group>.md. For each proposal: verdict (SOUND, SOUND WITH
FIXES with the exact fixes, OVERSTATED with the true weaker statement, WRONG with a counterexample, UNCLEAR with what
decides it), then the evidence: each proof step checked, each cited premise read at the pinned version and confirmed
to say what is used, at least two targeted perturbations of the check that you tried, a key number recomputed by your
own route, hidden hypotheses, overclaiming in title / one-liner / lay, literature quoted from memory and used in a
proof step, circularity, duplication of stored results. Say for each whether "proved" is the right status and
whether every clause labelled "proved" is proved in the proof text (not only computed in the check at samples).
Be adversarial. Candour over politeness: the maintainer wants errors found. Final reply under 350 words: verdict
per item and the fixes that matter most.

## Group A: heating, scrambling, and the energy restatement
A1. proposals/synthesis.heating-coefficients-across-curvature-couplings-and-on-the-chains-bath
A2. proposals/synthesis.rotation-weights-of-pair-sources-fix-the-channel-weights-and-forbid-a-fermion-trace
A3. proposals/scrambling.spreading-law-chaos-bound-saturated (a correction of the stored entity of that id: status
    conjectured -> proved, restated on a narrower scope)
A4. Not a proposal: a maintainer pass already applied to the store on this branch (uncommitted; see it with
    `git -C /home/claude/phys-graph diff -- store/claims/dark-matter.seeding-gravity-floor-dark-towers-temperature`
    and `git diff --stat -- store`). It replaces the stored energy count of the gravitational floor (3T per creation
    event, energy fraction 4Y) by the mean energy per event of the rate integral.

Points to settle.
- A1. (a) Recompute the closed form of c(D) and three of the quoted numbers by your own route (the crossing of c*
  inside the tilt window; the margins 1.84 and 1.27 at N_s = 188; the interval of xi on which four copies of the
  chain's content stay below c*). (b) Clause (iii) is the claim with consequences: is the chain's content between
  M_I and M_U as quoted (21 vectors, 48 Weyl fields, N_s = 64, 68 or 188), from the stored entities at their pinned
  versions, and is it true that the stored Pati-Salam clause (synthesis.seeding-remainder-excludes-perturbative-
  pati-salam, clause (i)) compares at temperatures where that content, and not the Standard Model's, is the bath?
  Read that clause: which reheating temperatures does it use, and is "all species taken massless" a fair bath
  there (the heavy fields have masses near M_I and M_U; what is light at 5e11 GeV and at 6e14 GeV)? If the massless
  count overstates the bath, say by how much the conclusion "fails at the tree-level value, holds at the conformal
  one" is at risk. (c) "Four copies of the chain's own content": does any stored statement ask about that content,
  or is it the proposal's own construction? (d) Is the Reading section's assignment of couplings to scalars
  supported by the cited theorems, or argued?
- A2. (a) Verify (ii) (the rotor mean, factor 1/5) and (iii) (norms s^2/6, s^2/4, 2 s^2; the vanishing weight-zero
  vector combinations) by your own computation, and that (iv) reproduces all nine stored weights. (b) (v): is the
  selection rule a theorem as stated, including "whatever its form"? (c) The Reading: is the step from the stored
  trace statement to "a source of the form mu((a.k)k - Q(k)a)R" proved, argued, or resting on the remembered fact
  that the trace is state-independent? Is "the correction to the chiral-fermion coefficient is zero at the next
  order as well" justified as worded, and is the interacting-theory paragraph labelled as argued? (d) Does the title
  claim more than (v) proves?
- A3. (a) Read the stored entity (store/claims/scrambling.spreading-law-chaos-bound-saturated) and the cited
  synthesis.affine-cell-boost-spreads-without-scrambling, synthesis.boost-evolution-on-generators-is-one-unitary-
  group, synthesis.phase-flow-is-time-rotor-flow-kms-continuation at their versions. Are (a) to (d) each already
  proved there, so that the correction proves nothing new but restates? If so, is "proved" earned by the entity or
  is it a duplicate of the stored theorem with a new title? (b) The stored title says "chaos bound saturated" and
  clause (d) says it is met, not saturated: is the entity's title now false, and should the proposal have said so?
  (c) Is (e) worded so that no reader takes the window law as proved?
- A4. (a) Rederive the mean energy per leg: weight E^3 f(E), Bose 4 zeta(5)/zeta(4) T, Fermi (30/7) zeta(5)/zeta(4)
  T, and the channel-weighted mean per event for the three species and for the Standard Model's content. Is the
  E^3 weighting right for every channel (the angular weight is s^2 times a constant: check that claim against the
  stored theorem's clause (v))? (b) Is "energy fraction (4/3)(E_event/T) Y" right, including its use of s/rho, and
  is the energy of BOTH produced quanta counted once? Does the produced pair carry E1 + E2 exactly? (c) Recompute
  the prefactor 1.23e-3, the two floors 6.6e-4 and 8.1e-4, eta' = 2.1, and one figure under (R). (d) The pass
  reports three conclusions that changed (two round bounds on Delta N_eff, the equality of the floor at the rescue
  temperature with the hot deposit, the share under (R)): open the entities and confirm each is restated truthfully
  at all four levels. (e) The hot deposit keeps "3T per unit of baryon number": is that a different quantity, or
  an inconsistency the pass left? (f) Spot-check two dependants for a stale figure.

## Group B: horizons
B1. proposals/synthesis.tube-point-clause-fixes-no-observer-where-rotations-have-no-fixed-point
B2. proposals/synthesis.even-parity-gravity-channels-zerilli-equation-equivalent-to-the-vacuum-equations

Points to settle.
- B1. (a) Clause (i): the centraliser of K and the classification of its so(3) subalgebras (is "every so(3) is the
  stabiliser of a vector of positive square in T" true in signature (1,3): what about so(3) subalgebras of so(1,3)
  that are not stabilisers, and is uniqueness up to conjugacy being confused with equality?). (b) Clause (iv) is
  the claim with consequences: "in every adapted gauge". Is the definition of an adapted gauge the only reading of
  the stored clause (synthesis.tube-point-clause-invariant-under-boost-commuting-symmetries, read it at its
  version), or does the proposal define away the cases where the clause would bite? Could the clause be read with
  the symmetries acting on the field and not linearly on tube points, and would the conclusion survive? (c) The
  stored de Sitter result fixes rho^2 = 12/Lambda: does the proposal's (ii)-(iii) reproduce it, and is the
  statement "Lambda_I is a datum of the gauge" consistent with it? (d) (v), (vi): recompute r_0, f(r_0), the ratio
  8/5 at the sample, by hand. (e) Is the closing "Consequently" paragraph within what is proved?
- B2. (a) What exactly is proved identically and what is computed at M = 1 with a homogeneity argument: is the
  homogeneity argument complete (which quantities scale how)? (b) Take one of the sixteen closed forms and one
  "differential multiple" identity and verify it by your own exact computation at a symbolic or generic rational
  point. (c) "(C3) is proved": state (C3) as the stored theorem cites it and check the new result gives exactly it,
  including the restriction to oscillating channels and the low multipoles l = 0, 1. (d) Are (C1) and (C2) used in
  any proof step of this proposal? (e) The gauge theory gravity setting: is the first-order field the stored one,
  and does the proof stay in the stored variables or pass through metric perturbation theory quoted from memory?

## Group C: walls
C1. proposals/synthesis.position-vector-eigenbundle-in-codimension-three-has-a-class-of-order-two
C2. proposals/synthesis.fixed-form-completion-over-a-ball-exists-iff-the-eigenbundle-is-stably-trivial
C3. proposals/synthesis.eigenbundle-class-of-a-corank-one-wall-is-the-dying-line
Background you may read: the stored synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump
(its clauses (4), (5), (8)), synthesis.wall-class-one-rung-obstruction, sheaf.wall-class,
synthesis.wall-rung-count-is-height-of-dying-line-class, and open problem op.eigenbundle-class-of-degenerations.

Points to settle.
- C1. (a) The claim is the STABLE one: the positive eigenbundle of multiplication by the position vector on the
  least module of Cl(3,0), over the two-sphere, is not stably trivial as a real bundle. Check the clutching
  function, the statement that its lift to the rotor group ends at -1, and above all the lifting lemma: is "the
  lift ends at -1" proved to be an invariant of the stable class (that is, of the class in pi_1 of the stable
  orthogonal group, of order two), with every homotopy-theoretic input either proved in the text or flagged as
  cited? An unstable statement dressed as a stable one is the failure to look for. (b) "On k copies a fixed-form
  completion exists if and only if k is even": both directions. (c) Does anything rest on Bott periodicity or on
  characteristic classes quoted from memory?
- C2. (a) "If and only if": check necessity against the stored transfer clause and sufficiency by following the
  explicit construction at one nontrivial example of your own. (b) Hypotheses: the base R^m, the degeneration
  inside a ball, "fixed form" as defined in the stored theorem, continuity versus smoothness, the rank added. Is
  "stably trivial" meant with the form's eigenspaces added (the open problem's wording), and does the statement
  say which? (c) The winding-two family with no rank-two completion: verify.
- C3. (a) "The class is the dying line L, the same information as (w(Sigma), w_1(L))": is this proved for every
  tame corank-one wall or for a model? Read the stored definition of tameness; the proposal states hypotheses
  directly and has no assumes edge on it: is anything of tameness used silently? (b) Does the transfer statement
  reproduce the stored necessity clause of the rung count, or only a two-sided variant; is the difference between
  two-sided and one-sided completions stated wherever a rung count is mentioned? (c) Is this a duplicate of the
  stored wall-class theorem in other words?
For all three: does any of them contradict the stored lens-space rung counts or the refutation recorded on
transport.obstructions-are-moved-never-destroyed (version 4)?

## Group D: the gravitational field
D1. proposals/synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints
D2. proposals/synthesis.constraint-and-dressing-do-not-restore-commutation-for-a-slaved-field-and-the-transverse-part-does
D3. proposals/synthesis.slaved-field-failure-is-a-first-order-signal-from-a-classical-source-and-no-stored-premise-bounds-it
Background you may read: the stored synthesis.gravitational-pair-production-from-the-operator-source-at-first-order,
synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation, store/conventions.md section
"Gravity and the graviton", open problem op.gravitational-field-at-null-momentum. Two standing decisions bind what
may be claimed: the operator source (OS) is a local hypothesis, not a premise; whether the field has a free part is
recorded as open and may not be settled by a result's wording.

Points to settle.
- D1. Recompute the kernel and cokernel dimensions of the first-order Einstein map at null and non-null momentum by
  your own route, and the count "two free directions, four constraints". Is the identification of the two with
  helicity two (if made) proved? Does any clause say or imply that the field has, or has not, a free part with
  states?
- D2. (a) The lattice model: rerun the check, perturb it twice, and recompute one commutator by hand. (b) "Constraint
  and dressing do not restore commutation": for which class of dressings is this shown (one dressing, a family, all
  first-order dressings)? The title says "do not"; is the proof about all of them? (c) "The transverse part does":
  what is the transverse part in a 1+1 lattice model, and is the carry-over to the gravitational field labelled as
  argued? (d) Is the model the stored one or a new one, and is its relation to gauge theory gravity overstated?
- D3. (a) "A first-order signal from a classical source": is the signalling probability computed, in what units, and
  at what order in the coupling; is "classical source" defined? (b) "No stored premise bounds it": this is a
  universal negative over the store. What was searched, and is the statement worded as the outcome of a search with
  its scope, or as a theorem? Read (C1), (C2) and the boundary-mode count yourself and try to derive a bound: if you
  can, the proposal is wrong. (c) Status: is "proved" right for a statement of this kind?
- D3, further. (d) The result rests on a local hypothesis (D): state it as the proposal does and say whether it is
  a mild modelling assumption or the whole content of the conclusion. (e) The proposal carries an argued estimate of
  the effect's size for gravity (about 1e-13 in proposed experiments; of order one for a few hundred kilograms at a
  metre). Recompute it. An order-one faster-than-light signal from a laboratory mass would be a refutation of the
  model by everyday experience, not a prediction: is the estimate about a signal outside the light cone, or about
  the ordinary retarded Newtonian influence, and does the text keep the two apart? If the model as stored implies
  an order-one superluminal signal at accessible masses, say so plainly and say what in the model produces it
  (the instantaneous part, the lattice dispersion, the absence of the field's own variables).
- D2, further. The lattice Maxwell model: "retarded form fails at 878 of 2750 spacelike events, except in one space
  dimension". A retarded field of a local source vanishing outside the light cone cannot fail to commute there
  with observables localised at spacelike separation unless the source operator itself fails to commute with them:
  find which operator carries the failure, and whether it is a lattice artefact (the lattice wave equation's
  support) or survives a continuum reading.

## Second pass (after the fix round)
You are the second-pass referee. Same rules as the common part, with one change: you DO read the first-pass reports
(verify/R-A.md, R-B.md, R-C.md, R-D.md as named in your group) and you check, for each proposal, (1) that every fix
the first referee required is applied at every level (title, one-liner, lay, technical, formal, proof, check,
coverage), (2) that a restated or reversed conclusion is true as now worded, by your own computation where a number
or a counterexample carries it, (3) that the fix round introduced no new overclaim or new unproved "proved" clause,
(4) that the check still fails under two perturbations of your choice. The gate logs after the fix round are
verify/check4_fix_<id>.log and verify/validate_fix_<id>.log. Do not re-referee what the first pass confirmed and the
fix round did not touch. Verdict per proposal: ACCEPT, ACCEPT WITH (exact wording changes, small enough for the
maintainer to apply), or NOT YET (what is still wrong). Report to verify/R2-<group>.md; final reply under 300 words.

### Second pass, group ABC
First-pass reports: R-A.md, R-B.md, R-C.md. Proposals (ids as they now stand under proposals/):
- synthesis.heating-coefficients-across-curvature-couplings-and-on-the-chains-bath (was WRONG in clause (iii);
  recomputed with the threshold on the chain's bath: confirm the new margins 2.83 and 1.95, the four-copies figures,
  and that no level still says or implies the exclusion fails at the tree-level value)
- synthesis.rotation-weights-of-pair-sources-fix-the-channel-weights-and-give-no-trace-at-nonzero-weight (renamed)
- scrambling.spreading-law-chaos-bound-saturated (status must be conjectured; no level may claim the law proved)
- synthesis.tube-point-clause-on-black-hole-fields-empty-for-the-horizon-flow-and-reading-dependent (renamed; was
  OVERSTATED; new clause (vii) is the first referee's counterexample: verify it as stated, and its stated condition
  on the fields' symmetries)
- synthesis.even-parity-gravity-channels-zerilli-equation-equivalent-to-the-vacuum-equations
- synthesis.position-vector-eigenbundle-in-codimension-three-has-a-class-of-order-two (lifting lemma closed and
  promoted to clause (L): check the new argument through the centre)
- synthesis.fixed-form-completion-over-a-ball-exists-iff-the-eigenbundle-is-stably-trivial (statement narrowed, then
  widened to every fixed form of the signature by a constant change of basis: check that widening; its validate log
  fails only because it cites the previous proposal, which is not yet stored: confirm that is the only cause)
- synthesis.eigenbundle-class-of-a-corank-one-wall-is-the-dying-line (wording restated to a two-sided statement)

## Group E: values (first pass, blind) and group D (second pass)
First pass, blind (do not read any report on these two):
E1. proposals/synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear
E2. proposals/synthesis.pell-values-are-the-running-maxima-of-the-pure-state-chsh-values-over-the-rationals
Gate logs: verify/check4_first_<id>.log and verify/validate_first_<id>.log. Background you may read: open problem
op.positivity-of-values and the entities it lists.

Points to settle.
- E1. This is a Gleason-type theorem over the rationals in dimension four with NO positivity or continuity
  hypothesis, which is stronger than what one expects (over the reals, additive frame functions without
  boundedness need not be linear; over Q in low dimension non-linear ones are known to exist in some settings).
  So look for the error first. (a) What exactly is the domain: all projectors of the matrix algebra over Q that
  Cl_Q(2,2) is, of every rank, or the rank-one projectors onto rational rays, and orthogonality with respect to
  which form or involution (the stored dagger of premise (P))? Are there enough orthogonal frames over Q for the
  additivity conditions to bite, and does the proof use frames whose vectors have rational norm only? (b) Follow
  the proof's reduction (rays as rational rotors, frames as cosets of half-turn groups) and the four finite exact
  computations: do the finite computations establish the general statement, or only the statement on a finite
  box? Where is the induction or the generation argument that carries a finite identity to all rational rays?
  (c) The second claim: a parity colouring gives non-linear additive weights on atoms of rational unit vectors
  alone. Is that consistent with the main claim, and does the statement make the difference in domain plain at
  every level? (d) Prior art: the proposal names Mushtari, Lobachevskii J. Math. 9 (2001) 47, unread. Use the web:
  find what is known about Gleason-type results over the rationals (Godsil and Zaks; Meyer; Havlicek, Krenn,
  Summhammer, Svozil on rational spheres; Mushtari) and say whether E1 contradicts, reproduces or extends a
  published result. A contradiction with a published theorem decides the verdict. (e) "With non-negativity these
  are exactly the states of (P)": check against the stored premise at its version. (f) Is "proved" right, and does
  any level present the result as a derivation of (P)? It is not one: (P) also asserts that values ARE given by
  such weights.
- E2. (a) The claim is for every denominator. Follow the number theory: deficit 4 b^2/Q^2 with b = 1 (Pell) or
  b >= 7; the exclusion of b = 3 and b = 5; the comparison Q_{n+1}^2 < 34 Q_n^2. Recompute the first twelve
  running maxima by brute force with your own code and compare. (b) Is "pure-state values of the sector" defined
  as in the stored theorem it extends, and is this a duplicate of a stored clause?

Second pass on group D (read verify/R-D.md; rules of the section "Second pass" above):
- synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints
- synthesis.two-dimensional-lattice-maxwell-coulomb-slaved-field-fails-and-string-dressed-detection-commutes
  (renamed; was OVERSTATED; one conclusion withdrawn: confirm no level still claims that constraint and dressing in
  general fail to restore commutation, and that the forward-cone statement about the 878 events is true as worded)
- synthesis.with-a-coupled-device-the-slaved-field-failure-is-a-first-order-signal-and-a-survey-finds-no-stored-bound
  (renamed: confirm the plain statement of the signal outside the light cone, its size, its cause and its
  experimental status, and that only clauses (1), (2), (4) are called proved)
Gate logs after the fix round: verify/check4_fix_<id>.log, verify/validate_fix_<id>.log.
Report everything to verify/R-E.md (first pass on E1, E2, then the second pass on the three D proposals).
