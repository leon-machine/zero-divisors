---
id: synthesis.array-ln2-is-zero-mode-doublet-one-tower
kind: claim
version: 6
title: 'Under (Q) version 2, an array''s ln 2 is its zero-mode charge doublet'
status: proved
region: synthesis
subject: thermality
tags: [boundary-modes, mode-counting, car-algebra, counting-rules, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: 'maintainer pass on Leon''s decisions, the weights kappa k labelled as version 2 of premise (Q)'
  version: 5
  source: maintainer pass 2026-11-07 (decisions)
- name: Claude Fable 5.2
  role: wording of the reference to Joint J3 aligned with its version 3, partial-wave channels in place of the s-wave of a field
  version: 6
  source: maintainer pass of 2026-11-09
review: draft
about:
- obj.hawking.boundary-mode-algebra-windows-boost-dynamics
derivations:
- name: main
  uses:
  - singularity.bosonisation-bridge-s-wave-sector@8
  - hawking.imported-s-wave-bosonic-sector@6
  - hawking.current-commutator-exactly-edge-split@4
  - synthesis.residue-from-mode-entropy@4
  - hawking.helicity-lift-joints-itemised@8
  - synthesis.capacity-per-mode-independent-of-helicity@2
  - synthesis.imported-jacobi-triple-product@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_charge_times_oscillator
- kind: check
  ref: check.py::check_currents_blind_to_doublet
- kind: check
  ref: check.py::check_one_tower_not_two
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.capacity-per-mode-independent-of-helicity
  - synthesis.residue-from-mode-entropy
  - hawking.joint-j3-s-wave-reduction
extraction:
  maintainer_pass_2026_11_09b:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: 'Version 5 -> 6, wording only: where the formal and technical levels said that Joint J3 identifies the current boson with the s-wave of a four-dimensional field (s-wave photons), they now say its partial-wave channels, as hawking.joint-j3-s-wave-reduction version 3 does (a photon has no s-wave). Clause (iv), one helicity channel per array at most, is the bound that J3 version 3 cites when it records that its identification is not one array tower per helicity channel; the clause is unchanged. Edges, proof and checks unchanged; pins left for the repin.'
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version labels (DECISIONS G7; Leon''s 23 October ''note only'' decision; R01 item 2): Premise (Q) singularity.q-joint-quasi-freeness-s-wave is at version 3 with weights kappa(k + 1/2), while this entity states version 2''s weights kappa k (sea at a site); the displays now say ''version 2 of premise (Q)'' where they use kappa k. Statement content, edges and pins unchanged.'
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Title, one-liner and lay said Under (Q) while the statement is at (Q) version 2 (weights kappa k), the offset at which the doublet exists; at version 3 (kappa(k + 1/2)) there is no doublet (clause (ii) already says so). They now name version 2. The formal and technical levels still say (Q) without a version; listed for Leon.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: >-
      Version 3 -> 4, note only, statement and proof unchanged. The theorem assumes Premise (Q) version 2,
      weights kappa k, and its doublet and per-array ln 2 in (ii) exist only at that offset. Premise (Q)
      version 3 (Leon's decision of 23 October) takes kappa(k + 1/2). At that offset, as (ii) already states,
      the ground energies are Q^2/2, there is one zero-energy configuration and no doublet, and the same
      single oscillator tower appears, so (i), (iii) and (iv) hold with the tower unchanged: one array is one
      helicity channel. The array then carries exactly (1/2) ln 2
      (synthesis.half-integer-weight-array-carries-half-ln2), two arrays carry one registered mode's ln 2
      under entropy matching, and so one registered mode carries two arrays, hence two helicity channels. The
      closing sentence (nothing here identifies one registered mode with two arrays or two helicities) and
      the reading that one array, hence one registered mode, supplies one helicity channel hold only for the
      offset kappa k. Deriving that one counted unit is two arrays, one massless species with both
      helicities, is open (op.residue-killing-weights).
  correction:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'W503: the lay level now states Premise (Q), which the formal statement assumes. Version 2 -> 3.'
  maintainer_pass_2026_10_22:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Maintainer pass: the Jacobi triple product, cited from memory in the proof, is now the imported Fact synthesis.imported-jacobi-triple-product, added to uses and cited in the proof and the check. Version 1 -> 2.'
  open_problem: op.helicity-per-boundary-mode
  note: >-
    Reads the boundary-mode array of the bosonisation bridge through the boson-fermion
    correspondence. Its Fock space is charge sectors times one oscillator tower; the ln 2 that
    the residue counts per array is the two-fold degeneracy of the charge-0 and charge-1
    ground states (the zero mode), which no current with m != 0 connects (the charge current
    a_0 reads it without changing it); the current boson, the object Joint J3 lifts to a
    four-dimensional field, carries only the tower's entropy. One array has one oscillator per boost weight, so it can register one helicity
    channel, not both. J3 itself is not derived. Transport-absent bosonisation applied to the
    series' array.
---

## formal
Assume (Q) (Premise \claimref{singularity.q-joint-quasi-freeness-s-wave}) in its version 2, as the bridge does, so that one boundary-mode array $\{\psi_{k}\}_{k \in \Z}$ of Theorem \claimref{singularity.bosonisation-bridge-s-wave-sector} has weights $\kappa k$, sea filled below $k = 0$, and is in the Gibbs state at $\beta = 2\pi/\kappa$. Measure charge $Q$ and energy $E$ (in units of $\kappa$) from the sea. Then:
\begin{enumerate}
\item[(i)] (charge times one tower) the configurations of charge $Q$ and energy $E$ are counted by $p(E - Q(Q-1)/2)$, with $p$ the partition function; equivalently the Fock space is $\bigoplus_{Q \in \Z}\mathcal{H}_{Q} \otimes \mathcal{F}$, where $\mathcal{H}_{Q}$ is one state of energy $Q(Q-1)/2$ and $\mathcal{F}$ is the Fock space of a single oscillator tower, one oscillator of energy $m$ for each $m \ge 1$, and the Gibbs state is the product of a charge distribution $P(Q) \propto e^{-2\pi Q(Q-1)/2}$ with the thermal state of the tower. Hence the array's thermal entropy splits exactly as $S_{\mathrm{array}} = S_{\mathrm{charge}} + S_{\mathrm{osc}}$ with $S_{\mathrm{osc}} = \sum_{m \ge 1}s_{\mathrm{B}}(2\pi m)$, $s_{\mathrm{B}}(x) = x/(e^{x} - 1) - \ln(1 - e^{-x})$;
\item[(ii)] (the doublet, and its dependence on the offset) exactly two configurations have zero energy, of charges $0$ and $1$ (the sea, and the sea with the zero mode filled), so $S_{\mathrm{charge}} > \ln 2$: the $\ln 2$ that Theorem \claimref{synthesis.residue-from-mode-entropy}(vi) assigns to the zero-weight mode of an array is the two-fold degeneracy of this charge doublet, and the charge sector carries that $\ln 2$ plus a positive excess from the higher charges. The doublet belongs to (Q)'s version-2 offset (sea at a site). For the other particle-hole symmetric offset, weights $\kappa(k + \tfrac12)$ with the sea between sites, the same count gives ground energies $Q^{2}/2$, the same oscillator tower, and a unique zero-energy configuration: no doublet (the classification of the two offsets is filed alongside, synthesis.q-splits-maximum-entropy-affine-weights);
\item[(iii)] (no current with $m \neq 0$ connects it) every current commutes with the total charge; every $a_{m}$ with $m \neq 0$ acts on the tower factor $\mathcal{F}$ alone and has no matrix element between the two doublet states, and no element of the current algebra carries one doublet state to the other, since they differ in charge and are related by a fermion. The charge current $a_{0}$, the normal-ordered total charge, acts on the charge factor: it reads the doublet (eigenvalues $0$ and $1$) without changing it. In particular the Bose-Einstein occupancy of the bridge's clause (3) and the current boson that Joint J3 (Proposition \claimref{hawking.helicity-lift-joints-itemised}) identifies with the partial-wave channels of a four-dimensional field (Fact \claimref{hawking.imported-s-wave-bosonic-sector}) carry $S_{\mathrm{osc}}$ only;
\item[(iv)] (one tower, so one channel) at each boost weight $m\kappa$ the current sector has exactly one oscillator: the charge-$0$ level counts are $p(E) = 1, 1, 2, 3, 5, 7, 11$ for $E = 0, \ldots, 6$, whereas two independent towers, which is what both helicities of one $(\omega, \ell, m)$ partial wave are, give $1, 2, 5, 10, 20, 36, 65$. So one array can register at most one helicity channel of the lift; two helicities need two arrays.
\end{enumerate}
Consequently, in the arrays reading of the residue, the two-fold degeneracy that supplies the per-array $\ln 2$ lies in the charge sector, exists only at (Q)'s version-2 offset, and does not depend on how Joint J3 assigns helicities; the current boson carries $S_{\mathrm{osc}}$ only (its value, computed in the proof, is a small fraction of $\ln 2$). At the other offset the array carries $\tfrac12\ln 2$ (filed alongside, synthesis.half-integer-weight-array-carries-half-ln2). Nothing here identifies one registered mode with two arrays or with two helicities.

## technical
The boson-fermion correspondence splits the series' s-wave array into two independent parts: a charge sector, labelled by the number of fermions added to or removed from the sea, and one tower of bosonic oscillators, which is what the currents create. With the (Q) weights of its version 2, the lowest energy at charge $Q$ is $Q(Q-1)/2$ in units of $\kappa$, so charges $0$ and $1$ are degenerate at zero energy: the zero mode can be empty or filled for free. That two-fold degeneracy is where the $\ln 2$ per array lives; with the sea placed between sites instead, the other particle-hole symmetric choice, there is no zero mode, no degeneracy, and the array carries half as much. The currents conserve charge: the charge current reads which of the two states the array is in, and no other current can move between them. The oscillators, which become the photons' partial-wave channels under Joint J3, carry only the tower's entropy, a small fraction of $\ln 2$ at the Hawking temperature. Since the current sector has one oscillator per frequency, an array supplies one helicity channel; the two helicities of a partial wave need two towers, whose state counts differ already at the first level. The capacity per array is a charge-sector quantity, so no reading of J3 can change it, and a residue built from helicity channels of the current would be far from both registered values.

## lay
The series models the boundary modes as a single row of fermion slots, and shows that their collective ripples behave like particles of light. Assuming, as the series does for this step, that the modes are jointly in the simplest thermal state (Premise (Q), in its earlier form, with one slot at exactly zero energy), this result separates the row's information into two parts. Almost all of it, one bit, sits in a single question: whether the slot exactly at the zero level is filled. The ripples, which are the light, cannot change that answer, and they carry only a small fraction of the information. The row also turns out to contain exactly one kind of ripple at each frequency, which is enough for one polarisation of light but not for both. So the earlier question of whether one boundary mode holds one polarisation or two does not affect the count that fixes the series' calibration, and one row of modes supplies one polarisation. In the premise's present form no slot sits at zero energy; there is then no such bit, a row holds half a bit, and the single kind of ripple per frequency is unchanged.

## one-liner
Under (Q) in its version 2 (weights $\kappa k$) the s-wave array is charge sectors times one oscillator tower: the per-array $\ln 2$ is the two-fold degeneracy of the zero-mode charge doublet of that offset, absent at the present offset $\kappa(k + \tfrac12)$, which no current with $m \neq 0$ connects, the current boson carries only the tower's entropy, and one array supplies one helicity channel, not two.
