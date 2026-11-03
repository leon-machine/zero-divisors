---
id: dark-energy.frozen-point-datum-kasner-wall
kind: claim
version: 7
title: The frozen-point datum at a Kasner wall
status: proved
region: dark-energy
subject: dark-energy
tags: [frozen-point, kasner, curvature-and-field-equations]
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
review: typed
derivations:
- name: main
  uses:
  - dark-energy.cosmological-constant-does-not-change-residue@6
  - dark-energy.frozen-point-makes-stelle-west-vector@5
  - dark-energy.imported-weighted-limit-schwarzschild-singularity-matching@5
  - sheaf.matching-fibre@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T10.py
  tags:
  - label:prop:kasnerwall
- kind: check
  ref: check.py::check_torsion_free_pole_and_regular_datum
- kind: check
  ref: check.py::check_double_pole_curvature_and_residue_equations
- kind: check
  ref: check.py::check_action_densities_at_the_wall
locators:
  paper: T10
  number: Prop 4.9
  label: prop:kasnerwall
  line: 887
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: on the Kasner gauge field (hb, Omega): torsion-free, simple pole with residue -B_w, regular soldering and Schouten, the double-pole curvature and Ricci in the store sign, and the Gauss-Bonnet, Einstein-Cartan and volume densities. Version 4 -> 5. The formal level restated: Fix round 2026-10-23: the Level paragraph''s count corrected to what the script runs (two Kasner exponent triples, two non-Kasner points). Version 5 -> 6. Check maintenance: comparisons over zip now also compare lengths, so a length mismatch cannot pass on a shorter prefix; no change to what is claimed. Version 6 -> 7.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the Bianchi I metric is the derived metric of a synchronous diagonal gravitational field on flat spacetime (hb^{-1}(e_tau) = e_tau, hb^{-1}(e_i) = a_i e_i), the coframe its physical frame, and the tractor connection its Cl(2,4) gauge field; the Levi-Civita block is the rotation-gauge field in the Cartan sign (DICTIONARY C10). Content unchanged. Fix (Leon 2026-10-23, referee GR1): displayed connection values re-signed to the GTG sign of the definition, D_a = a.nabla + Omega(a) x (Cartan forms omega^i_0 = sigma_i theta^i assemble to -sigma_i B_i; Hubble-normalised Kasner model -sum_i p_i B_i, DICTIONARY C10); content unchanged. The Cartan one-forms omega^{i0} = (p_i/tau) e^i are kept as forms; the bivector residue is displayed in the GTG sign.'
  typing:
    by: ai-typing-pass
    added:
    - dark-energy.imported-weighted-limit-schwarzschild-singularity-matching
    note: 'Added the weighted-limit fact, on which the statement''s identification of the frame with the
      exceptional chart and its Schwarzschild application rest; kept the other three premises, all used
      in the hypotheses or proof. Levels pass: the lay level now states the $p_1p_2p_3 \neq 0$ and leading-order
      conditions and that the curvature-squared action needs $\Lambda \neq 0$; the one-liner adds the
      leading-order qualifier and the $\Lambda \neq 0$ condition, and the technical level the $\Lambda
      \neq 0$ condition on the action.'
  env: proposition
  context_refs:
  - dark-energy.imported-weighted-limit-schwarzschild-singularity-matching
  eqrefs: 2
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-energy.imported-weighted-limit-schwarzschild-singularity-matching
---

## formal
Let $g = d\tau^2 - \sum_i a_i(\tau)^2(dx^i)^2$ be the derived metric of the synchronous diagonal gravitational field on flat spacetime with $\hb^{-1}(e_\tau) = e_\tau$, $\hb^{-1}(e_i) = a_i e_i$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), a solution of the Einstein equations with cosmological constant $\Lambda \neq 0$ in the diagonal Bianchi I class of Proposition \claimref{dark-energy.cosmological-constant-does-not-change-residue}, with residue $(p_1,p_2,p_3)$ at $\tau = 0$ and $p_1p_2p_3 \neq 0$ (which excludes exactly the permutations of $(1,0,0)$, the flat Milne point, where every curvature below vanishes and the pole is a coordinate horizon), so that $a_i = \tau^{p_i}(1 + O(\Lambda\tau^2))$ and the Kasner metric $d\tau^2 - \sum_i\tau^{2p_i}(dx^i)^2$ is its leading term; let $e^0 = d\tau$, $e^i = a_i\,dx^i$ be the orthonormal coframe (the physical frame of the field read as one-forms), and let the ambient datum be that of Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}: $I = (1, 0, \Lambda/6)$, $X = (0,0,1)$, and $\nabla$ the tractor connection \eqref{eq:conn} of $g$ (on flat spacetime the $\Cl(2,4)$ gauge field $\Omega_{T}$ of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}), whose Schouten tensor is $P_{ab} = (\Lambda/6)g_{ab}$ because $g$ is Einstein. (An exact Kasner metric is Ricci-flat and carries the null frozen point of $\Lambda = 0$. The statements of (i) and (ii) and the Gauss-Bonnet density of (iii) are computed on the leading Kasner term, with $\Lambda$ entering only through the Schouten summand, and hold verbatim for the exact Kasner metric at $\Lambda = 0$, the Schwarzschild exponents included; $\Lambda \neq 0$ is needed only for the statements about the curvature-squared form of the action, which are made on the Einstein family.) Then, in the orthonormal frame, which for the Schwarzschild-de Sitter interior is the sheaf paper's exceptional chart (Fact \claimref{dark-energy.imported-weighted-limit-schwarzschild-singularity-matching} with Proposition \claimref{dark-energy.cosmological-constant-does-not-change-residue}), at leading order in $\tau$:
\begin{enumerate}
\item[(i)] \emph{(What is regular, and what is not.)} $I$ and $X$ are constant sections of constant norm, the soldering form $\nabla_a X = e_a$ is regular of full rank, and the soldering and Schouten summands of $\nabla$ are the constant matrices $\eta_{ab}$ and $(\Lambda/6)\eta_{ab}$. The only singular part of the datum is the Levi-Civita block, and its leading term is a simple pole:
\[
\omega^{i0} \;=\; \frac{p_i}{\tau}\, e^i, \qquad \omega^{ij} = 0 ,
\]
with residue, read as the rotation-gauge field of the Definition (whose sign, $D_a = a \cdot \nabla + \Omega(a) \times$, takes the Cartan forms $\omega^{i0}$ to minus the boosts), the bivector-valued one-form $-\sum_i p_i\,B_i\otimes \hat e^i$, $B_i = e_0\wedge e_i$, whose legs are tangential to the wall. It is not a gauge pole: its curvature is a double pole,
\[
R^{i0} \;=\; \frac{p_i(p_i - 1)}{\tau^2}\, e^0\wedge e^i, \qquad R^{ij} \;=\; -\frac{p_i p_j}{\tau^2}\, e^i\wedge e^j .
\]
The datum therefore does not extend regularly across the wall in this chart, and in no chart: the Euler density of (iii) equals $\sqrt{|g|}$ times the Kretschmann scalar on an Einstein metric, because $-4R_{ab}R^{ab} + R^2 = -16\Lambda^2 + 16\Lambda^2 = 0$, so the Kretschmann scalar is $-16p_1p_2p_3\tau^{-4}$ at leading order, divergent when $p_1p_2p_3 \neq 0$, and a curvature scalar is chart-independent.
\item[(ii)] \emph{(The field equations at the wall are conditions on the residue.)} In the curvature convention of the geometry paper, in which de Sitter has $\mathrm{Ric}_{ab} = \Lambda g_{ab}$ and $P_{ab} = (\Lambda/6)g_{ab}$ (the convention that makes $I$ parallel), the Ricci tensor in the frame is diagonal with
\[
\tau^2 R_{00} = \sum_i p_i^2 - \sum_i p_i, \qquad \tau^2 R_{ii} = -\,p_i\Bigl(\sum_j p_j - 1\Bigr) ,
\]
so the vacuum equations at leading order are exactly the Kasner relations $\sum_i p_i = 1 = \sum_i p_i^2$; the second says that the residue bivector $-B_w$, with $B_w = \sum_i p_i B_i$, is a unit boost. With $\Lambda$ the Einstein-$\Lambda$ system of Proposition \claimref{dark-energy.cosmological-constant-does-not-change-residue} replaces Ricci-flatness at relative order $\Lambda\tau^2$ and does not affect the residue.
\item[(iii)] \emph{(The action at the wall.)} On the Kasner approach the three terms of Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}(2) have densities
\[
\begin{aligned}
\epsilon_{abcd}R^{ab}\wedge R^{cd} &= -16\,p_1p_2p_3\;\tau^{-3}\, d\tau\wedge d^3x, \\
\epsilon_{abcd}\,e^a e^b R^{cd} &= O(\Lambda\,\tau)\, d\tau\wedge d^3x, \qquad
\epsilon_{abcd}\,e^ae^be^ce^d = 24\,\tau\, d\tau\wedge d^3x .
\end{aligned}
\]
For the Schwarzschild-de Sitter exponents $p_1p_2p_3 = -4/27$ and the first density is $\tfrac{64}{27}\tau^{-3}$ (for Schwarzschild itself, $\Lambda = 0$, this is the divergence of the bare Gauss-Bonnet integrand, $\sqrt{|g|}$ times the Kretschmann scalar $64/(27\tau^4)$): the curvature-squared form of the action diverges at the wall as $\tau^{-2}$, through the topological term alone, which is exact and contributes nothing to the field equations; the Einstein-Cartan and cosmological terms are finite. The value of the frozen-point action is not defined at the singularity; its variational principle is, and its equations reach the wall as the residue conditions of (ii).
\end{enumerate}
\emph{Level:} (i)-(iii) proved by the displayed computations on the leading Kasner term, which the script confirms in exact arithmetic at two rational Kasner exponent triples and two non-Kasner points (where the Ricci tensor is confirmed nonzero), with the $\Lambda$-corrections controlled by Proposition \claimref{dark-energy.cosmological-constant-does-not-change-residue}; the script also runs the excluded point $(1,0,0)$ and confirms that every curvature coefficient and the Gauss-Bonnet density vanish there, so the hypothesis $p_1p_2p_3 \neq 0$ is needed. The application to the Schwarzschild and Schwarzschild-de Sitter interiors is through Fact \claimref{dark-energy.imported-weighted-limit-schwarzschild-singularity-matching}; the Kantowski-Sachs sphere adds its own relative corrections, $O(\tau^{1/3})$ in the rotation block and $O(\tau^{2/3})$ in the boost block, which do not reach the residue.

## technical
Take the derived metric of a synchronous diagonal gravitational field on flat spacetime, a Bianchi I Einstein-$\Lambda$ metric with Kasner residue $(p_1,p_2,p_3)$ at $\tau = 0$, $p_1p_2p_3\neq 0$, and the frozen-point datum $I = (1,0,\Lambda/6)$, $X = (0,0,1)$ with its tractor connection. In the orthonormal frame $I$, $X$, the soldering form and the Schouten summand are regular; the only singular part is the Levi-Civita block, whose leading term is the simple pole $\omega^{i0} = (p_i/\tau)\,e^i$, $\omega^{ij} = 0$, with residue $-\sum_i p_iB_i\otimes\hat e^i$ tangential to the wall. Its curvature is a double pole, and the Kretschmann scalar is $-16p_1p_2p_3\tau^{-4}$ at leading order, so the datum extends regularly across the wall in no chart.

At leading order $\tau^2R_{00} = \sum_ip_i^2 - \sum_ip_i$ and $\tau^2R_{ii} = -p_i(\sum_jp_j - 1)$, so the vacuum equations at the wall are exactly the Kasner relations $\sum_ip_i = 1 = \sum_ip_i^2$, the second saying that the residue bivector is a unit boost; $\Lambda$ enters only at relative order $\Lambda\tau^2$. Of the three densities of the curvature-squared action, which exists for $\Lambda \neq 0$, only the topological Gauss-Bonnet term diverges, as $-16p_1p_2p_3\tau^{-3}$, so the action's value is undefined at the wall while its field equations reach it as conditions on the residue. The application to the Schwarzschild interiors goes through the weighted limit.

## lay
Approaching a Kasner-type singularity at which none of the three Kasner exponents vanishes, and working at leading order near the wall, the structure built from the frozen point stays well behaved except for one piece, the part of the connection that describes how the frame turns, which blows up in a simple way that no change of frame removes. The coefficients of that blow-up are the Kasner exponents, and Einstein's equations at the wall become exactly the classic Kasner conditions on them. When the cosmological constant is nonzero, so that the curvature-squared form of the action exists, that action takes an infinite value at the wall, but only through a term that does not affect the equations, so the equations still make sense there.

## one-liner
At a Kasner wall with $p_1p_2p_3\neq 0$, at leading order in $\tau$, the frozen-point datum is regular except for a simple, non-gauge pole of the Levi-Civita block with residue $-\sum_ip_iB_i\otimes\hat e^i$, the field equations become the Kasner relations on that residue, and only the topological term of the curvature-squared action, which needs $\Lambda \neq 0$, diverges.
