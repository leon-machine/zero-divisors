# Fixes A: synthesis.colour-centre-flux-bounds-polyakov-lines-and-the-leading-glueball-tube (SOUND WITH FIXES)

Applied in place in proposals/<id>/ (entity.md, proof-main.tex, check.py, coverage.yaml; all files kept), mirrored to
work/A/<id>/.

1. Definition (formal): a colour rotor is now a rotor of the block (even, R R~ = 1, R v R~ a vector for every vector v,
   equivalently a product of an even number of unit vectors) with R E = E. Proof (i) gains a paragraph "Why the vector
   condition" with the referee's counterexample R = exp(-3 phi I/2) exp(-phi J/2), cos(phi/2) = 3/5. Check
   check_colour_block_pure_spinor_and_det_one now builds it exactly (cos(3phi/2) = -117/125, sin = 44/125), confirms it
   is even, R R~ = 1, R E = E, that R e3 R~ has grades {1, 5}, and that every generator of G satisfies the vector
   condition. Docstring and coverage updated.
2. (vi): formal now reads "On a box with N_t periodic time steps and free spatial boundary"; proof (vi) states the
   boundary condition and why (a periodic spatial extent lets a chain wind the short way round).
3. Zero triality: extraction note, technical and formal (v) now say the centre bound does not apply to lines of zero
   triality, with three coincident lines joined by the volume form (exactly 1) as an example, and that the adjoint
   loop's perimeter behaviour is argued, not proved; proof's argued paragraph reworded to match.
4. Lay: "the lightest excitation ... definite leading-order energy" replaced by the referee's wording (plaquette
   correlation falls by a definite factor per time step at leading order; the glueball-mass reading needs uniformity
   in the separation, not proved). Mass-gap disclaimer kept.
5. Proof end and extraction note: the uniform-in-t gap "is expected to follow from" the Osterwalder-Seiler expansion
   (cited from memory, not imported). Per Leon's decision it stays argued, no import.
6. The claimref to synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces is removed; it is cited
   in prose only ("the store's one-loop running coefficients from spacetime-algebra spin traces").
7. Overlap: no cross-citation (E201). Extraction note adds one sentence naming the sibling
   synthesis.a-finite-subgroup-of-colour-shares-its-strong-coupling-expansion-through-link-degree-three as the intended
   home of the shared degree-three lemma, to which clause (iii) can be repointed in a later version.

runcheck: all 8 functions PASS (proposals/<id>/check.py).
check4: pending (orchestrator)
