# Cross-subject items from reader R12 (tower, one-relation)

No entity outside R12's list was edited.

1. **The field theory's unit against T16's imaginary unit.**
   - one-relation.one-datum-not-two-imaginary-unit and one-relation.schr-odinger-slow-shadow (one-relation): the descent's
     complex structure is a right-acting bivector $J$ that commutes with the law's odd right factor $C$ (Hestenes'
     $I\sigma_3$). The pseudoscalar is excluded because it anticommutes with $C$.
   - conventions.md U1 and the field-theory results (for example synthesis.one-loop-qed-in-the-spacetime-algebra): the field
     theory's unit is $I_4$. It acts on the left on even values and as the right unit $xI_4$ otherwise.
   - Evidence (exact, lib/GA.py): $I_4$ anticommutes with $C = I_4\gamma_3$. So for even $\psi$ the phase $\psi \mapsto \psi
     e^{I_4\theta}$ is the chiral phase of one-relation.odd-square-roots-chiral-phase, which sends $C$ to $Ce^{2\theta I_4}$.
     It is not a symmetry of $\nabla\psi = m\psi C$, so $e^{-I_4 p\cdot x}$ is not the plane-wave unit of the massive
     Dirac-Hestenes law. The store relates the two units only on massless modes:
     synthesis.massless-frequency-sign-relative-to-i4-is-not-the-chirality (ii) gives $L_{I_4} = -\Gamma R_{I\sigma_3}$.
   - Proposed: a field-theory entity (or the conventions file) should say how its massive Dirac fields' $I_4$ relates to
     Hestenes' right unit. The two are different readings of the spinor (the field theory's massive numerators are not
     even). I added a "which unit acts where" sentence to one-datum. That does not settle the massive case.

2. **A mis-cited fact about the exceptional set.** scrambling.pair-mode-qubit-one-object (tower; in R12's list) and
   scrambling.epoch-modular-period-two-unknowns-become (scrambling; not mine) both attribute "one ladder pair per point of the
   exceptional set" to Fact tower.witt-index-quantum-capacity. That theorem states only the vector-mode capacity
   $\min(p,q)$; it says nothing about the exceptional set. The statement is T04's corank-one count:
   sheaf.schwarzschild-degeneration-boundary-tame (T04 Thm 8.7), quoted in singularity.c2-cell-density.
   - Proposed: cite the T04 entity, and add a `uses` edge in the first entity (maintainer decision; see For Leon).

3. **Ladder labelling between the atom and the tower.**
   - synthesis.phase-flow-is-time-rotor-flow-kms-continuation (iii) (not mine) reads $K_{\mathrm{tot}} = \sum (N_j -
     \tfrac12)$ with the atom's $v$ as annihilator ($N = v^*v$).
   - The tower's $v_j = \tfrac12(e_j + f_j)$ creates (tower.car-limit-even-charge), so there $N_j - \tfrac12 = -K_j$.
     Checked exactly: $vw - \tfrac12 = -\tfrac12 ef$.
   - I recorded this in synthesis.plane-grading-records-residue-sign, which combines the two. It has no effect on that
     result, because the weights become $-1$ and are still odd. The phase-flow theorem should say which labelling its
     $N_j$ uses when it is applied to tower planes.

4. **The $\gamma_5$ convention in two T14a remarks.** note.odd-extensions.added-axis-pseudoscalar and
   note.odd-extensions.one-operator-sees-difference (tower) read physicists' notation with
   $\gamma_5 = \gamma_0\gamma_1\gamma_2\gamma_3$. The source writes $i\gamma_5$ for the complexified $e_5$.
   - The conventions' chiral-loop section, and synthesis.chiral-abelian-loops-with-i4-as-the-bmhv-gamma5-need-finite-symmetry-restoring-counterterms
     and the triangle-anomaly result, use the Hermitian $\gamma_5$ (unit times $I_4$).
   - Under that convention the two readings exchange. Checked exactly in $\Cl(2,3)$:
     $I_5(I_5\omega') = -\omega'$ and $e_5 = \pm I_5\omega'$.
   - I stated the convention in both notes. No other subject needs a change.

5. **Complexification of the tower limit against U3.** conventions.md U3 says $\Cl(p,q)_\C$ is complexified by the odd
   extension ($I_5$, $I_7$). The tower results use a formal unit $1 \otimes I_4$ in a tensor factor:
   tower.structure-tower-c-norms, tower.car-limit-even-charge, hawking.imported-algebra-boundary-modes-car-algebra,
   synthesis.plane-grading-records-residue-sign (iv)-(v) and synthesis.tower-limit-forgets-residue (iv). The reason is that
   the floors' odd extensions do not pass to the limit.
   - For the physical ground this $I_4$ is not the ground's own volume element. I made that explicit in structure-tower and
     car-limit.
   - Proposed (conventions, maintainer): add this case to the unit principle. Its symbol $I_4$ there also clashes with the
     ground's $I_4 = \gamma_0\gamma_1\gamma_2\gamma_3 \in \Cl(1,3) \subset T_k$. A distinct symbol for the scalar factor's
     unit would remove the clash.
