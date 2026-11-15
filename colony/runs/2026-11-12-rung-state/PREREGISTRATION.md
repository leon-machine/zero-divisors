# Pre-registration: is the set/clear value of a new rung forced by the completion, or a datum?

Written before any computation, 12 November 2026. Asked by Leon after the review of the no-collapse result
(one-relation.record-chain-votes-measurement-without-collapse): could the unboundedly many fresh bits a collapse
needs come from iterating the transport infinitely?

## Setting (the store's own definitions)
A_l = Cl_k(l,l), k = Q, generators e_j, f_j (squares +1, -1), ladder pairs v_j = (e_j + f_j)/2, w_j = (e_j - f_j)/2
(tower.ladder-pairs-satisfy-car-vectors). One transport step adjoins one hyperbolic plane, unique up to isometry
(rungs.imported-totality-minimality-completion): A_l -> A_{l+1}. Values are given by a state under Premise (P)
(synthesis.premise-positivity-of-values): linear, normalised, positive, real, for the split e_j, f_j. A state on
A_{l+1} extending a state omega on A_l is an extension. "On" is the idempotent v w of the new rung, "off" is w v
(synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane).
Symmetries of the step: the automorphisms of A_{l+1} that fix A_l pointwise and preserve the adjoint of (P), i.e.
the sign changes of the new generators e, f.

## Hypotheses and kill conditions
H-forced: the completion forces the value: exactly one extension satisfying (P) that is sharp (on or off).
  Killed if both on and off extend omega under (P).
H-datum: the value is a datum with invariant meaning: the on and off extensions are not exchanged by any symmetry of
  the step, or strings of values on several rungs fall into more classes, under the symmetries, than the one stored
  orientation bit allows (more than two classes under the rotor group).
  Killed if a symmetry of the step exchanges on and off, and all 2^m strings on m rungs form one orbit, with exactly
  two classes under rotors.
H-coin: there is exactly one extension invariant under the symmetries of the step, it has value 1/2 on "on", it
  exists only when 1/2 is in the ring, and it is not sharp. Killed if there are several invariant extensions, or an
  invariant one that is sharp or integer valued.
Prediction (mine, before computing): H-forced killed, H-datum killed, H-coin holds.

## What each outcome would mean for the question
- H-forced holds: iteration supplies no freedom at all; no bits.
- H-datum holds: iteration supplies an unbounded string of data; a hidden-variable selector is available in the
  framework, and the framework's count of free data is not short.
- H-coin holds with the other two killed: iteration supplies unboundedly many two-state systems whose symmetric
  state is an unbiased coin with no value; values are labels. A selector would need a new premise (each rung's label
  a datum, and a law reading it).

## Also to record (not a kill condition)
Whether the invariant value 1/2 is the stored occupation of a boundary mode at zero weight
(synthesis.boundary-mode-thermal-entropy), and what the stored result on two-valued weights
(synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them) says about using a
string of rung values to pre-assign outcomes.
Exact arithmetic only (lib/GA.py, Fractions). Sizes: l = 1, 2 old modes plus one new; m = 3 rungs for the orbit count.
