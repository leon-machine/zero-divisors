---
id: families.skeleton-rank-one-plus-ordering-shift
kind: claim
version: 6
title: 'The skeleton: rank one plus the ordering shift, and the unbreakable $S_{2}$'
status: proved
region: families
subject: generations
tags: [pairing-and-bogoliubov, flavour-and-mixing, no-go]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 6
  source: maintainer pass 2026-11-07 (GA units)
review: typed
derivations:
- name: main
  uses:
  - families.imported-squeezed-vacuum-bosonic-pairing@3
  - families.rigidity-pairing-sector-one-event@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T13.py
  tags:
  - label:thm:skeleton
- kind: check
  ref: check.py::check_wick_pieces_and_closed_form
- kind: check
  ref: check.py::check_normal_ordered_rank_one_and_ordering_floor
- kind: check
  ref: check.py::check_spectrum_depends_only_on_depth
locators:
  paper: T13
  number: Thm 6.2
  label: thm:skeleton
  line: 801
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The channel phases e^{i chi} in {1, zeta, zeta^2} became e^{I_4 chi}, numbers read in span{1, I_4} as stated in the proof; no bare i remains. By Leon''s ruling R3 the face-space reading is stated once in R3''s words: numbers and the module''s complex structure in span{1, I_4}, the module read on the tower''s floors (notational).'
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 4: a marked note after the formal clauses and one sentence at the technical level record Leon''s decision of 2026-10-31 that the mass-squared reading of the face mass form, the one this theorem uses, is the primary reading of the 207 (a population ratio of the selected state, synthesis.pair-singlet-mass-form-is-floor-plus-face-density), with the square-root-mass circulant reading of the projected coherent vector (synthesis.koide-channel-phase-is-no-symmetry-angle) kept as a labelled alternative that conflicts with the charged-lepton texture c(J + delta_c E) of the neutrino paper (synthesis.theta23-at-s3-s2-direction). No clause or proof changed.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the four Wick pieces and H in Q(zeta), the rank-one normal-ordered form and ordering floor, and the spectrum depending only on the depth. Version 1 -> 2. Check maintenance: comparisons over zip now also compare lengths, so a length mismatch cannot pass on a shorter prefix; no change to what is claimed. Version 2 -> 3.'
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - 'channel phases e^{i chi} in {1, zeta, zeta^2}: roots of unity used as numbers in the check'
  env: theorem
  context_refs:
  - correspondence.shared-core-ordering-dictionary
  - families.alignment-computed-thirteenth-refutation-democracy-one
  eqrefs: 3
  typing:
    by: ai-typing-pass
    note: "Both edges are the Wick and Gaussian-data premises of the proof and were kept; the ordering dictionary and the alignment citations are a reading and a comparison and were not added."
  maintainer_pass_five_fronts:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 5: a second marked note after the formal clauses, and one sentence at the technical level, record Leons decision of 2026-11-01 that the face mass form gives pole masses, provisionally: exact Koide at pole masses is a premise of that reading, and at freezing-scale masses the target would be about 210.7 with a Sumino-type cancellation needed (citing synthesis.koide-channel-phase-target-depends-on-mass-definition as a claimref, not an edge). No clause or proof changed.'
---

## formal
For every pairing of the antisymmetric sector, at every strength, feeding ratio and channel phase, the mass form evaluates in closed form:
\begin{equation}
H_{kl} \;=\; \cosh^{2}r\;\delta_{kl} \;+\; x(5+6x)\,\bar{n}_{k}n_{l},
\qquad
\mathrm{spec}\,H \;=\; \bigl(\cosh^{2}r,\ \cosh^{2}r,\ 1 + 6x + 6x^{2}\bigr),
\end{equation}
with $\bar{n}n^{\mathsf{T}} =: P_{[\bar{v}]}$ the projector onto the conjugate coherent ray, and the trace identity $\tr H = 3 + 8x + 6x^{2}$ tying it to the diagonal reading. Three clauses.
\begin{enumerate}
\item \emph{(Rank one plus floor.)} The normal-ordered form $\langle\hat\Omega_{k}^{\dagger}\hat\Omega_{l}\rangle$ is exactly $2x(2+3x)\,P_{[\bar v]}$, rank one: one heavy family along the conjugate coherent ray with the light pair strictly massless. Proposition \claimref{families.alignment-computed-thirteenth-refutation-democracy-one}'s texture is a theorem of the Gaussian freezing at operator level.
\item \emph{(The floor is the ordering shift.)} The entire mass-squared of the light pair is the symmetric-ordering term $\tfrac12\langle[\hat\Omega_{l}, \hat\Omega_{k}^{\dagger}]\rangle = \cosh^{2}r\,\delta_{kl} + x\,P_{[\bar v]}$ restricted to the light plane, exactly $\cosh^{2}r$: the ordering shift, evaluated at depth $r$; that this is the same half-per-mode structure that determines $\hbar$ in the series is a reading, with the series' ordering dictionary \cite[Thm.~5.7]{ButlerT9} as its locator, and not part of the proved content. The light families' masses are the ordering shift alone.
\item \emph{(The $S_{2}$ is unbreakable in the class.)} The spectrum depends on the pairing only through the depth $r$ (Proposition \claimref{families.rigidity-pairing-sector-one-event}); the channel phase and, at fixed $r$, the feeding ratio move only the coherent ray, and the light-pair degeneracy is exact for every pairing of the sector. Everywhere in the antisymmetric Gaussian class, $m_{e} = m_{\mu}$ identically: the $S_{2} \to 1$ stage of the cascade provably lies outside the Gaussian freezing.
\end{enumerate}

\emph{Note (which reading of the $207$ is primary).} The store takes the reading used here, the eigenvalues of the face mass form $H$ as squared masses, as the primary dictionary for the charged-lepton ratio $m_{\mu}/m_{e} \approx 207$: in it the channel phase does not reach the spectrum of the source-built completions (Proposition \claimref{synthesis.real-structure-breaks-source-stabiliser-to-z2}), and the $207$ is a property of the selected state, a population ratio of the two directions of the source's plane (Proposition \claimref{synthesis.pair-singlet-mass-form-is-floor-plus-face-density}(iv)). The reading of the projected coherent face vector as the vector of square-root masses, the eigenvalues of a circulant whose channel phase carries the $207$ (Proposition \claimref{synthesis.koide-channel-phase-is-no-symmetry-angle}), is kept as a labelled alternative; it conflicts with the charged-lepton texture $c(\J + \delta_{c}E)$ that the neutrino paper's instances use with the breaking relation (Proposition \claimref{synthesis.theta23-at-s3-s2-direction}), which is not a circulant, and the two are not reconciled.

\emph{Note (the mass dictionary, provisional).} The eigenvalues of $H$ are read as the squares of \emph{pole} masses: the store's provisional dictionary assigns pole masses to the face mass form, in either reading. So exact Koide at pole masses is a premise of that reading, not a consequence: the stored targets (the channel-phase window, the exclusion of $\tfrac29$, the pair-number threshold) are pole-mass statements, and at common-scale running masses, as at the freezing scale, the target ratio would be about $210.7$ rather than $206.77$ and the series would need a cancellation of the logarithmic QED correction of the kind Sumino proposes (Proposition \claimref{synthesis.koide-channel-phase-target-depends-on-mass-definition}). The dictionary may be revised; this note records the choice, and the clauses above do not depend on it.

## technical
For every antisymmetric pairing, at any strength, feeding ratio and channel phase, Wick's theorem with the Gaussian data gives the mass form in closed form, $H_{kl} = \cosh^{2}r\,\delta_{kl} + x(5 + 6x)\,\bar{n}_{k}n_{l}$ with $x = \sinh^{2}r$, so $\mathrm{spec}\,H = (\cosh^{2}r, \cosh^{2}r, 1 + 6x + 6x^{2})$. Its normal-ordered part is $2x(2 + 3x)$ times the projector onto the conjugate coherent ray: rank one, one heavy family with the light pair strictly massless, so the democratic texture is a theorem of the Gaussian freezing at operator level.

The light pair's whole mass-squared is the symmetric-ordering term, exactly $\cosh^{2}r$ on the light plane; reading it as the series' ordering shift is an interpretation outside the proved content. Since the spectrum depends on the pairing only through $r$, the light-pair degeneracy is exact throughout the antisymmetric Gaussian class, so $m_{e} = m_{\mu}$ there identically and the $S_{2} \to 1$ stage lies outside the Gaussian freezing. Reading the eigenvalues of $H$ as squared masses is the store's primary dictionary for the muon-to-electron ratio; the square-root-mass circulant reading is a labelled alternative, in conflict with the charged-lepton texture of the neutrino paper. The masses are read as pole masses, provisionally, so exact Koide at pole masses is a premise of that reading.

## lay
The paper computes exactly the mass pattern produced by its simplest vacuum, for every setting of its parameters. The answer is always one heavy family and two light ones with exactly equal masses, and the light masses come entirely from a quantum ordering effect. Because the two light masses can never differ in this setting, the electron and the muon cannot be told apart here, so whatever separates them must come from beyond this class of vacua.

## one-liner
For every antisymmetric Gaussian pairing the mass form is $\cosh^{2}r\,\delta_{kl} + x(5 + 6x)\,\bar{n}_{k}n_{l}$, rank one plus an ordering floor, so the light pair is exactly degenerate and $S_{2}$ cannot break in the class.
