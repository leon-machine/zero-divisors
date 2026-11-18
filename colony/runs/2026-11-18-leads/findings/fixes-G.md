# Fix round, cluster G (referee report verify/R-D.md; D1, D2, D3 = proposals A, B, C)

Fixed in place under proposals/<id>/ (entity.md at all four levels, proof-main.tex, check.py, coverage.yaml). Only
`runcheck.py` was run. check4: pending (orchestrator). validate_draft: pending (orchestrator). The work copies under
work/G/P1, P2, P3 are the first filing and were not updated.

## D1 synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints
SOUND WITH FIXES; all five applied, none declined. No conclusion reversed. check.py unchanged (7 functions pass).
1. Lay level reworded: the two components are "at the momenta that light has, which the source does not fix"; "in
   standard physics they are the two polarisations of a gravitational wave; whether the series gives them any
   existence of their own is open". Reading: "the first-order equation has solutions without source only in those
   two components", with a sentence that their existence is open.
2. Helicity two in the Reading now cites the proved statement (a rotation of m1, m2 rotates n_+, n_x by twice the
   angle), which is also stated in the Setting.
3. (vii): B_N is presented as a definition; its reading as the interaction of a field varied within the Weyl-flat
   class is labelled argued in the clause head, the clause and the proof. "Do not test the trace-free channel" is
   scoped to the stored results; the deflection of light is named as the classical test outside the store (from
   memory).
4. "Two percent at most" replaced at the technical and lay levels and in the Reading: two percent for the mix
   read (massless neutrinos, photons and the two components), less for a hotter hole, more for one emitting photons
   alone.
5. Extraction note: the stored first-order theorem's clause (ii) already names N_p and G_p + N_p (computed at one
   null momentum); clause (i) here is its general proved form.

## D2 synthesis.constraint-and-dressing-do-not-restore-commutation-for-a-slaved-field-and-the-transverse-part-does
OVERSTATED; restated at every level. The referee's counterexample was checked and is right, so one conclusion of
the first filing is withdrawn.
- Computation that decides it (new check function
  check_string_shaped_slaved_field_keeps_the_constraint_and_is_not_static): E_l = g chi_l P1 plus a number has the
  divergence the constraint asks, lies in the matter algebra, and its commutator with the bare detection is
  g chi_l p q e2, zero on all 82 links off the string. So "a field with no variable of its own fails on 76 links"
  was a statement about the Coulomb choice (E^T = 0), a hypothesis the first filing did not state. Withdrawn: "the
  constraint and dressed observables do not restore commutation for a slaved field" as a general statement.
- What stands, and how it is now stated: (4) the Coulomb slaved field, characterised as the slaved field the field
  equation leaves unchanged, fails on the 76 links with every matter element that does not commute with the charge
  ([E_l, m] = g kappa_l [P1, m], the referee's one-line general statement; checked on four further elements, two
  commuting with the charge and two not); (5) the constraint alone does not fix a slaved field (the counterexample),
  the string-shaped one is not static (changed on 10 links after two steps; the Coulomb field unchanged) and the
  gradient part of what it becomes is kappa at every step; (7) the slaved field that obeys the field equation fails
  at 878 of 2750 spacelike events.
- Recorded as the referee found, and now checked: all 878 failing events lie in the forward cone of the source event
  and outside the cone of the detection; the failure is carried by the charge P1 at the source event, which does
  not commute with the detection of the same quantum five steps later (a timelike pair); none of the 878 is
  spacelike to the source. This is in clause (7), the technical level, the lay level, the one-liner and the proof.
- With transverse variables: clause (2) is now the general one-line statement for every dressing by one Weyl
  operator ([E_l, O_f] = g p q f_l X_f: commutation exactly off the support of f), with the string and the Coulomb
  dressing as its two cases, and the text says that sums of Weyl operators are not treated. The former clause (5)
  is merged into (2).
- One dimension: in the title ("in two dimensions"), the one-liner, clause (6) and the lay level.
- The Reading for gravity is marked as argued by analogy and now says that the gravitational constraints likewise
  leave the transverse trace-free data undetermined; the extraction note's decision sentence carries the same
  qualification.
- Not done: the referee's remark that the counts are the same at step 1 was not recomputed here; the coverage
  says so.
New title: "Lattice Maxwell in two dimensions: Coulomb slaved field fails, string dressing commutes".
The id's slug no longer describes the result. Proposed slug:
synthesis.two-dimensional-lattice-maxwell-coulomb-slaved-field-fails-and-string-dressed-detection-commutes

## D3 synthesis.slaved-field-failure-is-a-first-order-signal-from-a-classical-source-and-no-stored-premise-bounds-it
SOUND WITH FIXES; all applied, none declined. No conclusion reversed.
- Title, one-liner, technical and lay levels: the negative about the store is the outcome of a survey with its
  scope listed; (S) ends "the outcome of a survey, not a theorem about the store".
- Versions read are named: (C1) version 5, (C2) version 4, (C_loc) version 6.
- Labels: (1), (2), (4) proved; (3) computed, the 140 later events argued; (5) argued with computed numbers; the
  former clause (6) is a Remark (computed); (S) a survey. A status paragraph at the technical level says so.
- (D) carries the whole step: said after the hypothesis, in the proof of (1), at the technical level, in the
  Reading and at the lay level.
- Factor two: the text says why the half arises (each coupling takes half so that Newton's law holds at late
  times) and gives the numbers under it (6.4e-14 and 2.6e-3; phase one at about 380 kg). Checked.
- "The size of what is being accepted" replaced by the plain statement: with (D), a signal outside the light cone,
  of order one for about 190 kg at one metre against a superposed mass of 1e-14 kg; caused by the field having no
  variables of its own, not by lattice dispersion and not by an instantaneous part; not refuted by present
  experiments (mesoscopic superposition, source in place within about 3 ns); kept apart from the ordinary
  retarded Newtonian influence, with the sentence that in standard physics the phase in the window is zero. The
  check now holds 188 < m < 190 kg, the halves, and the light-crossing times 3.3 ns and 1.5 ps.
- Planck-length floor: (S)(f) and the proof say it would change the phase only at relative order l_P/d.
- Lay: "an ordinary mass will do, next to a superposed mass far heavier than any yet made".
New title: "Slaved field with a coupled device: a first-order signal; survey of stored bounds".
The id's slug states the survey's outcome as fact. Proposed slug:
synthesis.with-a-coupled-device-the-slaved-field-failure-is-a-first-order-signal-and-a-survey-finds-no-stored-bound

## Checks after the fixes (runcheck only)
D1: 7 of 7 pass. D2: 6 of 6 pass (one function added). D3: 5 of 5 pass.

## Second pass (verify/R-E.md, group D sections)
- D3: accepted, nothing changed.
- D1: the one-line computation of the rotation of n_+, n_x by twice the angle added to the proof of (i).
- D2: the referee's second counterexample checked: the slaved field S P1, string-shaped at the detection step 5,
  keeps the constraint at every step, commutes with the detection at step 5 at all 2750 spacelike events, and
  against a detection at step 7 fails at 86 of the 2562 events spacelike to that one (reproduced; now in the
  dynamics check, with ND_OTHER = 7 at module level). The general claim added in the fix round ("every slaved
  field obeying the field equation fails") is withdrawn; every level now says "the retarded slaved field", with
  the report's replacements in the extraction note, Reading, lay, technical and one-liner, and a Remark after
  clause (7) with its proof line. runcheck: D1 7 of 7, D2 6 of 6. check4 and validate_draft: pending (orchestrator).
