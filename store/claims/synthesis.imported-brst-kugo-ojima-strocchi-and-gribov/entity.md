---
id: synthesis.imported-brst-kugo-ojima-strocchi-and-gribov
kind: claim
version: 1
title: 'Imported: covariant quantisation of gauge fields: BRST symmetry (Becchi, Rouet and Stora 1976; Tyutin 1975), the Kugo-Ojima quartet mechanism (1979), Strocchi''s theorem that a local covariant vector potential obeying Maxwell''s equations needs an indefinite metric (1967 to 1970), and the Gribov ambiguity of non-abelian gauge fixing (1978)'
status: imported
region: synthesis
subject: quantum-fields
tags: [gauge-fields, no-go, classical-theorem, representation-theory]
proposed_by:
  kind: ai
  session: maintainer-2026-11-01
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'C. Becchi, A. Rouet and R. Stora, Renormalization of gauge theories, Ann. Phys. 98 (1976), 287--321.'
  key: BecchiRouetStora1976
  doi: 10.1016/0003-4916(76)90156-1
- citation: 'I. V. Tyutin, Gauge invariance in field theory and statistical physics in operator formalism, Lebedev Institute preprint LEBEDEV-75-39 (1975), arXiv:0812.0580.'
  key: Tyutin1975
- citation: 'T. Kugo and I. Ojima, Local covariant operator formalism of non-abelian gauge theories and quark confinement problem, Prog. Theor. Phys. Suppl. 66 (1979), 1--130.'
  key: KugoOjima1979
  doi: 10.1143/PTPS.66.1
- citation: 'F. Strocchi, Gauge problem in quantum field theory, Phys. Rev. 162 (1967), 1429.'
  key: Strocchi1967
  doi: 10.1103/PhysRev.162.1429
- citation: 'F. Strocchi, Gauge problem in quantum field theory. III. Quantization of Maxwell equations and weak local commutativity, Phys. Rev. D 2 (1970), 2334--2340.'
  key: Strocchi1970
  doi: 10.1103/PhysRevD.2.2334
- citation: 'H. Gottschalk, Indefinite metric, arXiv:math-ph/0501033 (review).'
  key: Gottschalk2005
- citation: 'V. N. Gribov, Quantization of non-Abelian gauge theories, Nucl. Phys. B 139 (1978), 1.'
  key: Gribov1978
  doi: 10.1016/0550-3213(78)90175-X
extraction:
  note: >-
    Imported so that the self-adjoint BRST result, and through the Krein-form premise the covariant loop results,
    can pin the standard frame of covariant gauge fixing instead of citing it from memory. Checked on 2026-11-01:
    the bibliographic data (titles, journals, volumes, pages, years, DOIs) of Becchi-Rouet-Stora, Kugo-Ojima,
    Strocchi 1967 and 1970 and Gribov 1978 against their INSPIRE records, and Tyutin's report number and arXiv
    number (LEBEDEV-75-39, arXiv:0812.0580) against its INSPIRE record (the record gives no journal); the content
    of (iii) against the review of Gottschalk, arXiv:math-ph/0501033, which states that Strocchi proved in a series
    of papers between 1967 and 1970 the impossibility of a local covariant quantisation on a positive-metric Hilbert
    space, its Theorem 1 concluding under the Wightman axioms and Maxwell's equations that the two-point function of
    the field tensor vanishes identically, and which calls the indefinite-metric Lorentz-gauge quantisation the
    Gupta-Bleuler formalism (Gupta, Bleuler 1950). Cited from memory, not checked against the sources: the content of (i) (nilpotency, the cohomological
    physical-state condition), of (ii) (the quartet theorem and its hypotheses), and of (iv) beyond the title.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (BRST, Kugo-Ojima, Strocchi and the Gribov ambiguity as a Fact, by Leon''s list of imports).'
---

## formal
\begin{enumerate}
\item[(i)] \emph{(BRST symmetry.)} The gauge-fixed action of a gauge theory in a covariant gauge, with Faddeev-Popov ghosts $c^{a}$, antighosts $\bar c_{a}$ and auxiliary fields, is invariant under a nilpotent fermionic symmetry $s$, $s^{2} = 0$, which acts on the gauge field as a gauge transformation with parameter $c$ and on the ghosts as $sc = -\tfrac12[c, c]$; its Noether charge $Q_{B}$ is nilpotent, and the physical states are the cohomology $\ker Q_{B}/\operatorname{im}Q_{B}$ \cite{BecchiRouetStora1976, Tyutin1975}.
\item[(ii)] \emph{(Quartet mechanism.)} In the local covariant operator formalism the state space carries an indefinite inner product for which $Q_{B}$ is self-adjoint; the physical subspace $\ker Q_{B}$ has a positive semi-definite inner product whose null space is $\operatorname{im}Q_{B}$, the unphysical modes (the timelike and longitudinal polarisations, ghosts and antighosts) forming BRST quartets of zero norm, so that the quotient is a Hilbert space and the physical scattering matrix is unitary \cite{KugoOjima1979}.
\item[(iii)] \emph{(Strocchi's theorem.)} A local, Lorentz-covariant vector potential $A_{\mu}$ realised on a Hilbert space with positive metric, whose field tensor obeys Maxwell's equations, has a field tensor with identically vanishing two-point function; a local covariant quantisation of a gauge field with nonzero field strength therefore needs an indefinite metric, as in the Gupta-Bleuler formalism \cite{Strocchi1967, Strocchi1970, Gottschalk2005}.
\item[(iv)] \emph{(The Gribov ambiguity.)} For a non-abelian gauge group the Coulomb (and the Landau) gauge condition does not fix the gauge uniquely: large field configurations carry several gauge-equivalent copies obeying the condition, so the Faddeev-Popov procedure is valid only perturbatively \cite{Gribov1978}.
\end{enumerate}

## technical
These are the standard foundations of the covariant quantisation of gauge fields. Becchi, Rouet and Stora, and independently Tyutin, found that the gauge-fixed action with ghosts keeps a nilpotent fermionic symmetry, now called BRST, whose charge defines the physical states as a cohomology. Kugo and Ojima showed that when this charge is self-adjoint for an indefinite inner product, the unphysical modes (timelike and longitudinal photons, ghosts and antighosts) pair into quartets of zero norm, so the physical states have positive norm and the physical scattering is unitary. Strocchi proved that the indefinite metric cannot be avoided: on a positive-metric space a local covariant vector potential satisfying Maxwell's equations has trivial field strength. Gribov showed that the usual non-abelian gauge conditions do not pick a unique representative of each gauge orbit beyond small fields, so the ghost construction is a perturbative tool.

## lay
Force fields such as light and the gluons carry a redundancy: many mathematical descriptions give the same physics. Removing it while keeping the equal treatment of space and time is done with fictitious ghost particles and a bookkeeping symmetry found in the 1970s. That bookkeeping works only if some unphysical states are allowed negative or zero length, which then cancel in groups of four; a theorem of Strocchi shows there is no way around this, and Gribov showed that for the gluons the usual way of removing the redundancy fails for very strong fields. The series takes these results from the literature.

## one-liner
BRST symmetry (a nilpotent ghost symmetry whose charge's cohomology is the physical space; Becchi-Rouet-Stora, Tyutin), the Kugo-Ojima quartet mechanism (positive physical space for a self-adjoint charge on an indefinite space), Strocchi's theorem (a local covariant vector potential with Maxwell's equations needs an indefinite metric) and the Gribov ambiguity of non-abelian gauge conditions.
