---
id: synthesis.position-vector-eigenbundle-in-codimension-three-has-a-class-of-order-two
kind: claim
version: 1
title: 'The position vector in codimension three: an eigenbundle class of order two'
status: proved
region: synthesis
subject: walls
tags: [degenerate-algebras, obstruction-types, no-go, classification]
proposed_by:
  kind: ai
  session: 2026-11-18-leads
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-18-leads
review: draft
derivations:
- name: main
  uses:
  - synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump@1
  - std-algebra.spin-double-cover@1
  - std-algebra.periodicity@2
  - primer.centre@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_least_module_and_symmetric_generators
- kind: check
  ref: check.py::check_hemisphere_frames_of_the_positive_eigenbundle
- kind: check
  ref: check.py::check_clutching_function_is_one_full_turn
- kind: check
  ref: check.py::check_rotor_lift_of_the_full_turn_ends_at_minus_one
- kind: check
  ref: check.py::check_two_copies_carry_a_fourth_generator
- kind: check
  ref: check.py::check_no_fourth_generator_on_the_least_module
- kind: check
  ref: check.py::check_elements_commuting_or_anticommuting_with_every_vector
lineage:
  motivated_by:
  - synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump
  - transport.obstructions-are-moved-never-destroyed
extraction:
  note: >-
    First attack item of the problem. The stored result proves the obstruction for the position vector on least
    modules for m = 1 and m = 2 and cites the rest; this adds m = 3 with a proof in the store's own terms: the
    clutching function of the positive eigenbundle is one full turn, its lift to rotors ends at -1, and a bundle
    that becomes trivial after adding directions would have a contractible clutching loop, whose lift closes.
    No characteristic class is imported; the lifting of a homotopy through the two-sheeted cover of the rotation
    group by the rotors is stated as clause (L) and written out in the proof from the stored double cover, the
    stored centre and compactness, so that other results can cite it. The
    statement that every module of Cl(3,0) with symmetric generators is a sum of copies of the least one is
    standard structure theory and is not used: the clauses are stated for sums of copies. The reading in terms
    of the second Stiefel-Whitney class and of the real K-group of the two-sphere is from memory and is not used.
    Codimension five and beyond are not treated: there the class is of infinite order (classical, from memory;
    the stored result cites only that the degeneration is not removable), and a proof in these terms needs an
    integer invariant of a three-sphere of rotations that the store does not hold.
  open_problem: op.eigenbundle-class-of-degenerations
---

## formal
Let $e_{1}, e_{2}, e_{3}$ be an orthonormal basis generating $\Cl(3,0)$, $p = \tfrac12(1 + e_{3})$, and $S = \Cl(3,0)\,p$, a left ideal of dimension four (a module of least dimension, \claimref{std-algebra.periodicity}), with the positive definite product $\langle \tilde\psi\varphi \rangle_{0}$. For $x = x_{1}e_{1} + x_{2}e_{2} + x_{3}e_{3}$ let $g(x)\psi = x\psi$ and $G_{x}(\psi, \varphi) = \langle \tilde\psi\, x\, \varphi \rangle_{0}$: multiplication by the position vector, the family of clause (8) of Theorem \claimref{synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump} for $m = 3$ on the least module. It is symmetric, $g(x)^{2} = Q(x)$, so it degenerates at the origin only and has signature $(2,2)$ elsewhere. For $k \geq 1$ let $S^{(k)}$ be the orthogonal sum of $k$ copies of $S$ with the same action. Over the unit sphere let $\pi(x) = \tfrac12(1 + x)$ and $G_{+} = \{(x, \psi) : x\psi = \psi\} = \pi(x)S$, the positive eigenbundle, of rank two; $G_{-}$ is defined with $-x$. A bundle is \emph{stably trivial} if its sum with some trivial bundle is trivial. Completions, strict completions and model completions (a fixed exterior form $K_{0}$ on a fixed space $W_{0}$) are those of the cited Theorem.
\begin{enumerate}
\item[(1)] \emph{(Frames and clutching function.)} $n_{1} = \pi(x)\,p$ and $n_{2} = \pi(x)\,e_{1}e_{2}\,p$ are orthogonal of square $\tfrac14(1 + x_{3})$, a frame of $G_{+}$ where $x_{3} > -1$; $s_{1} = \pi(x)\,e_{1}p$ and $s_{2} = \pi(x)\,e_{2}p$ are orthogonal of square $\tfrac14(1 - x_{3})$, a frame where $x_{3} < 1$. On the equator $x = \cos a\,e_{1} + \sin a\,e_{2}$,
\[
s_{1} = \cos a\; n_{1} - \sin a\; n_{2}, \qquad s_{2} = \sin a\; n_{1} + \cos a\; n_{2} :
\]
the second frame is the first turned through the angle of the point, one full turn round the equator.
\item[(2)] \emph{(Rotor lift.)} In the Clifford algebra of the fibre of $G_{+} \oplus \underline{\R}^{N}$, $N \geq 0$, with $f_{1}, f_{2}$ the unit vectors along $n_{1}, n_{2}$, the turn of (1) is $v \mapsto R_{a}v\tilde R_{a}$ with $R_{a} = \cos\tfrac a2 + \sin\tfrac a2\, f_{1}f_{2}$, which fixes the added directions; $R_{0} = 1$ and $R_{2\pi} = -1$. For $S^{(k)}$ the clutching function is the same turn in $k$ orthogonal planes and its rotor, the product of the $k$ plane rotors, ends at $(-1)^{k}$.
\item[(L)] \emph{(Lifting through the double cover.)} The \emph{rotors} of $\Cl(n,0)$ are the even versors of unit vectors, the group $\Spin(n,0) = \Spin^{+}(n,0)$ of Definition \claimref{obj.std-algebra.pin-spin} (in definite signature every unit vector has square one, so $R\tilde R = 1$ for each of them and $\mathrm{SO}^{+} = \mathrm{SO}$). Let $n \geq 1$ and let $\kappa \colon [0,1] \times [0,1] \to \mathrm{SO}(n)$ be continuous with $\kappa(u,0) = \kappa(u,1)$ for every $u$ and $\kappa(1,t)$ independent of $t$: a loop of rotations contracted through loops. Then there is a continuous map $\hat\kappa$ of the square into the rotors with $\hat\kappa(u,t)\,v\,\hat\kappa(u,t)^{\sim} = \kappa(u,t)v$ for all vectors $v$, $\hat\kappa(u,0) = \hat\kappa(u,1)$ for every $u$ and $\hat\kappa(1,t)$ independent of $t$; and every continuous path of rotors over $\kappa(0,\cdot)$ is $\hat\kappa(0,\cdot)$ or $-\hat\kappa(0,\cdot)$, so it is closed.
\item[(3)] \emph{(Not stably trivial.)} For $k$ odd, in particular on the least module, neither eigenbundle of the family on $S^{(k)}$ is stably trivial over the sphere: $G_{\pm} \oplus \underline{\R}^{N}$ is not trivial for any $N \geq 0$.
\item[(4)] \emph{(Completions, $k$ odd.)} Let $U \subset \R^{3}$ be a bounded open set containing the origin. For $k$ odd, no model completion of the family on $S^{(k)}$ standard outside $U$, with any $W_{0}$ and any $K_{0}$, is nondegenerate at every point. Strict completions exist (the double of the cited Theorem); the eigenbundles of their exterior form $K = -G$ are those of $G$ exchanged, so they carry the class, as the transfer clause requires.
\item[(5)] \emph{(Completions, $k$ even.)} Let $p_{4} = \tfrac12(1 + e_{1}e_{2}e_{3}e_{4})$ in $\Cl(4,0)$ and $T = \Cl(4,0)\,p_{4}$, of dimension eight. Under $\Cl(3,0)$, $T = S\,p_{4} \oplus S\,e_{1}p_{4}$, two orthogonal copies of $S$ (each map $s \mapsto s\,p_{4}$, $s \mapsto s\,e_{1}p_{4}$ commutes with left multiplication and halves the product), and left multiplication by $e_{4}$ is a fourth symmetric map of square one anticommuting with $e_{1}, e_{2}, e_{3}$. So on $S^{(2)} \cong T$, and on $S^{(k)}$ for every even $k$, the family $x + \beta e_{4}$, with $\beta$ continuous, positive at the origin and zero outside $U$, is nondegenerate at every point: a model completion with no added direction, and both eigenbundles are trivial over the sphere.
\item[(6)] \emph{(Summary.)} For the position vector of $\R^{3}$ on a sum of $k$ copies of the least module, a model completion standard outside a bounded neighbourhood of the origin and nondegenerate everywhere exists if and only if $k$ is even. The obstruction is the sign $(-1)^{k}$ at which the rotor lift of the clutching function ends. In the group of stable classes of real vector bundles over the two-sphere (bundles up to the addition of trivial bundles, under direct sum) the class of $G_{+}$ on the least module has order exactly two: it is not zero by (3), and twice it is the class of $G_{+}$ on $S^{(2)}$, which is zero by (5). It is a class of degree two: it is not seen on any circle of the sphere, the circle bounding a disc over which $G_{+}$ is trivial. On $S$ itself, (4) with $W_{0} = 0$ rules out every repair on the same module, of whatever form; the computation that no nonzero symmetric map anticommutes with $e_{1}, e_{2}, e_{3}$ shows only the special case that no repair of the form $x + \beta E$ of clause (8) of the cited Theorem exists.
\end{enumerate}
\emph{Reading.} With the cases $m = 1$ and $m = 2$ of the cited Theorem this proves, for the least modules of $\Cl(m,0)$ with $m = 1, 2, 3$, that the degeneration of the position vector at its zero divisor cannot be removed by a completion with a fixed exterior form, and for $m = 3$ that it is removed on exactly the even multiples of the least module. The codimensions $m \equiv 1, 2, 3, 5 \pmod 8$ beyond $m = 3$ remain as cited there (the periodicity theorem of Bott in the form of Atiyah, Bott and Shapiro, from memory, not used here). That the sign of (6) is the second Stiefel-Whitney class of the eigenbundle, and that it is the whole stable class of a bundle over the two-sphere, are classical statements cited from memory and not used.

## technical
For the position vector of $\R^{3}$ acting by left multiplication on $S = \Cl(3,0)\tfrac12(1 + e_{3})$, the least module, and on sums $S^{(k)}$ of $k$ copies:

(1) the positive eigenbundle over the unit sphere is $\pi(x)S$, $\pi(x) = \tfrac12(1 + x)$, with frames $\pi(x)p$, $\pi(x)e_{1}e_{2}p$ away from the south pole and $\pi(x)e_{1}p$, $\pi(x)e_{2}p$ away from the north pole; on the equator the second is the first turned through the angle of the point, one full turn;

(2) the rotor of that turn, $\cos\tfrac a2 + \sin\tfrac a2 f_{1}f_{2}$, runs from $1$ to $-1$, and to $(-1)^{k}$ on $S^{(k)}$, whatever trivial directions are added;

(3) a bundle that becomes trivial after adding directions has a contractible clutching loop of rotations, and a loop of rotations contracted through loops lifts to closed loops of rotors (clause (L), proved from the stored double cover, the stored centre and compactness); so for $k$ odd the eigenbundles are not stably trivial;

(4) hence, by the stored transfer clause, for $k$ odd no completion with a fixed exterior form is nondegenerate everywhere, with any added directions;

(5) for $k$ even the module is a sum of copies of the least module of $\Cl(4,0)$, on which $e_{4}$ repairs the family with no added direction.

A completion with a fixed exterior form exists iff $k$ is even: in the group of stable classes of real vector bundles over the two-sphere, the eigenbundle class of the isolated degeneration in codimension three on the least module has order two, and it is read off as the sign at which the rotor lift ends.

Ledger: transport-convenient. The statement is the classical nontriviality of the generator of the real K-group of the two-sphere (prior art: Atiyah, Bott and Shapiro 1964, from memory), proved here without characteristic classes, by the rotor of the full turn, and read on the series' object: division by a vector fails at the zero divisor $x = 0$, and in three dimensions the failure cannot be repaired by adjoining flat directions with a fixed form, only by doubling the module.

## lay
Multiplying by a position vector can be undone by dividing by it, except at the origin, where the vector is zero. An earlier result asked whether this failure of division at one point can be repaired by enlarging the space the multiplication acts on, in a way that looks the same in every direction far from the point. In one and two dimensions it cannot. In three dimensions the answer was only quoted from the literature.

This result proves it for three dimensions, by a direct computation. On a sphere around the origin the multiplication has a space of vectors that it leaves unchanged, and that space turns as the point moves over the sphere. Comparing its description on the northern and southern halves, one finds that along the equator the two differ by one full turn. A full turn is the motion that returns every vector to itself but reverses the sign of a rotor, the object that generates rotations in the algebra. That sign survives the addition of any number of further fixed directions, and it is what blocks the repair.

Two copies of the multiplication side by side make two full turns, the signs cancel, and the repair exists: it is the multiplication by a vector of four dimensions, restricted to three. So in three dimensions the failure of division at the origin carries a twist that can be cancelled only in pairs.

## one-liner
For the position vector of $\R^{3}$ on $k$ copies of the least module of $\Cl(3,0)$, the clutching function of the positive eigenbundle is one full turn in $k$ planes, its rotor lift ends at $(-1)^{k}$, so for $k$ odd the eigenbundles are not stably trivial and no completion with a fixed exterior form is nondegenerate everywhere, while for $k$ even the fourth generator of $\Cl(4,0)$ repairs the family with no added direction: a class of order two, in the group of stable classes of bundles over the two-sphere, and of degree two.
