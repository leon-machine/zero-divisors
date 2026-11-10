---
id: synthesis.chsh-over-the-rationals-pure-states-on-a-circle-and-the-pell-records
kind: claim
version: 1
title: 'CHSH over the rationals: pure states on a circle of square radius 8 and the Pell records'
status: proved
region: synthesis
subject: clifford-structure
tags: [entanglement, rotors-and-stabilisers, limits, finite-models]
proposed_by:
  kind: ai
  session: 2026-11-10-phase1
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-10-phase1
review: draft
derivations:
- name: main
  uses:
  - synthesis.signed-directions-and-the-integer-clifford-algebra@2
  - synthesis.division-gives-the-rationals@2
  - synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product@1
  - synthesis.the-sign-is-the-rotor-at-infinity@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_quarter_turned_chsh_elements_anticommute_and_values_lie_in_a_disc
- kind: check
  ref: check.py::check_pure_states_of_the_sector_are_rational_points_of_the_circle_of_square_radius_eight
- kind: check
  ref: check.py::check_denominator_law_and_the_pell_records
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.the-sign-is-the-rotor-at-infinity
  - synthesis.division-gives-the-rationals
  - synthesis.continuum-completion-premise
extraction:
  note: >-
    Question: before the completion of the coefficients, with the integer and rational algebras only, is the
    value $2\sqrt{2}$ of the CHSH combination attained or only approached? Kill conditions registered before
    computing: (a) rational data attaining squared value 8 exactly; (b) a supremum over rational data strictly
    below $2\sqrt{2}$. Neither fired. That a rational functional on a rational element has a rational value, so
    that $2\sqrt{2}$ is not a value, is immediate, and a sibling result of the same run (on the signatures in
    which a value above 2 exists; intended citation once stored) gives a family of rational states whose values
    fill the rationals of the open interval. So the supremum needs no approximation sequence, and another sibling result (on parity-even observables) records the values $2(c + s)$ of the equal-weight pair state at rational points, three of them explicitly. What this result adds is the structure of the approach and the answer to which values are best at bounded denominators: the pure
    states of the sector form the rational points of a circle of square radius 8 in the plane of two
    anticommuting CHSH elements, they are the orbit of one parity-even state under the stored rational rotors,
    the squared deficit of a pure state is a rational square, every rational value obeys a denominator law, and
    the values that meet it are a Pell sequence starting at the local value 2. Status: elementary mathematics;
    the circle is the correlation complementarity of two anticommuting observables (compare Kurzynski, Paterek,
    Ramanathan, Laskowski and Kaszlikowski, arXiv:1010.2012, checked on the web, for the general principle), and
    the Pell equation and the best-approximation property of its solutions are classical. No source stating the
    CHSH attainment question over the rationals in this form was found in a web search; that absence is weak
    evidence and no claim of priority is made. The bound $\omega(C)^{2} \le 8$ is Tsirelson's (cited from
    memory); here it is needed only at the settings of the statement, where it is one line. The completion
    postulate is not used. Not decided here: which rationals are values of pure states that do not lie in the
    sector. Transport-absent.
---

## formal
Let $\Cl_{\Q}(2,2)$ (Theorems \claimref{synthesis.signed-directions-and-the-integer-clifford-algebra}, \claimref{synthesis.division-gives-the-rationals}) have generators $e_{1}, f_{1}, e_{2}, f_{2}$ with $Q(e_{j}) = 1$, $Q(f_{j}) = -1$, parities $p_{j} = f_{j}e_{j}$, and let $\dagger$ be the linear extension of the inverse on blades (it fixes $e_{j}$ and negates $f_{j}$). A \emph{state} is a linear $\omega$ to $\Q$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$; a \emph{pure state} is $\omega_{\rho}(x) = 4\langle\rho x\rangle_{0}$ for a self-adjoint idempotent $\rho$ with $\rho x\rho = 4\langle\rho x\rangle_{0}\rho$ for all $x$. The two parties are mode $1$ and the Klein-twisted mode $2$ of Theorem \claimref{synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product}(ii), with the commuting self-adjoint settings of square one
\[
A_{1} = e_{1}, \quad A_{2} = p_{1}, \quad B_{1} = e_{2}p_{1}, \quad B_{2} = p_{2}, \qquad C = A_{1}(B_{1} + B_{2}) + A_{2}(B_{1} - B_{2}), \qquad K = e_{1}f_{2}, \quad P_{K} = \tfrac12(1 + K),
\]
for which $C^{2} = 4(1 + K)$ and $K^{\dagger} = K$, $K^{2} = 1$. Put $I = B_{1}B_{2} = e_{2}p_{1}p_{2}$ and $C^{\perp} = CI$.
\begin{enumerate}
\item[(i)] \emph{(Two anticommuting CHSH elements; proved.)} $I^{2} = -1$, $I^{\dagger} = -I$; $I$ commutes with $A_{1}, A_{2}, K$ and anticommutes with $B_{1}, B_{2}, C$. $C^{\perp} = A_{2}(B_{1} + B_{2}) - A_{1}(B_{1} - B_{2})$ is the CHSH element of the settings $(A_{2}, -A_{1}, B_{1}, B_{2})$; it is self-adjoint, $CC^{\perp} = -C^{\perp}C$, and $(xC + yC^{\perp})^{2} = 4(x^{2} + y^{2})(1 + K)$ for rational $x, y$. For every state, $\omega(C)^{2} + \omega(C^{\perp})^{2} \le 8$; in particular $\omega(C)^{2} \le 8$, and $\omega(C)^{2} \ne 8$ because $2$ is not a rational square.
\item[(ii)] \emph{(Pure states of the sector; proved.)} The corner $P_{K}\Cl_{\Q}(2,2)P_{K}$ has basis $P_{K}$, $C$, $IP_{K}$, $C^{\perp}$. Its self-adjoint idempotents other than $0$ and $P_{K}$ are exactly
\[
\rho_{X,Y} = \tfrac12P_{K} + \tfrac{1}{16}\bigl(XC + YC^{\perp}\bigr), \qquad X, Y \in \Q, \quad X^{2} + Y^{2} = 8,
\]
each defines a pure state, and $\omega_{\rho_{X,Y}}(C) = X$, $\omega_{\rho_{X,Y}}(C^{\perp}) = Y$. So the pure states with $K\rho = \rho$ are the rational points of the circle $X^{2} + Y^{2} = 8$, and for each of them the deficit $8 - \omega(C)^{2} = \omega(C^{\perp})^{2}$ is the square of a rational; the points $(\pm 2\sqrt{2}, 0)$ are not rational.
\item[(iii)] \emph{(The orbit of one even state under the rational rotors; proved.)} $\rho_{0} = \tfrac14(1 + A_{1}B_{1})(1 - A_{2}B_{2}) = \rho_{2,-2}$ commutes with the total parity $p_{1}p_{2}$. For $u \in \Q$ put $y_{u} = 1 + uI$, so $y_{u}^{\dagger}y_{u} = 1 + u^{2}$, and $c = (1 - u^{2})/(1 + u^{2})$, $s = 2u/(1 + u^{2})$. Then
\[
\rho_{u} = \frac{y_{u}\rho_{0}y_{u}^{\dagger}}{1 + u^{2}} = \rho_{X,Y}, \qquad (X, Y) = \bigl(2(c - s),\ -2(c + s)\bigr), \qquad \omega_{\rho_{u}}(C) = \frac{2(1 - 2u - u^{2})}{1 + u^{2}},
\]
$\rho_{\infty} = I\rho_{0}I^{\dagger} = \rho_{-2,2}$, and $u \mapsto \rho_{u}$ is a bijection from $\Q \cup \{\infty\}$ onto the pure states of (ii). Equivalently the state stays $\rho_{0}$ and the directions of party $B$ are turned: $\omega_{\rho_{u}}(C) = \omega_{\rho_{0}}(C_{u})$ with $C_{u}$ the CHSH element of $A_{1}, A_{2}$ and $b_{j} = y_{u}^{-1}B_{j}y_{u} = B_{j}R_{u}^{-1}$, where $R_{u} = (1 - uI)(1 + uI)^{-1} = c - sI$ is the rational rotor of Theorem \claimref{synthesis.the-sign-is-the-rotor-at-infinity} with $I$ for its bivector; $b_{1} = cB_{1} + sB_{2}$, $b_{2} = cB_{2} - sB_{1}$. No square root is taken: $\rho_{u}$ is rational for every rational $u$ (scaling $y_{u}$ to $y^{\dagger}y = 1$ would need $1 + u^{2}$ to be a square, and is not needed). Conjugation by $p_{1}p_{2}$ sends $\rho_{X,Y}$ to $\rho_{-Y,-X}$, so the pure states of (ii) that commute with the total parity are $\rho_{0}$ and $\rho_{\infty}$ only, with $\omega(C) = \pm 2$; $\rho_{\infty}$ is the pair state of clause (v) of the mode-split Theorem at $r = 0$, $cs = -\tfrac12$.
\item[(iv)] \emph{(Denominator law; proved.)} If $P \ge 0$, $Q \ge 1$ are coprime integers with $P^{2} < 8Q^{2}$ then $8Q^{2} - P^{2} \ge 4$, with equality exactly when $P = 2x$ and $x^{2} - 2Q^{2} = -1$. So every state value $\omega(C) = \pm P/Q$ in lowest terms has $8 - \omega(C)^{2} \ge 4/Q^{2}$.
\item[(v)] \emph{(Pell records; proved.)} The positive solutions of $x^{2} - 2Q^{2} = -1$ are $(x_{0}, Q_{0}) = (1, 1)$, $(x_{k+1}, Q_{k+1}) = (3x_{k} + 4Q_{k},\ 2x_{k} + 3Q_{k})$: $(1,1), (7,5), (41,29), (239,169), \dots$ The values
\[
S_{k} = \frac{2x_{k}}{Q_{k}} = 2,\ \tfrac{14}{5},\ \tfrac{82}{29},\ \tfrac{478}{169},\ \dots, \qquad 8 - S_{k}^{2} = \frac{4}{Q_{k}^{2}}, \qquad S_{k}^{2} < 8 < \bigl(S_{k} + Q_{k}^{-2}\bigr)^{2},
\]
are values of pure states of (ii) (at $u = 0, -\tfrac12, -\tfrac25, -\tfrac{5}{12}, \dots$, the points $(S_{k}, \pm 2/Q_{k})$), and $S_{k}$ is larger than every value of $C$ on any state whose denominator is smaller than $Q_{k}$. The sequence increases to $2\sqrt{2}$, which is the supremum of the values over the rationals and is not attained; its first term is the value $2$ of the parity-even state $\rho_{0}$.
\end{enumerate}

## technical
Before the coefficients are completed, the Clifford algebra of the foundation has integer and rational coefficients only, and the largest quantum value $2\sqrt{2}$ of the Clauser-Horne-Shimony-Holt combination is irrational. This result describes exactly how it is approached. For two modes of the split-signature algebra, with one party's quantities Klein-twisted so that the parties commute and each party's two directions anticommuting, the CHSH element $C$ has a partner $C^{\perp}$, the CHSH element of the settings with one party's pair turned by a quarter turn, which anticommutes with it and has the same square. The pair of values $(\omega(C), \omega(C^{\perp}))$ of any state lies in the disc of square radius $8$, and the pure states of the sector in which the square is $8$ are exactly the rational points of the boundary circle. These are the images of a single parity-even state under the rational rotors of the plane that the series already has (the Cayley parametrisation by a rational $u$), or equivalently the values of that one state when one party's directions are turned by a rational rotor; no square root is needed, because the state is the projector and not a unit vector. The point of the circle at which $C$ would take the value $2\sqrt{2}$ is the one where it meets an axis, and it is not rational.

The approach is governed by a denominator law: a rational value $P/Q$ falls short of $8$ in its square by at least $4/Q^{2}$, and the values that meet this are $2x/Q$ with $x^{2} - 2Q^{2} = -1$, a Pell sequence $2, 14/5, 82/29, 478/169, \dots$ Each of them is the value of a pure state, beats every value of smaller denominator, and the sequence converges to $2\sqrt{2}$ with error below $1/Q^{2}$. The first term is the local value $2$, and it is the only one (with its mirror image) reached by a pure state of the sector that respects the total parity at these fixed directions. Inside the rational algebra the element $C$ restricted to the sector is itself a square root of $8$: the number is present as an element, and what the rationals lack is a state on which that element has a sharp value.

## lay
The largest value that quantum theory allows for a famous combination of correlations between two separated experiments is 2 times the square root of 2, a number that cannot be written as a fraction. The series builds its algebra first with whole numbers and fractions only, and adds the continuum as a separate, later assumption. So one can ask whether the quantum maximum is reached before that assumption is made. It is not, but it is approached as closely as one likes, and in a very orderly way. The states that matter correspond to the points with fractional coordinates on a circle; the maximum would sit at a point of that circle which has no fractional coordinates. The best fractional values form a sequence, 2, then 14/5, then 82/29, then 478/169, and so on, generated by the same rule that produces the classical best fractional approximations to the square root of 2, each one closer than any fraction with a smaller denominator can be. The first member of the sequence, 2, is exactly the limit for a world of pre-existing answers. Each of these values comes from one fixed shared state by turning one experimenter's measuring directions through an angle whose sine and cosine are fractions, the kind of turn the series already uses.

## one-liner
For one mode and the Klein-twisted other mode of $\Cl_{\Q}(2,2)$ at anticommuting directions, the CHSH element $C$ and its quarter-turned partner $C^{\perp}$ anticommute, the pure states of the sector are the rational points of $X^{2} + Y^{2} = 8$ (the orbit of one parity-even state under the rational rotors), every rational value $P/Q$ has $8 - (P/Q)^{2} \ge 4/Q^{2}$, and equality holds exactly on the Pell sequence $2, \tfrac{14}{5}, \tfrac{82}{29}, \tfrac{478}{169}, \dots$, which increases to the unattained supremum $2\sqrt{2}$.
