# Report, run 2026-11-12-asymmetry

Target: op.matter-asymmetry-origin, approached from the foundation (the bit before number) and the bit and switch
results, at Leon's direction. Two attackers (constructive, adversarial), one blind referee, one fix round, two
maintainer agents. Baseline and final `tp check`: 0 errors, 0 warnings. 405 unit tests pass.

## Outcome
The problem is not settled. Status moved from open to partial. Neither branch of the success clause is met: no
stored dynamics produces the asymmetry, and there is no proof with named premises that none can generate or erase it.

## Established (four accepted results)
- synthesis.exchange-of-set-and-clear-is-inner-and-fixed-by-no-integer-state (SOUND WITH FIXES). Proved: on finitely
  many anticommuting switches the exchange of set and clear is an inner automorphism; no positive normalised
  integer-valued state is invariant (the invariant one needs 1/2). So an orientation must exist and its sign is a
  label for the algebra. Standard and elementary; transport-absent.
- synthesis.baryon-number-centraliser-in-the-five-mode-algebra (SOUND WITH FIXES). Proved under (S): baryon number
  commutes exactly with the elements shifting the pair number by 0 or 3; this contains the gauge algebra, the slot
  vectors and the Majorana element; the 24 slot-pair generators and the six leptoquark bivectors are outside.
- synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them (SOUND WITH FIXES). Proved for one family:
  only hypercharge survives every stored term. Conditional on the anomalous weak equilibrium (literature, cited from
  memory, not a stored Fact): baryon number is generated and erased from B - L; 28/79 for one light doublet, 8/23
  for two.
- synthesis.flag-conjugate-antilinear-on-one-chirality-and-conjugation-reverses-jarlskog (OVERSTATED, restated;
  renamed from its filed id). Proved: on one chirality the flag conjugate is antilinear; conjugating the quark
  matrices reverses J. Argued: for the laws the label is joint for (orientation, sign of J, arrow).

## Refuted in the run
"No stored dynamics changes the charge" fails for every candidate charge (pre-registered kill conditions triggered).

## Leon's decisions, 12 November 2026
1. Accept the restated fourth result; correct clause (3) of the stored CPT-conjugation claim (4 -> 5).
2. The inherited charge Q = epsilon N is B - L. Premise restated (4 -> 5); charge Proposition restated (10 -> 11).
3. The anomalous weak process is not imported; an attack item is registered (source it; fix the doublet count).
4. The CPT premise takes the adjoint reading on the family terms (3 -> 4).
5. The mirror share f_2 = 1 is restated as conditional on Hypothesis (equal conversion) in three results (copy
   theorem 10 -> 11, assembled share 9 -> 10, fragility 7 -> 8); ten dependants carry scope notes; the 5.364 total is
   conditional on it. No number changed.
6. The open problem's status is partial.

## Referee's deviation noted
The referee's explanatory definition of the Gram matrix in section G carried a wrong factor of 2; the stored
correction uses the definition derived and checked in the maintainer pass.

## Left open (attack items on the problem)
The heavy pair's split and widths (untouched); the conditional B - L inheritance theorem; sourcing the anomalous weak
process and the doublet count; the washout rate of the Majorana element; a rate bound for the 24; equal conversion in
the mirror; completeness beyond one family. The magnitude of epsilon is untouched.

## Not done, for a later pass
- The coverage judge has not re-agreed the reworded coverage line on the charge Proposition.
- Scope notes on ten dependants sit in extraction blocks and are not shown in rendered statements.
- The lay level of dark-matter.orientation-arrow-seventeenth-refutation reads more broadly than its formal conclusion.
- A possible contradiction flagged by the adversarial attacker (Hypothesis (B') with a uniform mode rotation against
  the stored mass terms), argued from stored text and not recomputed: for the next consistency run.
