# Referee brief, run 2026-11-12-asymmetry

You are an independent referee for four proposals that AI agents filed against the Physics Graph store (a claim
graph of a research programme on Clifford-algebra zero divisors as a bridge between general relativity and quantum
theory). LAB = /home/claude/phys-graph. Work only there and in your scratch folder
colony/runs/2026-11-12-asymmetry/verify/work-R1/. Never spawn agents, never commit, never edit store/ or proposals/.
Read colony/BRIEF.md (role: referee) first.

Blindness: you have NOT seen the agents' reasoning and must not look for it. Do not read
colony/runs/*/findings/, colony/runs/*/work/, RUN.md of this run, or other reports. Judge each proposal on its own
text, its premises in the store and its check.

Tools: proposals in proposals/<id>/ (entity.md, proof-main.tex, check.py, coverage.yaml);
`python3 colony/labcli.py get_claim|get_proof|search_claims|find_text|cone|conventions|notation '<json>'`;
`python3 colony/runcheck.py proposals/<id>/check.py`; lib/GA.py (exact Clifford algebra over Fractions; no sympy).
The orchestrator has run the evidence layer (check4) on all four: all exit 0. Logs:
colony/runs/2026-11-12-asymmetry/verify/check4/<id>.log; read them instead of rerunning check4.

The proposals (all address the open problem op.matter-asymmetry-origin; read it with get_open_problem):
1. synthesis.exchange-of-set-and-clear-is-inner-and-fixed-by-no-integer-state
2. synthesis.baryon-number-centraliser-in-the-five-mode-algebra
3. synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them
4. synthesis.reversing-baryon-number-is-a-conjugation-and-reverses-the-jarlskog-invariant

For each: check every proof step; confirm each cited store entity says what the proof needs at the pinned version;
read the check and break it with at least two targeted perturbations; recompute one key number by your own route;
hunt hidden hypotheses, overclaiming in title, one-liner or lay level, "proved" where only argued, literature cited
from memory, circularity, standard results presented as new, conditions missing from the title.

Specific points to settle:
A. Overlap: 2 and 3 are said to share content (the centraliser of baryon number; which terms break which charge). Say
   exactly which clauses duplicate, whether the computations agree, and whether they should stand as two, merge, or
   one be cut down. Do their identifications of baryon number, lepton number and B - L as elements agree with each
   other and with the store?
B. Consistency between 1 and 4: 1 says the exchange of set and clear is an inner automorphism (a label); 4 says
   reversing baryon number needs a conjugation and reverses the Jarlskog invariant. Are these compatible as stated
   (the algebra against the one-chirality module and the laws), or does one overstate? State the true joint
   statement in two or three sentences.
C. In 3: the use of the anomalous weak process and the coefficient 28/79. Is it presented as imported literature,
   with its source and its status (cited from memory or checked), and is any clause labelled proved that rests on
   it? Recompute 28/79 from the Standard Model field content with two Higgs doublets or one, whichever the store
   uses (find where the store uses it: dark-tower-matter.mirrors-composition), and say which.
D. In 4: is "no linear map of the sixteen normalising the gauge algebra reverses baryon number" proved for all linear
   maps or only checked on a finite family? Is the sign reversal of the Jarlskog invariant shown in general or on
   sample matrices?
E. In 1: is "no normalised integer-valued state is invariant" a statement about all states or about a class, and is
   the class stated? Does the proof use only the switch relations?
F. What do the four together establish about the open problem's success clause (a stored dynamics that produces the
   asymmetry, or a proof with named premises that none can generate or erase it)? Say plainly whether the problem
   is settled, partly settled, or open, and what exactly is missing.
G. One existing stored claim was flagged in passing: synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation,
   clause (3), last sentence, is said to state that the complex-linear Witt exchange does not preserve R^{2,4} while
   its own proof exhibits a real reflection that does. Read the stored claim and proof and say whether there is a
   defect, and if so the exact correction.

Verdict per proposal: SOUND, SOUND WITH FIXES (list the exact fixes), OVERSTATED (give the true weaker statement),
WRONG (counterexample), or UNCLEAR (what decides it). Write colony/runs/2026-11-12-asymmetry/verify/R1.md with a
section per proposal and sections A to G. Your final message to me: the four verdicts, one line each, plus the
answers to B, F and G in two or three lines each.
