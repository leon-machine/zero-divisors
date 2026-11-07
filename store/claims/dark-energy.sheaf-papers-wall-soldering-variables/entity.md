---
id: dark-energy.sheaf-papers-wall-soldering-variables
kind: claim
version: 9
title: The sheaf paper's wall in soldering variables
status: proved
region: dark-energy
subject: walls
tags: [degenerate-algebras, hyperbolic-plane, rotors-and-stabilisers]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T10, deposited version
- name: Claude Opus 5.5
  role: 'GA rewrite (coframe and metric components)'
  version: 9
  source: maintainer pass 2026-11-07 (consistency)
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - dark-energy.stelle-west-vector-frozen-point@5
  - dark-energy.walls-free-sector@5
  - sheaf.metrics-residue-square-root-twist@5
  - sheaf.localised-transport@5
  assumes:
  - sheaf.tameness@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T10.py
  tags:
  - label:prop:whichwall
- kind: check
  ref: check.py::check_soldering_form_acquires_half_power_pole
- kind: check
  ref: check.py::check_weighted_chart_and_seven_dim_stabiliser
- kind: check
  ref: check.py::check_dilation_lifts_to_ladder_boost
- kind: check
  ref: check.py::check_dichotomy_cases_through_the_free_sector
locators:
  paper: T10
  number: Prop 4.5
  label: prop:whichwall
  line: 844
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The coframe condition is written Q(hb^{-1}(v)) = G^{-1}(v,v) for the physical-vector map, with the coframe e^a and eta_{ab} as a labelled component reading; the internal cometric is the form eta(tau) on internal covectors with its Gram matrix diag(0, eta_3); the proof writes eta_{ab} e^a(r) e^b(r) as Q(hb^{-1}(r)) (the same scalar) and g_{mu nu} as the derived metric g; the stabiliser algebra {A : A eta + eta A^T = 0} and its block matrices stay, being the dimension count the result is about; notation only.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the simple pole of G^{-1} (half-power coframe), the weighted chart and 7-dimensional stabiliser, the 8-dimensional ambient lift and ladder boost, and the two computable cases of (iv). Version 7 -> 8.'
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Tractor wording completed by the lead: the tractor chart and the datum (nabla, I, V) are those of the Cl(2,4) tractor gauge field of the gravitational field, whose soldering part is hb^{-1}(a); at the sheaf wall hb^{-1} has a half-power pole, so the soldering summand of Omega_T is singular there. Content unchanged.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: proposition
  context_refs:
  - dark-energy.forcing-half-schwarzschild-wall-residue-sense
  - dark-energy.frozen-point-datum-kasner-wall
  - dark-energy.frozen-point-makes-stelle-west-vector
  - sheaf.degeneration-sheaf
  - sheaf.localised-transport
  outside_pilot_cites:
  - ButlerT4
  typing:
    by: ai-typing-pass
    added:
    - sheaf.localised-transport
    note: 'Added the localised-transport corollary because items (ii) and (iii) use its Witt partner,
      as the Level line says; the Kasner-wall datum and the forcing assembly cited in (iv) are later results
      reported for context and were not added. Levels pass: all three levels now name the tameness hypothesis
      the wall is assumed to satisfy.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - sheaf.localised-transport
    - sheaf.tameness
    note: Tameness cited where the corank-one form of the Gram at the wall is used.
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the cometric is the derived cometric of the gravitational field, G(a,b) = hb^T(a).hb^T(b); the soldering form (coframe) is the physical-vector map hb^{-1}; the frame map R^{1,3} -> TM is hb, so (i) reads: at the sheaf wall hb^{-1} acquires a half-power pole and hb itself drops rank; the Lorentz algebra is the rotation-gauge algebra of the invertible region. Statements, dimensions and cases unchanged; tractor wording in (iv) left to the lead. Proof: one opening sentence pointing to the GTG dictionary Fact.'
---

## formal
Let $\Sigma$ be a tame corank-one wall of the sheaf paper \cite[Hyp.~2.1, Thm.~3.1]{ButlerT4} for a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}): its derived cometric $G$, $G(a,b) = \hb^{T}(a) \cdot \hb^{T}(b)$ on covectors (in components $g^{\mu\nu} = g^\mu \cdot g^\nu$), has a one-dimensional radical $\mathcal{L}$ spanned by a covector $k$, with transversality datum $\delta$, and the derived metric has the residue $\lim_{\tau\to 0}\tau\, G^{-1} = k\otimes k/T$ of \cite[Thm.~6.2]{ButlerT4}, $T \neq 0$. Then:
\begin{enumerate}
\item[(i)] \emph{(Not a wall of the soldering form.)} Any physical-vector map $\hb^{-1}$ with $Q(\hb^{-1}(v)) = G^{-1}(v,v)$ (the soldering form, up to rotation gauge; in components a coframe $e^a(v) = \gamma^a \cdot \hb^{-1}(v)$ with $\eta_{ab}e^a e^b = G^{-1}$) has a component of order $\tau^{-1/2}$ along $k$: the soldering form $\hb^{-1}$ does not acquire a radical at $\Sigma$, it acquires a half-power pole, and it is the frame, the map $\hb : \mathbb{R}^{1,3} \to TM$ from physical to background vectors, that degenerates. Theorem \claimref{dark-energy.walls-free-sector} does not apply to $\Sigma$ in the physical chart.
\item[(ii)] \emph{(The weighted chart.)} In the sheaf paper's weighted module, where $k$ is rescaled to a regular section, the coframe is regular and of full rank and it is the internal cometric of the frame, the form $\eta(\tau)$ on the internal covectors with $\eta(\tau)(\gamma^a, \gamma^b) = G(e^a, e^b)$, that acquires the radical: its Gram matrix is $\eta(0) = \mathrm{diag}(0, \eta_3)$ with $\eta_3$ the nondegenerate form of the three surviving directions. The Lie algebra of frame transformations compatible with the degenerate internal cometric, $\{A \in \mathfrak{gl}(4) : A\eta + \eta A^{\mathsf T} = 0\}$, has dimension seven: the three-dimensional orthogonal algebra of the surviving directions, the three null rotations $m_i \mapsto m_i + v_i k$, and the dilation of the dying line $k \mapsto \alpha k$. Compared with the six-dimensional Lorentz algebra of rotation gauge on the invertible region, the wall opens exactly one new gauge generator per point, the dilation of $\mathcal{L}$.
\item[(iii)] \emph{(The dilation is the ladder pair's boost.)} In the ambient fibre $\mathbb{R}^{2,4}$ of the completion, with the four-plane $\mathcal{P} = T^*_x M$ carrying the degenerate form, the radical $k \in \mathcal{P}$, and the Witt partner $k^*$ of \cite[Cor.~4.5]{ButlerT4} ($\ip{k}{k^*} = 1$, $k^*$ null, $k^* \perp \mathcal{P}$ except for $k$), the subalgebra of $\mathfrak{so}(2,4)$ preserving $\mathcal{P}$ has dimension eight and restricts onto the full seven-dimensional algebra of (ii). The dilation of $\mathcal{L}$ lifts to the element $k \mapsto \alpha k$, $k^* \mapsto -\alpha k^*$, fixing the surviving directions: the $\mathfrak{so}(1,1)$ boost of the ladder plane $\mathrm{span}(k, k^*)$, which is the rescaling $k \mapsto ck$, $k^* \mapsto k^*/c$ that the sheaf paper's residue theorem identifies as the freedom of the partner line. The one gauge generator the wall opens is the one-parameter group of the ladder pair.
\item[(iv)] \emph{(Dichotomy for the dynamics.)} Wherever the MacDowell-Mansouri datum of Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector} is regular and its soldering form $e = \nabla V$ has full rank, the Einstein-Cartan equations have full rank (Theorem \claimref{dark-energy.walls-free-sector}(a) on the invertible region): nothing is vacated. Wherever $e$ is regular of corank one, Theorem \claimref{dark-energy.walls-free-sector} applies and the free sector is the symmetric form $M$. At the sheaf paper's wall, in the tractor chart (the splitting of the $\Cl(2,4)$ tractor gauge field $\Omega_{T}(a) = \Omega(a) - \nInf\wedge\hb^{-1}(a) + \nO\wedge\Sch(\hb^{-1}(a))$ of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}, whose soldering summand is $\hb^{-1}(a)$) $e$ has a pole and neither case applies; in the sheaf paper's own ambient chart the question is whether the datum $(\nabla, I, V)$, $V = X - (3/\Lambda)I$, extends regularly across $\Sigma$ with $\nabla X$ of full rank, which is the interface the sheaf paper itself flags in its tractor dictionary and poses among its successor problems \cite[\S 7.3-7.4]{ButlerT4}. For the Schwarzschild wall the answer is now known, and it is the second of the two answers just named, in a precise form: the datum has a simple pole whose residues are the completion's weights (Proposition \claimref{dark-energy.frozen-point-datum-kasner-wall}, Assembly \claimref{dark-energy.forcing-half-schwarzschild-wall-residue-sense}).
\end{enumerate}
\emph{Level:} (i)-(iii) proved, on the imported residue theorem and Witt partner; (iv) is a statement of cases, each case proved, with the case that obtains at the sheaf paper's wall open.

## technical
Under the sheaf paper's tameness hypothesis, let $\Sigma$ be a tame corank-one wall of the derived cometric $G(a,b) = \hb^T(a) \cdot \hb^T(b)$ of a gravitational field on flat spacetime, with radical spanned by a covector $k$ and residue $\lim_{\tau\to 0}\tau\,G^{-1} = k\otimes k/T$, $T \neq 0$. Any physical-vector map $\hb^{-1}$ with $Q(\hb^{-1}(v)) = G^{-1}(v,v)$ (a coframe in components) then has a component of order $\tau^{-1/2}$ along $k$: the soldering form $\hb^{-1}$ acquires a half-power pole rather than a radical, it is the frame map $\hb : \R^{1,3} \to TM$ that degenerates, and the free-sector theorem for a soldering form of corank one does not apply in the physical chart. In the weighted chart the coframe is regular of full rank and it is the internal cometric that acquires the radical, with Gram matrix $\eta(0) = \mathrm{diag}(0,\eta_3)$; its algebra $\{A : A\eta + \eta A^{\mathsf T} = 0\}$ is seven-dimensional (three rotations, three null rotations and the dilation $k \mapsto \alpha k$), one more than the Lorentz algebra.

In the ambient fibre $\R^{2,4}$, with the Witt partner normalised by $\ip{k}{k^*} = 1$, the subalgebra of $\so(2,4)$ preserving the four-plane of covectors is eight-dimensional and restricts onto that seven-dimensional algebra, and the dilation lifts to the boost $k \mapsto \alpha k$, $k^* \mapsto -\alpha k^*$ of the ladder plane $\mathrm{span}(k, k^*)$. For the Einstein-Cartan dynamics there are three cases: a full-rank soldering form vacates nothing, a regular corank-one form has the symmetric free sector, and at this wall the tractor-chart soldering form has a pole so neither applies. Whether the datum extends regularly in the ambient chart is open in general; at the Schwarzschild wall it has a simple pole whose residues are the completion's weights.

## lay
A gravitational field can degenerate at a wall in two different ways: the ruler for directions can lose a dimension, or the ruler for gradients can. Assuming the walls are tame (the sheaf paper's tameness hypothesis), this result shows that the walls of the Clifford-sheaf theory are of the second kind, so the analysis of the first kind does not apply to them directly. At such a wall exactly one new symmetry appears, a stretching of the dying direction, and it is the same as the boost relating the dying direction to its partner in the completion.

## one-liner
Under the tameness hypothesis, at a corank-one cometric wall the soldering form acquires a half-power pole rather than a radical, the wall opens exactly one new gauge generator, the dilation of the dying line, and this generator lifts to the boost of the ladder plane $\mathrm{span}(k, k^*)$.
