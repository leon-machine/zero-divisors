---
id: synthesis.frozen-point-datum-is-h
kind: claim
version: 1
title: The frozen point's datum is H
status: proved
region: synthesis
subject: dark-energy
tags: [frozen-point, cosmological-constant, horizons, null-directions, clifford-classification, rotors-and-stabilisers]
proposed_by:
  kind: ai
  session: 2026-11-08-frozen-point-datum
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-08-frozen-point-datum
review: draft
derivations:
- name: main
  uses:
  - mass.de-sitter-scale-frozen-point@6
  - synthesis.de-sitter-static-boost-frozen-point@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_identities_hold_for_every_lambda
- kind: check
  ref: check.py::check_with_h_every_construction_is_over_the_base_field
- kind: check
  ref: check.py::check_lambda_over_three_must_be_a_square
- kind: check
  ref: check.py::check_the_quadratic_extension_supplies_what_is_missing
- kind: check
  ref: check.py::check_lambda_seven_thirds_sphere_has_no_rational_point
- kind: check
  ref: check.py::check_lambda_six_centres_are_other_quadratic_fields
- kind: check
  ref: check.py::check_similar_to_the_standard_form_iff_sum_of_two_squares
- kind: check
  ref: check.py::check_the_mirror_needs_minus_one_not_a_square
- kind: check
  ref: check.py::check_rescaling_by_root_lambda_needs_root_three
- kind: check
  ref: check.py::check_anti_de_sitter_datum
- kind: check
  ref: check.py::check_operator_join_scale_needs_root_two
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.division-gives-the-rationals
  - synthesis.continuum-completion-premise
  - synthesis.cosmological-horizon-completed-pair
  - odd-extensions.two-towers-one-curved-universe
  - synthesis.mirror-extensions-causal-convention
  - odd-extensions.exceptional-algebra-residue-completion-both-sides
  - dark-matter.imported-frozen-point-de-sitter-radius
  - synthesis.operator-join-point-spectrum-on-positive-energy-modules
extraction:
  open_problem: op.frozen-point-rational-datum
  note: >-
    Settles the mathematical half of op.frozen-point-rational-datum: since the foundation postulates place the
    series' scalars in Q until the completion (synthesis.division-gives-the-rationals,
    synthesis.continuum-completion-premise), a construction that needs a square root of Lambda/3 holds over Q
    only for special Lambda. Leon's decision of 8 November takes H, with Lambda = 3H^2, as the datum; this result
    proves that with H in the base field every frozen-point construction the store makes is defined there, that
    without it each of them fails, and names the constructions that need more than H, each with its own exact
    condition. Pre-registered kill conditions: (K1) a construction listed under "exactly when Lambda/3 is a square"
    that exists over Q for some Lambda with Lambda/3 not a square leaves that list; (K2) a construction that fails
    over K although H is in K falsifies clause (iii). K1 fired for the bifurcation sphere (Lambda = 6 has the
    rational point e1 + e2) and for the stabiliser's identification with SO(1,4) (Lambda/3 = 2 = 1 + 1): both are
    stated in clause (v) with their own conditions, and only the point of the sphere on the observer's radial line
    stays in clause (ii). K2 did not fire. The analysed constructions are those of
    mass.de-sitter-scale-frozen-point, synthesis.de-sitter-static-boost-frozen-point (used),
    synthesis.cosmological-horizon-completed-pair, odd-extensions.two-towers-one-curved-universe(i),
    synthesis.mirror-extensions-causal-convention(v),
    odd-extensions.exceptional-algebra-residue-completion-both-sides(i), dark-matter.imported-frozen-point-de-sitter-radius
    and synthesis.operator-join-point-spectrum-on-positive-energy-modules(2) (cited, not used: the proof needs
    only their definitions, which are restated in the statement). Quadratic extensions in the check are
    span{1, u} with u = f1 f2 a bivector of two extra generators (squares 1 and -delta), central on the blades
    of Cl(2,4), so no imaginary unit is used. Prior art, as background only: the classification of quadratic
    forms and Clifford algebras over fields by discriminant and Hasse invariant, Witt's cancellation theorem
    (the one-dimensional case is proved here with a reflection versor) and Legendre's three-square theorem (not
    used; the case of 7 is proved by descent modulo 8). Ledger: transport-absent (arithmetic of the frozen
    point's square class).
---

## formal
Let $K$ be a field of characteristic $0$, $\Lambda \in K$ with $\Lambda \neq 0$, $d = \Lambda/3$, and $K^{2}$ the set of squares of $K$. Take the vectors of $\Cl_{K}(2,4)$ in the conventions of Lemma \claimref{mass.de-sitter-scale-frozen-point}: $e_{0}$ with $Q(e_{0}) = 1$, $e_{1}, e_{2}, e_{3}$ with $Q(e_{i}) = -1$, null $\nO, \nInf$ with $\ip{\nO}{\nInf} = 1$, all other pairs orthogonal, and $X(x) = \nO + x - \tfrac12 Q(x)\,\nInf$ for $x = \sum_{a} x_{a}e_{a}$. Let $I_{\Lambda} = \nInf + \tfrac{\Lambda}{6}\nO$, $W = \nInf - \tfrac{\Lambda}{6}\nO$, $B_{\Lambda} = e_{0}W$, $\Pi_{\Lambda} = \mathrm{span}\{e_{0}, W\}$ and $S_{\Lambda} = \{x : x_{0} = 0,\ Q(x) = -12/\Lambda\}$: the frozen point, the static boost, its plane and the bifurcation sphere of Proposition \claimref{synthesis.de-sitter-static-boost-frozen-point}. Let $\omega$ be the product of $e_{0}, e_{1}, e_{2}, e_{3}, W$ and $\omega'$ the same product with the form reversed ($Q \mapsto -Q$, the mirror).
\begin{enumerate}
\item[(i)] \emph{(For every $\Lambda$.)} Over $K$: $Q(I_{\Lambda}) = B_{\Lambda}^{2} = -Q(W) = d$, $\ip{W}{I_{\Lambda}} = 0$, $\ip{X(x)}{I_{\Lambda}} = 1 - \Lambda Q(x)/12$; $I_{\Lambda}^{\perp} = \mathrm{span}\{e_{0}, e_{1}, e_{2}, e_{3}, W\}$, an orthogonal basis with squares $\langle 1, -1, -1, -1, -d\rangle$; the map $x \mapsto \tfrac12(B_{\Lambda}x - xB_{\Lambda})$ sends $e_{0} \mapsto -W$, $W \mapsto -d\,e_{0}$ and is zero on $\Pi_{\Lambda}^{\perp}$, so its characteristic polynomial on $\Pi_{\Lambda}$ is $t^{2} - d$; $\omega$ is central in $\Cl_{K}(I_{\Lambda}^{\perp})$ with $\omega^{2} = d$, and $\omega'^{2} = -d$.
\item[(ii)] \emph{(The square class.)} The following are equivalent:
(a) $d \in K^{2}$, that is, $\Lambda = 3H^{2}$ for some $H \in K$;
(b) $\Pi_{\Lambda}$ contains a nonzero null vector;
(c) $\tfrac12(B_{\Lambda}x - xB_{\Lambda}) = t\,x$ for some vector $x \neq 0$ over $K$ and some $t \neq 0$ in $K$ (the null eigen-directions of the static boost);
(d) the line $K B_{\Lambda}$ contains an element $u$ with $u^{2} = 1$ (the unit boost);
(e) the line $K W$ contains a vector $e_{W}$ with $Q(e_{W}) = -1$;
(f) some $R_{h} \in K$ has $R_{h}^{2} = 3/\Lambda$, equivalently some $\kappa \in K$ has $\kappa^{2} = \Lambda/3$;
(g) the observer's radial line $K e_{1}$ meets $S_{\Lambda}$;
(h) $I_{\Lambda}^{\perp}$ is isometric over $K$ to $\langle 1, -1, -1, -1, -1\rangle$;
(i) $\Cl_{K}(I_{\Lambda}^{\perp}) \cong \Cl_{K}(1,4)$, equivalently its centre $\mathrm{span}\{1, \omega\}$ contains an idempotent other than $0$ and $1$ (the doubled type);
(j) the mirror's algebra, the Clifford algebra of $I_{\Lambda}^{\perp}$ with the form reversed, is isomorphic to $\Cl_{K}(4,1)$, equivalently its centre $\mathrm{span}\{1, \omega'\}$ is isomorphic to $\mathrm{span}\{1, \omega_{1}\}$, $\omega_{1}^{2} = -1$, the centre of $\Cl_{K}(4,1)$.
\item[(iii)] \emph{(With $H$.)} If $\Lambda = 3H^{2}$ with $H \in K$, all of (b) to (j) hold, with witnesses rational in $H$: $v = \tfrac12(e_{0} + W/H)$ and $v^{*} = \tfrac12(e_{0} - W/H)$ are null with $vv^{*} + v^{*}v = 1$, $v^{*}v - vv^{*} = u$, $\tfrac12(B_{\Lambda}v - vB_{\Lambda}) = -Hv$ and $\tfrac12(B_{\Lambda}v^{*} - v^{*}B_{\Lambda}) = Hv^{*}$; $u = B_{\Lambda}/H$; $e_{W} = W/H$; $R_{h} = 1/H$ and $\kappa = H$; $x = (2/H)e_{1} \in S_{\Lambda}$, where $\ip{X(x)}{I_{\Lambda}} = 2$ and the areal radius $(2/H)/2$ is $R_{h}$; the orthonormal basis $e_{0}, e_{1}, e_{2}, e_{3}, W/H$ of $I_{\Lambda}^{\perp}$; the central idempotents $\tfrac12(1 \pm \omega/H)$; and the mirror's central unit $\omega'/H$, of square $-1$. So the static boost's unit, its null eigen-directions, the horizon radius and surface gravity, the horizon point of the observer's slice, the isometry type of $I_{\Lambda}^{\perp}$ and the algebra types $\Cl(1,4)$ and $\Cl(4,1)$ are defined over every field of characteristic $0$ that contains $H$, and over $\R$ nothing changes.
\item[(iv)] \emph{(Counterexamples over $\Q$.)} For $\Lambda = 7/3$ ($d = 7/9$) all of (b) to (j) fail, and $S_{\Lambda}$ has no rational point at all. For $\Lambda = 6$ ($d = 2$) all of (b) to (j) fail: the centre of $\Cl_{\Q}(I_{\Lambda}^{\perp})$ is the field $\mathrm{span}\{1, \omega\}$, $\omega^{2} = 2$, and the mirror's is $\mathrm{span}\{1, \omega'\}$, $\omega'^{2} = -2$, the quadratic field of discriminant $-8$, not that of $\Cl_{\Q}(4,1)$, of discriminant $-4$; yet $S_{6}$ has the rational point $e_{1} + e_{2}$, and (v)(b) holds.
\item[(v)] \emph{(Conditions other than $d \in K^{2}$.)}
(a) $S_{\Lambda}$ has a $K$-point if and only if $d$ is a sum of three squares in $K$; this follows from $d \in K^{2}$ and is strictly weaker over $\Q$ ($\Lambda = 6$), and $\Lambda = 7/3$ fails it.
(b) There is a similarity $T$ from $I_{\Lambda}^{\perp}$ onto $\langle 1, -1, -1, -1, -1\rangle$ ($Q(Tx) = c\,Q(x)$ with $c \in K$, $c \neq 0$), which carries the frozen point's stabiliser $SO(I_{\Lambda}^{\perp})$ and its bivector Lie algebra onto $SO_{K}(1,4)$ and $\mathfrak{so}_{K}(1,4)$, if and only if $d$ is a sum of two squares in $K$; this follows from $d \in K^{2}$, is strictly weaker over $\Q$ ($\Lambda = 6$), and fails over $\Q$ for $\Lambda = 9$ ($d = 3$).
(c) The mirror's algebra is complexified (its centre is a field) if and only if $-d \notin K^{2}$; when $d \in K^{2}$ this is $-1 \notin K^{2}$, which holds over every ordered field and fails over $\mathrm{span}\{1, u\}$ with $u^{2} = -1$, where $u\omega'/H$ has square $1$ and the mirror's algebra is doubled. So the reading "the frozen point's complement doubles ours to $\Cl(1,4)$ and complexifies the mirror's to $\Cl(4,1)$" holds over $K$ exactly when $d \in K^{2}$ and $-1 \notin K^{2}$.
(d) The rescaling $W \mapsto W/\sqrt{|\Lambda|}$ needs $|\Lambda| \in K^{2}$, and then gives $Q = -\mathrm{sgn}(\Lambda)/3$; $\Cl_{K}(1,3) \perp \langle \pm\tfrac13\rangle$ is isomorphic to $\Cl_{K}(2,3)$ (upper sign) or $\Cl_{K}(1,4)$ (lower sign) if and only if $3 \in K^{2}$. With $H \in K$, $|\Lambda| = 3H^{2}$, so this rescaling needs $\sqrt{3} \in K$ besides $H$; normalising by $H$ instead, $Q(W/H) = -1$, needs nothing more.
(e) The anti-de Sitter side has its own datum: each of the following is equivalent to $-d \in K^{2}$, that is, $\Lambda = -3H'^{2}$ with $H' \in K$: $K B_{\Lambda}$ contains $u$ with $u^{2} = -1$; $K W$ contains $e_{W}$ with $Q(e_{W}) = 1$; $I_{\Lambda}^{\perp} \cong \langle 1, -1, -1, -1, 1\rangle$; $\Cl_{K}(I_{\Lambda}^{\perp}) \cong \Cl_{K}(2,3)$. The witnesses are $B_{\Lambda}/H'$ and $W/H'$, and over an ordered $K$ with $\Lambda < 0$ the plane $\Pi_{\Lambda}$ is definite, so (b) and (c) fail.
(f) The matched scale of Proposition \claimref{synthesis.operator-join-point-spectrum-on-positive-energy-modules}(2), $\lambda s^{4} = 1$ with $\lambda = \Lambda/6$, has a solution $s^{2} \in K$ if and only if $\lambda \in K^{2}$; with $\Lambda = 3H^{2}$ and $H \neq 0$, $\lambda = H^{2}/2$, so that scale and the normalisation by $\sqrt{\lambda}$ need $\sqrt{2} \in K$ besides $H$.
\end{enumerate}

## technical
With the foundation's scalars in $\Q$ until the completion, the frozen point $I_{\Lambda} = \nInf + \tfrac{\Lambda}{6}\nO$ has square $d = \Lambda/3$, and everything in which $\Lambda$ enters rationally (the norm, the static boost $B_{\Lambda} = e_{0}W$ with $B_{\Lambda}^{2} = d$, the scale $\sigma = 1 - \Lambda Q(x)/12$, the complement $I_{\Lambda}^{\perp} = \langle 1,-1,-1,-1,-d\rangle$) is defined over any field $K$ of characteristic $0$. What needs a square root is a single condition: the boost's null eigen-directions, the unit boost $B_{\Lambda}/H$, the unit vector $W/H$, the horizon radius $R_{h} = 1/H$ and surface gravity $H$, the horizon point $(2/H)e_{1}$ of the observer's slice, the isometry of $I_{\Lambda}^{\perp}$ with the standard $(1,4)$ space, the doubled type $\Cl(1,4)$ and the mirror's $\Cl(4,1)$ each exist over $K$ exactly when $\Lambda/3$ is a square in $K$. Taking $H$ as the datum, $\Lambda = 3H^{2}$, makes them all hold over $K$ as written; over $\R$ nothing changes. Over $\Q$, $\Lambda = 7/3$ loses all of them, the bifurcation sphere having no rational point at all, and $\Lambda = 6$ loses them too, with centres the quadratic fields of discriminants $8$ and $-8$. Five constructions need a condition of their own: a point of the bifurcation sphere ($\Lambda/3$ a sum of three squares), a similarity carrying the frozen point's stabiliser to $SO(1,4)$ ($\Lambda/3$ a sum of two squares, which fails for $\Lambda = 9$), the complexified reading of the mirror ($-1$ not a square, automatic over an ordered field), the sheaf rescaling by $\sqrt{|\Lambda|}$ ($\sqrt{3}$ besides $H$) and the operator join's matched scale ($\sqrt{2}$ besides $H$). On the anti-de Sitter side the datum is $H'$ with $\Lambda = -3H'^{2}$. Statements that need the completion anyway, such as the Euclidean period $2\pi/\kappa_{\Lambda}$, are unaffected.

## lay
Before the series passes to the real numbers, its numbers are fractions. The frozen point, the vector that carries the cosmological constant, has squared length one third of that constant, and several constructions built on it (the light-like directions of the horizon's boost, the horizon's radius, the type of algebra the frozen point leaves behind) need the square root of that number. With the cosmological constant itself as the given number they work only for special values; with the expansion rate H as the given number, the constant being three times its square, they all work. A few constructions need a little more, such as the square root of 2 or of 3, and this result says exactly which, and what each needs.

## one-liner
Over any field $K$ of characteristic $0$, the static boost's null eigen-directions and unit, $R_{h} = 1/H$, the observer's horizon point, the isometry type of $I_{\Lambda}^{\perp}$ and the types $\Cl(1,4)$ and $\Cl(4,1)$ exist exactly when $\Lambda/3$ is a square in $K$, so all hold with the datum $H$, $\Lambda = 3H^{2}$; a sphere point, $SO(1,4)$, the mirror's complexification, the $\sqrt{|\Lambda|}$ rescaling and the operator join's scale need their own conditions.
