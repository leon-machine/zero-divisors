---
id: note.one-relation.where-exhaustiveness-first-fails-4-quadric
kind: note
version: 2
title: 'Where exhaustiveness first fails: the $\nu = 4$ quadric'
status: remark
subject: one-relation
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T16, deposited version
comments_on:
- one-relation.third-constant-conversion-constant-between-charts
- one-relation.imported-pure-spinors-incidence-chart
- one-relation.imported-cartans-purity-theorem-thouless-form
- one-relation.spacetime-manifold-vacuum-lines
locators:
  paper: T16
  number: Rem 4.5
  label: rem:quadric
  line: 725
extraction:
  source_title: 'Where exhaustiveness first fails: the $\nu = 4$ quadric'
  source_formal: |-
    Fact \claimref{one-relation.imported-pure-spinors-incidence-chart}'s statement that every twistor is a vacuum is Cartan's purity theorem at $2\nu = 6$ (Fact \claimref{one-relation.imported-cartans-purity-theorem-thouless-form}), and it is a low-dimensional coincidence: the even sector of $\nu$ modes has projective dimension $2^{\nu - 1} - 1$ and the vacua form the spinor variety of dimension $\nu(\nu - 1)/2$, which agree at $\nu = 1, 2, 3$ and first differ at $\nu = 4$, seven against six. At $\nu = 3$ the vacuum orbit is open in the even sector and is everything: this is the transitivity of $SL(4, \C)$ on $\mathbb{P}^{3}$, the exceptional isomorphism $\mathrm{Spin}(6, \C) \cong SL(4, \C)$ on which the twistor correspondence rests, so the reason every twistor is a vacuum is the reason twistor space is a $\mathbb{P}^{3}$ on which the conformal group acts transitively. At $\nu = 4$, writing an even state as $\psi = \psi_{0}|0\rangle + \sum_{i<j}\psi_{ij}|ij\rangle + \psi_{1234}|1234\rangle$, the vacuum condition is the single quadric
    \[
    \mathcal{Q}(\psi) \;=\; \psi_{0}\,\psi_{1234} \;-\; \bigl(\psi_{12}\psi_{34} - \psi_{13}\psi_{24} + \psi_{14}\psi_{23}\bigr) \;=\; 0 ,
    \]
    the $\mathrm{Spin}(8)$-invariant triality form, and the reason is the Thouless form of Fact \claimref{one-relation.imported-cartans-purity-theorem-thouless-form}:
    \[
    \exp\Bigl(\sum_{i<j} A_{ij}a^{\dagger}_{i}a^{\dagger}_{j}\Bigr)|0\rangle \;=\; |0\rangle + \sum_{i<j} A_{ij}|ij\rangle + \mathrm{Pf}(A)|1234\rangle
    \]
    exactly, so the quartic coefficient of a vacuum is forced to be the Pfaffian of its quadratic coefficients, and at $\nu = 3$ there is no quartic term to constrain. The script verifies the identity on random antisymmetric $A$, the criterion $\mathcal{Q} = 0$ against the Gaussian purity test $M^{2} = -1$ on random even states, the tangent ranks $1 + \nu(\nu - 1)/2$ of the vacuum orbit at $\nu = 2, 3, 4$ with the orbit open at $\nu = 3$ and a hypersurface at $\nu = 4$, and a non-vacuum's orbit rank $8$. What this says for this paper: the incidence-line structure of Proposition \claimref{one-relation.spacetime-manifold-vacuum-lines} is a complex-capacity statement at $\nu = 3$, where purity is automatic, while the real capacity of $(1,3)$, one, admits no pairing at all ($\nu(\nu - 1)/2 = 0$); that answers half of successor problem (1). The definition of entanglement as mismatch between Witt decompositions, which the singularity paper's boundary mode space and its thermofield angle $\tan^{2}\theta = e^{-\omega/T}$ both use \cite[Lem.~7.2, Thm.~7.3]{ButlerT5}, is exhaustive at $\nu \leq 3$ and stops being so at $\nu = 4$, where $\mathcal{Q}$ is the order parameter of the states that belong to no Witt decomposition; that is the first instance of the quasi-free limit of the series' state class, named here and not opened.
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Converted every twistor to every conformal spinor, twistor space to $\PCS$ and the twistor correspondence to the point-line correspondence of conformal spinors. Kept $\mathrm{Spin}(6,\C) \cong SL(4,\C)$, a complex group, with the GA reading $\Cl^+(2,4) \cong \Mat_4(\C)$ over $I_6$ (TWGA E1.3c) added in parentheses.'
---

## formal
Fact \claimref{one-relation.imported-pure-spinors-incidence-chart}'s statement that every conformal spinor $Z \in \CS$ (every twistor) is a vacuum is Cartan's purity theorem at $2\nu = 6$ (Fact \claimref{one-relation.imported-cartans-purity-theorem-thouless-form}), and it is a low-dimensional coincidence: the even sector of $\nu$ modes has projective dimension $2^{\nu - 1} - 1$ and the vacua form the spinor variety of dimension $\nu(\nu - 1)/2$, which agree at $\nu = 1, 2, 3$ and first differ at $\nu = 4$, seven against six. At $\nu = 3$ the vacuum orbit is open in the even sector and is everything: this is the transitivity of $SL(4, \C)$ on $\mathbb{P}^{3}$, the exceptional isomorphism $\mathrm{Spin}(6, \C) \cong SL(4, \C)$ (in geometric algebra, $\Cl^+(2,4) \cong \Mat_4(\C)$ over the complex unit $I_6$) on which the correspondence between points and lines of conformal spinors rests, so the reason every conformal spinor is a vacuum is the reason the projective spinor space $\PCS$ is a $\mathbb{P}^{3}$ on which the conformal group acts transitively. At $\nu = 4$, writing an even state as $\psi = \psi_{0}|0\rangle + \sum_{i<j}\psi_{ij}|ij\rangle + \psi_{1234}|1234\rangle$, the vacuum condition is the single quadric
\[
\mathcal{Q}(\psi) \;=\; \psi_{0}\,\psi_{1234} \;-\; \bigl(\psi_{12}\psi_{34} - \psi_{13}\psi_{24} + \psi_{14}\psi_{23}\bigr) \;=\; 0 ,
\]
the $\mathrm{Spin}(8)$-invariant triality form, and the reason is the Thouless form of Fact \claimref{one-relation.imported-cartans-purity-theorem-thouless-form}:
\[
\exp\Bigl(\sum_{i<j} A_{ij}a^{\dagger}_{i}a^{\dagger}_{j}\Bigr)|0\rangle \;=\; |0\rangle + \sum_{i<j} A_{ij}|ij\rangle + \mathrm{Pf}(A)|1234\rangle
\]
exactly, so the quartic coefficient of a vacuum is forced to be the Pfaffian of its quadratic coefficients, and at $\nu = 3$ there is no quartic term to constrain. The script verifies the identity on random antisymmetric $A$, the criterion $\mathcal{Q} = 0$ against the Gaussian purity test $M^{2} = -1$ on random even states, the tangent ranks $1 + \nu(\nu - 1)/2$ of the vacuum orbit at $\nu = 2, 3, 4$ with the orbit open at $\nu = 3$ and a hypersurface at $\nu = 4$, and a non-vacuum's orbit rank $8$. What this says for this paper: the incidence-line structure of Proposition \claimref{one-relation.spacetime-manifold-vacuum-lines} is a complex-capacity statement at $\nu = 3$, where purity is automatic, while the real capacity of $(1,3)$, one, admits no pairing at all ($\nu(\nu - 1)/2 = 0$); that answers half of successor problem (1). The definition of entanglement as mismatch between Witt decompositions, which the singularity paper's boundary mode space and its thermofield angle $\tan^{2}\theta = e^{-\omega/T}$ both use \cite[Lem.~7.2, Thm.~7.3]{ButlerT5}, is exhaustive at $\nu \leq 3$ and stops being so at $\nu = 4$, where $\mathcal{Q}$ is the order parameter of the states that belong to no Witt decomposition; that is the first instance of the quasi-free limit of the series' state class, named here and not opened.

## technical
pending

## lay
pending

## one-liner
pending
