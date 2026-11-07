---
id: dark-energy.frozen-point-datum-kasner-wall
kind: claim
version: 8
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
- name: Claude Opus 5.5
  role: GA rewrite (connection, curvature and action densities in GA, forms as labelled readings)
  version: 8
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  uses:
  - dark-energy.cosmological-constant-does-not-change-residue@7
  - dark-energy.frozen-point-makes-stelle-west-vector@7
  - dark-energy.imported-weighted-limit-schwarzschild-singularity-matching@5
  - sheaf.matching-fibre@5
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
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Forms to GA on every level and in the proof: the datum is I = ninf + (Lambda/6) n0, X = n0 with Omega_T(a) = Omega(a) - ninf ^ hb^{-1}(a) + n0 ^ P(hb^{-1}(a)); the pole is Omega(hb(e_i)) = -(p_i/tau) B_i with residue a -> -sum_i p_i (a . e^i) B_i; the double pole is calR(B_i) = p_i(p_i - 1) tau^-2 B_i, calR(e_i ^ e_j) = p_i p_j tau^-2 e_i ^ e_j (store sign); the Ricci map tau^2 calR(e_0) = (sum p^2 - sum p) e_0, tau^2 calR(e_i) = p_i(sum p - 1) e_i; the three action densities are E det(hb)^{-1}, -2 (d_a . calR(a)) det(hb)^{-1} and 24 det(hb)^{-1} with E = 2 <calR(a ^ b) I_4^{-1} calR(I_4 d_b ^ d_a)>; Cartan forms, two-forms and epsilon contractions stay as labelled component readings; the proof solves the torsion equation hb^T(grad ^ f^a) = sum_b e^b ^ (omega(e_b) . e^a) and computes the field strength from Omega. Checked exactly with lib/GA.py (the check module''s Synchronous field) in the maintainer scratch at the check''s Kasner points (2/3, 2/3, -1/3) at tau = 8, 27 and (-2/7, 3/7, 6/7) and the non-Kasner points (1/2, 1/2, 1/2), (2/3, 2/3, 2/3): calR is diagonal with exactly these eigenvalues, the Ricci coefficients are as stated, the GA Euler density equals the check''s eps-eps Gauss-Bonnet sum (-16 p1 p2 p3 tau^-4 at the Kasner points) and the eps e e R sum equals -2 times the store scalar. The Euler form E = 2 <X I^{-1} X(I .)> was checked against the component Euler density on constant-curvature and generic Gauss-type operators in Cl(1,3) and Cl(4,0). Statement unchanged.'
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
Let $(\hb, \Omega)$ be the synchronous diagonal gravitational field on flat spacetime with $\hb^{-1}(e_0) = e_0$, $\hb^{-1}(e_i) = a_i e_i$ on the background frame of the labels $(\tau, x^i)$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}; derived metric, in components, $g = d\tau^2 - \sum_i a_i(\tau)^2(dx^i)^2$), a solution of the Einstein equations with cosmological constant $\Lambda \neq 0$ in the diagonal Bianchi I class of Proposition \claimref{dark-energy.cosmological-constant-does-not-change-residue}, with residue $(p_1,p_2,p_3)$ at $\tau = 0$ and $p_1p_2p_3 \neq 0$ (which excludes exactly the permutations of $(1,0,0)$, the flat Milne point, where every curvature below vanishes and the pole is a coordinate horizon), so that $a_i = \tau^{p_i}(1 + O(\Lambda\tau^2))$ and the Kasner field $a_i = \tau^{p_i}$ (derived metric $d\tau^2 - \sum_i\tau^{2p_i}(dx^i)^2$) is its leading term; the physical frame is $\{e_0, e_i\}$, the unit physical vectors over the background directions $\hb(e_0) = e_0$, $\hb(e_i) = e_i/a_i$ (in components, the orthonormal coframe $e^0 = d\tau$, $e^i = a_i\,dx^i$), and $\omega(e_a) := \Omega(\hb(e_a))$. Let the ambient datum be that of Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}: $I = \nInf + \tfrac{\Lambda}{6}\nO$ and $X = \nO$ (tractor components $(1, 0, \Lambda/6)$ and $(0, 0, 1)$), and $\nabla$ the tractor connection \eqref{eq:conn}, on flat spacetime the $\Cl(2,4)$ gauge field $\Omega_{T}(a) = \Omega(a) - \nInf\wedge\hb^{-1}(a) + \nO\wedge\Sch(\hb^{-1}(a))$ of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}, whose Schouten map is $\Sch(a) = \tfrac{\Lambda}{6}a$ because the field is Einstein. (An exact Kasner metric is Ricci-flat and carries the null frozen point of $\Lambda = 0$. The statements of (i) and (ii) and the Gauss-Bonnet density of (iii) are computed on the leading Kasner term, with $\Lambda$ entering only through the Schouten summand, and hold verbatim for the exact Kasner metric at $\Lambda = 0$, the Schwarzschild exponents included; $\Lambda \neq 0$ is needed only for the statements about the curvature-squared form of the action, which are made on the Einstein family.) Then, in the orthonormal frame, which for the Schwarzschild-de Sitter interior is the sheaf paper's exceptional chart (Fact \claimref{dark-energy.imported-weighted-limit-schwarzschild-singularity-matching} with Proposition \claimref{dark-energy.cosmological-constant-does-not-change-residue}), at leading order in $\tau$:
\begin{enumerate}
\item[(i)] \emph{(What is regular, and what is not.)} $I$ and $X$ are constant, of constant norm $Q(I) = \Lambda/3$, $Q(X) = 0$; the soldering $\Omega_{T}(a)\times X = \hb^{-1}(a)$, on the physical frame $e_a$, is regular of full rank; and the soldering and Schouten summands of $\Omega_{T}$ on the physical frame, $\Omega_{T}(\hb(e_a)) - \omega(e_a) = -\nInf\wedge e_a + \tfrac{\Lambda}{6}\nO\wedge e_a$, are constant (in components, the constant matrices $\eta_{ab}$ and $(\Lambda/6)\eta_{ab}$). The only singular part of the datum is the Levi-Civita block, the rotation-gauge field, and its leading term is a simple pole:
\[
\omega(e_i) \;=\; -\frac{p_i}{\tau}\, B_i, \qquad \omega(e_0) = 0, \qquad B_i = e_0\wedge e_i ,
\]
in the sign of the Definition, $D_a = a \cdot \nabla + \Omega(a) \times$ (in components, a labelled reading: the Cartan forms $\omega^{i0} = (p_i/\tau)\,e^i$, $\omega^{ij} = 0$, which that sign takes to minus the boosts), with residue the bivector-valued linear map $a \mapsto -\sum_i p_i\,(a\cdot e^i)\,B_i$ of physical vectors, which vanishes on $e_0$: its legs are tangential to the wall (in components $-\sum_i p_i\,B_i\otimes \hat e^i$). It is not a gauge pole: its field strength is a double pole,
\[
\mathcal{R}(B_i) \;=\; \frac{p_i(p_i - 1)}{\tau^2}\, B_i, \qquad \mathcal{R}(e_i\wedge e_j) \;=\; \frac{p_i p_j}{\tau^2}\, e_i\wedge e_j \quad (i \neq j),
\]
in the store's sign (in components, the curvature two-forms $R^{i0} = \frac{p_i(p_i - 1)}{\tau^2}\, e^0\wedge e^i$ and $R^{ij} = -\frac{p_i p_j}{\tau^2}\, e^i\wedge e^j$). The datum therefore does not extend regularly across the wall in this chart, and in no chart: the Euler density of (iii) equals $\det(\hb)^{-1}$ times the Kretschmann scalar $2\langle\mathcal{R}(a\wedge b)\,\mathcal{R}(\partial_b\wedge\partial_a)\rangle$ on an Einstein field, because $-4\,\mathcal{R}(\partial_a)\cdot\mathcal{R}(a) + (\partial_a\cdot\mathcal{R}(a))^2 = -16\Lambda^2 + 16\Lambda^2 = 0$, so the Kretschmann scalar is $-16p_1p_2p_3\tau^{-4}$ at leading order, divergent when $p_1p_2p_3 \neq 0$, and a curvature scalar is gauge-invariant.
\item[(ii)] \emph{(The field equations at the wall are conditions on the residue.)} In the store's curvature convention, that of the geometry paper, in which de Sitter has $\mathcal{R}(a) = \Lambda a$ and $\Sch(a) = \tfrac{\Lambda}{6}a$ (the convention that makes $I$ parallel), the Ricci map is diagonal on the physical frame,
\[
\tau^2\,\mathcal{R}(e_0) = \Bigl(\sum_i p_i^2 - \sum_i p_i\Bigr)e_0, \qquad \tau^2\,\mathcal{R}(e_i) = p_i\Bigl(\sum_j p_j - 1\Bigr)e_i
\]
(in components $R_{00} = e_0\cdot\mathcal{R}(e_0)$ and $R_{ii} = e_i\cdot\mathcal{R}(e_i)$, so $\tau^2 R_{ii} = -p_i(\sum_j p_j - 1)$),
so the vacuum equations at leading order are exactly the Kasner relations $\sum_i p_i = 1 = \sum_i p_i^2$; the second says that the residue bivector $-B_w$, with $B_w = \sum_i p_i B_i$, is a unit boost. With $\Lambda$ the Einstein-$\Lambda$ system of Proposition \claimref{dark-energy.cosmological-constant-does-not-change-residue} replaces Ricci-flatness at relative order $\Lambda\tau^2$ and does not affect the residue.
\item[(iii)] \emph{(The action at the wall.)} On the Kasner approach the three terms of Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}(2) have densities, per unit $d\tau\,d^3x$ and with the volume factor $\det(\hb)^{-1} = a_1a_2a_3 = \tau$ at leading order,
\[
E\,\det(\hb)^{-1} = -16\,p_1p_2p_3\;\tau^{-3}, \qquad
-2\,\bigl(\partial_a\cdot\mathcal{R}(a)\bigr)\det(\hb)^{-1} = O(\Lambda\,\tau), \qquad
24\,\det(\hb)^{-1} = 24\,\tau ,
\]
with $E = 2\langle\mathcal{R}(a\wedge b)\,I_4^{-1}\,\mathcal{R}(I_4\partial_b\wedge\partial_a)\rangle$ the Euler density, $I_4 = e_0e_1e_2e_3$ the pseudoscalar (in components, a labelled reading: these are $\epsilon_{abcd}R^{ab}\wedge R^{cd}$, $\epsilon_{abcd}\,e^a e^b R^{cd}$ and $\epsilon_{abcd}\,e^ae^be^ce^d$ against $d\tau\wedge d^3x$). For the Schwarzschild-de Sitter exponents $p_1p_2p_3 = -4/27$ and the first density is $\tfrac{64}{27}\tau^{-3}$ (for Schwarzschild itself, $\Lambda = 0$, this is the divergence of the bare Gauss-Bonnet integrand, $\det(\hb)^{-1}$ times the Kretschmann scalar $64/(27\tau^4)$): the curvature-squared form of the action diverges at the wall as $\tau^{-2}$, through the topological term alone, which is exact and contributes nothing to the field equations; the Einstein-Cartan and cosmological terms are finite. The value of the frozen-point action is not defined at the singularity; its variational principle is, and its equations reach the wall as the residue conditions of (ii).
\end{enumerate}
\emph{Level:} (i)-(iii) proved by the displayed computations on the leading Kasner term, which the script confirms in exact arithmetic at two rational Kasner exponent triples and two non-Kasner points (where the Ricci tensor is confirmed nonzero), with the $\Lambda$-corrections controlled by Proposition \claimref{dark-energy.cosmological-constant-does-not-change-residue}; the script also runs the excluded point $(1,0,0)$ and confirms that every curvature coefficient and the Gauss-Bonnet density vanish there, so the hypothesis $p_1p_2p_3 \neq 0$ is needed. The application to the Schwarzschild and Schwarzschild-de Sitter interiors is through Fact \claimref{dark-energy.imported-weighted-limit-schwarzschild-singularity-matching}; the Kantowski-Sachs sphere adds its own relative corrections, $O(\tau^{1/3})$ in the rotation block and $O(\tau^{2/3})$ in the boost block, which do not reach the residue.

## technical
Take the derived metric of a synchronous diagonal gravitational field on flat spacetime, a Bianchi I Einstein-$\Lambda$ metric with Kasner residue $(p_1,p_2,p_3)$ at $\tau = 0$, $p_1p_2p_3\neq 0$, and the frozen-point datum $I = (1,0,\Lambda/6)$, $X = (0,0,1)$ with its tractor connection. In the orthonormal frame $I$, $X$, the soldering form and the Schouten summand are regular; the only singular part is the Levi-Civita block, the rotation-gauge field, whose leading term on the physical frame is the simple pole $\Omega(\hb(e_i)) = -(p_i/\tau)\,B_i$, $\Omega(\hb(e_0)) = 0$, with residue $a \mapsto -\sum_i p_i\,(a\cdot e^i)\,B_i$ tangential to the wall. Its curvature is a double pole, and the Kretschmann scalar is $-16p_1p_2p_3\tau^{-4}$ at leading order, so the datum extends regularly across the wall in no chart.

At leading order the Ricci map is $\tau^2\mathcal{R}(e_0) = (\sum_ip_i^2 - \sum_ip_i)\,e_0$ and $\tau^2\mathcal{R}(e_i) = p_i(\sum_jp_j - 1)\,e_i$, so the vacuum equations at the wall are exactly the Kasner relations $\sum_ip_i = 1 = \sum_ip_i^2$, the second saying that the residue bivector is a unit boost; $\Lambda$ enters only at relative order $\Lambda\tau^2$. Of the three densities of the curvature-squared action, which exists for $\Lambda \neq 0$, only the topological Gauss-Bonnet term diverges, as $-16p_1p_2p_3\tau^{-3}$, so the action's value is undefined at the wall while its field equations reach it as conditions on the residue. The application to the Schwarzschild interiors goes through the weighted limit.

## lay
Approaching a Kasner-type singularity at which none of the three Kasner exponents vanishes, and working at leading order near the wall, the structure built from the frozen point stays well behaved except for one piece, the part of the connection that describes how the frame turns, which blows up in a simple way that no change of frame removes. The coefficients of that blow-up are the Kasner exponents, and Einstein's equations at the wall become exactly the classic Kasner conditions on them. When the cosmological constant is nonzero, so that the curvature-squared form of the action exists, that action takes an infinite value at the wall, but only through a term that does not affect the equations, so the equations still make sense there.

## one-liner
At a Kasner wall with $p_1p_2p_3\neq 0$, at leading order in $\tau$, the frozen-point datum is regular except for a simple, non-gauge pole of the Levi-Civita block, $\Omega(\hb(e_i)) = -(p_i/\tau)B_i$, with residue $-\sum_ip_iB_i$ on the tangential directions, the field equations become the Kasner relations on that residue, and only the topological term of the curvature-squared action, which needs $\Lambda \neq 0$, diverges.
