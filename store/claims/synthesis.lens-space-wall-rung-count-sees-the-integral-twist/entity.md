---
id: synthesis.lens-space-wall-rung-count-sees-the-integral-twist
kind: claim
version: 5
title: 'Lens-space wall: the rung count sees the integral twist'
status: proved
region: synthesis
subject: walls
tags: [degenerate-algebras, tameness, hyperbolic-plane, no-go]
proposed_by:
  kind: ai
  session: 2026-10-31-all-open
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
- name: Claude Opus 5.5
  role: unit resolution, every imaginary unit written as a geometric-algebra pseudoscalar
  version: 4
  source: maintainer pass 2026-11-07 (resolve units)
- name: Claude Opus 5.5
  role: consistency pass, formal now cites the imported Stiefel and Grassmannian Fact its proof uses
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
review: draft
about:
- obj.sheaf.collar-data-coupling
derivations:
- name: main
  uses:
  - synthesis.wall-rung-count-is-height-of-dying-line-class@2
  - synthesis.wall-class-one-rung-obstruction@3
  - sheaf.one-sided-completion@4
  - sheaf.degeneration-sheaf@6
  - sheaf.imported-real-line-bundles@1
  - std-algebra.spin-double-cover@1
  - std-algebra.radical-ideal-and-quotient@2
  - synthesis.imported-stiefel-connectivity-and-grassmannian-classification@1
  assumes:
  - sheaf.tameness@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_adjoint_frame_twisted_by_half_turn
- kind: check
  ref: check.py::check_indefinite_lens_wall_form_has_trivial_negative_bundle
- kind: check
  ref: check.py::check_definite_lens_wall_three_rungs
- kind: check
  ref: check.py::check_torus_comparison_two_rungs_definite
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - sheaf.wall-class
  - synthesis.wall-rung-count-is-height-of-dying-line-class
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: "The closing sentence of the formal level said the classical inputs were cited from memory and not imported, but the derivation uses synthesis.imported-stiefel-connectivity-and-grassmannian-classification and the proof cites it as a Fact; the sentence now names that Fact, and the remark on the complex structure of L + L uses (y1, y2) for fibre coordinates instead of (s, t), t being the cometric parameter. The extraction note above it predates the import."
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle (U1, a plane''s unit bivector): the classical remark, not used in the proof, now writes the complexification of the real line bundle L as L + L with the fibrewise complex structure (s, t) -> (-t, s), the unit bivector of each fibre plane, in place of the realification of L (x) C. No complex field or bare i remains, so the outside_ga declaration (other, for C only) is removed. Version kept at 3, already bumped in this pass.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The quaternion unit of the lens-space action is now the bivector B = e_2e_3 ((z_1, z_2) -> (B z_1, B z_2) on R = z_1 + z_2 e_1e_2, z_j in span{1, B}), and the nowhere-zero section is valued in span{1, B} with phase e^{B phi}; C stays only in the classical remark (not used) that L + L is the realification of the complex line bundle L tensor C, with its first Chern class.'
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'uses edge added to std-algebra.radical-ideal-and-quotient@1, now stored: the closing remark of the proof (why the invariant is a class of the bundle of algebras, not of fibrewise module data) rests on its nilpotent radical ideal and quotient, and now cites it (the theorem''s clauses (1) to (3) do not use it); and to the new Fact synthesis.imported-stiefel-connectivity-and-grassmannian-classification@1, which pins the inputs (S) and (G) of case (1), previously cited from memory. Version 1 -> 2.'
  open_problem: op.wall-class-invariant
  note: >-
    Decides the test case of the open problem. Cross-subject input: the adjoint map of rotors
    (std-algebra.spin-double-cover) is equivariant for the half-turn rotor e2e3, whose square is -1, so it
    gives an explicit global frame of R + L + L over L(4,1) = S^3/Z4. With it the wall form may rotate one
    negative direction of the physical metric into the rungs, which the collar-confined construction of
    the parent claim does not do. Classical inputs cited from memory, not imported: the Stiefel manifold
    V_k(R^m) is (m-k-1)-connected, and the Grassmannian of k-planes in R^m classifies rank-k bundles over
    complexes of dimension below m-k (Milnor and Stasheff; Husemoller); c1 of the complexification of a
    real line bundle is the integral Bockstein of w1 (used only in a remark). Transport-absent: bundle
    algebra of symmetric forms, with the store's wall theory as the only series input.
---

## formal
Let $(M, G)$ be a tame corank-one degeneration (\claimref{sheaf.tameness}) with $\dim M = 4$, compact wall $\Sig \cong L(4,1) = S^{3}/\mathbb{Z}_{4}$, physical side $\Mp$ of signature $(p,q)$, $p \geq 1$, dying line $\shL$ with $x := w_1(\shL) \neq 0$, and $k(\Sig)$ the least number of rungs of a completion in the sense of \claimref{synthesis.wall-rung-count-is-height-of-dying-line-class}. Then $x^{2} = 0$, so $\operatorname{ht}(x) = 2$, and:
\begin{enumerate}
\item \emph{(Indefinite side.)} If $q \geq 1$, then $k(\Sig) = 2 = \operatorname{ht}(x)$: the lower bound of the parent claim is attained, by a completion whose wall form rotates one direction of the physical metric of sign opposite to the dying direction into the rungs.
\item \emph{(Definite side.)} If $q = 0$, then $k(\Sig) = 3 = e(\shL) > \operatorname{ht}(x)$.
\item \emph{(The deciding datum.)} The wall $T^{3}$ with $x \neq 0 = x^{2}$ pulled back from a circle has $k = 2$ with a definite physical side. So two walls with the same mod-2 data ($w(\Sig) = 1$, $x \neq 0 = x^{2}$) and the same signature need different numbers of rungs: in the definite case the rung count is not a function of $W(\Sig) = (w(\Sig), x)$ and the signature; what separates the two walls is whether $\shL \oplus \shL$ is trivial, which on $L(4,1)$ it is not.
\end{enumerate}
Classical inputs, imported as Fact \claimref{synthesis.imported-stiefel-connectivity-and-grassmannian-classification}: $V_{k}(\R^{m})$ is $(m-k-1)$-connected, and $[X, \mathrm{Gr}_{k}(\R^{m})]$ is the set of isomorphism classes of rank-$k$ bundles over a complex $X$ of dimension less than $m - k$.

## technical
The parent claim bounds the rung count of a tame wall between the height of the dying line's class and the least rank of a trivial bundle containing the dying line, and leaves the lens space $L(4,1)$ open: there the class squares to zero, so the lower bound is two, but the doubled dying line is not trivial, so the dying line does not sit in the trivial bundle of rank two that two rungs offer. The key is the adjoint map of rotors. On unit rotors of $\Cl(3,0)$, left multiplication by the half-turn rotor $e_2e_3$, whose square is $-1$, generates the $\mathbb{Z}_4$ with quotient $L(4,1)$, and the frame $R e_a \tilde R$ transforms by $\mathrm{diag}(1,-1,-1)$: its first row is a global section of the trivial line and its other two rows are sections of the dying line, so $\underline{\R} \oplus \shL \oplus \shL$ is trivial with an explicit frame.

When the physical side is indefinite, the wall form takes the hyperbolic partner of the dying line and one further negative direction from the rungs, built with this frame; its negative bundle is then the negative part of the physical metric plus $\shL \oplus \shL$, which the frame identifies with the negative bundle of the standard form. A form with that negative bundle can be joined to the standard form through nondegenerate forms, by the connectivity of Stiefel manifolds, and that join is a two-rung completion. When the physical side is definite there is no direction to borrow: the necessity argument forces $\shL \oplus \shL$ trivial, which fails because an odd map from $S^3$ to the punctured plane would wind by half a turn per quarter turn of the fibre, so three rungs are needed and suffice, the dying line being the second row of the frame inside the trivial bundle of rank three. On a three-torus with the same mod-2 data the doubled dying line is trivial and two rungs suffice even with a definite side, so with a definite side the rung count separates walls the mod-2 classes do not; with an indefinite side it is the mod-2 height on both walls. All of this assumes the tame-wall setting of the parent claim.

## lay
At a wall where the geometry changes signature, extra pairs of directions (rungs) can repair the degeneracy, and an earlier result bounded how many are needed by how the dying direction twists. The open test case was a wall shaped like the lens space $L(4,1)$, where the bounds were two and three. The answer depends on the side we live on. If that side has directions of both signs, as ordinary spacetime does, two rungs suffice: the repair borrows one direction of the opposite sign from the physical geometry and twists it together with the rungs, using the rotation of space by a half turn, whose spinor squares to minus one. If that side is definite there is nothing to borrow and three rungs are needed. A wall shaped like a three-torus with the same simple twist needs only two either way. So when the side we live on is indefinite, the price is set by the simple twist class alone; only when that side is definite is the price set by a finer property of the twist (whether the doubled dying direction can be untwisted, classically an integer-valued class) that the simple twist class does not record.

## one-liner
Assuming the tameness hypotheses, a tame wall with cross-section $L(4,1)$ and twisted dying line needs exactly two rungs when the physical side is indefinite (the lower bound $\operatorname{ht}(w_1\shL)$ is attained, using the adjoint frame of the half-turn rotor) and exactly three when it is definite, while a three-torus wall with the same mod-2 data needs two in both cases.
