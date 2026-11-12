# Result: is a new rung's set/clear value forced by the completion, or a datum?

Pre-registration: PREREGISTRATION.md (commit 4bdb5a0, before any computation).
Stored as synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight.

| hypothesis | kill condition | outcome |
|---|---|---|
| forced | both on and off extend the state under (P) | killed: every weight in [0,1] extends, none outside |
| datum | a symmetry of the step exchanges on and off; all strings one orbit; two classes under rotors | killed: all three hold (3 rungs: 8 strings, one orbit, classes 4 and 4) |
| coin | several invariant extensions, or an invariant one that is sharp or integer valued | holds: exactly one invariant extension, weight 1/2, not sharp, not integer |

Prediction made before computing: forced killed, datum killed, coin holds. Outcome as predicted.

One failure during the work, recorded: the first run of the positivity check failed for the sharp extensions. The
cause was an error in my exact positive-semidefinite routine (a wrong symmetrisation step), not in the claim; the
routine was replaced by plain Schur-complement elimination and tested on five small matrices of known definiteness.

Not reviewed by an independent referee. Depends on Premise (P) (a new assumes edge, for the maintainer) and on the
reading of "symmetry of the step" as the sign changes of the new generators.
