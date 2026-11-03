---
id: families.alignment-computed-thirteenth-refutation-democracy-one
kind: claim
version: 4
title: 'The alignment computed: the thirteenth refutation, democracy, and one heavy family'
status: proved
region: families
subject: generations
tags: [refutation, flavour-and-mixing, cosmological-constant, mass-generation]
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
review: typed
derivations:
- name: main
  uses:
  - families.imported-indifference-instrument@2
  - families.source-term-linear-tilt-mass-functional@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T13.py
  tags:
  - label:prop:alignment
- kind: check
  ref: check.py::check_magnitude_window
- kind: check
  ref: check.py::check_democratic_line_and_rank_one_texture
locators:
  paper: T13
  number: Prop 4.3
  label: prop:alignment
  line: 659
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the magnitude window 10^-105 to 10^-44 and the democratic line with the rank-one texture of spectrum (3, 0, 0). Version 3 -> 4.'
  env: proposition
  context_refs:
  - families.imported-indifference-instrument
  - families.source-term-linear-tilt-mass-functional
  - families.three-generations-faces-maximal-composite
  eqrefs: 1
  typing:
    by: ai-typing-pass
    added:
    - families.imported-indifference-instrument
    - families.source-term-linear-tilt-mass-functional
    note: 'Added the source term (clause 1 estimates its Lambda-suppressed condensate) and the indifference
      instrument (clause 3 forces the democratic line by it); the faces conjecture was not added because
      it supplies the setting the result refines, not a premise; the democratic spectrum (3,0,0) is classical
      (HHW1978) but no imported store claim carries it, so no standard route was added. Levels pass: conditions
      already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - families.imported-indifference-instrument
---

## formal
Four statements, the first a refutation, the rest its redirection, each at the level marked.
\begin{enumerate}
\item \emph{(The thirteenth refutation, by magnitude; a dimensional estimate.)} The source term of Proposition \claimref{families.source-term-linear-tilt-mass-functional} is $\Lambda$-suppressed, so the condensate it can induce is $\delta b \sim \Lambda\,\Omega_{\mathrm{vac}}$ with $\Omega_{\mathrm{vac}}$ a length; for any vacuum length between the Planck and Hubble scales, $\Lambda\Omega_{\mathrm{vac}}$ lies between $H^{2}/M_{P} \approx 10^{-94}$ eV and $H \approx 10^{-33}$ eV, that is between roughly $10^{-105}$ and $10^{-44}$ of the weak scale $10^{11}$ eV: the tilt cannot reach $10^{2}$ GeV, the natural conjecture that the vacuum $\omega$-area sets the weak scale is refuted, and the weak scale falls back to the weight question, where the hierarchy has remained since the mass paper's fifth refutation.
\item \emph{(The redirection.)} Alignment requires only a nonzero tilt, and directions are ratios, $\Lambda$-independent; so what the vacuum $\omega$-area does determine is its \emph{direction} in the three-dimensional face space of Conjecture \claimref{families.three-generations-faces-maximal-composite}, which carries the family ordering and the mixing. The magnitude was never the physical content; the direction is, and the direction is computable from symmetry where the magnitude was not.
\item \emph{(The direction, at structural level, under the Gram-square reading.)} The kinematic vacuum cannot break $S_{3}$ before its own source exists: a face-anisotropic vacuum would be uncaused structure, forbidden by the indifference instrument (Fact \claimref{families.imported-indifference-instrument}). The source therefore lies on the democratic line, spanned by $u = (1,1,1)/\sqrt{3}$. If the leading mass form is the Gram square of the source, $Y_{0} \propto u' u'^{\mathsf{T}}$ with $u' = (1,1,1)$, the democratic mass matrix of \cite{HHW1978} (the reading Section \ref{sec:gaussian} realises at operator level and successor problem (2) asks to derive in general), then $Y_{0}$ has spectrum $(3, 0, 0)$ times the condensate scale: one heavy family and two light ones at leading order, the third generation's dominance as structure rather than fit; and Conjecture \claimref{families.three-generations-faces-maximal-composite} is refined rather than replaced: the physical families are the \emph{eigenvectors} of the face-space mass form, at leading order the democratic vector (heavy) and its orthogonal plane (light), the faces up to the rotation the vacuum performs.
\item \emph{(The residue, named.)} The second-order breaking $S_{3} \to S_{2} \to 1$, the anisotropic corrections that lift the two light families and convert the CKM shape into CKM numbers: the family programme's next computable target, confronted in Sections \ref{sec:koide}-\ref{sec:gaussian}. Everything in this proposition past the magnitude refutation is at the structural and observation levels stated.
\end{enumerate}

## technical
The source term of the mass functional is suppressed by $\Lambda$, so the condensate it can induce is $\delta b \sim \Lambda\,\Omega_{\mathrm{vac}}$ with $\Omega_{\mathrm{vac}}$ a length. For any vacuum length between the Planck and Hubble scales this lies between $H^{2}/M_{P} \approx 10^{-94}$ eV and $H \approx 10^{-33}$ eV, at least $10^{44}$ below the weak scale, so the conjecture that the vacuum $\omega$-area sets the weak scale is refuted by this dimensional estimate and the hierarchy stays with the weight question. What survives is the direction of the vacuum value in the three-dimensional face space, since directions are ratios and do not depend on $\Lambda$.

At structural level, the indifference instrument forbids a face-anisotropic kinematic vacuum, so the source lies on the democratic line spanned by $u = (1,1,1)/\sqrt{3}$. Under the further reading that the leading mass form is the Gram square of the source, $Y_{0} \propto u'u'^{\mathsf{T}}$ with $u' = (1,1,1)$ is the democratic matrix, with spectrum $(3,0,0)$ times the condensate scale: one heavy family and two light ones at leading order, the families being the eigenvectors of the face-space mass form. The second-order breaking $S_{3} \to S_{2} \to 1$ that lifts the light pair is named as the next target, not computed.

## lay
The paper first asks whether a tiny effect tied to the cosmological constant could set the energy scale of the weak force, and a size estimate shows it falls short by more than forty orders of magnitude, so that idea is ruled out. What the effect can still fix is a direction rather than a size. Assuming nature does not favour one family over another without cause, and assuming a particular form for the leading mass pattern, that direction gives one heavy family and two light ones at first approximation. Separating the two light families is left as the next problem.

## one-liner
The $\Lambda$-suppressed source cannot set the weak scale, but its direction, democratic under the indifference instrument, gives under the Gram-square reading a rank-one mass form with one heavy and two light families at leading order.
