# Fix round, run 2026-11-08-colour-lattice

Referee report: colony/runs/2026-11-08-colour-lattice/verify/C.md (read your proposals' sections in full; the fixes
below are its required fixes). Apply every fix in place in proposals/<id>/ at every level (formal, technical, lay,
one-liner, extraction note). Keep every stored file. Run ONLY
`PYTHONDONTWRITEBYTECODE=1 python3 colony/runcheck.py proposals/<id>/check.py`; never check4, validate_draft or tp check
(the orchestrator reruns check4 and validate_one centrally afterwards). Write findings/fixes-<name>.md with
"check4: pending (orchestrator)". Rebut a fix only with a computation. Do not edit store/, commit, push or spawn agents.

Cross-citations between your proposals (the referee's overlap ruling: the degree-3 lemma stored once, in B1; A and B2
citing it; B1 citing A for the SU(3) statements) are impossible now (E201: a proposal cannot cite a proposal). Do not
attempt them. Leave each proposal self-contained; the maintainer pass after acceptance does the repointing (version 2).
In each extraction note, add one sentence naming the sibling proposal id as the intended home of the shared lemma or
statement, so the maintainer can repoint.

## A: synthesis.colour-centre-flux-bounds-polyakov-lines-and-the-leading-glueball-tube (SOUND WITH FIXES)
1. Definition: a colour rotor is a genuine rotor of the e3..e8 block (R v R~ a vector for every vector v, R R~ = 1, even)
   with R E = E (the referee's counterexample R = exp(-3 phi I/2) exp(-phi J/2), cos(phi/2) = 3/5, satisfies the old
   conditions but R e3 R~ has grades 1 and 5; add it as a check that the old definition fails and the new one excludes it).
2. (vi): state free spatial boundary, or periodic spatial extent L > 2r.
3. Zero triality wording, extraction and technical: "the centre bound does not apply to lines of zero triality; for
   example three coincident lines joined by the volume form give exactly 1"; the adjoint perimeter law is argued.
4. Lay: replace "the lightest excitation of the field has a definite leading-order energy" by a leading-order statement
   that the plaquette correlation falls by a definite factor per time step; reading it as a glueball mass needs
   uniformity in the separation, not proved.
5. "follows from the convergent expansion of Osterwalder and Seiler" -> "is expected to follow from ... (cited from
   memory; not imported)". Leon's decision: the uniform-in-t gap stays argued, no import.
6. Pin synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces in derivations.uses at its current
   version, or cite it in prose only.

## B1: synthesis.a-finite-subgroup-of-colour-shares-its-strong-coupling-expansion-through-link-degree-three (OVERSTATED)
Restate to the referee's true weaker statement at every level (quoted in C.md, B1 section): the term (beta/18)^A from a
rectangle's own plaquettes is shared (leading for SU(3) by its centre, not shown leading for G); lay "many of the first
terms", not "the first terms". Also:
1. Centre proof: Schur's lemma (G irreducible on the J-complex 3-space, commutant span{1, j}) in place of the sampled
   cube-root check; add the commutant computation to the check.
2. Move the lattice-spacing and stored-gaps survey out of formal, technical and lay into the extraction note (it is a
   statement about the store's current contents). Leon's decision: the weak-coupling freezing of finite groups stays
   argued (cited from memory, not imported).
3. Prior art: Petcher-Weingarten (Phys. Rev. D 22 (1980) 2465) is about discrete subgroups of SU(2), not SU(3); correct.
4. Pin synthesis.field-level-brst-differential-of-the-derived-gauge-fields-is-nilpotent and
   synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces in uses, or cite them in prose only.
5. Optional, if cheap: record the referee's mechanism (a theta graph of seven plaquettes gives G a nonzero Polyakov term
   (1/3)(1/18)^7 at N_t = 1 where SU(3) has 0) as a computed remark supporting "not shown leading for G"; label it.

## B2: synthesis.colour-triplets-give-the-fundamental-colour-loop-a-perimeter-law-at-strong-coupling (SOUND WITH FIXES)
1. Title "... at infinite coupling" (or "at beta = 0"); the id stays.
2. Formal summary sentence: "at beta = 0 frozen triplets give exactly a perimeter law, and Wilson quarks a leading
   hopping term of perimeter form"; the comparison with (beta/18)^RT at small beta > 0 marked argued, leading terms only.
3. Technical and lay: "at leading hopping order" for quarks; "the physical colour question is the one with quarks"
   labelled a reading.
4. n_g is an input of the stored running-coefficients result (3 at the imported values), not derived.
5. Pin the Fradkin-Shenker Fact (synthesis.imported-singer-gauge-slice-neuberger-lattice-brst-and-fradkin-shenker-complementarity)
   and the one-loop entity in uses, or cite them in prose only.
6. outside_ga: either recast the fermion integral as the Clifford algebra of the zero form (as the field-level BRST
   entity treats Grassmann generators), or extend the declaration to name the complex unit of the spinor module as a GA
   element and its identification with J on colour. Prefer the recast if it is cheap.
7. Wilson fermions with r = 1: attribute to Wilson's 1975 Erice lectures, "cited from memory".
