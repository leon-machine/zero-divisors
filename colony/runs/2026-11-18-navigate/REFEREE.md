# Referee brief, run 2026-11-18-navigate

You are the blind referee (role "referee" in colony/BRIEF.md; read that role and the Standards section, and
colony/POLICIES.md section 2). LAB = /home/claude/phys-graph. Do NOT read colony/runs/2026-11-18-navigate/findings/
or work/, nor LEADS.md or RUN.md in this folder. Read only: the three proposal folders under LAB/proposals/, the
store (through `python3 colony/labcli.py ...` or the files under store/), and the check4 logs in
colony/runs/2026-11-18-navigate/verify/check4_*.log. You may run `python3 colony/runcheck.py proposals/<id>/check.py`
and your own scratch scripts under /tmp/referee/ (exact arithmetic; lib/GA.py is importable with
sys.path.insert(0, '/home/claude/phys-graph/lib')). Do not run check4.py, validate_draft or tp check. Do not edit
anything under proposals/ or store/. Never spawn agents. You may use the web to check literature claims.

Write your report to colony/runs/2026-11-18-navigate/verify/R1.md. For each proposal: verdict (SOUND, SOUND WITH
FIXES with the exact fixes, OVERSTATED with the true weaker statement, WRONG with a counterexample, UNCLEAR with what
decides it), then the evidence: each proof step checked, each cited premise read at the pinned version and confirmed to
say what is used, at least two targeted perturbations of the check that you tried, a key number recomputed by your own
route, hidden hypotheses, overclaiming in title / one-liner / lay, misquoted literature, circularity, duplication of
stored results. Be adversarial. Candour over politeness: the maintainer wants errors found.

## Proposals

A. proposals/synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump
B. proposals/synthesis.gravitational-pair-production-from-the-operator-source-at-first-order
C. proposals/synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation

## Points to settle

### A (strict completions and the signature jump)
1. Is "strict completion, standard outside U" as defined here the same notion as in the stored
   sheaf.conservation-degeneracy-absolute-form (version 4) and in version 3 of the conjecture
   transport.obstructions-are-moved-never-destroyed? In particular: in clause (2) the complement carries K = -G, a
   form that varies from point to point. Does the stored reading of "standard" ("h = G perp K for a nondegenerate
   form K on a complement, with sig(K) the same on both exterior regions") admit that, or does it implicitly mean
   a fixed model form? If the stored reading is ambiguous, say what the result is under each reading (for the
   counter-model x^2 the proposal also gives a completion with the constant K = -1; is there a constant-K completion
   for diag(x,-x) and for [[x,y],[y,-x]]? Find one or show none exists: this decides whether clause (4) survives a
   stricter reading).
2. The conjecture says "any completion that is nondegenerate of constant signature on one side of the locus
   degenerates on a displaced locus on the other side". Do the counter-models refute that sentence as written, or
   only a neighbouring one? State exactly which sentence is refuted.
3. Proof of (1): the path argument, closedness, "lies in U". Proof of (2): hat h^2, the signature (n,n), existence
   of beta. Clause (6): the bound and the Witt-index statement against the cited Fact at its pinned version.
4. Clause (5): is Cl(4,0) isomorphic to Cl(0,4), and does the cited entity say so? Is "the invariant is the integer
   signature, not its residue modulo 8" a fair reading of what the conjecture conjectured?
5. Is any clause already stored (synthesis.wall-class-one-rung-obstruction clause (2), or elsewhere)? Is the lay
   level's "settles the general case" justified?

### B (gravitational pair production)
1. Recompute clause (i) from the stored curvature map by your own route (not the proposal's gauge choice): the
   identity G_k[T - 1/2 id tr T] = 1/2 Q(k) T and the kernel dimensions 4 and 6.
2. Clause (ii): is the constant 8 pi G right? Check it a second way (for instance against the known amplitude for
   gravitational scattering of two distinguishable massless scalars, or by an independent derivation from the
   linearised field equation with a stated convention). Is the passage from the interaction kernel to the invariant
   amplitude, and the Born relation with the 4 m1 m2, right?
3. Clauses (iii), (iv): recompute at least the scalar-to-scalar and fermion-to-scalar squared brackets by hand, and
   one channel the proof does not treat analytically (for instance vector to vector, or fermion to fermion) by a
   route different from the check's. Is the degree-four argument for the angular dependence sound? Are the
   identical-quanta factors right in each channel (real scalar pair 1/2, vector pair 1/2, fermion-antifermion 1)?
   Is the weight 3 for one chiral fermion (particle with its antiparticle) right, against 1 for a real scalar and 12
   for a real massless vector?
4. Clause (v): rederive the rate formula with its factors (1024 pi^6, 32/3, the thermal integrals) and the number
   5789 pi^3 / 82944000. Does Gamma count events or quanta, and is that stated consistently? Hidden hypotheses
   (thermal masses, final-state occupation, the bath's content at the temperature in question, chemical potentials).
5. Clause (vi): read arXiv:2112.15214 (equations (2), (11), (79), (83) to (90)) and arXiv:1803.01866 (its coupling,
   equation (3), its matrix elements, and if you can its appendix and Table I) on the web, and the stored Fact
   dark-matter.imported-massless-graviton-production-rate. Is each statement of (vi) true as worded? In particular:
   (a) do the later paper's amplitudes weight each Standard-Model fermion as a Dirac fermion; (b) is the factor
   sixteen between the two published values correctly attributed; (c) is "the normalisation fixed by Newton's law is
   the later one" established. If the proposal's attribution goes beyond what the sources show, give the wording
   that the sources support.
6. Clause (vii): is the mean-field statement right as worded (which fields, which era, what order)?
7. Hypothesis (OS): is it a well-defined hypothesis, is "proved given (OS)" a fair status, and does the Reading's
   statement of the consequences for the stored floors (factors 1.6 to 1.8 and 7 to 11) follow from the stored
   users' formulas (dark-matter.seeding-gravity-floor-dark-towers-temperature and
   dark-matter.coefficients-floors-they-give-what-gravity)? Does the proposal anywhere imply the stored Fact is
   "wrong" beyond what is shown?
8. Is the result transport-absent, as the technical level says?

### C (slaved field and commutation at spacelike separation)
1. Recheck (1) by hand, and the derivation in (4) with its signs and its "first order" scope. Recount 172 and 502
   with your own script.
2. Does the Reading describe the store fairly? Read store/conventions.md (section "Gravity and the graviton"),
   pred.gravity-entangles-standard-phase, field-theory.operator-newtonian-coupling and
   synthesis.locality-of-the-attached-free-fields-fixes-their-statistics. Does the store hold (E), (N), (L) as the
   Reading states them? Is "(E) carried beyond the instantaneous order by the retarded rule" something the store
   holds, or something the proposal supplies? If the latter, the conflict is conditional: say how it should be
   worded.
3. How much does a scalar lattice model with no gauge constraint show about the gravitational gauge field? Is the
   title or the one-liner stronger than the model supports?
4. Clause (5): is it right that the retarded, advanced and symmetric rules differ by solutions at null momentum,
   and does the cited theorem say what is used?
5. Prior art and attribution; the outside_ga declaration.

## Also say
- where the three proposals duplicate or contradict each other or stored results;
- the three most serious problems across all of them, in order.
