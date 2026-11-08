# Run 2026-11-08-composite-higgs: report

Target: op.qft-bosons-and-the-rung-field: is there, on the tower, a gapped composite scalar doublet beyond mean field?
Method: attacker pair (A constructive, B adversarial), blind referee H, one fix round, close-out.

## Accepted (three results)
- synthesis.even-composite-doublet-needs-a-singlet-constituent-and-its-pair-modes-are-quasi-spins (B; SOUND WITH FIXES):
  an even doublet needs an odd number of singlet fermion factors (generalising the rung field's no-even-doublet clause);
  when its channel matrix squares to zero its pair modes on a null generator are quasi-spins (a corollary of the stored
  helicity-one theorem with isospin weights); counterexample with M^2 != 0 in the check.
- synthesis.uniform-pair-channel-of-a-tower-condensate-is-a-goldstone-rotor (B; SOUND WITH FIXES): finite Goldstone (rotor)
  bound for pairing-type elements ([X, X*] a function of the charges): the second difference of the lowest energies across
  neighbouring charge sectors is at most G times the step, at every size; on the single shell 2G, attained; the doublet
  floor and coupled condensates are not covered. Prior art Bes-Broglia, Bohr-Mottelson.
- synthesis.two-species-floor-pairing-has-a-gapped-doublet-pair-mode-that-closes-where-it-condenses (A; OVERSTATED,
  restated; Leon accepted): on the symmetric band of a two-species floor the doublet pair mode is a gapped composite
  doublet, even, isospin 1/2, bound below pair breaking with exact gap omega_D, closing where the band's doublet condenses;
  the lowest-doublet-level clause by reduction to the pair-sum spectrum, computed exactly for n_b <= 6 and conjectured
  beyond; the band need not hold the floor's ground state at fixed N and the condensed phase has further sub-threshold
  levels (exact counterexamples in clause (x)).

## Leon's decisions (8 November)
Accept the restated proposal; record the outcome on the open problem as proposed (a composite doublet allowed by parity, no
model here giving a doublet vacuum value with a gapped doublet, the elementary reading standing, argued; open cases named);
add a low-priority attack item for the pair-sum spectrum at every size. Status stays partial.

## Checks
Baseline 0 errors 0 warnings. Gate after fixes: all three check4 exit 0 with no warnings, validate ok. Final check 0 errors 0
warnings; build 0 errors; layout, site, lock; 393 tests OK.

## Costs (approximate subagent tokens)
Attacker A 767k (with fixes), attacker B 652k (with fixes), referee H 273k: about 1.7M.
