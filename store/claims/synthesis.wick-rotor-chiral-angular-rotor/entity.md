---
id: synthesis.wick-rotor-chiral-angular-rotor
kind: claim
version: 3
title: 'The Wick-rotated boost as the angular rotor on each chiral half'
status: proved
region: synthesis
subject: thermality
tags: [rotors-and-stabilisers, pseudoscalar-and-centre, chirality, conformal-spinors]
proposed_by:
  kind: ai
  session: synthesis-bridges-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
derivations:
- name: main
  uses:
  - singularity.euclidean-rotor-where-it-lies@4
  - state-selection.euclidean-partner-curvature-selected@4
  - field-theory.where-each-lives@3
  - odd-extensions.imported-conformal-completion@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_generator_identities
- kind: check
  ref: check.py::check_chiral_splitting
- kind: check
  ref: check.py::check_not_a_rotor_on_vectors
lineage:
  motivated_by:
  - note.pairing.setting-two-claims-kill-conditions-fixed-3
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: in Cl(2,4), I6 sigma = E e2e3 (square -1, central in the even algebra), the chiral splitting R^W = eps_+ R_theta + eps_- R_-theta and I6 = +-I4 on the halves at four rational points, and the failure of R reverse(R) = 1 and of vector preservation off pi Z. Version 2 -> 3.'
  check_lost:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'check.py (check_wick_rotor) was lost in an earlier sync and is not on any copy; the check evidence is removed and the claim rests on its proof text until the check is rebuilt.'
  review_fixes:
    by: ai-review-fix
    date: 2026-10-21
    note: 'Referee fixes: the no-isometry statements restricted to theta outside pi Z (at theta = pi the element is the versor E e2 e3); proof notes that left and right multiplication by I6 agree on the conformal spinors.'
---

## formal
Let $\sigma = e_{0}e_{1}$ be the radial boost bivector ($\sigma^{2} = +1$), $I_{4} = e_{0}e_{1}e_{2}e_{3}$, $E = e_{+}e_{-}$ and $I_{6} = I_{4}E$ as in Proposition \claimref{field-theory.where-each-lives}, and $I_{4}\sigma = e_{2}e_{3}$ the angular member of the curvature-selected pair (Proposition \claimref{state-selection.euclidean-partner-curvature-selected}). Take as the unit of the continuation $\lambda \mapsto i\theta$ of Proposition \claimref{singularity.euclidean-rotor-where-it-lies} the complex unit $I_{6}$ of the conformal spinors $\CS$ (Fact \claimref{odd-extensions.imported-conformal-completion}). Then:
\begin{enumerate}
\item[(i)] $I_{6}\sigma = E\,(I_{4}\sigma) = E\,e_{2}e_{3}$, a $4$-blade of the real even algebra $\Cl^{+}(2,4)$, commuting with $\sigma$ and with $E$, with $(I_{6}\sigma)^{2} = -1$; so $R^{W}_{\theta} := \exp(\theta I_{6}\sigma/2) = \cos(\theta/2) + \sin(\theta/2)\,E\,e_{2}e_{3}$ is a real even element, with $R^{W}_{2\pi} = -1$ and $R^{W}_{4\pi} = +1$.
\item[(ii)] With the idempotents $\varepsilon_{\pm} = \tfrac12(1 \pm E)$ and the angular rotor $R_{\theta} = \exp(\theta I_{4}\sigma/2)$,
\[
R^{W}_{\theta} \;=\; \varepsilon_{+}R_{\theta} \;+\; \varepsilon_{-}R_{-\theta} .
\]
On $\CS = L_{0} \oplus L_{\infty}$, the $E = \pm 1$ eigenspaces on which $I_{6} = \pm I_{4}$, the continued boost therefore acts on $L_{0}$ as the real angular rotor $R_{\theta}$ and on $L_{\infty}$ as $R_{-\theta}$: on each chiral doublet the Wick-rotated radial boost is a real rotation of the angular plane, its sense fixed by the chirality, that is by the relative sign of $I_{6}$ and $I_{4}$.
\item[(iii)] $R^{W}_{\theta}$ is not a rotor: $R^{W}_{\theta}\rev{R^{W}_{\theta}} = \cos\theta + \sin\theta\,E\,e_{2}e_{3} \neq 1$ for $\theta \notin 2\pi\Z$, and for $\theta \notin \pi\Z$ conjugation by it does not map vectors to vectors. For $\theta \notin \pi\Z$ it is no isometry of the ambient vectors, so clause (3) of Proposition \claimref{singularity.euclidean-rotor-where-it-lies} stands for vectors and for every holonomy of a real connection, while the identification of the Euclidean rotation with the angular member in Proposition \claimref{state-selection.euclidean-partner-curvature-selected} holds on each chiral half of the conformal spinors, up to the orientation sign.
\end{enumerate}

## technical
The singularity paper continues the radial boost $\exp(\lambda\sigma/2)$ to imaginary rapidity with an external unit $i$ and finds that the result is no real rotor of $\Cl(1,3)$; the state-selection note instead reads the Euclidean rotation as the real angular rotor $\exp(\theta I\sigma_r/2)$, $I\sigma_r = e_{2}e_{3}$. Taking for $i$ the conformal spinors' own unit $I_{6} = I_{4}E$ reconciles the two. Since $I_{6}\sigma = E\,e_{2}e_{3}$ with $E$ and $e_{2}e_{3}$ commuting, the continued boost is the real even element $\cos(\theta/2) + \sin(\theta/2)E\,e_{2}e_{3}$, equal to $\tfrac12(1+E)R_{\theta} + \tfrac12(1-E)R_{-\theta}$. On the chiral halves $L_{0}$, $L_{\infty}$ of the conformal spinors ($E = \pm1$) it is the angular rotor turned one way or the other, so the state-selection reading holds on each chirality, the sense of rotation being the orientation bit. For $\theta \notin \pi\Z$ it is not even in the Clifford group, so the singularity paper's statement that no real rotor, and no holonomy, realises the Euclidean rotation is untouched.

## lay
A standard way to see that black holes are hot is to turn the time of a static observer into an angle. Two of the series' texts seemed to disagree about which real rotation that angle belongs to: one says no real rotation of spacetime does the job, the other says the rotation along the horizon sphere does. Using the imaginary unit that the series' twistor-like spinors already carry, this result shows both are right in their own place: acting on spinors of one handedness the turned boost is exactly the rotation along the sphere, in a direction set by the handedness, while acting on ordinary directions in spacetime it is not a rotation at all.

## one-liner
With $i = I_{6}$, $\exp(\theta I_{6}\sigma/2) = \tfrac12(1+E)\exp(\theta e_{2}e_{3}/2) + \tfrac12(1-E)\exp(-\theta e_{2}e_{3}/2)$: on each chiral half of the conformal spinors the Wick-rotated radial boost is the real angular rotor, while for $\theta \notin \pi\Z$ it acts on vectors as no isometry.
