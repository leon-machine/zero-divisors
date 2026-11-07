# Fixes, GA: synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators

Verdict (referee G): SOUND WITH FIXES. All nine fixes applied in place in proposals/<id>/ (entity.md, proof-main.tex,
check.py). runcheck.py: all 6 check functions pass. check4: pending (orchestrator).

1. (iii) unit on the null data, corrected. The data sit in the nbar ^ E_perp part; I4(nbar ^ u) = J_perp(nbar ^ u) =
   -(nbar ^ u)J_perp, while I4(n ^ u) = (n ^ u)J_perp (a component with no null data). E_perp(I4 F) = J_perp E_perp =
   -E_perp J_perp, so on the data I4 is right multiplication by -J_perp; eps(I4 F) = -J_perp eps. Helicity sentence
   restated relative to I4: data of positive frequency relative to I4 have eps ~ e^{+J_perp k lambda} and rotation phase
   e^{+J_perp phi} (same sense, one helicity), compared with and cited as field-theory.fock-space-maxwell-modes (ii), (iii)
   (added to uses at @5; the check touches it). Proof gives the four explicit products for nbar and n. Check: the
   identity moved to the nbar component (referee's P1 is now the test), plus E_perp(I4 F) = J E_perp and
   eps(I4 F) = -J eps on three generic bivectors, and "n ^ a carries no E_perp". "New here" no longer claims the old
   identification; it lists the computed relation as a restatement of the stored photon result on the null data.
2. Two units named apart: J_perp = g1 g2 (spacetime, (ii), (iii)) and J the tower's kernel bivector ((ii)'s
   quantisation, (iv), (v)), with the statement that they are not identified (U6). The photon modes of (ii) are quantised
   with the tower's J because (v) realises them on tower pairs; with I4 (U1) the algebra is the same. Channel weights
   +-1/2 with unit J are stated as a definition, matched to (not derived from) light-ray (iv), which uses Hestenes' unit.
   The unit J is justified by citing synthesis.kernel-bivector-is-the-unit-of-hermitian-boson-fields-on-the-tower.
3. (ii): Dirac's rule [ , ] = J{ , } labelled the quantisation hypothesis (clause title "proved, with the quantisation
   rule a hypothesis"); completeness of the data on N (zero modes dropped) taken as the light-front setting with Kogut
   and Soper cited; the closed generator named as the discretised light-cone setting, distinct from the full-line null
   vacuum of (v).
4. Reading and technical rewritten: free Maxwell theory in STA gives the null-plane kinematics (classical, transverse,
   as in light-front quantisation); the ladder adds exact helicity-0 pairs (density waves, not photons) and the
   helicity +-1 relations only collectively, in mean square on the null vacuum in the continuum of generators. Technical
   ends with "Not given: the transverse dynamics, the coupling to charges, or other gauge bosons."
5. One-liner: "exact canonical pairs only at helicity 0 (density waves, not photons) ... vanishing in mean square on the
   null vacuum ...; not the transverse dynamics, the coupling to charges, or other gauge bosons".
6. Lay: "reproduce the photon's commutation relations on the vacuum, on average, in the limit of infinitely many light
   rays"; the free-data sentence credited to ordinary electromagnetism.
7. Dispersion scoped: [H, j] = -m j is for the window level operator, i.e. the second quantisation of the compression of
   the null translation generator to the band modes up to the shift 1/2 and the band scale, citing
   synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves (ii), (iii); not the
   generator itself (formal (v) and a new proof paragraph). Also added: [eps_m, eps_m*] on Omega has no fluctuation
   (j_0^{xy} Omega = delta_xy h Omega), the defect is only off-diagonal.
8. Prior art: Kogut and Soper and Pryce marked verified (per the referee); covariant phase space (Crnkovic and Witten;
   Lee and Wald) for (i), discretised light-cone quantisation (Maskawa and Yamawaki; Pauli and Brodsky), Goddard and
   Olive, Jordan: cited from memory.
9. Q(E_perp) for E_perp^2 at every level and in the proof.
Optional item done: (v) checked with a J-valued M = [[1, J], [2, -J]] (||M M*||_F^2 = 31, tr 7: ||D Omega||^2 = 62,
central value 7, matching the referee's own computation). Not done: an exact check of the (ii) mode algebra (still
proof only).

Overlap rulings applied: the window identity is cited as synthesis.density-modes-bosonise-only-along-one-null-direction
(i), "here for unequal shifts m, l" (the identity stays displayed since the unequal-shift case is used and proved here);
the rotation cited as synthesis.ladder-bosons-inherit-spin-statistics-from-the-single-modes (i) with weights +-1/2; (v)
cross-cites synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins (iv) for the finite capacity (this
proposal being the mean-square side). Also from the referee's notes: transverse cells made explicit (one generator per
cell of area s, the cell form of delta^2(y - y')); the check's distinct-generator commutation is noted as tested on
distinct channels.
