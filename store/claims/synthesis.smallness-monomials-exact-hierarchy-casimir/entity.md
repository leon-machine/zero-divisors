---
id: synthesis.smallness-monomials-exact-hierarchy-casimir
kind: claim
version: 3
title: 'The smallness problems as exact monomials in $N$'
status: proved
region: synthesis
subject: dark-energy
tags: [the-number-n, cosmological-constant, mass-generation, refutation]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
review: draft
derivations:
- name: main
  uses:
  - standard-model.imported-frozen-point-dictionary@7
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_gravitational_monomials
- kind: check
  ref: check.py::check_hierarchy_entry
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.one-number-explain
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The de Sitter weight -3/2 +- i nu, a physical number, is written -3/2 +- I_4 nu with numbers read in span{1, I_4} (formal and proof); Im w is its I_4 part; no bare i remains.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  open_problem: op.t12-n-after-the-count
  note: 'Supplies, as a proved result, the exponent computation that Observation standard-model.one-number-explain calls exact, and corrects its third entry: Im w(m) = (m/M_P) N holds only asymptotically (relative gap below 9H^2/(4m^2), about 1e-77 for the electron), while the exact monomial is the Casimir -w(w+3) = (m/M_P)^2 N^2 of the weight; for m <= 3H/2 the weight is real and Im w = 0. It carries the corrected statement of refutation 10 (one number in every smallness problem) at proved level, given the dictionary and the convention that gravity is compared at the Hubble scale; it does not touch the Dirac age coincidence, which Observation standard-model.what(iii) treats separately and conditionally. The identities themselves are standard de Sitter kinematics (m^2 = Delta(3 - Delta) H^2); the series contributes the reading of H^2 as the frozen point''s norm and of mass as weight against it, so the result is transport-convenient.'
---

## formal
Let $\Lambda = 3H^{2} > 0$, in units $\hbar = c = 1$ with $G = M_{P}^{-2}$, let $I_{\Lambda}$ be the frozen point of Fact \claimref{standard-model.imported-frozen-point-dictionary}, so $Q(I_{\Lambda}) = H^{2}$, and let $N := M_{P}/H$. For a mass $m$ let $w(m)$ be a weight the dictionary of that Fact assigns, $m^{2} = c(w)\,H^{2}$ with $c(w) := -w(w+3)$, the Casimir of the weight. Then:
\begin{enumerate}
\item[(i)] \emph{(The two gravitational entries.)} Exactly, $G\Lambda = 3N^{-2}$ and $G\,Q(I_{\Lambda}) = (H/M_{P})^{2} = N^{-2}$.
\item[(ii)] \emph{(The hierarchy entry, exactly.)} For every mass, $c(w(m)) = (m/M_{P})^{2}\,N^{2}$: the exact monomial is the Casimir of the weight, not its imaginary part.
\item[(iii)] \emph{(The imaginary part, asymptotically.)} For $m > 3H/2$ the weights are $w = -\tfrac32 \pm I_4\nu$ (numbers are read in $\mathrm{span}\{1, I_4\}$) with $\nu^{2} = (m/M_{P})^{2}N^{2} - \tfrac94$, and with $x = m/H = (m/M_{P})N$,
\[
\frac{9}{8x} \;\le\; x - \nu \;\le\; \frac{9}{4x}, \qquad 0 < 1 - \frac{\operatorname{Im} w}{(m/M_{P})N} \le \frac{9H^{2}}{4m^{2}},
\]
so $\operatorname{Im} w(m) = (m/M_{P})\,N$ holds for no mass exactly and for every mass far above $H$ to relative order $H^{2}/m^{2}$. For $m \le 3H/2$ the weight is real, $w \in [-3, 0]$, and $\operatorname{Im} w = 0$.
\item[(iv)] \emph{(The two readings of N.)} With $N_{w} := \operatorname{Im} w(M_{P})$, exactly $N^{2} = N_{w}^{2} + \tfrac94$, so $0 < N - N_{w} \le 9/(4N)$.
\end{enumerate}
So the three smallness numbers of Observation \claimref{standard-model.one-number-explain} are exactly $3N^{-2}$, $N^{-2}$ and, for the hierarchy, $m/M_{P} = \sqrt{c(w(m))}/N$: one number enters every one of them, given the dictionary and the choice of $H$ as the scale at which gravity's weakness is compared. The hierarchy entry is not a power of $N$: it carries a second number, the weight's Casimir, equivalently $m/M_{P}$ itself (for the weak scale the rung unit $v/M_{P}$, which the series holds kinematically independent of $N$).

## technical
With $N = M_{P}/H$, $G = M_{P}^{-2}$ and $H^{2} = \Lambda/3$ the norm of the frozen point, the cosmological-constant problem is exactly $G\Lambda = 3N^{-2}$ and the weakness of gravity at the Hubble scale is exactly $(H/M_{P})^{2} = N^{-2}$. For the mass hierarchy the series' dictionary reads a mass $m$ as a weight $w$ with $m^{2} = -w(w+3)H^{2}$, so the exact monomial is the weight's Casimir, $-w(w+3) = (m/M_{P})^{2}N^{2}$.

The statement that the imaginary part of the weight is $(m/M_{P})N$ is only asymptotic: for $m > 3H/2$, $\operatorname{Im} w = \sqrt{(m/H)^{2} - 9/4}$, smaller than $m/H$ by between $9H/(8m)$ and $9H/(4m)$, a relative gap of order $H^{2}/m^{2}$ (about $10^{-77}$ for the electron), and for $m \le 3H/2$ the weight is real. Likewise the two readings of $N$, $M_{P}/H$ and $\operatorname{Im} w(M_{P})$, differ by $N^{2} - N_{w}^{2} = 9/4$. One number enters all three smallness problems, given the dictionary and the choice of $H$ as the comparison scale; the first two are powers of it, while the hierarchy entry also carries the mass's own ratio $m/M_{P}$, a second number that is not a function of $N$.

## lay
Several puzzles about why some quantities in nature are so small, such as the tiny cosmological constant, the weakness of gravity and the lightness of particles compared with the Planck mass, can each be written using one large number, about $10^{61}$. This result checks the arithmetic exactly. Two of the puzzles are exactly proportional to that number to the power minus two, with factors three and one. For particle masses, the framework writes a mass as a complex label, and the exact statement involves a combination of that label rather than its imaginary part, which matches the large number only to an extremely good approximation. So one number does appear in every one of these puzzles, given the framework's dictionary for masses and a chosen comparison scale, although for particle masses a second number, the particle's own mass compared with the Planck mass, enters too.

## one-liner
Exactly, $G\Lambda = 3N^{-2}$, $(H/M_{P})^{2} = N^{-2}$ and the weight's Casimir $-w(w+3) = (m/M_{P})^{2}N^{2}$, while $\operatorname{Im} w(m) = (m/M_{P})N$ holds only to relative order $H^{2}/m^{2}$ and fails below $m = 3H/2$.
