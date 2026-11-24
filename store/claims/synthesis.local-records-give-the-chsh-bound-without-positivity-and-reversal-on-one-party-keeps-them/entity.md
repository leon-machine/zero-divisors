---
id: synthesis.local-records-give-the-chsh-bound-without-positivity-and-reversal-on-one-party-keeps-them
kind: claim
version: 1
title: "Under (CP) one party's values bound CHSH without (P); local record weights do not fix (P)"
status: proved
region: synthesis
subject: clifford-structure
tags: [entanglement, measurement-and-records, finite-models]
proposed_by:
  kind: ai
  session: 2026-11-24-three-routes
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-24-three-routes
review: draft
derivations:
- name: main
  uses:
  - synthesis.signed-directions-and-the-integer-clifford-algebra@2
  - tower.commuting-copies@5
  - synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear@1
  - synthesis.additive-weights-on-the-rational-projectors-are-linear-in-every-size-from-four@1
  - std-algebra.quaternions@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_certificate_and_bound_from_values_of_one_party_given_the_other_partys_outcomes
- kind: check
  ref: check.py::check_weights_of_records_of_one_party_of_two_modes_give_the_bound
- kind: check
  ref: check.py::check_weights_of_records_of_one_party_of_three_modes_give_the_bound
- kind: check
  ref: check.py::check_reversal_on_one_party_is_well_defined_and_fixes_products_of_local_observables
- kind: check
  ref: check.py::check_reversal_of_the_two_mode_state_and_two_copies_select_the_end_points
- kind: check
  ref: check.py::check_one_unitary_between_the_parties_exposes_the_reversed_functional
- kind: check
  ref: check.py::check_field_theory_unit_makes_the_separating_blade_a_product_of_local_observables
lineage:
  motivated_by:
  - synthesis.premise-positivity-of-values
  - synthesis.local-weights-give-the-chsh-bound-and-do-not-fix-positivity-of-values
  - synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate
  - one-relation.recorded-sectors-superselected-premise
extraction:
  maintainer_pass_2026_11_24_three_routes:
    by: maintainer-2026-11-24
    date: '2026-11-24'
    note: 'Maintainer edit before first acceptance, version kept at 1. After Leon''s decisions of 24 November 2026. The relation to the reading that every rational projector can label a record, stated in the note with a plain-text ''filed alongside'' citation, is added to the Reading as item (e) with a reference to the stored result under Hypothesis (RP), and the note''s citation is a reference; (RP) stays a named hypothesis (Leon''s decision), neither adopted nor rejected. No mathematics, link or check changed; no uses edge is added.'
  open_problem: op.positivity-of-values
  note: >-
    Bears on the first attack item of the open problem (derive (P) or show it independent). It extends two
    clauses of synthesis.local-weights-give-the-chsh-bound-and-do-not-fix-positivity-of-values from one twisted
    mode per party and directions to any number of modes and any pair of observables per party: its clause (ii)
    (non-negative local weights give the bound) becomes clauses (i) to (iii) here, with a certificate that is
    linear in the CHSH element and uses positivity only on one party's elements times an outcome of the other;
    its clause (iv) (a family of functionals with the values of a state on the span of the nine products of one
    observable of each party) becomes the
    reversal of clause (iv) here, which works for every state and every number of modes, and clause (v) shows
    which members of the stored family survive two copies. Kill conditions registered before computing: the
    multiplication map of the two parties' algebras not a bijection, or the reversal moving a product of one local
    observable of each party, or the reversed two-mode state satisfying (P) (none occurred); no negative weight on two copies
    for some $c^{2} \ne 1$ (the predicted weight $(c^{2} - 1)/16$ occurs); a functional with non-negative
    conditional values and a CHSH value of square above $8$ (excluded by the identity of clause (i)). No uses
    edge is drawn to results that hold given (P): the functionals $\lambda_{c}$ and the box functional of the
    stored results are named for comparison with their definitions restated, so nothing here is under a premise
    about values. Hypotheses stated inside clauses: (CP) in clause (ii) and the conditions on $\mu$ in clause
    (iii); neither is a stored premise. Relation to the reading that every projector with rational
    coefficients of the algebra of both parties can label a record: under that reading the weights on two modes
    are the restriction of a state by the stored theorem on additive weights, which gives the bound at once
    (\claimref{synthesis.under-rp-record-weights-bound-the-chsh-sum-of-correlators-on-two-modes}, which
    states that reading as a named hypothesis and bounds the sum of the four correlators on two modes);
    clause (iii) asks for records of one party's projectors and the other party's four outcomes only, so it uses
    no projector that is not a product of local ones, needs the first party to hold at least two modes, and holds for the
    reversed functional of clause (v) as well. Literature, all cited from memory and to be confirmed before any import.
    That quantum theory over the reals is not locally tomographic, and that a state of two real systems and its
    partial transpose agree on all local data: W. K. Wootters (1990), L. Hardy and W. K. Wootters, Found. Phys.
    42 (2012) 454, C. M. Caves, C. A. Fuchs and P. Rungta, Found. Phys. Lett. 14 (2001) 199; clause (iv) is that
    fact written in the algebra of modes, and no claim of novelty is made for it. That functionals that are
    non-negative on products of local effects give only quantum correlations for two parties: H. Barnum, S.
    Beigi, S. Boixo, M. B. Elliott and S. Wehner, Phys. Rev. Lett. 104 (2010) 140401; clause (ii) is a special
    case with an explicit certificate over the rationals. Macroscopic locality (M. Navascues and H. Wunderlich,
    Proc. R. Soc. A 466 (2010) 881) derives the same bound from the requirement that coarse counts over many
    pairs have a joint distribution; it is not used, and the Reading says how it stands to clause (ii).
    Positivity of maps under tensor powers (A. Mueller-Hermes, D. Reeb and M. M. Wolf, J. Math. Phys. 57 (2016)
    015202) is the general question behind clause (v). Tsirelson's bound is B. S. Cirel'son, Lett. Math. Phys. 4
    (1980) 93. Ledger: transport-absent. The clauses are statements about rational Clifford algebras of modes;
    clause (vii) uses the series' convention that the unit of the field theory commutes with the mode vectors.
    Clause (iii) is stated for a first party of two or more modes: for two modes it rests on the stored
    two-mode theorem, and for more on the stored theorem that additive weights on the rational projectors are
    linear in every size from four (its clauses (i) and (iii)); the check exhibits, for a first party of three
    modes, one $\mu$ satisfying the hypotheses that comes from a functional that is not a state, and the bound;
    the passage from additive to linear is the stored theorem's and is not recomputed.
    Not done: whether non-negative weights of local records on every number of copies force a functional to be
    a state or the reversal of one; ordered fields other than $\Q$ in clauses (iii) and (vi); which stored
    premises speak of records of projectors that are not products of local ones (the Reading states the
    question; it is a premise decision).
---

## formal
Let $k$ be an ordered field, $\ell = m + n$ with $m, n \ge 1$, and $\Cl_{k}(\ell,\ell)$ the algebra of $\ell$ modes: generators $e_{j}$, $f_{j}$ with $Q(e_{j}) = 1$, $Q(f_{j}) = -1$, $p_{j} = f_{j}e_{j}$, the adjoint $\dagger$ the linear extension of the inverse on blades (Theorem \claimref{synthesis.signed-directions-and-the-integer-clifford-algebra}), $\langle x\rangle_{0}$ the scalar part. Party $1$ holds the first $m$ modes and party $2$ the others: $\mathcal{A}$ is the subalgebra generated by $e_{j}, f_{j}$, $j \le m$, and $\mathcal{B}$ the subalgebra generated by the twisted generators $\gamma e_{j}$, $\gamma f_{j}$, $j > m$, with $\gamma = p_{1}\cdots p_{m}$ (Proposition \claimref{tower.commuting-copies}). A \emph{local observable} of a party is a self-adjoint element of its algebra. $\mathcal{A}$ and $\mathcal{B}$ are closed under $\dagger$ and commute elementwise, and multiplication $\mathcal{A} \otimes \mathcal{B} \to \Cl_{k}(\ell,\ell)$ is a bijection (Preliminaries of the proof). Let $A_{0}, A_{1} \in \mathcal{A}$ and $B_{0}, B_{1} \in \mathcal{B}$ be self-adjoint of square $1$, and
\[
S = A_{0} + A_{1}, \quad D = A_{0} - A_{1}, \quad F_{\pm} = \tfrac12(1 \pm B_{0}), \quad G_{\pm} = \tfrac12(1 \pm B_{1}), \quad C = SB_{0} + DB_{1} = A_{0}B_{0} + A_{0}B_{1} + A_{1}B_{0} - A_{1}B_{1} .
\]
(P) is Premise \claimref{synthesis.premise-positivity-of-values}; it is not assumed in any clause.
\begin{enumerate}
\item[(i)] \emph{(A certificate linear in $C$; proved.)} For every $t \in k$,
\[
4 + 2t^{2} - 2tC = (S - t)^{2}F_{+} + (S + t)^{2}F_{-} + (D - t)^{2}G_{+} + (D + t)^{2}G_{-} ,
\]
and each term is $yy^{\dagger}$ with $y = sF$, $s$ a self-adjoint element of $\mathrm{span}\{1, A_{0}, A_{1}\}$ and $F$ an outcome idempotent of party $2$. The identity uses only $A_{0}^{2} = A_{1}^{2} = 1$; that each term is $yy^{\dagger}$ uses that the four elements are self-adjoint, that $B_{j}^{2} = 1$ and that each $A_{i}$ commutes with each $B_{j}$. Both hold for such elements of every $\Cl_{k}(p,q)$.
\item[(ii)] \emph{(The bound from one party's values given the other's outcomes; proved.)} Hypothesis (CP): $\lambda : \Cl_{k}(\ell,\ell) \to k$ is $k$-linear with $\lambda(1) = 1$ and $\lambda(s^{2}F) \ge 0$ for every self-adjoint $s \in \mathrm{span}\{1, A_{0}, A_{1}\}$ and every $F \in \{F_{+}, F_{-}, G_{+}, G_{-}\}$. Under (CP), $\lambda(C)^{2} \le 8$, with strict inequality for $k = \Q$. A functional satisfying (P) satisfies (CP); so does every linear normalised $\lambda$ for which the four functionals $a \mapsto \lambda(aF)$ on $\mathcal{A}$ are non-negative on the elements $aa^{\dagger}$; and for one mode per party with directions as observables and $k$ a subfield of $\R$, Hypothesis (L) of Theorem \claimref{synthesis.local-weights-give-the-chsh-bound-and-do-not-fix-positivity-of-values} (non-negative weights at every pair of local directions) gives (CP). Neither the reality clause nor positivity on any other element is used. The box functional $\langle(1 + C_{0})x\rangle_{0}$ of two modes ($C_{0}$ the element $C$ at $A_{0} = X_{1}$, $A_{1} = Z_{1}$, $B_{0} = X_{2}$, $B_{1} = Z_{2}$ in the notation of clause (v)) has value $4$ on $C_{0}$ and the value $-\tfrac12$ on each of the four terms of (i) at $t = 1$.
\item[(iii)] \emph{(Weights of the records of one party of two or more modes; proved, given the stored theorems on additive weights.)} Let $k = \Q$ and $m \ge 2$. Let $\mu$ be a function with rational values on the products $EF$, $E$ a self-adjoint idempotent of $\mathcal{A}$ and $F \in \{1, F_{+}, F_{-}, G_{+}, G_{-}\}$, such that $\mu(1) = 1$, $\mu(EF) \ge 0$, $\mu((E + E')F) = \mu(EF) + \mu(E'F)$ whenever $EE' = 0$, and $\mu(EF_{+}) + \mu(EF_{-}) = \mu(E) = \mu(EG_{+}) + \mu(EG_{-})$. Put $c_{i0} = \sum_{a, b = \pm 1}ab\,\mu\bigl(\tfrac12(1 + aA_{i})\,\tfrac12(1 + bB_{0})\bigr)$, $c_{i1}$ likewise with $B_{1}$, and $V = c_{00} + c_{01} + c_{10} - c_{11}$. Then $V^{2} < 8$. No linear functional is assumed: by Theorem \claimref{synthesis.additive-weights-on-the-rational-projectors-are-linear-in-every-size-from-four} (for $m = 2$ it is Theorem \claimref{synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear}) each $E \mapsto \mu(EF)$ is the restriction of a linear functional on $\mathcal{A}$, which is then non-negative on the squares of self-adjoint elements, and the four values of (i) sum to $4 + 2t^{2} - 2tV$.
\item[(iv)] \emph{(The reversal on one party; proved.)} There is exactly one $k$-linear map $\theta$ of $\Cl_{k}(\ell,\ell)$ with $\theta(ab) = ab^{\dagger}$ for $a \in \mathcal{A}$, $b \in \mathcal{B}$. It satisfies $\theta^{2} = 1$, $\theta(1) = 1$, $\theta(x^{\dagger}) = \theta(x)^{\dagger}$, $\theta(axa') = a\,\theta(x)\,a'$ for $a, a' \in \mathcal{A}$, $\theta(bxb) = b\,\theta(x)\,b$ for self-adjoint $b \in \mathcal{B}$, and it commutes with the parity automorphism. For a $k$-linear $\lambda$ put $\lambda^{\theta} = \lambda \circ \theta$. Then $\lambda^{\theta}$ is linear with $\lambda^{\theta}(1) = \lambda(1)$; it is real ($\lambda^{\theta}(x^{\dagger}) = \lambda^{\theta}(x)$) if $\lambda$ is, and even if $\lambda$ is; and $\lambda^{\theta}(ab) = \lambda(ab)$ for every $a \in \mathcal{A}$ and every self-adjoint $b \in \mathcal{B}$. Hence $\lambda^{\theta}$ and $\lambda$ have the same values on every product $ab$ of an element of $\mathcal{A}$ with one local observable $b$ of party $2$ (in particular on every product of one local observable of each party); they can differ on products with two observables of party $2$ that do not commute, for example $(X_{1}Z_{1})(X_{2}Z_{2}) = -K$ in (v), where $\lambda_{-1}$ has the value $1$ and its reversal $-1$. They have the same weight $\lambda(P_{1}\cdots P_{r-1}P_{r}P_{r-1}\cdots P_{1})$ on every sequence of self-adjoint idempotents $P_{i}$ each lying in $\mathcal{A}$ or in $\mathcal{B}$ (the weights of sequences of local records), and satisfy (CP) together; and $\lambda^{\theta} \circ E_{o} = (\lambda \circ E_{o})^{\theta}$ for the sector average $E_{o}(x) = \tfrac12(x + oxo)$ of a local observable $o$ of square $1$. $\lambda^{\theta}$ need not satisfy (P) when $\lambda$ does (clause (v)).
\item[(v)] \emph{(Two modes, and two copies; proved.)} For $\ell = 2$, $m = n = 1$ write $X_{1} = e_{1}$, $Z_{1} = p_{1}$, $X_{2} = e_{2}p_{1}$, $Z_{2} = p_{2}$, $Y_{j} = X_{j}Z_{j}$, $U = X_{1}X_{2}$, $V = Z_{1}Z_{2}$, $K = e_{1}f_{2} = -Y_{1}Y_{2}$, and $\lambda_{c}(x) = \langle(1 - U - V + cK)x\rangle_{0}$, the functionals of the Theorem cited in (ii). Their weights on the joint outcomes $\tfrac14(1 + uU)(1 + vV)$ are $\tfrac14(1 - u - v - c\,uv)$, so $\lambda_{c}$ is non-negative on all $xx^{\dagger}$ only for $c = -1$, where it is $x \mapsto 4\langle P_{s}x\rangle_{0}$ with $P_{s} = \tfrac14(1 - U)(1 - V)$ (proved here; also clause (iv) of that Theorem, recalled for comparison). Then $\lambda_{c}^{\theta} = \lambda_{-c}$: the functional $\lambda_{1}$ is the reversal of the state $\lambda_{-1}$; it has the weights $-\tfrac12, \tfrac12, \tfrac12, \tfrac12$ on the joint outcomes at $(u,v) = (+,+), (+,-), (-,+), (-,-)$, and the form $\lambda_{1}(xy^{\dagger})$ has inertia $(12, 4, 0)$. For two copies take $\ell = 4$, $m = n = 2$, $X_{j} = e_{j}p_{1}\cdots p_{j-1}$, $Z_{j} = p_{j}$, and let $\lambda_{c} \otimes \lambda_{c}$ be the functional that is $\lambda_{c}$ on the pair of modes $(1,3)$ and on the pair $(2,4)$, $x \mapsto \langle M^{(13)}_{c}M^{(24)}_{c}x\rangle_{0}$ with $M^{(ab)}_{c} = 1 - X_{a}X_{b} - Z_{a}Z_{b} - cY_{a}Y_{b}$. Its value on the product of the self-adjoint idempotents $\tfrac14(1 + sX_{1}X_{2})(1 + tZ_{1}Z_{2})$ of party $1$ and $\tfrac14(1 + s'X_{3}X_{4})(1 + t'Z_{3}Z_{4})$ of party $2$ is
\[
\tfrac{1}{16}\bigl(1 + ss' + tt' + ss'tt'\,c^{2}\bigr), \qquad s, t, s', t' = \pm 1 ,
\]
which is $(c^{2} - 1)/16$ at $ss' = tt' = -1$ and $(1 - c^{2})/16$ at $ss' = 1$, $tt' = -1$. So for $c^{2} \ne 1$ the two copies have a negative weight on a product of local idempotents, although every $\lambda_{c}$ has non-negative weights at all pairs of local directions of one copy; for $c = -1$ the product is a state; and for $c = 1$ it is the reversal of that state, with by (iv) the weights of a state on every sequence of local records.
\item[(vi)] \emph{(One unitary between the parties; proved for $k = \Q$, $\ell = 2$.)} Let $P$ be an atom of $\Cl_{\Q}(2,2)$ (a self-adjoint idempotent with $\langle P\rangle_{0} = \tfrac14$). A $\Q$-linear $\lambda$ satisfies $\lambda(xx^{\dagger}) \ge 0$ for all $x$ if and only if $\lambda(uPu^{\dagger}) \ge 0$ for every $u$ with $uu^{\dagger} = 1$. For the reversed functional: $u = \tfrac12(1 + Z_{2} + X_{1} - X_{1}Z_{2})$ is self-adjoint with $u^{2} = 1$, it carries the local atom $\tfrac14(1 + Z_{1})(1 + X_{2})$ to $\tfrac14(1 + U)(1 + V)$, and $\lambda_{1}$ gives the first the weight $\tfrac14$ and the second $-\tfrac12$, where $\lambda_{-1}$ gives $\tfrac14$ and $0$.
\item[(vii)] \emph{(With the unit of the field theory; proved.)} In $\Cl_{k}(3,5)$, spacetime generators $\gamma_{0}, \dots, \gamma_{3}$ with $Q(\gamma_{0}) = 1$, $Q(\gamma_{i}) = -1$, together with the two modes of (v), the element $I_{4} = \gamma_{0}\gamma_{1}\gamma_{2}\gamma_{3}$ commutes with the mode vectors, $I_{4}^{2} = -1$, $I_{4}^{\dagger} = -I_{4}$, and $I_{4}Y_{1}$, $I_{4}Y_{2}$ are commuting self-adjoint elements of square $1$, the first commuting with $X_{2}, Z_{2}$ and the second with $X_{1}, Z_{1}$, with $(I_{4}Y_{1})(I_{4}Y_{2}) = K$. So where the unit $I_{4}$ multiplies the elements of both parties, the blade $K$ that separates the functionals $\lambda_{c}$ is a product of one self-adjoint element of each party. Without the unit it is a product of local observables only with two of each party, $K = -(X_{1}Z_{1})(X_{2}Z_{2})$, each factor $X_{j}Z_{j}$ anti-self-adjoint.
\end{enumerate}
\emph{Reading (argued, not proved).} (a) The bound on the CHSH value does not need (P) on the algebra of both parties. It needs that the values of one party, given each recorded outcome of the other, are non-negative on that party's squares, clause (ii); and over $\Q$, for a party of two or more modes, it follows from weights of that party's records that are non-negative, do not depend on the context (in particular their sum over the other party's outcomes is the same for both of its settings) and add on orthogonal projectors, clause (iii), with no linearity assumed and with no projector that is not a product of local ones. (b) No condition on records of local observables of two fixed parties gives (P): by (iv) a state and its reversal on one party agree on the weight of every such record (not on the value of every product of local observables), on any number of modes, after any local records, and on any coarse count formed from them, so each such condition holds for both or for neither, and the reversal of the two-mode state violates (P). Conditions of this kind include non-negative weights at all local settings, no signalling, the bound itself, and the requirement of macroscopic locality that coarse counts over many pairs have a joint distribution (prior art, from memory). That the stored premises on recording (Premises \claimref{one-relation.recording-irreversible-stated-so-it-can} and \claimref{one-relation.recorded-sectors-superselected-premise}) are of this kind is a reading: they speak of records being permanent and of interference between recorded sectors being inaccessible, and name neither weights nor the projectors that can label a record. (c) What separates a state from its reversal is a record of a projector that is not a product of local ones, or equivalently, by (vi), a local record made after a unitary that does not preserve the two parties' algebras; with non-negative weights for such records every linear functional on two modes satisfies the positivity clause of (P). So on this scope (P) is not implied by any condition on the weights of local records (it implies all of them) and is decided by whether the parties' modes can be brought together and recorded. (d) By (vii), where the numbers are read with the unit $I_{4}$ of the field theory, a state and its reversal differ in the value of a product of one self-adjoint element of each party; the reversal is then the partial transposition, which keeps the weights of local records non-negative (prior art, from memory; not proved here). (e) Under the reading that every projector with rational coefficients of the algebra of both parties can label a record, the weights on two modes are the restriction of a state by the stored theorem on additive weights for two modes, which gives the bound at once; Theorem \claimref{synthesis.under-rp-record-weights-bound-the-chsh-sum-of-correlators-on-two-modes} states that reading as its named Hypothesis (RP) and bounds the sum of the four correlators on two modes. Clause (iii) here uses no projector that is not a product of local ones, needs the first party to hold at least two modes, and holds for the reversed functional of (v) as well. (RP) stays a named hypothesis, neither adopted nor rejected (Leon's decision of 24 November 2026).

## technical
Premise (P), positivity of values, asks that values be given by a linear functional that is non-negative on every $xx^{\dagger}$ of the algebra of all modes. Two things are proved about how much of it records of local observables can supply, for two parties holding any numbers of modes. First, the CHSH bound needs much less than (P). For two observables of square one per party, $4 + 2t^{2} - 2tC$ is, for every number $t$, a sum of four squares, each a square of one party's element times one outcome projector of the other party. So a normalised linear functional that is non-negative on these has $\lambda(C)^{2} \le 8$ (take $t = \lambda(C)/2$), strictly over the rationals. Over the rationals, for a party holding two or more modes the hypothesis follows from weights of that party's records, given the other party's outcome, that are non-negative, add on orthogonal projectors, and whose sum over the other party's two outcomes does not depend on its setting, by the stored theorems that such weights are linear (one mode is excluded: there additivity does not give linearity). This extends the stored result for one twisted mode per party to any number of modes and any observables, and the box functional of value $4$ fails it by $-\tfrac12$ on each square.

Second, records of local observables never fix (P). The algebra of all modes is the product of the two parties' algebras, so the adjoint can be applied on one party's factor only. This reversal is linear, fixes every product of an element of the first party with a self-adjoint element of the second, and commutes with local sector averages. A state composed with it is a linear, normalised, real functional with the state's values on every product of one observable of each party and on every sequence of local records, on any number of modes; the two can differ on a product that contains two observables of the second party that do not commute, and such a product is not the weight of any sequence of local records. It need not be a state: on two modes the reversal of the state $\lambda_{-1}$ of the stored family is $\lambda_{1}$, with weight $-\tfrac12$ on one joint outcome of the commuting pair $U$, $V$. Within the stored family $\lambda_{c}$, two copies shared by the same parties already have a negative weight on a product of local projectors unless $c = \pm 1$; the two survivors are the state and its reversal. One unitary that mixes the parties' modes turns a local atom into the joint outcome and exposes the reversed functional; and on two modes a linear functional is non-negative on all squares exactly when one atom has non-negative weight after every unitary. Where the unit $I_{4}$ of the field theory multiplies both parties' elements, the separating blade is a product of local observables. That the algebra of two real systems is not fixed by local data is known (Wootters; Hardy and Wootters, from memory); what is added is the form in the algebra of modes, the certificate, and the count of what survives two copies.

## lay
Two experimenters share pairs of particles and each chooses between two measurements. Quantum theory limits how strongly their results can be correlated, and in this series that limit has rested on an assumption called positivity of values: every conceivable yes-or-no question about the whole system, including questions that neither experimenter can ask alone, gets a probability that is not negative. This result separates two parts of that assumption. The limit on correlations needs only a local part: given what one experimenter recorded, the other experimenter's probabilities must not be negative. That part can be read off from records each of them makes. The rest of the assumption cannot be tested by such records at all. There is a second assignment of values, obtained from an ordinary one by reversing one experimenter's side as in a mirror, that agrees with the ordinary one on everything the two can record separately, however many particles they share, and yet gives a negative "probability" to a joint question. Only a measurement made on both particles together, after bringing them into contact, tells the two apart. So whether positivity is an extra assumption comes down to whether such joint measurements are counted among the possible records.

## one-liner
In $\Cl_{k}(\ell,\ell)$ with the modes split between two parties: $4 + 2t^{2} - 2tC$ is a sum of four squares $s^{2}F$ ($s$ of one party, $F$ an outcome of the other), so non-negative values of one party given the other's outcomes (Hypothesis (CP)) give $\lambda(C)^{2} \le 8$ without (P) (over $\Q$, for a party of two or more modes, from non-negative additive weights of its records given each outcome of the other party, with the same marginal for both of the other party's settings); and the adjoint applied on one party's factor turns every state into a functional with the same weights on all sequences of local records at every number of modes (and the same values on products of one observable per party, not on all products of local observables), which on two modes has weight $-\tfrac12$ on a joint outcome and is exposed by one unitary between the parties.
