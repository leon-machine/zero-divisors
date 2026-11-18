---
id: synthesis.majorana-scale-not-carried-by-rung-frame-boost
kind: claim
version: 4
title: 'The rung-frame boost does not carry the Majorana scale'
status: proved
region: synthesis
subject: standard-model
tags: [seesaw-and-majorana, undetermined-input, symmetry-breaking, no-go, confronted-with-data]
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
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: 'consistency pass, notation clash on N resolved'
  version: 3
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'notation: the Hermitian norm renamed sans-serif N'
  version: 4
  source: maintainer pass 2026-11-07 (decisions, second round)
review: draft
derivations:
- name: main
  uses:
  - synthesis.rung-unit-is-frame-boost@3
  - synthesis.rung-unit-transverse-to-norm@3
  - synthesis.rung-field-on-the-lift-locus@5
  - synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus@6
  - standard-model.majorana-element@7
  - synthesis.georgi-jarlskog-is-rung-vector-times-pair-part-of-majorana-square@2
  - standard-model.what-angle-asks-neutrino-sector@4
  - synthesis.majorana-scale-free-on-pati-salam-route@6
  - standard-model.imported-clebsch-structure-seesaw@1
  proof: proof-main.tex
quantities:
- quantity.reduced-planck-constant@1
- quantity.megaparsec@1
- quantity.hubble-constant@1
- quantity.w-boson-mass@1
- quantity.weak-mixing-angle-mz@1
- quantity.inverse-fine-structure-mz@1
- quantity.planck-mass@1
- quantity.heaviest-neutrino-mass@1
checked_by:
- kind: check
  ref: check.py::check_frame_boost_is_twice_right_isospin
- kind: check
  ref: check.py::check_majorana_directions_have_frame_weight_two
- kind: check
  ref: check.py::check_star_norm_is_chebyshev_in_the_frame
- kind: check
  ref: check.py::check_frame_tied_majorana_scale_against_record
- kind: check
  ref: check.py::check_other_extensions_tie_to_v_or_h
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.rung-unit-second-free-number
  - synthesis.majorana-scale-free-input
  - synthesis.majorana-scale-free-on-pati-salam-route
extraction:
  maintainer_pass_decisions_2:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Notation (Leon, second round, answer 8; DECISIONS H5, consistency-R04 item 4): the rung-field results wrote N for the Hermitian norm of the rung component, N(c) = (|alpha|^2 + |beta|^2)/2, while N = M_P/H is the hierarchy number in the same subject, and this entity used both (the norm N = ||c||_*, v^2 = 2N; N = M_P/H in the proof''s last remark). N = M_P/H and the number operator N_R keep their letters. The norm is now \mathsf{N} (its values \mathsf{N}^*, \mathsf{N}_0, its derivative \partial_{\mathsf{N}}, and W(\mathsf{N})) in formal, proof and the other levels, in every rung-field entity that writes it (14 entities, one batch), so the family stays uniform. The letter was chosen free in the entity and in its subject (standard-model and quantum-fields): R04''s example \mathcal{N} is the store macro \Ncone (the null cone) and the number operator of synthesis.floor-regulator-... in quantum-fields. No content change.'
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The statement uses N for the Hermitian norm of the rung component (N = ||c||_*, v^2 = 2N); one sentence of the proof used N for the ratio M_P/H; it now says N = M_P/H there.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By Leon''s ruling R3: the compact flow of the proof''s parenthesis is exp(I_4 phi ad 2T_3R), the Clifford algebra of the ten read over span{1, I_4} on the tower''s floors, where I_4 commutes with the ten vectors (stated once; notational); no bare i remains, so the earlier declaration is removed.'
  open_problem: op.rung-unit
  note: >-
    Tests the one series structure that could tie the Majorana scale to the weak scale: the frame boost
    that is the rung unit. The stored boost acts on one rung plane; extended U(2)-covariantly to both rung
    slots and as the identity on the pair slots, it is the real-rapidity flow of twice the right-handed
    isospin on the ten, so its weight on a hypercharge-neutral element is minus its B - L charge, and the
    directions that give a Majorana entry (B - L = -2 or +2, Y = 0: the T-type and T*-type classes) have
    weight two against one for the rung vector. A Majorana vev of weight two whose size is fixed in Hubble
    units in one frame (a nonzero frame-invariant pairing, kappa^2 times that of the balanced element) and
    read in the weak frame obeys M^2 = kappa^2 (v^4/(2H^2) - H^2) with the stored normalisation v^2 = 2N, a
    seesaw-type relation that would remove one free number; for kappa of order one it gives M > 2.1e46 GeV,
    and light neutrinos reach m_3 only with a Majorana family coupling below 1/1.38e30; a rescue needs kappa
    below 1e-34 or such a coupling, a new hierarchy. The other extensions are excluded likewise: boosting
    slot 4 alone gives T weight one and M of order kappa v, extending as the complexified hypercharge gives
    weight zero and M of order kappa H, both far from the stored v_R for kappa of order one. The stored
    Majorana element T is null for the pairing and lies outside the class: the frame fixes no size for it.
    The refutation does not depend on the status of v/H (a parameter of the laws, or initial data under the
    promotion): a tie would have made the Majorana scale share that status, and none exists. The same boost
    is read as the conformal dilatation of the ground point in
    synthesis.scale-free-rung-potentials-need-the-flat-physical-branch(5); the two
    readings agree on the rung plane. Pre-registered (formula, inputs and exponent rule written before any
    value was computed); look-elsewhere count of the session: eight formulas, two flagged in advance as
    contaminated. Transport-convenient: the boost acts on the rung summand that transport adjoins and the
    lift supplies the rung component; the weight computation is Lie theory of the ten. The value of v is
    read from the stored W mass, weak angle and fine-structure constant through v^2 = M_W^2 sin^2(theta_W)
    alpha^-1/pi (standard tree relation, cited from memory). H here is H_0 (an upper bound for the
    H_0 sqrt(Omega_Lambda) of the convention of N; the two differ by a factor of order one).
---

## formal
Let $v_{a}, w_{a}$ ($a = 1, \dots, 5$) be the mode vectors of the ten of Proposition \claimref{standard-model.majorana-element}, $v_{a}w_{b} + w_{b}v_{a} = \delta_{ab}$, with pair slots $a = 1, 2, 3$ and rung slots $a = 4, 5$, number operators $n_{a} = v_{a}w_{a}$, $N_{R} = n_{4} + n_{5}$, $T_{3R} = \tfrac12(N_{R} - 1)$, $B - L = -\tfrac23\sum_{a \le 3}(n_{a} - \tfrac12)$ and $Y = T_{3R} + \tfrac12(B - L)$ (\claimref{synthesis.georgi-jarlskog-is-rung-vector-times-pair-part-of-majorana-square}), $*$ the tower's conjugation with $v_{a}^{*} = w_{a}$, $\|X\|_{*}$ the scalar part of $X^{*}X$, and $T = v_{1}v_{2}v_{3}v_{4}v_{5}$ the Majorana element. The frame boost of Theorems \claimref{synthesis.rung-unit-is-frame-boost}(4) and \claimref{synthesis.rung-unit-transverse-to-norm}(1) acts on one rung plane; here, for $s = e^{\eta} > 0$, $B_{s}$ is its $U(2)$-covariant extension, $v_{a} \mapsto sv_{a}$, $w_{a} \mapsto s^{-1}w_{a}$ on both rung slots and the identity on the pair slots, extended to the algebra. Units with $H^{2} = \Lambda/3$; the rung component has $\mathsf{N} = \|c\|_{*}$, $v^{2} = 2\mathsf{N}$ (as in \claimref{synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus}), and on the lift family $\mathsf{N} = H^{2}\cosh t$ with $t = 2\eta$, $\lambda = He^{\eta}$.
\begin{enumerate}
\item \emph{(The boost is right-handed isospin at real rapidity.)} $B_{s}$ is the automorphism induced by an isometry of the ten, $B_{1/\lambda}c_{1} = c_{\lambda}$ on the lift family, and on every element $X$ with $[N_{R}, X] = qX$ it acts as $B_{s}X = s^{q}X$, where $q$ is twice the $\operatorname{ad} T_{3R}$ weight: $B_{e^{\eta}} = \exp(\eta\,\operatorname{ad} 2T_{3R})$.
\item \emph{(Majorana directions have weight two.)} On every hypercharge-neutral element of definite weights the frame weight is $q = -(B - L)$. The elements with $Y = 0$ and $B - L = \mp 2$, the directions giving a Majorana entry $\nu^{c}\nu^{c}$, are combinations of the $T$-type and $T^{*}$-type monomials, of frame weight $\pm 2$; the rung vectors have $Y = \pm\tfrac12$ and weight $\pm 1$.
\item \emph{(Chebyshev scaling.)} Distinct frame weights are $*$-orthogonal and $\|B_{s}X\|_{*} = s^{2q}\|X\|_{*}$ for weight $q$, while the pairing given by the scalar part of $\widetilde{X}X$ is frame-invariant. For the balanced rung component $c_{H} = H(v_{4} - w_{4})$ and the balanced Majorana element $D_{H} = H(T + T^{*})/\|T\|_{*}^{1/2}$, $\|B_{s}c_{H}\|_{*} = H^{2}\cosh t$ and $\|B_{s}D_{H}\|_{*} = H^{2}\cosh 2t = H^{2}\bigl(2(\|B_{s}c_{H}\|_{*}/H^{2})^{2} - 1\bigr)$; in general weight $q$ gives $H^{2}T_{q}(\|B_{s}c_{H}\|_{*}/H^{2})$ with $T_{q}$ the Chebyshev polynomial. The stored Majorana element $T$ alone is null for the pairing, and $\|B_{s}T\|_{*} = s^{4}\|T\|_{*}$ takes every positive value: the frame fixes no size for it.
\item \emph{(The weight-two tie is excluded.)} Let a Majorana vev lie in the weight $\pm 2$ span with its size fixed in Hubble units in one frame, by a frame-invariant pairing $\kappa^{2}$ times that of $D_{H}$, and let its size $M$ be its $*$-norm in the weak frame, where the rung component has $v^{2} = 2\mathsf{N}$ (fixed normalisations of $M$ absorbed in $\kappa$). Then $M^{2} = \kappa^{2}(v^{4}/(2H^{2}) - H^{2})$, so $M \ge \kappa v^{2}/(2H)$, a relation between the Majorana scale and $v/H$. With the stored record and $\kappa = 1$, $M > 2.1 \times 10^{46}$ GeV, above $1.7 \times 10^{27}M_{P}$ and above $4.05 \times 10^{34}$ times the perturbative cap $4\pi v_{R}$ of \claimref{synthesis.majorana-scale-free-on-pati-salam-route}(iii) ($v_{R} = 4.15 \times 10^{10}$ GeV, \claimref{standard-model.what-angle-asks-neutrino-sector}); under the imported seesaw (\claimref{standard-model.imported-clebsch-structure-seesaw}), with Dirac entries at most $\sqrt{4\pi}\,v$ and the Majorana matrix $M$ times a family coupling of smallest singular value $\sigma$, every light mass is below $8\pi H/\sigma$, so the stored $m_{3}$ needs $\sigma < 1/(1.38 \times 10^{30})$. Bringing $M$ under the cap needs $\kappa < 10^{-34}$; either rescue is a new hierarchy.
\item \emph{(Other extensions.)} Boosting rung slot $4$ alone gives $T$ weight $1$ and a tied size of order $\kappa v$; extending the boost as the complexified hypercharge on the whole algebra gives every $Y = 0$ element weight $0$ and a tied size of order $\kappa H$. For $\kappa$ of order one both are excluded by the stored $v_{R}$, which exceeds $v$ by more than $1.6 \times 10^{8}$ and $H_{0}$ by more than $2.8 \times 10^{52}$.
\end{enumerate}
So the frame boost does not tie the Majorana scale to $v/H$ through a weight-two vev of fixed Hubble-unit size, under any of the three extensions; the stored null Majorana element is not tied at all.

## technical
The rung unit is a boost of the rung frame (Theorem \claimref{synthesis.rung-unit-is-frame-boost}); the same boost is read as the conformal dilatation of the ground point in the result \claimref{synthesis.scale-free-rung-potentials-need-the-flat-physical-branch}(5), and the readings agree on the rung plane. Extended to both rung slots of the ten and as the identity on the pair slots, the boost is the real-rapidity flow generated by twice the right-handed isospin $T_{3R}$, so each element is rescaled by a power fixed by its charges; on hypercharge-neutral elements the power is minus the $B - L$ charge. The directions that give the right-handed neutrino its Majorana mass carry $B - L = \mp 2$ and no hypercharge, so they have weight two, where the rung vector, which carries the weak scale, has weight one. If a Majorana vev of weight two had its size fixed in Hubble units in one frame, as the lift's rung component has, and were read in the frame that gives the weak scale, then $\cosh 2t = 2\cosh^{2}t - 1$ with the stored $v^{2} = 2\mathsf{N}$ would force $M^{2} = \kappa^{2}(v^{4}/(2H^{2}) - H^{2})$, roughly $v^{2} \approx 2MH/\kappa$, a seesaw-type relation removing one free number. For $\kappa$ of order one the record rules it out: $M$ exceeds $2 \times 10^{46}$ GeV, far above the Planck mass and the stored range of the Majorana scale, and the seesaw then makes every light neutrino lighter than $8\pi H$ divided by the smallest Majorana family coupling, so the measured mass needs that coupling below $10^{-30}$. A rescue needs $\kappa$ below $10^{-34}$ or such a coupling, a new hierarchy either way. The other extensions of the boost (one rung slot only, or the full complexified hypercharge) tie the Majorana size to $v$ or to $H$, also excluded for $\kappa$ of order one; and the stored Majorana element is null, so the frame fixes no size for it. Whatever the status of $v/H$ (a parameter of the laws, or initial data under the promotion), the frame boost supplies no relation tying the Majorana scale to it.

## lay
In this framework the strength of the weak force's symmetry breaking is set by how a particular reference frame in some extra directions is stretched. The same stretch acts on every quantity built from those directions, by an amount fixed by its charges. The quantity that gives the heavy neutrinos their mass carries twice the relevant charge of the Higgs field, so if its size were fixed once and then read through the same stretch, the heavy neutrino mass would come out as roughly the square of the weak scale divided by the expansion rate of the universe: about $10^{46}$ GeV, far beyond the Planck mass, and the ordinary neutrinos would be about $10^{30}$ times lighter than they are measured to be, unless some other coupling were itself absurdly small. Other ways of setting up the stretch give the opposite failure, heavy neutrino masses far too small. So the stretch that sets the weak scale does not set the heavy neutrino mass; that remains a separate number of the theory.

## one-liner
The rung-frame boost, extended to both rung slots, is the real-rapidity flow of $2T_{3R}$, so Majorana directions ($Y = 0$, $B - L = \mp 2$) have frame weight two; a weight-two Majorana vev with size fixed in Hubble units in one frame would obey $M^{2} = \kappa^{2}(v^{4}/(2H^{2}) - H^{2})$, so for $\kappa$ and the Majorana couplings of order one $M > 2 \times 10^{46}$ GeV and the light neutrinos lie below $8\pi H$, against the record: the frame boost does not tie the Majorana scale to $v/H$.
