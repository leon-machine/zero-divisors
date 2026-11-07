---
id: synthesis.diagonal-kasner-momentum-constraint
kind: claim
version: 4
title: The momentum constraints of the diagonal variable-exponent class
status: proved
region: synthesis
subject: interior
tags: [kasner, curvature-and-field-equations]
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
  role: 'GA rewrite (declared outside_ga (coordinate Ricci computation))'
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'GTG proof: Omega from the torsion equation of the synchronous gauge field, the boost row of the field strength and the mixed Ricci component; cross product written as a dual; Christoffel route kept as a labelled reading'
  version: 4
  source: maintainer pass 2026-11-07 (GTG proofs)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - dark-energy.variable-exponents-residue-pointwise-corrections-are@4
  - sheaf.collision-census@2
  - dark-energy.wall-counterterm@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_momentum_constraint_formula
- kind: check
  ref: check.py::check_tangent_and_collisions
- kind: check
  ref: check.py::check_one_coordinate_fields
- kind: check
  ref: check.py::check_counterterm_scale_factor
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_gtg_rotation_gauge_field_and_mixed_ricci
lineage:
  motivated_by:
  - dark-energy.forcing-half-schwarzschild-wall-residue-sense
extraction:
  maintainer_pass_gtg_proof:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'GTG proof made the main proof: for hb^{-1}(e_tau) = e0, hb^{-1}(e_i) = A_i e_i the torsion equation gives Omega(e_tau) = 0, Omega(e_{x^i}) = -d_tau A_i B_i - sum_j (d_j A_i/A_j) e_i ^ e_j; the boost row calR(e0 ^ e_k) = -A_k^{-1} d_tau Omega(e_{x^k}), the symmetric Ricci map gives e0 . calR(e_i) = sum_{k != i} A_k^{-1} d_tau(d_i A_k/A_i), and R_0i = -g_0 . calR(g_i) reproduces the formula (log tau cancelling on the circle); (i) writes t = (1,1,1) x p as the dual -I3((1,1,1) ^ p) in Cl(3,0); (ii) states the boost block -(p_i/tau) B_i and the slice volume through hb^{-1}; the Christoffel computation is kept as a labelled reading. New check check_gtg_rotation_gauge_field_and_mixed_ricci (exact jets with p exactly on the circle, two values of L; also the dual form of t); runcheck 5/5, check4 clean on a proposals copy. outside_ga removed: no stand-in remains (R_0i are components with their GTG reading). Statement, status, links unchanged.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Declared outside_ga (other) and left as written: the result states the mixed coordinate Ricci components R_{0i} of the derived metric, with their GTG reading R_{0i} = -g_0 . R(g_i) already given, and the proof and its check are a coordinate Christoffel computation of those components; a GTG proof through the rotation-gauge field would be a different derivation, not a rewrite of notation, and is listed for Leon.'
  maintainer_pass_2026_10_22:
    by: ai-maintainer-pass
    note: 'W503: technical and one-liner now state the open-Kasner-circle hypothesis, and the technical level the leading-order qualifier on the counterterm density.'
  open_problem: op.forcing-half-beyond-diagonal
  note: 'Attack route 1 of the open problem, carried out exactly: derived from the definition of the Ricci tensor and machine-checked. Transport-absent and not new: a standard statement of general relativity, applied to the ansatz of the variable-exponents lemma; what it adds to the store is the consequence (i) for that lemma. Context, not a premise: the condition is the diagonal case of the asymptotic momentum constraint of Fournodavlos and Luk, Asymptotically Kasner-like singularities (arXiv:2003.13591, eq. (1.6)), verified by substitution (c_ll = a_l^2, off-diagonal c and kappa zero, kappa_i^i = -p_i, which reduces (1.6) to 2 sum_l (p_l - p_i) d_i b_l - 2 d_i p_i = 0); they construct vacuum solutions for data obeying it with p_1 < p_2 < p_3 < 1; the store holds no import of that theorem. Computed but not claimed: for exponent fields depending on all three coordinates, the system (M) for the scale functions is formally solvable through Taylor degree three at random rational jets (full row rank of the exact linear system for the Taylor coefficients); all orders open.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the metric is the derived metric of a gravitational field (hb, Omega) on flat spacetime; R_0i are the coordinate components of the round-sphere-positive Ricci tensor of the derived metric, R_0i = -g_0 . R(g_i) in the store sign (the sign of the check''s Christoffel formula); Ric = Lambda g becomes R(a) = Lambda a; the connection one-forms are the rotation-gauge field. Formula, (M) and clauses unchanged; check unchanged. Proof: one opening sentence pointing to the GTG dictionary Fact.'
---

## formal
Let $U \subset \R^{3}$ be open and connected, let $p = (p_{1}, p_{2}, p_{3}) \colon U \to \R^{3}$ be smooth with values in the open Kasner circle ($\sum_i p_{i} = 1 = \sum_i p_{i}^{2}$, all $p_{i} < 1$), let $a_{i} = e^{b_{i}} > 0$ be smooth on $U$, and let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose derived metric is
\[
g \;=\; d\tau^{2} - \sum_i a_{i}(x)^{2}\,\tau^{2p_{i}(x)}\,(dx^{i})^{2}, \qquad 0 < \tau < \tau_{0},
\]
the metric of Lemma \claimref{dark-energy.variable-exponents-residue-pointwise-corrections-are} with scale functions $a_{i}$ (the Lemma is the case $a_{i} = 1$). Then, exactly and for every $\tau$, in coordinate components of the Ricci tensor of $g$ in the convention in which the round sphere has positive Ricci curvature, $R_{0i} = -g_0 \cdot \mathcal{R}(g_i)$ with $g_\mu = \hb^{-1}(e_\mu)$, and with no sum on $i$,
\[
\tau\,R_{0i} \;=\; \partial_{i}p_{i} + \sum_{j}(p_{i} - p_{j})\,\partial_{i}b_{j} ,
\]
the terms in $\log\tau$ cancelling identically by the Kasner relations. Hence the $0i$ components of the Einstein condition $\mathcal{R}(a) = \Lambda a$ (for the derived metric $\mathrm{Ric} = \Lambda g$), for any $\Lambda$, hold if and only if
\[
\text{(M)} \qquad \partial_{i}p_{i} \;=\; \sum_{j}(p_{j} - p_{i})\,\partial_{i}b_{j} \qquad (i = 1, 2, 3).
\]
\begin{enumerate}
\item[(i)] \emph{(The Lemma's ansatz.)} With $a_{i} = 1$, (M) holds, that is $R_{0i} = 0$ exactly for the ansatz metric itself, if and only if $p$ is constant on $U$. Equivalently: writing $dp = t \otimes s$ with $t = (p_{3} - p_{2},\, p_{1} - p_{3},\, p_{2} - p_{1})$ the tangent of the circle, (M) at $b = 0$ reads $s_{i}t_{i} = 0$, and $t_{i}$ vanishes on the open circle only at the collision with $p_{j} = p_{k} = \tfrac23$.
\item[(ii)] \emph{(Scale functions restore variable exponents.)} Every $p$ depending on one coordinate, $p = p(x^{1})$, satisfies (M) with $b_{1} = 0$ and $b_{2}, b_{3}$ functions of $x^{1}$ with $\partial_{1}b_{j} = \partial_{1}p_{1}\,(p_{j} - p_{1})/D$, $D = (p_{2} - p_{1})^{2} + (p_{3} - p_{1})^{2} > 0$. For any scale functions the boost block of the rotation-gauge field, the residue and the order bounds of the Lemma hold unchanged: in connection one-forms $\omega^{i0} = (p_{i}/\tau)\,e^{i}$, the residue is the pointwise Kasner boost, and the tangential block, which gains terms in $\partial b$ and factors $1/a_{j}$, is $O(\tau^{-p_{\max}}(1 + |\log\tau|))$; the wall counterterm density of Proposition \claimref{dark-energy.wall-counterterm}(ii) acquires the factor $a_{1}a_{2}a_{3}(x)$, becoming $8\,p_{1}p_{2}p_{3}\,a_{1}a_{2}a_{3}(x)\,\varepsilon^{-2}d^{3}x$ at leading order.
\item[(iii)] In general (M) is a linear first-order system for $b$ whose $i$-th equation differentiates only along $x^{i}$, with coefficient matrix $(p_{j} - p_{i})$ antisymmetric and with a nonzero entry in every row on the open circle.
\end{enumerate}

## technical
The variable-exponents lemma of the action paper computes the orders of the rotation-gauge field and its field strength for a gravitational field on flat spacetime whose derived metric is of Kasner type with exponents that vary from point to point, and leaves the momentum constraints, the mixed time-space components of the field equations, unanalysed. Computed exactly for the lemma's metric with added scale functions $a_{i}(x)$, the mixed components are $\tau R_{0i} = \partial_{i}p_{i} + \sum_{j}(p_{i} - p_{j})\partial_{i}\log a_{j}$: the logarithms of $\tau$ that the variable exponents introduce cancel identically because the exponents stay on the Kasner circle, and $\Lambda$ does not enter. With the lemma's own choice $a_{i} = 1$ the condition is $\partial_{i}p_{i} = 0$ for each $i$, and, provided the exponents stay on the open Kasner circle (all $p_{i} < 1$), this forces the exponents to be constant: for the exact ansatz metric, whose mixed components must vanish exactly, the lemma's variable-exponent class is the constant-exponent class. Genuinely variable exponents need scale functions; with them, for instance for exponents varying along one coordinate, the constraints are solved explicitly, and the lemma's boost block, residue and order bounds survive unchanged, since the scale functions alter only the subleading tangential block; the wall counterterm density picks up the factor $a_{1}a_{2}a_{3}$ at leading order. The result is standard general relativity and is not new: the condition is the diagonal case of the asymptotic momentum constraint of Fournodavlos and Luk (2020), their equation (1.6), as substitution of diagonal data $c_{ll} = a_{l}^{2}$, $\kappa_{i}{}^{i} = -p_{i}$ confirms. What it adds to the store is the consequence for the lemma's ansatz.

## lay
Near a generic singularity the gravitational field is expected to stretch and squeeze lengths at different rates in different directions, rates that may vary from place to place. The action paper studied such varying rates but did not check one family of Einstein's equations, the ones that link time and space. Doing that check shows that the rates can only vary from place to place if the spatial scales vary along with them; in the paper's simplified form, where those scales are held fixed, the rates are forced to be the same everywhere. With varying scales allowed, the paper's main conclusion about the singularity is unaffected.

## one-liner
For the diagonal Kasner ansatz, assuming exponents $p_{i}(x)$ on the open Kasner circle and scale functions $a_{i}(x)$, exactly $\tau R_{0i} = \partial_{i}p_{i} + \sum_{j}(p_{i} - p_{j})\partial_{i}\log a_{j}$; with $a_{i} = 1$ the momentum constraints force constant exponents, while scale functions admit variable ones and leave the residue unchanged.
