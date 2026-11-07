---
id: synthesis.rung-field-level-needed-off-balance-and-not-right-invariant
kind: claim
version: 5
title: 'Off balance the rung vacuum needs a level, which is not right-invariant'
status: proved
region: synthesis
subject: standard-model
tags: [symmetry-breaking, gauge-fields, undetermined-input]
proposed_by:
  kind: ai
  session: 2026-11-01-weak-scale
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: 'GA rewrite (the weak generators as slot bilinears)'
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'notation: the Hermitian norm renamed sans-serif N'
  version: 5
  source: maintainer pass 2026-11-07 (decisions, second round)
review: draft
derivations:
- name: main
  uses:
  - synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus@6
  - synthesis.rung-field-on-the-lift-locus@5
  - synthesis.rung-unit-transverse-to-norm@3
  - standard-model.generation-ten-under-pati-salam@7
  - synthesis.imported-fayet-iliopoulos-level-only-for-abelian-factors@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_level_necessary_for_an_off_balanced_vacuum
- kind: check
  ref: check.py::check_commutant_of_weak_su2_is_su2_containing_hypercharge
- kind: check
  ref: check.py::check_right_moment_maps_and_the_orbit_of_m
- kind: check
  ref: check.py::check_level_not_right_invariant_and_mirror_in_right_group
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.rung-unit-second-free-number
  - synthesis.rung-field-charged-scalar-sum-rule
  - synthesis.up-down-split-under-conjugate-reading-needs-su2r-odd-weighting
extraction:
  maintainer_pass_decisions_2:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Notation (Leon, second round, answer 8; DECISIONS H5, consistency-R04 item 4): the rung-field results wrote N for the Hermitian norm of the rung component, N(c) = (|alpha|^2 + |beta|^2)/2, while N = M_P/H is the hierarchy number in the same subject. The norm is now \mathsf{N} (its values \mathsf{N}^*, \mathsf{N}_0, its derivative \partial_{\mathsf{N}}, and W(\mathsf{N})) in formal, proof and the other levels, in every rung-field entity that writes it (14 entities, one batch), so the family stays uniform. The letter was chosen free in the entity and in its subject (standard-model and quantum-fields): R04''s example \mathcal{N} is the store macro \Ncone (the null cone) and the number operator of synthesis.floor-regulator-... in quantum-fields. No content change.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4. The weak generators, written as Pauli matrices on the coefficient doublet (T_j = (I_4/2) sigma_j, Y = (I_4/2) 1), are now Clifford elements in the slot generators E_ab = v_a w_b: T_1 = (I_4/2)(E_45 + E_54), T_2 = (1/2)(E_45 - E_54), T_3 = (I_4/2)(E_44 - E_55), Y = (I_4/2)(E_44 + E_55), as reader R04 proposed; the matrices on alpha stay as a labelled reading. Verified exactly with lib/GA.py in Cl(2,2) (v_a w_b + w_b v_a = delta_ab, [E_ab, v_c] = delta_bc v_a, [E_ab, w_c] = -delta_ac w_b) and by the matrix identities (I_4/2) sigma_j = the stated combinations of matrix units.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The unit on the rung field is written as I_4, which commutes with the rung vectors (C read as span{1, I_4}): the weak generators (I_4/2) sigma_j, R_2 = (1/2)(I_4 epsilon beta, -I_4 epsilon alpha), the moment maps G(c, -I_4 R_a c), and the substitution d -> I_4 d in the proof; nothing stays.'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2: uses edge to the imported Fayet-Iliopoulos Fact @1 (a D-term level exists only for abelian factors), which clause (2) makes explicit on the rung summand; the proof and the note, earlier citing it from memory, now cite the Fact. Content unchanged.'
  open_problem: op.rung-unit
  note: >-
    Taken adversarially, from the problem's second line of attack (can the level be anything but an input)
    and from the search for a symmetry of the stored structure that moves v/H. No such symmetry exists: the
    frame boost commutes with the tower conjugation only trivially, and N/|Q| = cosh 2 eta separates the
    frames, so the independence of v/H is of free-constant type, carried by the level. This entity sharpens
    that in two directions. (1) The level cannot be traded for the second invariant: clause (1) is a
    corollary of the stored clause (4), a two-line elimination of W'(N*) between the stored vacuum equation and
    the stored charged mass, giving m_pm^2 = (M_Z^2 - M_W^2)(xi/m* - 1) for every W(N), with or without
    dimensionful constants (a term linear in m would itself be a level, so functions of N are the general
    level-free case); a locally stable charge-preserving vacuum off the balanced frame needs xi of the vacuum's
    sign with |xi| > |m*|, and |m*| is about N* = v^2/2 for v >> H. (2) The level is not allowed by the right-handed su(2), the standard fact that a Fayet-Iliopoulos level exists only for abelian factors of the gauge algebra (Fayet and Iliopoulos 1974, imported as synthesis.imported-fayet-iliopoulos-level-only-for-abelian-factors) transposed to the rung summand: the commutant of the weak
    su(2) in the isometries of (G, Q) on the rung summand is three-dimensional (complete computation), an
    su(2) containing the hypercharge, which on the stored Pati-Salam decomposition is su(2)_R on the slot
    bidoublet; it moves the moment map over the whole fibre of the orbit space, so its invariants on the
    locus are functions of N alone, and its element 2 R1 followed by a slot swap in U(2) (an element of the group
    generated by U(2) and su(2)_R, not of su(2)_R) is the mirror involution mu -> H^2/mu. Reading (argued, not part of the statement): at a stage with su(2)_R gauged the level
    vanishes and the frame's charge alignment is undecided; the electroweak level, which (1) bounds below by
    |m*|, can only be the T_3R-odd remnant of su(2)_R breaking, the same kind of spurion that the up-down
    split needs. No value of v/H is computed. Clause (2), the obstruction, is transport-absent (gauge
    invariance); the setting of clauses (1) and (3), the locus, the lift family and the mirror frames, is
    transport's, so those clauses are transport-convenient.
---
## formal
In the setting of Theorem \claimref{synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus}: $c = \sum_{a}(\alpha_{a}v_{a} + \beta_{a}w_{a})$ in $\mathcal{R}_{\C}$, $Q(c) = \alpha^{\mathsf T}\beta$, $\mathsf{N}(c) = \tfrac12(|\alpha|^{2} + |\beta|^{2})$, $G(c, d) = \operatorname{Re}(c^{*}\cdot d)$, the weak $\su(2)$ generated by $T_{1} = \tfrac{I_{4}}{2}(E_{45} + E_{54})$, $T_{2} = \tfrac12(E_{45} - E_{54})$, $T_{3} = \tfrac{I_{4}}{2}(E_{44} - E_{55})$, in the slot generators $E_{ab} = v_{a}w_{b}$, which act by commutator as the matrix unit on the $\alpha$-coefficients and as minus its transpose on the $\beta$-coefficients ($\alpha \mapsto \tfrac{I_{4}}{2}\sigma_{j}\alpha$ in the coefficient reading, the unit on the rung field being the field theory's unit $I_{4}$, which commutes with the rung vectors, $\C = \mathrm{span}\{1, I_{4}\}$, $\beta \mapsto \overline{\tfrac{I_{4}}{2}\sigma_{j}}\beta$), the hypercharge $Y$, the moment map $m = \tfrac12(|\alpha|^{2} - |\beta|^{2})$, $H^{2} = \Lambda/3$, the locus $L = \{Q = -H^{2}\}$, the lift family $c_{\lambda}$ ($\alpha = (H^{2}/\lambda, 0)$, $\beta = (-\lambda, 0)$), the D-term potential $V_{D}$ with level $\xi$ and the tree masses $M_{W}^{2} = \tfrac12 g^{2}\mathsf{N}^{*}$, $M_{Z}^{2} = \tfrac12(g^{2} + g'^{2})\mathsf{N}^{*}$. Let $\varepsilon = \bigl(\begin{smallmatrix}0 & 1\\ -1 & 0\end{smallmatrix}\bigr)$, $R_{1}(\alpha, \beta) = \tfrac12(\varepsilon\beta, \varepsilon\alpha)$, $R_{2}(\alpha, \beta) = \tfrac12(I_{4}\varepsilon\beta, -I_{4}\varepsilon\alpha)$.
\begin{enumerate}
\item \emph{(The level is needed off the balanced frame.)} Let $V = V_{D} + W(\mathsf{N})$ with $W$ any twice differentiable function, and let $c_{\lambda^{*}}$ be a critical point of $V$ on $L$ with $m^{*} = m(c_{\lambda^{*}}) \neq 0$ ($\lambda^{*} \neq H$). Then the two charged modes have
\[
m_{\pm}^{2} = (M_{Z}^{2} - M_{W}^{2})\Bigl(\frac{\xi}{m^{*}} - 1\Bigr).
\]
Hence the vacuum is locally stable against charge breaking only if $\xi/m^{*} > 1$: the level is nonzero, has the sign of $m^{*}$ and exceeds $|m^{*}| = H^{2}|\sinh 2\eta^{*}|$ in size. With $\xi = 0$ every critical point of the family off the balanced frame has $m_{\pm}^{2} = -(M_{Z}^{2} - M_{W}^{2}) < 0$, for every $W(\mathsf{N})$.
\item \emph{(The right-handed $\su(2)$.)} The real-linear maps of $\mathcal{R}_{\C}$ that preserve $G$ and $Q$ and commute with the weak $\su(2)$ form a three-dimensional real Lie algebra, spanned by $R_{1}$, $R_{2}$ and $Y$, with $[R_{1}, R_{2}] = Y$, $[R_{2}, Y] = R_{1}$, $[Y, R_{1}] = R_{2}$. Its moment maps $\mu_{R,a}(c) = G(c, -I_{4}R_{a}c)$ satisfy $\mu_{R,3} = \mu_{Y} = \tfrac12 m$ and $\sum_{a}\mu_{R,a}^{2} = \sum_{j}\mu_{j}^{2} = \tfrac14(\mathsf{N}^{2} - |Q|^{2})$. The Cayley elements $C_{t} = \bigl((1 - s) + 2tR_{1}\bigr)/(1 + s)$, $s = t^{2}/4$, of $tR_{1}$ keep $\mathsf{N}$ and $Q$, commute with the weak $SU(2)$, and give $m(C_{t}c_{\lambda}) = \frac{(1 - s)^{2} - 4s}{(1 + s)^{2}}\,m(c_{\lambda})$, which runs from $m(c_{\lambda})$ at $t = 0$ to $-m(c_{\lambda})$ at $t = 2$. Consequently on $L$ every function invariant under $U(2)$ and $C_{t}$ is a function of $\mathsf{N}$ alone, and a potential $V_{0} + k\mu_{Y}$ with $V_{0}$ invariant under $C_{t}$ is invariant only for $k = 0$; in particular the level term of $V_{D}$ is not invariant, while $g^{2}\sum_{j}\mu_{j}^{2} + g_{R}^{2}\sum_{a}\mu_{R,a}^{2}$ is. On the decomposition of Proposition \claimref{standard-model.generation-ten-under-pati-salam}, in which the rung directions span the bidoublet $(2,2,1)$, this algebra is the $\su(2)_{R}$ acting on the bidoublet, and $Y$ acts there as $T_{3R}$.
\item \emph{(The mirror involution through the right-handed $\su(2)$.)} $C_{2} = 2R_{1}$, and the swap $S$ of the two slots ($\alpha \mapsto S\alpha$, $\beta \mapsto S\beta$, an element of $U(2)$) after $C_{2}$ sends $c_{\lambda}$ to $c_{H^{2}/\lambda}$: the involution $\mu \mapsto H^{2}/\mu$ of Theorem \claimref{synthesis.rung-unit-transverse-to-norm}(3), which exchanges the two doublet lifts, is realised by an element of the group generated by $U(2)$ and $\su(2)_{R}$.
\end{enumerate}

## technical
Take the rung field's D-term action on the null-lift locus and add any function $W(\mathsf{N})$ of the Hermitian norm. At a charge-preserving vacuum on the lift family away from the balanced frame, eliminating $W'(\mathsf{N}^{*})$ between the stored vacuum equation and the stored charged mass (a corollary of the stored result) gives the charged pair's mass in terms of the level alone: $m_{\pm}^{2} = (M_{Z}^{2} - M_{W}^{2})(\xi/m^{*} - 1)$. So local stability against charge breaking needs a level of the vacuum's sign and larger than the vacuum's moment map; with no level, every off-balanced point of the family is a saddle in the charged directions, whatever $W$ is, and constants inside $W$ cannot replace the level. A term linear in the moment map would itself be a level, so functions of the norm are the general level-free case. The level, in turn, is forbidden by the right-handed $\su(2)$, the familiar statement that a Fayet-Iliopoulos level exists only for abelian factors of the gauge algebra: the maps commuting with the weak $\su(2)$ and preserving both forms make up exactly one more $\su(2)$, which contains the hypercharge itself; its rotations move the hypercharge moment map at fixed norm across the whole fibre of the orbit space, so its invariants on the locus are functions of the norm alone, and a constant shift of the hypercharge moment map is not one of them. One of its elements, followed by a slot swap in $U(2)$, is the mirror involution of the units that exchanges the two doublet lifts. On the stored Pati-Salam decomposition this $\su(2)$ is $\su(2)_{R}$ on the slot bidoublet.

## lay
In this framework the size of the Higgs field is set by a constant called the level, and it was not known whether some other ingredient of the Higgs potential could do the same job. It cannot: whatever else is added, a stable vacuum with the observed charge conservation needs the level, and the level must be at least as large as the Higgs field's own size squared. The level, however, is forbidden by the larger left-right symmetric structure that the framework's particle content already has, because that symmetry rotates the hypercharge into other directions. So the weak scale can only come from whatever breaks the left-right symmetry, the same kind of ingredient that is needed to make up-type and down-type quark masses differ.

## one-liner
For $V_{D} + W(\mathsf{N})$ with any $W$, an off-balanced charge-preserving vacuum has $m_{\pm}^{2} = (M_{Z}^{2} - M_{W}^{2})(\xi/m^{*} - 1)$, so it needs a level $\xi/m^{*} > 1$; the commutant of the weak $\su(2)$ on the rung summand is an $\su(2)_{R}$ containing $Y$, whose invariants on the locus are functions of $\mathsf{N}$ and under which the level is not invariant, and whose element $2R_{1}$, followed by a slot swap in $U(2)$, is the mirror involution $\mu \mapsto H^{2}/\mu$.
