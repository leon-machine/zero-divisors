---
id: synthesis.q-splits-maximum-entropy-affine-weights
kind: claim
version: 5
title: 'Premise (Q) splits into maximum entropy and an affine weight law'
status: proved
region: synthesis
subject: thermality
tags: [thermal-premises, car-algebra, boundary-modes, bosonisation, undetermined-input, needs-continuum]
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
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 5
  source: maintainer pass 2026-11-07 (GA units)
review: draft
about:
- obj.singularity.geometric-modular-condition-g
derivations:
- name: main
  uses:
  - singularity.chains-state-class-stability@7
  - singularity.exact-equilibrium-over-determines-boundary-modes@5
  - singularity.kms-uniqueness-factor@4
  - singularity.deficit-carried-quanta-correlations@5
  - singularity.deficit-theorem-cost-descent-exactly@4
  - hawking.imported-quasi-free-states-car-algebra@2
  - singularity.bosonisation-bridge-s-wave-sector@7
  - scrambling.boundary-mode-space-matrix@4
  - scrambling.principality-indifference-sphere@4
  - synthesis.residue-common-weight-particle-hole@4
  - synthesis.residue-from-mode-entropy@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_quasi_free_part
- kind: check
  ref: check.py::check_affine_law
- kind: check
  ref: check.py::check_planck_offset_free
- kind: check
  ref: check.py::check_particle_hole_offsets
- kind: check
  ref: check.py::check_tensor_placement
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - singularity.q-joint-quasi-freeness-s-wave
  - synthesis.residue-common-weight-particle-hole
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The unit of the fermion array mode space (boundary modes) is written as the field unit I_4: the boost-flow phases and the conjugations e^{I_4 t K_geo}, with C read as span{1, I_4}; nothing stays.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Version 1 -> 2, note only, statement and proof unchanged. The text writes (Q-w) as omega_k = kappa k and names the class with the sea at a site (d = 0) as (Q)''s choice; that is Premise (Q) version 2. Premise (Q) version 3 (Leon''s decision of 23 October) adopts the other class, d = c/2 at y = 2 pi, weights kappa(k + 1/2), by decision on the reading of the modes as spinor fields of boost weight 1/2 under (N+), not by derivation. The theorem''s content (the maximum-entropy clause, the affine law, the Planck clause for every affine law, the two offset classes and the free slope) is unchanged; under version 3 the zero-weight principal level of (v) does not occur on the array, and the entropy of one array at y = 2 pi is (1/2) ln 2 (synthesis.half-integer-weight-array-carries-half-ln2), not ln 2 + epsilon. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3. Sample inputs moved to module level; no change to what is tested. Version 3 -> 4.'
  open_problem: pr.q-quasi-freeness
  note: >-
    Splits Premise (Q) into its two clauses and settles what each needs. The quasi-free clause,
    given (P) and (R), is equivalent to (G) and to the maximum-entropy rule on the class of
    states with the marginals (R) fixes, so it is a selection principle, not a consequence of
    (P) and (R). The weight clause is reduced to its affine form, which is forced if each current of the
    bosonisation bridge is a normal mode of the boost flow (the reading of its Planck clause),
    plus two data the framework does not fix: the sea offset (two
    particle-hole symmetric classes, (Q) taking the one with a zero-weight mode) and the
    dimensionless slope beta c, which (Q) sets to 2 pi. The tension with rotation equivariance
    found for (Q)'s weights on a principal window disappears when the array index and the
    magnetic index are different tensor factors. Mostly transport-absent fermion algebra; the
    series enters through the class C, (G), the array of the bosonisation bridge and the
    principal embedding. Filed alongside: synthesis.half-integer-weight-array-carries-half-ln2
    (the entropy of one array in the class with the sea between sites) and
    synthesis.r-le-i-independent-spectrum-condition-separates (a unique-ground-state selection
    cannot give (R) with (L_E)); read together, the selection that delivers (R) under (L_E) is of
    maximum-entropy type, which is clause (i) here.
---

## formal
Let $\{\psi_{k}\}_{k \in \Z}$ be the fermion array of Theorem \claimref{singularity.bosonisation-bridge-s-wave-sector}, with currents $a_{m} := \sum_{k}\psi_{k}^{\dagger}\psi_{k+m}$, mode weights $\omega_{k}$, number operators $N_{k} = \psi_{k}^{\dagger}\psi_{k}$, $K_{k} = N_{k} - \tfrac12$ and $K_{\mathrm{geo}} = \sum_{k}\omega_{k}K_{k}$, and let $\mathcal{C}$ be the class of Corollary \claimref{singularity.chains-state-class-stability}: the even states every single-mode marginal of which is the Gibbs state of $K_{k}$ at $\beta = 2\pi/\kappa$, with occupation $n_{k} = (e^{\beta\omega_{k}} + 1)^{-1}$. Premise \claimref{singularity.q-joint-quasi-freeness-s-wave} has two clauses: (Q-qf) the joint state is the gauge-invariant quasi-free state with $\langle\psi_{k}^{\dagger}\psi_{l}\rangle = \delta_{kl}n_{k}$; (Q-w) $\omega_{k} = \kappa k$. Then:
\begin{enumerate}
\item[(i)] (the quasi-free clause is a maximum-entropy selection) on every finite window, for $\varrho \in \mathcal{C}$ with product of marginals $\sigma$, one has $S(\sigma) - S(\varrho) = C(\varrho) = \rel{\varrho}{\sigma}$, with $C$ the total correlation of Corollary \claimref{singularity.deficit-carried-quanta-correlations}, and the following are equivalent: (a) $\varrho$ satisfies (Q-qf); (b) $\varrho = \sigma$; (c) $\varrho$ satisfies the geometric modular condition (G); (d) $C(\varrho) = 0$; (e) $\varrho$ has the largest von Neumann entropy in $\mathcal{C}$. Since $\mathcal{C}$ contains correlated states, (Q-qf) does not follow from (P) and (R); given them it is the maximum-entropy rule at the marginals (R) fixes, equivalently (G) in the stationary idealisation;
\item[(ii)] (the affine law) every current $a_{m}$, $m \neq 0$, is a normal mode of the boost flow, $e^{I_{4}tK_{\mathrm{geo}}}a_{m}e^{-I_{4}tK_{\mathrm{geo}}} = e^{-I_{4}\lambda_{m}t}a_{m}$ for all $t$ (the unit of the mode space is $I_{4}$; numbers are read in $\mathrm{span}\{1, I_{4}\}$), if and only if the weights are affine, $\omega_{k} = ck + d$; then $\lambda_{m} = cm$, and the linear span of the currents is invariant under the flow exactly in this case;
\item[(iii)] (the Planck clause holds for every affine law) for affine weights with $c > 0$ and the symbol $n_{k} = (e^{\beta(ck + d)} + 1)^{-1}$, $\sum_{k \in \Z}n_{k+m}(1 - n_{k}) = m/(e^{\beta cm} - 1)$ for every $m > 0$ and every offset $d$: the Bose-Einstein occupancy at temperature $1/\beta$ and frequency $cm$ holds for every affine law, so clause (3) of Theorem \claimref{singularity.bosonisation-bridge-s-wave-sector} fixes neither $d$ nor $c$; that it requires the affine form rests on reading each current as a normal mode of the boost flow, which is (ii);
\item[(iv)] (the two free data) for affine weights and an integer $k_{0}$, the particle-hole map $\psi_{k} \mapsto \psi_{k_{0} - k}^{\dagger}$ commutes with the boost flow, and carries the quasi-free Gibbs state at each $\beta$ to itself, if and only if $ck_{0} + 2d = 0$. Up to relabelling the array there are exactly two such classes: the sea at a site ($d = 0$: one mode of zero weight per array, with $n_{0} = \tfrac12$, the flow at time $2\pi/c$ the identity), which is (Q)'s choice, and the sea between sites ($d = c/2$: no zero-weight mode, the flow at time $2\pi/c$ the parity automorphism $\psi \mapsto -\psi$). In either class the one remaining datum is the dimensionless slope $y := \beta c$, the ratio of the KMS period to the recurrence time $2\pi/c$ of the flow, multiplied by $2\pi$; (Q-w) sets $y = 2\pi$, the value at which the recurrence time of the array's flow equals the KMS period;
\item[(v)] (rotations) let the counted modes be $\psi_{k,a}$ on $\ell^{2}(W) \otimes \C^{n}$ ($\C = \mathrm{span}_{\R}\{1, I_{4}\}$), with the principal $\mathfrak{su}(2)$ of Theorem \claimref{scrambling.principality-indifference-sphere} on the second factor and the array index on the first. A quasi-free number-preserving generator with weights $\omega_{k,a}$ commutes with the second-quantised rotations if and only if $\omega_{k,a} = \omega_{k}$ does not depend on $a$; with (ii) in each channel, rotation equivariance and normal-mode currents together give $\omega_{k,a} = ck + d$, and the quasi-free state with symbol $\operatorname{diag}(n_{k}) \otimes \id$ is rotation invariant. At each array level the $n$ modes are a principal mode space of common weight $ck + d$, as Theorem \claimref{synthesis.residue-common-weight-particle-hole}(i) requires; the conflict of its clause (iv) arises exactly when a window of the array index is placed on the magnetic index. In the class with the sea at a site, the level $k = 0$ is a principal mode space at zero weight, maximally mixed and invariant under the particle-hole map of that theorem, the equality case of Theorem \claimref{synthesis.residue-from-mode-entropy}(ii).
\end{enumerate}
So (Q) is the conjunction of a maximum-entropy rule, an affine weight law (forced if each current is a normal mode of the boost flow, as the Planck clause reads it), and two choices the framework does not make: the offset class and the value $y = 2\pi$. At $y = 2\pi$ the entropy of one array is the value $\ln 2 + \varepsilon$ of Theorem \claimref{synthesis.residue-from-mode-entropy}(vi) in the class with the sea at a site; its value in the class with the sea between sites is the subject of a result filed alongside, synthesis.half-integer-weight-array-carries-half-ln2.

## technical
Premise (Q) bundles two assumptions about the boundary modes: that their joint state is the simplest (quasi-free, uncorrelated) one with the thermal marginals, and that the mode energies are $\omega_k = \kappa k$. This result separates them and says what each one is.

The first is a selection rule, not a consequence of (P) and (R). Among all states with the marginals (R) fixes, the uncorrelated product is exactly the one satisfying the geometric modular condition (G) and exactly the one of largest entropy: the entropy deficit of any other member equals its total correlation, which is its relative entropy to the product. So the quasi-free clause is Jaynes' maximum-entropy rule at the marginals (R) supplies.

The second splits further. For each current $a_m$ of the bosonisation bridge to be a normal mode of the boost flow, as the Planck clause reads it, the weights must be affine, $\omega_k = ck + d$; conversely, for any affine law the current occupations come out as Bose-Einstein at the frequencies $cm$, whatever the offset. So the Planck clause itself holds for every affine law; affinity is forced by the normal-mode reading, not by the occupancy formula. Particle-hole symmetry leaves two offsets: the sea level at a mode, giving one zero-weight mode per array (the choice of (Q)), or midway between two modes, giving none. What remains is the dimensionless slope $\beta c$; (Q) sets it to $2\pi$, which makes the time after which the array's flow returns to itself equal to the KMS period. The tension found earlier between (Q)'s weights and rotation invariance disappears when the array index (frequency) and the magnetic index (direction) are separate labels, as the channel identification of the s-wave reduction has them: weights depending on frequency only are rotation invariant, and each frequency level is a rotation multiplet of common weight.

## lay
One of the series' assumptions about the quantum modes at a black hole's boundary, called (Q), turns out to be two assumptions of very different kinds. The first says the modes are as uncorrelated as their individual thermal behaviour allows; this is exactly the rule "assume nothing beyond what is known", the state of greatest entropy, so it is a principle of inference rather than a derived fact. The second fixes the energies of the modes. Part of it is forced: if each combination of modes is to behave as a particle of one definite frequency, which is how the series reads its derivation of the thermal spectrum of Hawking radiation, the energies must be evenly spaced; the thermal spectrum itself comes out right for any even spacing. What is left over is a choice of where the evenly spaced ladder sits (with or without a rung at zero energy) and how far apart the rungs are compared with the temperature. A previously noted clash between these energies and the roundness of the black hole disappears once the energy label and the direction label are treated as separate.

## one-liner
Given (P) and (R), the quasi-free clause of (Q) is the maximum-entropy rule (equivalently (G)); the weight clause is an affine law (forced if each current is a normal mode of the boost flow, as the Planck clause reads it) plus two free data, the sea offset (with or without a zero-weight mode) and the slope $\beta c = 2\pi$; with array and magnetic indices as separate factors the weights are rotation invariant.
