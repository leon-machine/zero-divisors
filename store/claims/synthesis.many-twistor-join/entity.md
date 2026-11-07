---
id: synthesis.many-twistor-join
kind: claim
version: 3
title: The join for many conformal spinors
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
  - mass.exact-join@8
  - mass.chart-form-spin-isomorphism@6
  - mass.de-sitter-scale-frozen-point@6
  - mass.imported-flat-model-twistor-chart-infinity@7
  - mass.casimir-form-join@8
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_many_twistor_join
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - mass.exact-join
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The chart''s complex unit, which the convention line already read as I_6 but wrote i, is now written I_6 in the moment M_A and the slot-form components, numbers read in span{1, I_6}, and the coefficient space C^N is written span{1, I_6}^N; no bare i remains.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  open_problem: op.many-twistor-grip
  note: Clause (v) sharpens Theorem mass.exact-join(5) at two constituents, where the multiple of the identity is forced to be zero. At Lambda = 0 clause (ii) is the classical N-twistor mass formula of twistor particle theory (R. Penrose and M. A. H. MacCallum, Phys. Rep. 6 (1973) 241; Z. Perjes, Phys. Rev. D 11 (1975) 2031; L. P. Hughston, Twistors and Particles, Lecture Notes in Physics 97, 1979); the frozen-point term and the remainder are the series' content. Transport-absent in the sense that it uses only the flat chart and the frozen point, no tower structure. A suggested store follow-up is a note on mass.exact-join(5) recording that its multiple of the identity is zero, so that the two statements are not read as in tension.
---

## formal
Let $I_{\Lambda} = n_{\infty} + \lambda n_{0}$ with $\lambda = \Lambda/6$ be the frozen point of Lemma \claimref{mass.de-sitter-scale-frozen-point}, and $Z^{1}, \dots, Z^{N} \in \CS$, $N \ge 2$, a composite of conformal spinors, $Z^{i} = (\omega^{i}, \pi^{i})$, with the conventions of Theorem \claimref{mass.exact-join}: $t_{il} := \hp{\pi^{i}}{\omega^{l}}$, the Gram matrix $h_{il} := \bar{Z}^{i}\cdot Z^{l}$, so $h = t + t^{\dagger}$, and
\[
B^{il}_{\Lambda} := \ip{I_{\Lambda}}{Z^{i}\wedge Z^{l}} = \br{\pi^{i}\pi^{l}} + \lambda\,[\omega^{i}\omega^{l}] .
\]
Let $P = M(I_{\Lambda})$ be the grip and $p$, $k$, $d$ its slot forms $p(x) = M_{x\wedge n_{\infty}}$, $k(x) = M_{x\wedge n_{0}}$, $d = M_{n_{\infty}\wedge n_{0}}$.
\begin{enumerate}
\item \emph{(Components.)} $Q(P) = Q(p) + 2\lambda\,(p\cdot k - d^{2}) + \lambda^{2}\,Q(k)$ with
\[
Q(p) = 2\sum_{i<l}|\br{\pi^{i}\pi^{l}}|^{2},\quad Q(k) = 2\sum_{i<l}|[\omega^{i}\omega^{l}]|^{2},\quad p\cdot k = \sum_{i,l}|t_{il}|^{2},\quad d = \mathrm{Im}\,\tr t .
\]
\item \emph{(The join.)} 
\[
m^{2} = Q(P) = 2\sum_{i<l}|B^{il}_{\Lambda}|^{2} + \frac{\Lambda}{3}\,C_{N},
\qquad
C_{N} := \tfrac12\tr(h^{2}) - \tfrac14(\tr h)^{2} = \tfrac12\tr(h_{0}^{2}) - \frac{N-2}{4N}(\tr h)^{2},
\]
with $h_{0}$ the traceless part of $h$; at $N = 2$, $C_{2}$ is the Casimir $C$ of Theorem \claimref{mass.exact-join}.
\item \emph{(The remainder is a $\uu(N)$ invariant.)} Under the mixing $Z^{i} \mapsto \sum_{j}Z^{j}U_{ji}$, $U \in U(N)$, $h \mapsto U^{\dagger}hU$ and $B_{\Lambda} \mapsto U^{\mathsf T}B_{\Lambda}U$; the grip, $m^{2}$, $\sum_{i<l}|B^{il}_{\Lambda}|^{2} = \tfrac12\tr(B_{\Lambda}B_{\Lambda}^{\dagger})$ and $C_{N}$ are invariant. $C_{N}$ is the combination $\tfrac12\tr(h^{2}) - \tfrac14(\tr h)^{2}$ of the two quadratic invariants of the Gram matrix, which for $N > 2$ is not the $\su(N)$ Casimir alone.
\item \emph{(Positivity.)} $h$ has at most two positive and at most two negative eigenvalues. Writing them $a_{1} \ge a_{2} \ge 0$ and $-b_{1} \le -b_{2} \le 0$ (padded with zeros), $4C_{N} = (a_{1} - a_{2})^{2} + (b_{1} - b_{2})^{2} + 2(a_{1} + a_{2})(b_{1} + b_{2}) \ge 0$, so $m^{2} \ge 0$ for $\Lambda \ge 0$. For $N \ge 3$ this uses the signature of $\CS$: the Hermitian matrix $1_{N}$ has $C_{N} = N(2 - N)/4 < 0$.
\item \emph{(The massless locus.)} For $\Lambda > 0$, $m^{2} = 0$ if and only if $B^{il}_{\Lambda} = 0$ for all $i < l$ and $h = 0$: the constituents span a subspace that is null for the twistor form and isotropic for the frozen point's pairing. In particular, at $N = 2$ the multiple of the identity in Theorem \claimref{mass.exact-join}(5) is zero.
\item \emph{(The de Sitter Casimir.)} For $\Lambda \ne 0$ and any $N$, $C_{2}(I_{\Lambda}^{\perp}) = \tfrac12\tr(h^{2}) - \frac{6}{\Lambda}\sum_{i<l}|B^{il}_{\Lambda}|^{2}$, in the normalisation of Proposition \claimref{mass.casimir-form-join}.
\end{enumerate}

## technical
For any number $N$ of conformal spinors the grip on the frozen point decomposes exactly as twice the sum over pairs of the squared deformed brackets $B^{il}_{\Lambda} = \br{\pi^{i}\pi^{l}} + \tfrac{\Lambda}{6}[\omega^{i}\omega^{l}]$, plus $\tfrac{\Lambda}{3}C_{N}$, where $C_{N} = \tfrac12\tr h^{2} - \tfrac14(\tr h)^{2}$ is built from the Gram matrix $h$ of the constituents and is invariant under the $U(N)$ that mixes them. The proof is the two-spinor one run pair by pair: the slot forms are sums over constituents, the pairings are per pair, and the cross terms of the brackets are the principal $2\times 2$ minors of the mixed-pairing matrix $t$, whose sum is $\tfrac12((\tr t)^{2} - \tr t^{2})$. Positivity for $N \ge 3$ is not automatic, since $C_{N}$ is indefinite on Hermitian matrices; it holds because $h = \mathbf{Z}^{\dagger}S\mathbf{Z}$ with $S$ of signature $(2,2)$, which bounds the inertia of $h$. For $\Lambda > 0$ the massless composites are exactly those whose span is null for the twistor form and isotropic for the frozen point's pairing; a nonzero multiple of a rank-two projector is excluded by an antilinear map $J$ with $J^{2} = -\lambda$ that would double a definite isotropic plane into a definite four-space. The de Sitter Casimir of the composite is $\tfrac12\tr h^{2} - (6/\Lambda)\sum|B^{il}_{\Lambda}|^{2}$ for every $N$.

## lay
The series' mass formula for a particle made of two twistors extends to any number of them. The mass squared is a sum over all pairs of constituents of how misaligned each pair is, read against the built-in cosmological scale, plus a small correction proportional to the cosmological constant that depends only on how the constituents overlap, and that does not care how they are relabelled or mixed. For a positive cosmological constant the correction is never negative, but for three or more constituents only because twistor space has the particular shape it has. A composite is massless only when every pair is aligned and the constituents do not overlap at all.

## one-liner
For $N$ conformal spinors $m^{2} = 2\sum_{i<l}|B^{il}_{\Lambda}|^{2} + \tfrac{\Lambda}{3}\bigl(\tfrac12\tr h^{2} - \tfrac14(\tr h)^{2}\bigr)$, a $U(N)$-invariant remainder that is nonnegative, so $m^{2} \ge 0$ for $\Lambda \ge 0$; massless iff all $B^{il}_{\Lambda}$ and $h$ vanish.
