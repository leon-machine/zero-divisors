---
id: synthesis.gravitational-pair-production-from-the-operator-source-at-first-order
kind: claim
version: 1
title: Gravitational pair production from the operator source at first order
status: proved
region: synthesis
subject: quantum-fields
tags: [quantum-gravity, scattering-amplitudes, recovers-known-physics, mirror-sector]
proposed_by:
  kind: ai
  session: 2026-11-18-navigate
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-18-navigate
review: draft
derivations:
- name: main
  uses:
  - synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel@1
  - synthesis.imported-einstein-cartan-matter-coupling@1
  - field-theory.operator-newtonian-coupling@4
  - synthesis.imported-maxwell-stress-spacetime-algebra@2
  - synthesis.electron-positron-to-muon-pairs-in-the-spacetime-algebra-lsz-tree-cross-section-and-one-loop-unitarity@4
  - synthesis.imported-conformal-covariance-of-massless-fields-and-local-conformal-flatness@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_first_order_field_at_non_null_momentum_is_fixed_by_the_source
- kind: check
  ref: check.py::check_bilinear_is_normalised_by_the_stored_newtonian_coupling
- kind: check
  ref: check.py::check_pair_sources_and_their_brackets
- kind: check
  ref: check.py::check_channel_weights_are_products_of_the_spin_two_weights
- kind: check
  ref: check.py::check_rate_coefficients_and_the_published_values
lineage:
  motivated_by:
  - dark-matter.imported-massless-graviton-production-rate
  - pred.gravity-entangles-standard-phase
  - dark-matter.seeding-gravity-floor-dark-towers-temperature
  - dark-matter.coefficients-floors-they-give-what-gravity
extraction:
  open_problem: op.graviton-rate-as-classical-field-process
  note: >-
    Filed against the first two attack items of the problem. Hypothesis (OS) is a hypothesis of this result
    and not a stored premise: in the static limit it is the stored operator Newtonian coupling, and beyond
    that limit the store holds nothing (the problem's own text). Whether the series adopts (OS), and for which
    momenta, is the maintainer's decision; it is tied to the decision put by the result filed alongside on
    the field at null momentum. The comparison with the literature was the test registered before the
    computation: reproduce the stored scalar coefficient. It failed by a factor that this result accounts for
    from the sources (a factor sixteen between two published values of the same quantity, and the weight given
    to the Standard Model's fermions), both read on the web during the run: arXiv:1803.01866 (the stored
    Fact's source; coupling and matrix elements read on ar5iv by the proposer, its appendix, equations (17),
    (25) to (27), (31) and Table I, by the referee) and arXiv:2112.15214 (S. Clery, Y. Mambrini, K. A. Olive and
    S. Verner; equations (2), (11), (79) and (83) to (90)). Footnote 5 of the second concerns a different
    earlier paper and is not evidence about the stored Fact's source. The improvement term of the scalar stress
    and the symmetric Dirac stress are standard forms cited from memory. Not
    done here: the correction of the stored Fact and of the numbers in its four direct users, which are
    maintainer edits; the vector coefficient of the stored Fact was not re-derived from its source (a massive
    vector has a third polarisation; the value here is for a massless one).
---

## formal
Units $\hbar = c = 1$, signature $(+,-,-,-)$ in $\Cl(1,3)$, $\bar{M}_{P}^{-2} = 8\pi G$. A \emph{source} at momentum $k$ is a symmetric linear map $\mathcal{T}$ of the vectors with $\mathcal{T}(k) = 0$; $\ip{\mathcal{T}_{1}}{\mathcal{T}_{2}} = \sum_{a} \mathcal{T}_{1}(e_{a}) \cdot \mathcal{T}_{2}(e^{a})$, $\tr\mathcal{T} = \sum_{a} e^{a} \cdot \mathcal{T}(e_{a})$, and
\[
B(\mathcal{T}_{1}, \mathcal{T}_{2}) \;=\; \ip{\mathcal{T}_{1}}{\mathcal{T}_{2}} - \tfrac12\,\tr\mathcal{T}_{1}\,\tr\mathcal{T}_{2} .
\]
\emph{Hypothesis (OS) (operator source at first order).} To first order in $G$ the gravitational gauge field is the solution of the stored frame equation (Fact \claimref{synthesis.imported-einstein-cartan-matter-coupling}(a), $\Lambda = 0$) linearised about the flat field, with the stress map of the matter fields, an element of the matter algebra, as its source, and matter responds to it through its stress map (clause (v) of Theorem \claimref{synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel}); no state of the gauge field enters. (OS) is assumed here, not derived. In the static limit it is the stored coupling of Proposition \claimref{field-theory.operator-newtonian-coupling}.
\begin{enumerate}
\item[(i)] \emph{(The field at non-null momentum is fixed by the source; proved.)} With the stored first-order curvature $\mathcal{R}_{k}[h](B) = -\tfrac12\,k \wedge h(B \cdot k)$ and its Einstein map $\mathcal{G}_{k}$, every source at $k$ satisfies $\mathcal{G}_{k}[\mathcal{T} - \tfrac12\,\id\,\tr\mathcal{T}] = \tfrac12\,Q(k)\,\mathcal{T}$. For $Q(k) \neq 0$ the kernel of $\mathcal{G}_{k}$ on symmetric maps is the four-dimensional space of displacements, so the first-order field of a source is $h = \lambda\,(\mathcal{T} - \tfrac12\,\id\,\tr\mathcal{T})/Q(k)$ up to a displacement, with one constant $\lambda$: there is no solution without source, and nothing to choose between retarded, advanced, symmetric or time-ordered inverses. For $Q(k) = 0$ the kernel has dimension six: two directions beyond the displacements are not fixed by the source.
\item[(ii)] \emph{(The bilinear and its normalisation; proved given (OS).)} The first-order interaction of two sources at $k$, $Q(k) \neq 0$, is $8\pi G\,B(\mathcal{T}_{1}, \mathcal{T}_{2})/Q(k)$. For two bodies at rest, $\mathcal{T}_{i}(a) = m_{i}(a \cdot e_{0})e_{0}$, one has $B = \tfrac12 m_{1}m_{2}$ and $Q(k) = -|\mathbf{k}|^{2}$, and the interaction is $-4\pi G m_{1}m_{2}/|\mathbf{k}|^{2}$, the transform of $-G m_{1}m_{2}/r$: the stored Newtonian coupling fixes the constant. The transition amplitude between a pair of total momentum $k$, $Q(k) = s > 0$, and another pair is $|\mathcal{M}| = 8\pi G\,|B|/s$.
\item[(iii)] \emph{(Pair sources; computed.)} For incoming momenta $p_{1}, p_{2}$ and outgoing $p_{3}, p_{4}$, all null, with $t = Q(p_{1} - p_{3})$, $u = Q(p_{1} - p_{4})$, $s + t + u = 0$: a pair of quanta of a real scalar field with curvature coupling $\xi$ has the source $\mathcal{T}(a) = -(a \cdot p_{2})p_{1} - (a \cdot p_{1})p_{2} + (p_{1} \cdot p_{2})a + 2\xi\bigl((a \cdot k)k - Q(k)a\bigr)$, of trace $(1 - 6\xi)s$; a pair of quanta of a vector field with field bivectors $F_{i} = p_{i} \wedge \epsilon_{i}$ has $\mathcal{T}(a) = -\tfrac12(F_{1}aF_{2} + F_{2}aF_{1})$ (Fact \claimref{synthesis.imported-maxwell-stress-spacetime-algebra}), trace-free; a particle and antiparticle of one massless chiral fermion have $\mathcal{T}(a) = \tfrac14\bigl(j\,(a \cdot d) + d\,(a \cdot j)\bigr)$, $d = p_{1} - p_{2}$, with $j$ the pair's transition current, whose spin sum against real vectors $w$ is $2\br{p_{2}wp_{1}w}_{0}$ (half the sum of Theorem \claimref{synthesis.electron-positron-to-muon-pairs-in-the-spacetime-algebra-lsz-tree-cross-section-and-one-loop-unitarity}(1) at zero mass). Then, summed over polarisations, $B^{2} = t^{2}u^{2}$ for scalars to scalars at $\xi = 0$, $2t^{2}u^{2}$ for vectors to scalars and $\tfrac14(t - u)^{2}tu$ for the fermion pair to scalars; in the centre-of-mass frame the scalar bracket is $\tfrac{s^{2}}{4}(\cos^{2}\theta - \tfrac13) - \tfrac{s^{2}}{6}(1 - 6\xi_{1})(1 - 6\xi_{2})$, a spin-two part and a trace part.
\item[(iv)] \emph{(The channels factorise; computed.)} Let $W_{ij}$ be the integral over the sphere of $\sum B^{2}/s^{4}$ from a pair of species $i$ to a pair of species $j$, with a factor $\tfrac12$ for each pair of identical quanta. For real scalars, chiral fermions and real massless vectors, in all nine channels,
\[
W_{ij} \;=\; \frac{\pi}{180}\bigl(c_{i}c_{j} + 5\,\tau_{i}\tau_{j}\bigr), \qquad c = 1,\ 3,\ 12, \qquad \tau = (1 - 6\xi)^{2} \text{ for a scalar and } 0 \text{ otherwise.}
\]
\item[(v)] \emph{(The rate; proved given (OS) and the standard rate formula.)} In a bath at temperature $T$ of $N_{s}$ real scalars of trace weights $\tau_{i}$, $N_{w}$ chiral fermions and $N_{v}$ vectors, all free and massless at this order, with zero chemical potentials, pairs of a species $j$ absent from the bath are created at the rate per volume
\[
\Gamma_{j} \;=\; \alpha_{j}\,\frac{T^{8}}{\bar{M}_{P}^{4}}, \qquad
\alpha_{j} \;=\; \frac{\pi^{3}}{17280}\left[\frac{c_{j}(N_{s} + 12N_{v}) + 5\tau_{j}\sum_{i}\tau_{i}}{225} + \frac{49\,c_{j}\,N_{w}}{4800}\right],
\]
$\Gamma_{j}$ counting creation events, each of two quanta; tree level, no thermal masses, no occupation of the produced species. For the Standard Model's content $(N_{s}, N_{w}, N_{v}) = (4, 45, 12)$ with $\xi = 0$: $\alpha = 5789\pi^{3}/82944000 \approx 2.16 \times 10^{-3}$ for a real scalar, $16087\pi^{3}/82944000 \approx 6.01 \times 10^{-3}$ for a chiral fermion (twice that for a Dirac fermion), $16087\pi^{3}/20736000 \approx 2.41 \times 10^{-2}$ for a real massless vector, and $1519247\pi^{3}/82944000 \approx 0.568$ in total for a copy of that content. The value does not depend on the inverse chosen in (i): the integrand is bounded and $s = 0$ only where the incoming momenta are parallel, a set of measure zero.
\item[(vi)] \emph{(Against the published values.)} With each of the $45$ fermions given the weight $6$ of a Dirac fermion in place of $3$, the formula gives $3997\pi^{3}/41472000$ for a scalar and $11351\pi^{3}/20736000$ for a Dirac fermion, the values of arXiv:2112.15214 (its equations (86) and (90), with the coupling $-h_{\mu\nu}T^{\mu\nu}/\bar{M}_{P}$ of a canonically normalised field). The value stored in Fact \claimref{dark-matter.imported-massless-graviton-production-rate}, $3997\pi^{3}/663552000$ from \cite{Bernal2018}, is one sixteenth of the first: its source writes the coupling as $h_{\mu\nu}T^{\mu\nu}/(2\bar{M}_{P})$ with the propagator of a canonically normalised field, and its squared amplitudes are one sixteenth of the canonical ones: a factor two in the coupling is a factor sixteen in the rate. The normalisation of (ii), fixed by Newton's law, is the later one. So the stored scalar coefficient is low by $46312/3997 \approx 11.6$ against (v): sixteen from the coupling, $5789/7994$ from the fermion weight.
\item[(vii)] \emph{(The mean-field source gives no such rate; argued, standard.)} If instead the field is sourced by the expectation value of the bath's stress map, it is the homogeneous isotropic field of the expanding bath, Weyl-flat, and chiral fermions, vectors and conformally coupled scalars in their conformal vacuum stay in it (Fact \claimref{synthesis.imported-conformal-covariance-of-massless-fields-and-local-conformal-flatness}); a scalar with $\xi \neq \tfrac16$ is created only through the scalar curvature, which vanishes for a bath of trace-free stress. No pairs are created at order $G^{2}T^{8}$, up to terms suppressed by the trace of the bath's stress and by the expansion rate over the temperature.
\end{enumerate}
\emph{Reading.} The rate the store imports from a calculation with a quantum of a spin-two field is, at this order, a process between matter and matter: it needs the operator source and uses no state of the gauge field, because the exchange is at $Q(k) = s > 0$, where by (i) the field has no freedom. It is the same whether or not the field has a free part at null momentum, which this rate does not probe; the standard calculation with a quantised field gives the same tree rate. Only the mean-field source changes it. So the correction of the stored coefficient in (vi) does not depend on (OS): it holds on the standard account as well. With (OS), the dark towers' gravitational heating stands with larger coefficients: the temperature floors, which go as $\alpha^{1/4}$, rise by a factor between $1.6$ and $1.8$, and the yields, which go as $\alpha$, by a factor between $7$ and $11$, on the stored brackets. With the mean-field source there is no floor at all. The scalar coefficients depend on the curvature couplings through $\tau$, the datum of the stored reading $\xi = 0$.

## technical
Assume (OS): at first order in $G$ the gauge field is the linearised solution of the frame equation sourced by the matter's stress map as an element of the matter algebra, with no state of its own. Then:

(i) At momentum $k$ with $Q(k) \neq 0$ the linearised field is fixed by a conserved source up to a displacement, $h \propto (\mathcal{T} - \tfrac12\id\tr\mathcal{T})/Q(k)$; at null $k$ two more directions are free.

(ii) Two sources interact through $8\pi G\,B/Q(k)$, $B = \ip{\mathcal{T}_{1}}{\mathcal{T}_{2}} - \tfrac12\tr\mathcal{T}_{1}\tr\mathcal{T}_{2}$; the constant is fixed by the stored Newtonian coupling ($B = \tfrac12 m_{1}m_{2}$ at rest).

(iii), (iv) For pairs of massless quanta the angular integral of $\sum B^{2}$, with the identical-quanta factors, is $(\pi/180)\,s^{4}(c_{i}c_{j} + 5\tau_{i}\tau_{j})$ with $c = 1, 3, 12$ for a real scalar, a chiral fermion and a real vector, and $\tau = (1 - 6\xi)^{2}$ on scalars.

(v) From a thermal bath, $\Gamma_{j} = \alpha_{j}T^{8}/\bar{M}_{P}^{4}$ with the closed form above; for the Standard Model's content $\alpha = 5789\pi^{3}/82944000$ for a scalar.

(vi) The stored coefficient $3997\pi^{3}/663552000$ is one sixteenth of the later published $3997\pi^{3}/41472000$ (a factor two in the coupling; the later normalisation is the one that gives Newton's law), and both give the $45$ chiral fermions the weight of Dirac fermions.

(vii) A mean-field source gives no production at this order in a bath of trace-free stress.

Ledger: transport-absent. This is linearised gravity at tree level; the series contributes the reading (operator source, no quantum of the field needed at $Q(k) \neq 0$) and the normalisation by its own Newtonian coupling.

## lay
The series treats gravity as a classical field and holds no graviton. One of its imported numbers, the rate at which hot ordinary matter creates particles of a hidden sector through gravity alone, came from a calculation that exchanges a graviton, so it was flagged as not belonging to the series.

This result shows the rate does not need a graviton. If the gravitational field is fixed by the matter that sources it, as the series already assumes when it predicts that gravity entangles two masses, then two particles of ordinary matter can turn into two hidden particles through that field, and the rate comes out with the familiar law (temperature to the eighth power over the Planck mass to the fourth). The reason is that in this process the field is never free to travel on its own: it is forced, at every moment, by its source.

Doing the calculation from scratch, with the strength of gravity fixed by Newton's law, also shows that the number the series had imported is too small. The paper it came from used half the correct coupling, which makes the rate sixteen times too small, a normalisation its authors' later paper uses correctly; and both papers count each of the Standard Model's fermions twice. The corrected rate is about eleven times the stored one for a hidden scalar. The series' conclusions that gravity warms the hidden sectors without filling them survive, with larger numbers.

If instead gravity were sourced only by the average of the matter, there would be no such production at all.

## one-liner
Assuming the operator source (OS) at first order, the plasma creates pairs of a gravitationally coupled species at $\Gamma = \alpha T^{8}/\bar{M}_{P}^{4}$ with no quantum of the gauge field, since at $Q(k) = s > 0$ the field is fixed by its source; channels factorise as $(\pi/180)(c_{i}c_{j} + 5\tau_{i}\tau_{j})$, $c = 1, 3, 12$, giving $\alpha = 5789\pi^{3}/82944000$ for a scalar from the Standard Model's content, about $11.6$ times the stored coefficient (sixteen from a factor two in the source's coupling, the rest from counting chiral fermions as Dirac); a mean-field source gives no such rate.
