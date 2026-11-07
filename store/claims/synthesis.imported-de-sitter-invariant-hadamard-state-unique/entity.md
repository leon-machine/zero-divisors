---
id: synthesis.imported-de-sitter-invariant-hadamard-state-unique
kind: claim
version: 2
title: 'Imported: the unique de Sitter-invariant Hadamard state (Allen 1985)'
status: imported
region: synthesis
subject: dark-energy
tags: [frozen-point, cosmological-constant, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'B. Allen, Vacuum states in de Sitter space, Phys. Rev. D 32 (1985), 3136--3149.'
  key: Allen1985
  doi: 10.1103/PhysRevD.32.3136
- citation: 'R. Brunetti, K. Fredenhagen and S. Hollands, A remark on alpha vacua for quantum field theories on de Sitter space, J. High Energy Phys. 2005, no. 05, 063; arXiv:hep-th/0503022.'
  key: BrunettiFredenhagenHollands2005
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the Hankel expansion is quoted from the literature in complex-analysis form; declared (version and levels unchanged).'
  note: >-
    Imported so that synthesis.frozen-point-geometry-reads-descent-as-vacuum can cite the
    uniqueness of the stabiliser-invariant Hadamard state and the non-Hadamard character of the
    alpha-vacua, which its proof cites from memory (Allen 1985). Checked on 2026-10-26: Allen 1985 against
    the APS abstract (title, author, journal, DOI; for massive fields a one-complex-parameter family of
    de Sitter-invariant states containing the Euclidean vacuum, obtained from it by a
    frequency-independent Bogoliubov transformation; for the massless minimally coupled field no
    de Sitter-invariant Fock vacuum, but E(3)-invariant states including Bunch-Davies); the facts that
    the family is all de Sitter-invariant states, that the Euclidean state is Hadamard and that every
    other member is singular at antipodal points and so not Hadamard, against the ar5iv text of
    arXiv:hep-th/0503022, which attributes both to Allen. The authors and journal reference of
    hep-th/0503022, and the flat-slicing Hankel mode with its asymptotics (DLMF 10.17), are cited from
    memory.
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Created by the maintainer pass (fix round of 26 October: the de Sitter-invariant Hadamard state, cited from memory by the frozen-point descent result, to be imported as a Fact).'
  maintainer_pass_deposit_state:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2, at Leon''s decisions of 2026-11-01 (deposit state): a marked note after the formal statement records that the massless minimally coupled Bunch-Davies state is infrared-divergent on slice fields of nonzero mean (synthesis.imported-ford-parker-infrared-divergence); the massive statement and the index-2 conclusion that uses it are unaffected. Content otherwise unchanged.'
outside_ga:
  kind: imported
  why: 'the large-argument Hankel expansion H_nu(z) ~ sqrt(2/pi z) e^{i(z - nu pi/2 - pi/4)}(1 + i(4 nu^2 - 1)/8z + ...) is quoted as the source states it, complex analysis of Bessel functions'
---

## formal
Let $\phi$ be a free real scalar field of mass $m^{2} > 0$ (curvature coupling absorbed into $m^{2}$) on the de Sitter gravitational field of Hubble rate $H$ (a gravitational field on flat spacetime, Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}). The pure quasi-free states invariant under the connected de Sitter group form a one-complex-parameter family, the $\alpha$-vacua, obtained from the Euclidean state $\omega_{0}$ (the analytic continuation of the Euclidean theory on the sphere) by a frequency-independent Bogoliubov transformation; for real $\alpha$ their symmetric two-point functions are $G_{\alpha}(x,y) = \cosh 2\alpha\,G_{0}(x,y) + \sinh 2\alpha\,G_{0}(x,\bar y)$, $\bar y$ the antipode of $y$. The Euclidean state is Hadamard; every other member is singular also at antipodal points, and since two Hadamard two-point functions differ by a smooth function, none of them is Hadamard. So for $m^{2} > 0$ the de Sitter-invariant Hadamard state is unique. In the flat slicing, with conformal time $\eta < 0$ and scale factor $a = -1/(H\eta)$, it is the Bunch-Davies state, the mode of the rescaled field $a\phi$ being $\chi_{k} \propto (-\eta)^{1/2}H^{(1)}_{\nu}(-k\eta)$, $\nu^{2} = \tfrac94 - m^{2}/H^{2}$, whose large-argument expansion $H^{(1)}_{\nu}(z) \sim \sqrt{2/\pi z}\,e^{i(z - \nu\pi/2 - \pi/4)}\bigl(1 + i(4\nu^{2} - 1)/8z + O(z^{-2})\bigr)$ fixes its short-distance behaviour. For the massless minimally coupled field there is no de Sitter-invariant Fock vacuum; states invariant under the Euclidean group $E(3)$ of the flat slicing exist, the Bunch-Davies state among them. \emph{Provenance:} \cite{Allen1985}; \cite{BrunettiFredenhagenHollands2005} (the antipodal singularity and the failure of the Hadamard condition, as attributed there to Allen).

\emph{Note (the massless case; added 1 November).} The $E(3)$-invariant Bunch-Davies state of the massless minimally coupled field ($\nu = \tfrac32$) is infrared-divergent: its slice fields smeared with test functions of nonzero mean have infinite variance, those of zero mean or derivatives finite variance (Ford and Parker, Fact \claimref{synthesis.imported-ford-parker-infrared-divergence}). It is a state only on the algebra of the latter, and a comparison with it needs an infrared regularisation. The massive statement above, and the index-$2$ conclusion of the frozen-point reading of the descent, which uses it for fields with $m^{2} > 0$ (the conformal weight, $m^{2} = 2H^{2}$, $\nu = \tfrac12$, among them), are unaffected.

## technical
A massive free field on de Sitter has many states that look the same at every point and in every direction, the $\alpha$-vacua, all related to the Euclidean (Bunch-Davies) state by one fixed mixing of positive and negative frequencies. Only the Euclidean state has the short-distance behaviour of the vacuum in flat spacetime, the Hadamard condition; every other member also correlates each point with its antipode singularly, so it cannot be a physically regular state. So the regular de Sitter-invariant state is unique. In the flat slicing its modes are Hankel functions, whose large-argument expansion gives its spectrum on scales well inside the horizon. For a massless minimally coupled field no fully de Sitter-invariant vacuum exists, only states invariant under the flat slicing's translations and rotations.

## lay
In a universe expanding at a constant rate there is a whole family of states that each look like empty space everywhere. Allen showed that only one of them behaves like ordinary empty space at short distances; the others hide singular correlations between opposite points of the universe.

## one-liner
For $m^{2} > 0$ the de Sitter-invariant states are the $\alpha$-vacua, Bogoliubov transforms of the Euclidean state; only the Euclidean state is Hadamard, the others being singular at antipodal points (Allen 1985).
