---
id: synthesis.imported-sl2r-discrete-series-tensor-product
kind: claim
version: 1
title: 'Imported: tensor products of $SL(2,\R)$ discrete series (Pukanszky; Repka)'
status: imported
region: synthesis
subject: mass
tags: [representation-theory, classical-theorem]
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
imported_from:
- citation: 'L. Pukanszky, On the Kronecker products of irreducible representations of the 2 x 2 real unimodular group. I, Trans. Amer. Math. Soc. 100 (1961), 116--152.'
  key: Pukanszky1961
- citation: 'J. Repka, Tensor products of unitary representations of SL2(R), Amer. J. Math. 100 (1978), 747--774.'
  key: Repka1978
extraction:
  note: >-
    Imported so that the point-spectrum result for the operator join
    (synthesis.operator-join-point-spectrum-on-positive-energy-modules, clause (5)) can pin the
    decomposition it cites from memory. What was checked on 2026-10-26: the title, journal, volume
    and pages of Pukanszky 1961 (reference list of J. Repka, Bull. Amer. Math. Soc. 82 (1976),
    930--932, the announcement of the 1978 paper under the same title); the journal, volume and
    year of Repka 1978 (reference list of arXiv:1912.00720); the pages 747--774 are from memory.
    The decomposition itself was not checked against either source: it is cited from memory, as
    the result that uses it states, and is consistent with the mixed-sign statement in
    arXiv:1912.00720 (the discrete part of a product of a positive and a negative discrete series
    contains discrete series of one sign only) and with the lowest-weight recurrence that the
    point-spectrum result proves for itself. The extension to half-integral lowest weights (the
    double cover, which the oscillator modules realise) is from memory: the argument (Fell
    absorption and the Plancherel formula of the cover) is the same.
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Created by the maintainer pass of 2026-10-26 (Leon accepted the operator-join results and asked for this import); bibliographic data partly checked, the decomposition cited from memory.'
---

## formal
Let $G$ be $SL(2,\R)$ or its double cover, with maximal compact generator $K_{0}$ and Casimir $C$ normalised so that $C = \kappa(\kappa - 1)$ on the discrete series. For $\kappa \in \tfrac12\mathbb{Z}$, $\kappa > 0$, let $D^{+}(\kappa)$ be the unitary irreducible lowest-weight representation with $K_{0}$-spectrum $\kappa, \kappa + 1, \dots$ and $D^{-}(\kappa)$ its conjugate, with $K_{0}$-spectrum $-\kappa, -\kappa - 1, \dots$. For $\kappa_{1}, \kappa_{2} \ge 1$:
\begin{enumerate}
\item[(i)] $D^{+}(\kappa_{1})$ is square-integrable, so $D^{+}(\kappa_{1}) \otimes D^{-}(\kappa_{2})$ is contained in a multiple of the regular representation of $G$ (Fell absorption).
\item[(ii)] $D^{+}(\kappa_{1}) \otimes D^{-}(\kappa_{2})$ decomposes as the finite direct sum of the discrete series $D^{\pm}(|\kappa_{1} - \kappa_{2}| - n)$, $n = 0, 1, \dots$ with $|\kappa_{1} - \kappa_{2}| - n > \tfrac12$, of sign $+$ if $\kappa_{1} > \kappa_{2}$ and $-$ if $\kappa_{1} < \kappa_{2}$ (none if $|\kappa_{1} - \kappa_{2}| \le \tfrac12$), each once, plus a direct integral of principal series representations, of the central character of the product, over a measure absolutely continuous with respect to Lebesgue measure on the principal parameter; no complementary series occurs.
\item[(iii)] Hence the point spectrum of $C$ on $D^{+}(\kappa_{1}) \otimes D^{-}(\kappa_{2})$ consists of the values $\kappa(\kappa - 1)$ of the discrete series in (ii), and every normalisable eigenvector of $C$ lies in their sum; on the principal series $C = -\tfrac14 - \nu^{2}$, $\nu$ real, which carries no point spectrum.
\end{enumerate}
\emph{Provenance:} \cite{Pukanszky1961} (Kronecker products of irreducible unitary representations of $SL(2,\R)$), \cite{Repka1978} (tensor products of unitary representations of $SL(2,\R)$, including the discrete series of opposite signs); the double cover and half-integral $\kappa$ by the same argument, cited from memory.

## technical
The group $SL(2,\R)$, the symmetry of the hidden $\mathfrak{su}(1,1)$ in the series' operator join, has two families of discrete series, one with energies bounded below and one with energies bounded above, and a continuous family, the principal series. When one representation bounded below is multiplied by one bounded above, the product splits into finitely many discrete series, all of the sign of the larger lowest weight and with lowest weights $|\kappa_{1} - \kappa_{2}|$, $|\kappa_{1} - \kappa_{2}| - 1$, and so on down to just above one half, plus a continuous superposition of principal series with no isolated weights and no complementary series. So an eigenvector of the Casimir that can be normalised must lie in the discrete part. The series uses this to show that the operator join has no normalisable zero modes on the positive-energy modules.

## lay
Some symmetry groups have representations that come in a continuous range as well as in separate, countable steps. This standard result of representation theory says what happens when two particular kinds of such representations are combined: the result is a finite number of the countable kind together with a smooth spread of the continuous kind. Only the countable pieces can hold states that are properly normalised. The series uses it to show that a certain mass operator has no genuine massless states.

## one-liner
For $SL(2,\R)$ (and its double cover), $D^{+}(\kappa_{1}) \otimes D^{-}(\kappa_{2})$ with $\kappa_{1}, \kappa_{2} \ge 1$ is the finite sum of discrete series $D^{\pm}(|\kappa_{1} - \kappa_{2}| - n)$, $|\kappa_{1} - \kappa_{2}| - n > \tfrac12$, plus an absolutely continuous direct integral of principal series, with no complementary series, so the Casimir's point spectrum is the discrete-series part (Pukanszky 1961, Repka 1978).
