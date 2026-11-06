---
id: synthesis.imported-wilson-lattice-gauge-theory-and-strong-coupling-confinement
kind: claim
version: 1
title: 'Imported: Wilson''s lattice gauge theory and strong-coupling confinement'
status: imported
region: synthesis
subject: quantum-fields
tags: [gauge-fields, classical-theorem, symmetry-breaking, finite-models]
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
- citation: 'K. G. Wilson, Confinement of quarks, Phys. Rev. D 10 (1974), 2445--2459.'
  key: Wilson1974
  doi: 10.1103/PhysRevD.10.2445
- citation: 'K. Osterwalder and E. Seiler, Gauge field theories on the lattice, Ann. Phys. 110 (1978), 440.'
  key: OsterwalderSeiler1978
  doi: 10.1016/0003-4916(78)90039-8
- citation: 'S. Elitzur, Impossibility of spontaneously breaking local symmetries, Phys. Rev. D 12 (1975), 3978--3982.'
  key: Elitzur1975
  doi: 10.1103/PhysRevD.12.3978
- citation: 'A. H. Guth, Existence proof of a nonconfining phase in four-dimensional U(1) lattice gauge theory, Phys. Rev. D 21 (1980), 2291.'
  key: Guth1980
  doi: 10.1103/PhysRevD.21.2291
- citation: 'J. Froehlich and T. Spencer, Massless phases and symmetry restoration in abelian gauge theories and spin systems, Commun. Math. Phys. 83 (1982), 411--454.'
  key: FrohlichSpencer1982
  doi: 10.1007/BF01213610
- citation: 'A. Denbleyker, D. Du, Y. Liu, Y. Meurice and A. Velytsky, Series expansions of the density of states in SU(2) lattice gauge theory, arXiv:0807.0185, equation (2) and the definition after it.'
  key: Denbleyker2008
extraction:
  note: >-
    Imported so that the rotor-lattice result can pin its lattice inputs instead of citing them from memory. Checked
    on 2026-11-01: the bibliographic data of all five original papers against their INSPIRE records; the abstracts of
    Osterwalder-Seiler (lattice Yang-Mills and fermion fields satisfy physical positivity, giving a positive
    self-adjoint transfer matrix; existence and analyticity of the infinite-volume limit at strong coupling; Wilson's
    confinement bound verified), Elitzur (spontaneous breaking of a local symmetry without gauge fixing is impossible,
    shown for abelian lattice gauge fields), Guth (a rigorous lower bound on the Wilson loop for four-dimensional U(1)
    with a Villain-type action: no confinement of electric charge below about g^2 = 0.168) and Froehlich-Spencer (a
    deconfining transition to a massless QED phase in four-dimensional U(1) lattice gauge theory) against the same
    records; the Wilson action sum_p (1 - (1/N) Re Tr U_p) with beta = 2N/g^2 against Denbleyker et al.,
    arXiv:0807.0185, equation (2) and the line after it (beta = 4/g^2 for N = 2). Cited from memory, not checked: the
    leading strong-coupling coefficient (beta/4 per plaquette for SU(2), beta/2 for U(1)) and the
    character-expansion form of (ii), which the citing result recomputes exactly, and the form of action Froehlich and
    Spencer treat.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (Wilson, Osterwalder-Seiler, Elitzur, beta = 4/g^2 and compact U(1) deconfinement as a Fact, by Leon''s list of imports).'
---

## formal
\begin{enumerate}
\item[(i)] \emph{(Wilson's lattice gauge theory.)} On a hypercubic lattice with link variables $U_{\ell}$ in a compact group $G$ and plaquette products $U_{p}$, the weight $\exp(-\beta\sum_{p}(1 - \tfrac1N\mathrm{Re}\,\mathrm{Tr}\,U_{p}))$ with the Haar measure on each link defines a gauge-invariant theory with no gauge fixing; for $G = SU(N)$, $\beta = 2N/g^{2}$, so $\beta = 4/g^{2}$ for $SU(2)$, and as the lattice spacing goes to zero the weight reduces to the Yang-Mills action \cite{Wilson1974, Denbleyker2008}. At strong coupling (small $\beta$) the expectation of a Wilson loop decreases as the exponential of minus the area it encloses, at leading order in $\beta$ \cite{Wilson1974}.
\item[(ii)] \emph{(Reflection positivity and the area law.)} Wilson's lattice gauge theories, with or without fermions, satisfy reflection (physical) positivity, which gives a Hilbert space and a positive self-adjoint transfer matrix; at strong coupling the infinite-volume limit exists and is analytic in $\beta$, and Wilson loops obey the area law (Wilson's confinement bound) \cite{OsterwalderSeiler1978}.
\item[(iii)] \emph{(Elitzur's theorem.)} A local gauge symmetry cannot be broken spontaneously in a gauge-invariant lattice theory without gauge fixing: gauge-variant observables have vanishing expectation \cite{Elitzur1975}.
\item[(iv)] \emph{(Compact $U(1)$ deconfines.)} Four-dimensional compact $U(1)$ lattice gauge theory has, at weak coupling, a phase without confinement of electric charge, a massless phase of quantum electrodynamics, separated by a phase transition from its confining strong-coupling phase; proved for a Villain-type action by Guth and by Fr\"ohlich and Spencer \cite{Guth1980, FrohlichSpencer1982}.
\end{enumerate}

## technical
Wilson put gauge theory on a spacetime lattice with group-valued link variables and the action built from the trace of the product around each elementary square; the theory is gauge invariant with no gauge fixing, its coupling is $\beta = 2N/g^{2}$ for $SU(N)$, and it reduces to Yang-Mills theory as the lattice spacing shrinks. Under strong coupling Wilson loops fall with the area they enclose, which is confinement of static charges. Osterwalder and Seiler proved that these lattice theories have a positive transfer matrix, so they describe quantum theories at finite spacing, and proved the strong-coupling area law rigorously. Elitzur showed that a local symmetry cannot break spontaneously on the lattice. The strong-coupling area law does not distinguish abelian from non-abelian groups: four-dimensional compact $U(1)$ also confines at strong coupling, but it is proved to have a deconfined, massless phase at weak coupling.

## lay
Putting the forces of nature on a grid of points in space and time, as Wilson did in 1974, avoids the redundancy problems of their usual description and makes it possible to prove things about them. On such a grid, if the coupling is strong, a pair of test charges is held together with a force that does not weaken with distance. This is proved rigorously, but it holds for electromagnetism on a grid too, which is known to stop confining at weak coupling, so it is not by itself evidence that the real strong force confines.

## one-liner
Wilson's lattice gauge theory (gauge invariant without gauge fixing, $\beta = 2N/g^{2}$, $4/g^{2}$ for $SU(2)$, area law under strong coupling), reflection positivity and the rigorous strong-coupling area law (Osterwalder-Seiler), Elitzur's theorem, and the proved weak-coupling deconfined phase of four-dimensional compact $U(1)$ (Guth; Fr\"ohlich-Spencer).
