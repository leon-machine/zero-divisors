---
id: synthesis.nondiagonal-kasner-residue-weighted-shear
kind: claim
version: 5
title: The residue in the non-diagonal Kasner class and the weighted shear criterion
status: proved
region: synthesis
subject: interior
tags: [kasner, curvature-and-field-equations]
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
  role: 'GA rewrite (declared outside_ga)'
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'GTG proof: the boost block from the torsion equation on the constant physical frame; Ricci and constraint along gamma_0'
  version: 4
  source: maintainer pass 2026-11-07 (consistency, GTG proofs)
- name: Claude Opus 5.5
  role: 'GTG review (referee F1): torsion-equation citation corrected'
  version: 4
  source: maintainer pass 2026-11-07 (consistency, GTG review)
- name: Claude Opus 5.5
  role: 'formal (i) restated at Leon''s second-round decisions: the e^0-leg of the rotation block with its definite sign'
  version: 5
  source: maintainer pass 2026-11-07 (decisions, second round)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - dark-energy.variable-exponents-residue-pointwise-corrections-are@5
  - synthesis.diagonal-kasner-momentum-constraint@4
  - dark-energy.frozen-point-datum-kasner-wall@8
  - dark-energy.cosmological-constant-does-not-change-residue@7
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_boost_block_identity
- kind: check
  ref: check.py::check_weighted_criterion
- kind: check
  ref: check.py::check_counterexample_rate
- kind: check
  ref: check.py::check_residue_relations_on_kasner_circle
- kind: check
  ref: check.py::check_gtg_torsion_equation_gives_the_boost_block
lineage:
  motivated_by:
  - dark-energy.forcing-half-schwarzschild-wall-residue-sense
extraction:
  maintainer_pass_decisions_2:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5. Leon''s second-round answer 1 (REPORT.md For Leon item 5, fix-F1.md): formal (i) replaces "the e^0-leg of the rotation block is tau^-1 times the antisymmetric part of B (up to the sign convention)" with "the e^0-leg of the rotation block is omega(gamma_0) = tau^-1 sum_{l<m} antisym(B)_lm gamma_l ^ gamma_m in the sign of the Definition, D_a = a . nabla + Omega(a) x", the text proposed in fix-F1.md. Exact check, by a route independent of the engines torsion solver: the Levi-Civita derivative nabla_{E_0} E_m of the orthonormal frame from the Christoffel symbols of g (first derivatives exact, then Fractions at tau = 32 and 1, p = (-1/5, 2/5, 4/5), theta0 = [[1, 0, x2/3], [x3/4, 1, 0], [0, x1/2, 1]] at x = (1/2, 1/3, 1/5), three G with entries above and below the diagonal) equals W x gamma_m for all m with W = tau^-1 sum_{l<m} antisym(B)_lm gamma_l ^ gamma_m, and fails for -W: the sign is the Definitions, D_a = a . nabla + Omega(a) x. check_gtg_torsion_equation_gives_the_boost_block already asserts this value, so no check changes.'
  maintainer_pass_gtg_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Referee F1 fix 9.1 applied (citation): the frame torsion equation is attributed to Definition obj.synthesis.gtg-flat-spacetime-gauge-fields(f), D ^ hb^T(a) = hb^T(grad ^ a) applied to a = f^a, not to Fact synthesis.imported-gtg-dictionary(ii). The referee''s optional formal change (formal (i) could now fix the sign it leaves ''up to the sign convention'') is listed for Leon, not applied. Pins (all notation: GA rewrites with the component form kept as reading, or formal unchanged): dark-energy.variable-exponents-residue-pointwise-corrections-are 4 -> 5, synthesis.diagonal-kasner-momentum-constraint 3 -> 4, dark-energy.frozen-point-datum-kasner-wall 7 -> 8, dark-energy.cosmological-constant-does-not-change-residue 6 -> 7.'
  maintainer_pass_gtg_proof:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Proof rewritten in Gauge Theory Gravity: the field hb^{-1}(e_tau) = gamma_0, hb^{-1}(e_i) = sum_l E_li gamma_l, E = Delta G theta0; the torsion equation hb^T(grad ^ f^a) = sum_b gamma^b ^ (omega(gamma_b) . gamma^a) gives, from its a = 0 part, no boost in omega(gamma_0) and a symmetric boost block, and from the gamma^0-legs of a = l, omega(gamma_m) = -(1/tau) sum_l sym(B)_lm gamma_0 ^ gamma_l + spatial and omega(gamma_0) = (1/tau) antisym(B) (the definite sign of the statement''s ''up to the sign convention''); the second fundamental form as A -> (A . D) gamma_0 = sym(B)/tau in the physical frame; (iv) through gamma_0 . calR(gamma_0) = d_tau tr K + tr K^2 and -2 gamma_0 . calG(gamma_0) = (tr K)^2 - tr K^2 + s R3 in the store sign. Cartan forms and coordinate K kept as labelled readings; (ii), (iii) unchanged (matrices of real components of linear maps). Original proof kept as orig-proof-main.tex. New exact check check_gtg_torsion_equation_gives_the_boost_block (engine-solved rotation-gauge field at tau0 = 1 and 2^7, three shears, x-dependent theta0: boost block, omega(gamma_0), (gamma_m . D) gamma_0; on flat slices the Ricci 00 and constraint identities), which computes the connection identification the coverage judge had listed as argued only. outside_ga withdrawn: no stand-in remains.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Declared outside_ga (other) and left in its language: The result works with connection one-forms omega in a coframe e, the matrix G of the derived metric and the extrinsic-curvature matrix K (traces tr K^2, tr R); the matrix and form computation is the content.'
  open_problem: op.forcing-half-beyond-diagonal
  note: 'Attack route 2 of the open problem (the non-diagonal class, frame rotating as the wall is approached), carried out exactly. Transport-absent and standard in substance: the boost block is the second fundamental form, and the leading Raychaudhuri and Hamiltonian equations give the Kasner relations (textbook general relativity, cited from memory). The weighted admissibility criterion (off-diagonal frame terms weighted by tau^(p_l - p_m), harmless only when triangular in the order of the exponents) is not new: it is the symmetry-wall structure of the Iwasawa-frame analysis of cosmological billiards (Damour, Henneaux and Nicolai 2003; Heinzle, Uggla and Rohr 2009; cited from memory, not checked here). What the entity adds to the store: that criterion stated in the residue sense for the completion''s weights, with exact checks, and the explicit observation that a rotation at rate o(1/tau), even one with a convergent frame, can destroy the simple pole. Context, not a premise: the upper-triangular asymptotic data of Fournodavlos and Luk, Asymptotically Kasner-like singularities (arXiv:2003.13591), have this ordered shape (recalled from memory, not checked here). Not done: the subleading momentum constraints for non-diagonal data, and the condition that the slices'' scalar curvature is subleading, which is assumed in (iv) and not derived; for generic vacuum data with a negative exponent it is expected to fail (BKL bounces, literature from memory), which is why (iv) is stated conditionally. Filed alongside, synthesis.unit-boost-residue-needs-nonpositive-exponent: a unit-boost residue has an exponent <= 0, the case in which the curvature hypothesis of (iv) generically fails.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the Kasner-like metric is the derived metric of a gravitational field on flat spacetime; the Levi-Civita connection is its rotation-gauge field in connection one-forms of the orthonormal coframe (with a note that the matrix Omega of the statement is the coframe''s logarithmic rate, not the rotation-gauge field); Ric = Lambda g becomes R(a) = Lambda a. Clauses (i)-(iv) and the closing paragraph unchanged; check unchanged. Proof: one opening sentence pointing to the GTG dictionary Fact. Check entries synced with check.py: +1, -1 (added check_residue_relations_on_kasner_circle; removed check_residue_field_equations). Version 2 -> 3. check_boost_block_identity strengthened: (tau d_tau E) E^{-1} = B and tau K in the orthonormal frame = sym(B) asserted entrywise at the 12 sample cases; check_residue_field_equations renamed check_residue_relations_on_kasner_circle (it tests the residue relations only); docstrings (a), (d) reworded.'
---

## formal
Let a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) have derived metric $g = d\tau^{2} - \sum_{l}\tau^{2p_{l}}(\theta^{l})^{2}$ on $(0, \tau_{0})\times U$, with real weights $p_{l}$ and a coframe of the slices $\theta = G(\tau, x)\,\theta_{0}(x)$, $G$ smooth and invertible for $\tau > 0$. Write $P = \mathrm{diag}(p_{l})$, $\Delta = \mathrm{diag}(\tau^{p_{l}})$, $\Omega = \tau(\partial_{\tau}G)G^{-1}$ and
\[
B \;=\; P + \Delta\,\Omega\,\Delta^{-1}, \qquad B_{lm} \;=\; p_{l}\,\delta_{lm} + \Omega_{lm}\,\tau^{p_{l} - p_{m}} ,
\]
and use the orthonormal coframe $e^{0} = d\tau$, $e^{l} = \tau^{p_{l}}\theta^{l}$ (here the matrix $\Omega$ is the coframe's logarithmic rate of change, not the rotation-gauge field, which below is written as connection one-forms $\omega$ in this coframe).
\begin{enumerate}
\item[(i)] \emph{(Exact.)} The boost block of the rotation-gauge field (the Levi-Civita connection of $g$) is $\omega^{l0} = \tau^{-1}\,\mathrm{sym}(B)_{lm}\,e^{m}$, the $e^{0}$-leg of the rotation block is $\omega(\gamma_{0}) = \tau^{-1}\sum_{l<m}\mathrm{antisym}(B)_{lm}\,\gamma_{l}\wedge\gamma_{m}$ in the sign of the Definition, $D_{a} = a\cdot\nabla + \Omega(a)\times$, and $\tau K$, with $K$ the mixed second fundamental form of the slices, is similar to $\mathrm{sym}(B)$. For $G = 1$ this is the boost block of Lemma \claimref{dark-energy.variable-exponents-residue-pointwise-corrections-are}.
\item[(ii)] \emph{(Weighted criterion.)} The boost block and the $e^{0}$-leg of the rotation block have at most a simple pole at $\tau = 0$ if and only if $\Delta\Omega\Delta^{-1}$ is bounded, and its residue is the diagonal Kasner boost of the weights, $\omega^{l0} \sim (p_{l}/\tau)e^{l}$, with no rotation residue, if and only if $\Delta\Omega\Delta^{-1} \to 0$, that is $\Omega_{ll} \to 0$ and $\Omega_{lm}\tau^{p_{l} - p_{m}} \to 0$ for $l \neq m$. For distinct weights, a shear at rate up to $1/\tau$ ($\Omega$ bounded) leaves the residue unchanged when it is strictly triangular in the order of the weights ($\Omega_{lm} \neq 0$ only where $p_{l} > p_{m}$). For $G = \exp(c\log\tau\,N)$ with $N$ strictly triangular in some order of the indices, $\Omega = cN$ and $\mathrm{tr}((\tau K)^{2}) = \sum_{l}p_{l}^{2} + \tfrac{c^{2}}{2}\sum_{l \neq m}N_{lm}^{2}\tau^{2(p_{l} - p_{m})}$, which tends to $\sum_{l}p_{l}^{2}$ when $N$ is triangular in the order of the weights and is unbounded when $N$ has an entry against it.
\item[(iii)] \emph{(Rate alone does not decide.)} A coframe that converges, rotating at rate $o(1/\tau)$, can destroy the simple pole: at the Kasner point $(-\tfrac27, \tfrac37, \tfrac67)$, $G = 1 + \tau^{3/7}E_{12}$ tends to the identity, and $\mathrm{tr}((\tau K)^{2}) = 1 + \tfrac{9}{98}\tau^{-4/7}$.
\item[(iv)] \emph{(Forcing, conditionally.)} Suppose the residue $R = \lim_{\tau\to 0}\tau K$ exists with $\tau\partial_{\tau}(\tau K) \to 0$, and assume $\tau^{2}R^{(3)} \to 0$, with $R^{(3)}$ the scalar curvature of the slices. Then the $00$ component of the Einstein condition $\mathcal{R}(a) = \Lambda a$ (for the derived metric $\mathrm{Ric} = \Lambda g$) and the Hamiltonian constraint, at order $\tau^{-2}$, give $\mathrm{tr}\,R = \mathrm{tr}\,R^{2} = (\mathrm{tr}\,R)^{2}$, so for $\mathrm{tr}\,R > 0$ the eigenvalues of $R$ lie on the Kasner circle, for every $\Lambda$; when the shear satisfies the criterion of (ii) they are the weights $p_{l}$.
\end{enumerate}
So, given subleading spatial curvature, the residue-sense forcing of the diagonal class holds for the non-diagonal class exactly when the coframe's shear is weighted-admissible, and the completion's weights read from such a coframe are the residue's eigenvalues. The curvature hypothesis is not generic: a residue on the Kasner circle has an exponent $\leq 0$, and for generic vacuum data with a negative exponent the slices' curvature is expected to grow and produce a bounce (argued, from the billiard literature), so (iv) applies to non-generic data such as velocity-dominated or matter-stabilised approaches. The weighted criterion of (ii) is the symmetry-wall structure of the Iwasawa-frame analysis of cosmological billiards (cited from memory).

## technical
For a gravitational field on flat spacetime whose derived metric is Kasner-like, written in a coframe that may shear or rotate as the singularity is approached, the singular part of the rotation-gauge field is controlled by one matrix: the weights on the diagonal plus the frame's logarithmic rate of change, each off-diagonal entry multiplied by $\tau^{p_{l} - p_{m}}$. The boost block is its symmetric part over $\tau$, exactly. The pole stays simple precisely when the weighted rate stays bounded, and its residue is the diagonal Kasner boost of the weights precisely when the weighted rate tends to zero. A frame may therefore shear at a rate as fast as $1/\tau$ in the direction from a larger to a smaller weight without changing the residue at all, while any shear in the opposite direction must decay like $\tau^{p_{m} - p_{l}}$; convergence of the frame, or a rate below $1/\tau$, does not suffice, and an explicit converging frame at the Kasner point $(-\tfrac27, \tfrac37, \tfrac67)$ makes the curvature invariant $\tau^{2}\mathrm{tr}K^{2}$ diverge like $\tau^{-4/7}$. Assuming the slices' intrinsic curvature is subleading, the leading Raychaudhuri equation and Hamiltonian constraint put the residue's eigenvalues on the Kasner circle, so the diagonal class's forcing statement carries over to every admissible non-diagonal coframe. The content is standard general relativity: the weighted criterion is the symmetry-wall structure of the Iwasawa-frame analysis of cosmological billiards (Damour, Henneaux and Nicolai; Heinzle, Uggla and Rohr; cited from memory). What the store gains is that criterion read in the residue sense, with exact checks, and the observation that a frame rotating at a rate below $1/\tau$ can still destroy the simple pole. The curvature assumption is not generic: for generic vacuum data with a negative exponent it is expected to fail.

## lay
Near some singularities the gravitational field stretches and squeezes lengths at different rates in different directions, and the theory's completion is built from those rates. Earlier work showed that Einstein's equations fix the rates when the stretching directions stay put. This result handles directions that turn as the singularity is approached. It confirms, in the language of the completion, a rule already known from the study of such singularities: a turning that tilts toward the more slowly squeezed direction is harmless, however fast, and leaves the rates exactly as they were, while a turning the other way must die off quickly or it destroys the simple structure altogether, even if it slows down. Assuming the curvature within each slice of space stays small compared with the stretching, which is not the typical case, Einstein's equations then fix the rates exactly as before.

## one-liner
For gravitational fields with Kasner-like derived metric in a shearing coframe, the connection's pole is simple iff the shear rate weighted by $\tau^{p_{l} - p_{m}}$ is bounded and its residue is the weights' Kasner boost iff that weighted rate vanishes; assuming subleading slice curvature (non-generic), the leading field equations then put the weights on the Kasner circle; the criterion is the billiard symmetry-wall structure.
