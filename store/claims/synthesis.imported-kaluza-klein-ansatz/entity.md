---
id: synthesis.imported-kaluza-klein-ansatz
kind: claim
version: 1
title: 'Imported: the Kaluza-Klein ansatz (Kaluza 1921, Klein 1926)'
status: imported
region: synthesis
subject: dark-energy
tags: [classical-theorem, gauge-fields]
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
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'T. Kaluza, Zum Unitaetsproblem der Physik, Sitzungsber. Preuss. Akad. Wiss. Berlin (Math. Phys.) 1921, 966--972.'
  key: Kaluza1921
- citation: 'O. Klein, Quantentheorie und fuenfdimensionale Relativitaetstheorie, Z. Phys. 37 (1926), 895--906.'
  key: Klein1926
- citation: 'J. M. Overduin and P. S. Wesson, Kaluza-Klein gravity, Phys. Rep. 283 (1997), 303--378; arXiv:gr-qc/9805018.'
  key: OverduinWesson1997
  locator: 'eqs. (5) and (9)'
extraction:
  note: >-
    Imported so that the two Kasner-mode results can pin the ansatz they cited from memory (the
    Kaluza-Klein vector g_a4 = b^2 A_a and the weight of its field strength). Checked on 2026-11-01
    against Overduin and Wesson, arXiv:gr-qc/9805018 (PDF): the ansatz, their eq. (5), with blocks
    g_ab + kappa^2 phi^2 A_a A_b, kappa phi^2 A_a and phi^2, and the reduced action, their eq. (9),
    S = -int d^4x sqrt(-g) phi (R/(16 pi G) + (1/4) phi^2 F_ab F^ab + (2/(3 kappa^2)) d_a phi d^a
    phi/phi^2), so the Maxwell term carries phi^3. The bibliographic data of Kaluza 1921, Klein 1926
    and of the journal version of the review are from memory, not checked. The sign of the action
    and the signature follow the review; only the powers of phi are used.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (Leon approved the import of the Kaluza-Klein ansatz as a routine Fact).'
---

## formal
Let a five-dimensional gravitational field on flat $\R^{1,4}$ (the $d$-dimensional clause of Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) have a derived metric independent of the fifth coordinate $y$, written in the Kaluza-Klein form
\[
g_{AB} = \begin{pmatrix} g_{ab} + \kappa^{2}\phi^{2}A_{a}A_{b} & \kappa\phi^{2}A_{a} \\ \kappa\phi^{2}A_{b} & \phi^{2} \end{pmatrix},
\]
with $g_{ab}$ a four-dimensional metric, $A_{a}$ a vector potential and $\phi$ the scale of the fifth direction (up to the sign of $g_{yy}$ fixed by the signature). Then the five-dimensional Einstein-Hilbert action reduces, per unit length of $y$, to $S = -\int d^{4}x\,\sqrt{-g}\,\phi\,\bigl(\tfrac{R}{16\pi G} + \tfrac14\phi^{2}F_{ab}F^{ab} + \tfrac{2}{3\kappa^{2}}\,\partial_{a}\phi\,\partial^{a}\phi/\phi^{2}\bigr)$: four-dimensional gravity, a Maxwell field $F = dA$ whose kinetic term carries $\sqrt{-g}\,\phi^{3}$, and a scalar; the transformations $y \mapsto y + \kappa\lambda(x)$ act on $A$ as gauge transformations $A_{a} \mapsto A_{a} - \partial_{a}\lambda$. \emph{Provenance:} \cite{Kaluza1921}, \cite{Klein1926}; in the form of \cite{OverduinWesson1997} (eqs. (5), (9)).

## technical
Kaluza and Klein noticed that the components of a five-dimensional metric that mix the fifth direction with the other four behave, in four dimensions, as an electromagnetic potential, and that coordinate changes along the fifth direction act on it as gauge transformations. Reducing the five-dimensional gravitational action gives four-dimensional gravity, a Maxwell field whose coupling depends on the size of the fifth direction (its kinetic term carries the cube of that size), and a scalar field for the size itself.

## lay
A century ago Kaluza and Klein showed that gravity in five dimensions looks, to four-dimensional observers, like gravity plus electromagnetism plus one extra field measuring the size of the hidden dimension. That bookkeeping is what lets one read part of a five-dimensional gravitational field as a four-dimensional vector field.

## one-liner
With $g_{ay} = \kappa\phi^{2}A_{a}$, $g_{yy} = \phi^{2}$ and no dependence on $y$, five-dimensional gravity reduces to four-dimensional gravity, a Maxwell field weighted by $\sqrt{-g}\,\phi^{3}$ and a scalar (Kaluza 1921, Klein 1926).
