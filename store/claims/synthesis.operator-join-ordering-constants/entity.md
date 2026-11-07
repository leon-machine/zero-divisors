---
id: synthesis.operator-join-ordering-constants
kind: claim
version: 3
title: The operator join and its ordering constants
status: proved
region: synthesis
subject: mass
tags: [frozen-point, conformal-spinors]
proposed_by:
  kind: ai
  session: colony-2026-10-22
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
about:
- obj.mass.grip-mass-composite
derivations:
- name: main
  uses:
  - correspondence.symmetrised-quadratics-palatial-algebra@5
  - correspondence.shared-core-ordering-dictionary@4
  - mass.chart-form-spin-isomorphism@5
  - mass.imported-flat-model-twistor-chart-infinity@7
  - mass.de-sitter-scale-frozen-point@6
  - mass.exact-join@8
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_operator_join
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - mass.exact-join
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The unit in the symmetrised moment M_A := i sum (1/2)(Zbar . AZ + AZ . Zbar) and in F = i A_U, G = i A_V became I_6, the complex unit of CS that the classical moment of mass.exact-join carries, with numbers and oscillator coefficients read in span{1, I_6}; no bare i remains.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  open_problem: op.operator-join
  note: Clause (3) is stated for two constituents, where the classical join is Theorem mass.exact-join; the same computation gives the constant -(N Lambda/3) hbar^2 for N constituents once the classical N-constituent join holds, which is the companion proposal synthesis.many-twistor-join, and the check confirms the operator identity directly at N = 3. On the seed question (T11 successor problem (4)), the ordering terms contain no operator linear in the brackets, so the seed is not in the ordering constants; this agrees with the settlement recorded in note.mass.what-join-says (the seed is the classical Lambda-linear source term of families.source-term-linear-tilt-mass-functional). A Capelli-identity route had suggested constants linear in the helicity charge with a factor (4 - N); that is not what happens for the join as a whole, where the helicity terms cancel in palatial ordering and the normal-ordered coefficient is independent of N.
---

## formal
Let $Z^{1}, \dots, Z^{N}$ be $N$ copies of the palatial oscillators, $[Z^{\alpha}_{i}, \bar{Z}_{l\beta}] = \hbar\,\delta_{il}\delta^{\alpha}_{\beta}$, let $I_{\Lambda} = n_{\infty} + \lambda n_{0}$ with $\lambda = \Lambda/6$ be the frozen point of Lemma \claimref{mass.de-sitter-scale-frozen-point}, and quantise each moment component of the grip as a symmetrised quadratic (Lemma \claimref{correspondence.symmetrised-quadratics-palatial-algebra}, Theorem \claimref{correspondence.shared-core-ordering-dictionary}): $\hat{M}_{A} := I_{6}\sum_{i}\tfrac12\bigl(\bar{Z}_{i}\cdot AZ^{i} + AZ^{i}\cdot\bar{Z}_{i}\bigr)$, with $I_{6}$ the complex unit of $\CS$, the chart's unit of Theorem \claimref{mass.exact-join} (numbers, and the coefficients of polynomials in the oscillators, are read in $\mathrm{span}\{1, I_{6}\}$). Put $\ip{\hat{P}}{U} := \hat{M}_{U\wedge I_{\Lambda}}$ and $\hat{m}^{2} := Q(\hat{P})$. Write $\hat{h}_{il}$ for the symmetrised Gram operators (so $\hat{h}_{ii}$ is the palatial helicity generator of constituent $i$), $:\;:$ for normal ordering with every $\bar{Z}$ to the right of every $Z$, $\hat{B}^{il}$ for the bracket $B^{il}_{\Lambda} = \br{\pi^{i}\pi^{l}} + \lambda[\omega^{i}\omega^{l}]$ (a polynomial in the $Z$ alone) and $\hat{B}^{il\dagger}$ for its conjugate (a polynomial in the $\bar{Z}$ alone), and $m^{2}$ for the classical squared grip.
\begin{enumerate}
\item \emph{(No shift in the grip.)} Every generator $A(U\wedge I_{\Lambda})$ is traceless, so every component of $\hat{P}$ carries no ordering shift, and $\hat{m}^{2}$ is a symmetric contraction of products of them: the operator grip and its square are fixed by the palatial quantisation without further choice.
\item \emph{(Normal form.)} For any $N$,
\[
\hat{m}^{2} \;=\; :m^{2}: \;-\; \tfrac54\,\hbar\,Q(I_{\Lambda})\,:\tr h: \;=\; :m^{2}: \;-\; \frac{5\Lambda}{12}\,\hbar\,:\tr h:,
\qquad :\tr h: \;=\; \tr\hat{h} + 2N\hbar ,
\]
because $\sum_{U,V}G^{UV}A(U\wedge I_{\Lambda})A(V\wedge I_{\Lambda}) = -\tfrac54Q(I_{\Lambda})\,1$ on $\CS$, with $G^{UV}$ the inverse ambient metric.
\item \emph{(Palatial form.)} For two constituents,
\[
\hat{m}^{2} \;=\; \hat{B}^{\dagger}\hat{B} + \hat{B}\hat{B}^{\dagger} \;+\; \frac{\Lambda}{3}\,\hat{C} \;-\; \frac{2\Lambda}{3}\,\hbar^{2},
\qquad \hat{C} := \tfrac12\sum_{i,l}\hat{h}_{il}\hat{h}_{li} - \tfrac14(\tr\hat{h})^{2},
\]
the symmetric quantisation of $2|B_{\Lambda}|^{2} + \tfrac{\Lambda}{3}C$ of Theorem \claimref{mass.exact-join} plus one central constant: the terms of order $\hbar$ times a quadratic cancel, and $[\hat{B}, \hat{B}^{\dagger}] = \hbar\lambda(\hat{h}_{11} + \hat{h}_{22})$. The value of the constant depends on how the classical right side is quantised, while $\hat{m}^{2}$ does not: the constant $-\tfrac{2\Lambda}{3}\hbar^{2}$ is relative to the Jordan-symmetrised products of the palatial factors $\hat{B}$, $\hat{B}^{\dagger}$, $\hat{h}$ displayed above, whereas relative to the Weyl quantisation $W(m^{2})$ of the classical quartic, $\hat{m}^{2} = W(m^{2}) - \tfrac{5N\Lambda}{12}\hbar^{2}$ for any $N$. More generally, whenever the classical identity $m^{2} = 2\sum_{i<l}|B^{il}_{\Lambda}|^{2} + \tfrac{\Lambda}{3}C_{N}$, $C_{N} = \tfrac12\tr h^{2} - \tfrac14(\tr h)^{2}$, holds for $N$ constituents, the same computation gives $\hat{m}^{2} = \sum_{i<l}(\hat{B}^{il\dagger}\hat{B}^{il} + \hat{B}^{il}\hat{B}^{il\dagger}) + \tfrac{\Lambda}{3}\hat{C}_{N} - \tfrac{N\Lambda}{3}\hbar^{2}$.
\item \emph{(Flat limit.)} At $\Lambda = 0$ both forms carry no ordering terms.
\end{enumerate}

## technical
The operator join is computed exactly. Each component of the grip is the palatial quadratic of a traceless generator, so the grip operator and its square need no ordering choice. Written in normal order (every conjugate oscillator to the right), the squared grip is the normal-ordered classical expression minus $\tfrac{5\Lambda}{12}\hbar$ times the normal-ordered total helicity, the $\tfrac54$ being the contraction of the five generators $A(U\wedge I_{\Lambda})$ on the four-dimensional conformal spinor space. Written in the palatial (symmetric) order of the classical join's own terms, the helicity-linear terms cancel and a single central constant remains, $-\tfrac{N\Lambda}{3}\hbar^{2}$, $-\tfrac{2\Lambda}{3}\hbar^{2}$ for the pair. The number is convention-relative: it is the constant relative to the Jordan-symmetrised products of $\hat{B}$, $\hat{B}^{\dagger}$ and $\hat{h}$; relative to the Weyl quantisation of the classical quartic the operator is $W(m^{2}) - \tfrac{5N\Lambda}{12}\hbar^{2}$. No ordering term is linear in the brackets $\hat{B}$, $\hat{B}^{\dagger}$, so the ordering constants supply no source for the flat bracket: the condensation seed is not in them, and the classical $\Lambda$-linear source term stands as the seed. Two independent exact routes confirm the identities: Moyal composition of Weyl symbols, and the holomorphic realisation $\bar{Z} = -\hbar\,\partial/\partial Z$ on test polynomials.

## lay
The series' mass formula for a composite was a classical formula. Turning it into an operator raises the usual question of what order to write the factors in, and each choice can add small extra terms. Here those extra terms are computed. In the series' preferred symmetric ordering of the formula's own terms they collapse to one fixed number, proportional to the cosmological constant and to the number of constituents (the number itself depends on that ordering convention). They contain no term linear in the bracket, so they are not the seed of condensation in the sense the series uses, a source term linear in the cosmological constant and in the bracket.

## one-liner
In Jordan-symmetrised palatial ordering $\hat{m}^{2} = \sum_{i<l}\{\hat{B}^{il}, \hat{B}^{il\dagger}\} + \tfrac{\Lambda}{3}\hat{C}_{N} - \tfrac{N\Lambda}{3}\hbar^{2}$, one central constant, and in normal order $\hat{m}^{2} = :m^{2}: - \tfrac{5\Lambda}{12}\hbar:\tr h:$.
