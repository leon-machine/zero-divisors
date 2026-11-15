# Referee brief 2, run 2026-11-12-rung-state

You are an independent referee. LAB = /home/claude/phys-graph (git clone, branch test/rung-state-forced-or-datum).
Do not commit, push, switch branches, spawn agents, or edit anything under store/. Scratch:
colony/runs/2026-11-12-rung-state/verify/work-R2/. Do not read colony/runs/2026-11-12-rung-state/work/.
Read colony/BRIEF.md ("Role: referee" and the Standards) first.

Background. The maintainer (Leon) asked whether the framework holds a mechanism for the collapse of the wave
function. Two claims were filed and reviewed earlier today (report: verify/R-opus.md; both "sound with fixes").
The maintainer then approved three further steps on the infinite tower and told the author to take more care,
because the first review caught many mistakes. Under review now:

  3. store/claims/synthesis.records-of-unbounded-length-on-the-tower-interference-factor-and-limit
  4. store/claims/synthesis.infinite-strings-tail-classes-and-no-reading-law-inside-the-algebra
  and the fixes applied to claims 1 and 2 after the first review:
  1. store/claims/synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight
  2. store/claims/synthesis.selector-candidates-on-the-tower-integer-states-parity-deterministic-laws
Pre-registration for 3 and 4: colony/runs/2026-11-12-rung-state/PREREGISTRATION-3.md (committed before computing;
`git log --stat` shows the order). RESULT.md records outcomes and the first review.

Tools: `python3 colony/labcli.py get_claim|get_proof|search_claims|find_text|cone|conventions '<json>'`;
`python3 colony/runcheck.py <abs path>/check.py`; lib/GA.py, lib/fock.py (exact; no sympy). Use your own code and
your own route for recomputation; do not reuse the author's helper functions.

Tasks.
A. Claims 3 and 4: check every proof step line by line. In particular:
   - claim 3 (i): the factor c^(N-k). Is the proof valid for every element, including odd ones and elements that
     move quanta between the system and a record pair? Recompute independently for at least N = 2 and N = 3.
   - claim 3 (iii): does the limit exist as stated, is it a state, is the mixture formula right, and is "no
     element of the algebraic tower has a nonzero interference" exactly what is proved?
   - claim 3 (iv) and claim 4 (ii): is the imported Powers-Stormer criterion applied correctly (are these states
     gauge-invariant quasi-free with projection operators; is the Hilbert-Schmidt statement right)? Read the
     import (synthesis.imported-powers-stormer-takesaki-disjointness) and say whether it says what is needed.
   - claim 4 (i): are G1, G2, G3 well defined as groups of automorphisms of the algebraic limit commuting with the
     adjoint, and are the orbit statements right for each? Is there a natural group the author left out that
     changes the picture?
   - claim 4 (iv): the lemma (a quadratic form taking only the values 0 and 1 at all rational points of the unit
     circle is constant) and its use. Is the lemma proved without continuity? Is "no reading law inside the
     algebra" exactly what follows, or broader? Name any rule that a reasonable reader would call "inside the
     algebra" and that escapes the argument (for example a rule using two elements, a rule depending on the data
     in a non-product way, a nonlinear function of values).
   - claim 4 (v): the arithmetic and the probability statements.
B. Break each check with at least two targeted perturbations; say which checks are weak or tautological.
C. Claims 1 and 2: were the fixes F1 to F6 and G1 to G6 of verify/R-opus.md applied faithfully? Did the fixes
   introduce anything new that is wrong or overstated?
D. Titles, one-liners, technical and lay levels of claims 3 and 4: do they say more than the proofs? Is the
   "Reading" in each clearly separated from what is proved?
E. The pre-registration 3: are the items marked TEST real tests? The author says one (2c) was mislabelled; is the
   rest labelled fairly?
F. The overall answer the author will give the maintainer is:
   "Step 1: in a model coupling, the stored premise that recorded outcomes cannot interfere becomes a statement
   that holds in the limit of unbounded records and fails at every finite stage; it selects nothing. Step 2:
   whether rung values are data on the infinite tower depends on which symmetries count; under changes on
   finitely many rungs the tail class is an infinite datum that nothing in the algebra connects, under sign
   changes of arbitrary sets of generators it is a label. Step 3: even granting an actual string, no rule
   expressible by values of elements of the algebra can select an outcome with state-dependent odds; a rule
   outside the algebra can, and needs three premises the store lacks. So there is still no mechanism in the
   stored content; a mechanism would be a theory of a different kind added to it."
   Is each sentence supported by what is proved or computed? Is anything important missing or overstated? If you
   see a route to a mechanism that this leaves open, describe it and test it if a small exact computation can.
G. Verdict per claim (3, 4, and the amended 1, 2): SOUND, SOUND WITH FIXES (exact fixes), OVERSTATED (true weaker
   statement), WRONG (counterexample), UNCLEAR (what decides it).

Write colony/runs/2026-11-12-rung-state/verify/R2-opus.md. Final message: the four verdicts with exact fixes, the
answers to F, and a count of the errors you found by kind (wrong mathematics; unsupported or overstated wording;
weak checks).
