---
id: synthesis.imported-theta-function-identities
kind: claim
version: 1
title: 'Imported: the Jacobi theta and Dedekind eta identities'
status: imported
region: synthesis
subject: entropy
tags: [bosonisation, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-22
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'E. T. Whittaker and G. N. Watson, A Course of Modern Analysis, 4th ed., Cambridge University Press, Cambridge (1927).'
  key: WhittakerWatson1927
  locator: 'Ch.~21'
- citation: 'D. Mumford, Tata Lectures on Theta I, Progress in Mathematics 28, Birkhauser, Boston (1983).'
  key: Mumford1983
  locator: 'Ch.~I'
extraction:
  note: >-
    Imported for the exact value of the half-offset array's entropy at the Hawking temperature.
    Cited from memory, not checked against the source. During filing each identity (the product
    forms against the series, the three transformations including that of theta_4, the quartic
    identity and theta_2 theta_3 theta_4 = 2 eta^3) was evaluated in double precision at tau = i t
    for t = 0.7, 1, 1.9, with agreement to rounding (about 1e-15), and theta_3(i)/eta(i) = sqrt 2
    likewise; this is a numerical confirmation of the statements, not a proof and not a check of the
    references.
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Created by the maintainer pass so that the half-offset array result can pin the theta-function identities it cited from memory; statements confirmed numerically, references cited from memory.'
---

## formal
For $\tau$ in the upper half-plane put $q = e^{2\pi i\tau}$ and
\[
\vartheta_{3}(\tau) = \sum_{n \in \Z}q^{n^{2}/2}, \quad \vartheta_{4}(\tau) = \sum_{n \in \Z}(-1)^{n}q^{n^{2}/2}, \quad \vartheta_{2}(\tau) = \sum_{n \in \Z}q^{(n + 1/2)^{2}/2}, \quad \eta(\tau) = q^{1/24}\prod_{n \geq 1}(1 - q^{n}).
\]
Then:
\begin{enumerate}
\item[(a)] (products) $\vartheta_{3} = \prod_{n \geq 1}(1 - q^{n})(1 + q^{n - 1/2})^{2}$, $\vartheta_{4} = \prod_{n \geq 1}(1 - q^{n})(1 - q^{n - 1/2})^{2}$, $\vartheta_{2} = 2q^{1/8}\prod_{n \geq 1}(1 - q^{n})(1 + q^{n})^{2}$;
\item[(b)] (the transformation $\tau \mapsto -1/\tau$) $\vartheta_{3}(-1/\tau) = \sqrt{-i\tau}\,\vartheta_{3}(\tau)$, $\vartheta_{2}(-1/\tau) = \sqrt{-i\tau}\,\vartheta_{4}(\tau)$, $\vartheta_{4}(-1/\tau) = \sqrt{-i\tau}\,\vartheta_{2}(\tau)$, $\eta(-1/\tau) = \sqrt{-i\tau}\,\eta(\tau)$, with the branch of the square root positive on the imaginary axis;
\item[(c)] (Jacobi's quartic identity) $\vartheta_{3}^{4} = \vartheta_{2}^{4} + \vartheta_{4}^{4}$;
\item[(d)] $\vartheta_{2}\vartheta_{3}\vartheta_{4} = 2\eta^{3}$.
\end{enumerate}
On the imaginary axis all four functions are positive. \emph{Provenance:} \cite[Ch.~21]{WhittakerWatson1927}; \cite[Ch.~I]{Mumford1983}.

## technical
The Jacobi theta functions $\vartheta_{2}, \vartheta_{3}, \vartheta_{4}$ and the Dedekind eta function, written as series or products in $q = e^{2\pi i\tau}$, satisfy classical identities: under $\tau \mapsto -1/\tau$, $\vartheta_{3}$ and $\eta$ go to themselves and $\vartheta_{2}$, $\vartheta_{4}$ to each other, each times $\sqrt{-i\tau}$; Jacobi's quartic identity $\vartheta_{3}^{4} = \vartheta_{2}^{4} + \vartheta_{4}^{4}$ holds; and $\vartheta_{2}\vartheta_{3}\vartheta_{4} = 2\eta^{3}$. The product forms follow from the Jacobi triple product.

## lay
Theta functions are special functions, built from sums of exponentials of squares, that appear throughout number theory and physics. They obey a small set of exact identities, discovered by Jacobi in the nineteenth century, including a symmetry that exchanges a parameter with its reciprocal. These are classical results taken from the literature.

## one-liner
With $q = e^{2\pi i\tau}$: the product forms of $\vartheta_{2}, \vartheta_{3}, \vartheta_{4}$, their and $\eta$'s behaviour under $\tau \mapsto -1/\tau$ (each times $\sqrt{-i\tau}$, with $\vartheta_{2} \leftrightarrow \vartheta_{4}$), $\vartheta_{3}^{4} = \vartheta_{2}^{4} + \vartheta_{4}^{4}$ and $\vartheta_{2}\vartheta_{3}\vartheta_{4} = 2\eta^{3}$.
